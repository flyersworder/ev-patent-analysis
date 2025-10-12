# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an EV (Electric Vehicle) patent analysis research project that analyzes patent filing patterns across the United States, China, and the European Union from 2014-2024. The analysis focuses on seven core EV technology domains and uses Google's Public Patent Dataset via BigQuery.

## Tech Stack & Environment

- **Python**: >=3.12 (managed with `uv`)
- **Package Manager**: `uv` (see pyproject.toml)
- **Key Dependencies**:
  - `marimo` (>=0.16.5) - Interactive notebook framework
  - `pandas` (>=2.3.3) - Data analysis
  - `plotly` (>=6.3.1) - Interactive visualizations

## Development Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Run the main script
uv run python main.py
```

### Running Marimo Notebooks
```bash
# Run the interactive notebook application
uv run marimo edit patent_analysis_chapter.py

# Export notebook to different formats
uv run marimo export html patent_analysis_chapter.py -o output.html
uv run marimo export ipynb patent_analysis_chapter.py -o output.ipynb
```

## Project Architecture

### Core Analysis Flow

The project follows a data pipeline architecture:

1. **Data Source**: Google BigQuery `patents-public-data.patents.publications` table
2. **Data Processing**: CSV data loaded from `../data/bquxjob_1552e56a_199b9009593.csv`
3. **Analysis**: Patent data pivoted and analyzed by:
   - Region (US, China, EU)
   - Year (2014-2024)
   - Technology domain (7 categories)
4. **Visualization**: Plotly interactive charts with dual-axis displays (percentage + absolute counts)

### Key Files

- **`patent_analysis_chapter.py`**: Main marimo notebook containing the full research chapter with:
  - Data loading and processing
  - Visualization functions
  - Analysis narrative (markdown cells)
  - Academic writing structure (Introduction → Findings → Recommendations → Conclusion)

- **`patent_analysis_chapter.ipynb`**: Jupyter notebook version of the same analysis

- **`main.py`**: Simple entry point script

### Technology Domain Categories

The analysis uses CPC (Cooperative Patent Classification) codes to categorize patents into 7 domains:

1. **Battery Technology** (H01M, H01G11)
2. **EV Propulsion & Charging** (B60L, H02K, H02P, H02J7, H02M)
3. **Autonomous Driving** (B60W, G05D1)
4. **Hybrid & Energy Management** (B60K6, B60W20, F02D)
5. **Safety & ADAS** (B60R, B60Q, G08G)
6. **Thermal Management** (B60H, F28D)
7. **Infotainment & Connectivity** (B60K35, B60K37, H04W4, G07C5, H04N7/18)

### Visualization Functions

Two main plotting functions in `patent_analysis_chapter.py`:

1. **`plot_plotly_stacked_bar_and_line()`**: Creates stacked bar charts with overlay line chart
   - Primary Y-axis: Percentage share (stacked bars)
   - Secondary Y-axis: Total patent counts (line)
   - Used for overall regional comparisons

2. **`plot_per_application_area()`**: Generates per-domain visualizations
   - Iterates through all 7 technology domains
   - Creates separate chart for each domain
   - Same dual-axis format as above

### Data Processing Pattern

Standard pandas workflow throughout:
```python
# Pivot for regional comparison
pivot_data = data.pivot_table(
    index="year",
    columns="country",
    values="patent_count",
    aggfunc="sum"
).fillna(0)

# Calculate percentage shares
pivot_data_percentage = pivot_data.div(pivot_data.sum(axis=1), axis=0) * 100
```

## Important Methodological Notes

### Patent Attribution
- Patents counted by **assignee/inventor country**, NOT patent office location
- This is critical: Chinese companies file 93.7% domestically while US/EU file 45-60% internationally
- All percentages represent share **among three regions only** (US, China, EU)

### Data Specifics
- 2024 data is incomplete (partial year) - marked with asterisk (*) in analysis
- EU region aggregates all 27 current member states
- Data path: `../data/bquxjob_1552e56a_199b9009593.csv`

## Marimo-Specific Conventions

The marimo notebook (`patent_analysis_chapter.py`) uses:

- **Cell decorators**: `@app.cell` and `@app.cell(hide_code=True)` for markdown cells
- **Reactive execution**: Cells automatically re-run when dependencies change
- **Cell structure**:
  - Import cells define reusable functions
  - Data cells load and transform data
  - Visualization cells call plotting functions
  - Markdown cells (`mo.md()`) contain narrative text

### Working with Marimo

- Each cell returns variables that become available to dependent cells
- Hidden code cells (`hide_code=True`) display only output in the rendered notebook
- The app structure: `app = marimo.App()` with cell decorators

### Marimo Core Principles & Best Practices

#### Reactivity and DAG Structure
- **Automatic execution**: Cells execute automatically when their dependencies change
- **DAG (Directed Acyclic Graph)**: Notebook forms a dependency graph - avoid circular dependencies
- **No variable redeclaration**: Variables cannot be redeclared across cells (unlike Jupyter)
- **Local variables**: Prefix with underscore (`_variable`) to keep variables cell-local
- **Last expression displayed**: The last expression in a cell is automatically displayed as output

#### Coding Requirements
- **Always import marimo**: First cell should include `import marimo as mo`
- **Complete runnable code**: Each cell must contain complete, executable code
- **No global definitions**: Avoid using `global` keyword
- **Return values**: Return variables from cells to make them available to dependent cells:
  ```python
  @app.cell
  def _():
      data = load_data()
      processed = process(data)
      return data, processed  # Make available to other cells
  ```

#### Visualization Best Practices
- **Plotly/Altair**: Return the figure/chart object directly as last expression
- **Matplotlib**: Use `plt.gca()` to return the current axes
- **Interactive elements**: Plotly charts are already interactive, no extra configuration needed
- **Chart objects**: Store charts in variables and return them to display

#### UI Elements (if adding interactivity)
- **Access values**: Use `.value` attribute to access UI element values
- **Separate definition and usage**: Define UI elements in one cell, reference in others
- **Layouts**: Use `mo.hstack()` and `mo.vstack()` for horizontal/vertical layouts
- **Reactive updates**: UI changes trigger automatic notebook updates

#### Data Handling
- **Current project uses pandas**: Existing code uses pandas for data manipulation
- **Efficient structures**: Use appropriate data types (e.g., `.fillna(0)` for missing values)
- **Validation**: Implement data validation for critical operations

#### Troubleshooting
- **Circular dependencies**: If cells depend on each other circularly, refactor to break the cycle
- **Variable conflicts**: Check for accidental variable redeclaration across cells
- **Check formatting**: Run `marimo check --fix` to catch common issues
- **Cell execution order**: Remember cells execute based on dependencies, not file order

## BigQuery SQL Query Structure

The source data comes from a complex BigQuery query with:
1. **CPC mapping CTE**: Maps classification codes to 7 technology domains
2. **EU countries CTE**: Lists all 27 EU member state codes
3. **Patent data CTE**: Joins publications with CPC codes and assignees
4. **Regional aggregation CTE**: Maps countries to US/CN/EU regions
5. **Final SELECT**: Groups by region, domain, and year

Full SQL query is documented in the notebook's Appendix A section.

## Research Context

This is an academic research chapter analyzing:
- **Main finding**: EU patent share declined from 42% (2014) → 28% (2024), while China surged from 9% → 25%
- **Key insight**: China treats EVs as consumer electronics (smartphone playbook), EU relies on traditional auto engineering
- **Recommendation focus**: EU should pursue "Premium Sustainable Mobility" positioning rather than competing on China's rapid-iteration model

---

## Current Project Status (Updated 2025-10-12)

### Overview
**Target**: 9,000±500 word academic chapter for conference proceedings
**Current**: ~5,600 words (60% complete)
**Structure**: 9 sections with theoretical framework, empirical analysis, and policy recommendations

### Analysis Expanded to 5 Regions
The analysis has been expanded from 3 regions (US, CN, EU) to **5 regions** (US, CN, EU, JP, KR):
- **Japan**: Included for hybrid powertrain and battery expertise
- **South Korea**: Included for battery dominance (LG Energy Solution, Samsung SDI, SK Innovation)
- **Taiwan**: Excluded (not a significant automotive player - no major OEMs/R&D centers)

### Data Assets Available

All 7 BigQuery queries have been executed, debugged, and verified:

1. **`data/01_global_context_5regions.csv`** (385 rows)
   - Patent counts by region, year, and technology domain (5 regions)
   - Key finding: Korea dominates batteries (14,354 patents in 2022 vs CN 9,166)

2. **`data/02_collaborative_patents.csv`** (713 rows)
   - Multi-assignee patents showing cross-regional collaboration
   - Key finding: Most patents single-region; EU-Korea battery collaboration significant

3. **`data/03_patent_quality_citations.csv`** (385 rows)
   - Forward citation counts by region, year, domain
   - Key finding: US has 2-3× higher citations than other regions

4. **`data/05_technology_lifecycle_scurves.csv`** (385 rows)
   - Year-over-year growth rates and lifecycle stage classifications
   - Key finding: Hybrid powertrains declining; autonomous driving in emergence phase

5. **`data/06_generality_originality_indices.csv`** (35 rows)
   - Hall-Jaffe-Trajtenberg quality indices
   - Key finding: US highest quality (0.801/0.855), Korea batteries lowest (0.488/0.544)

6. **`data/07_knowledge_flow_networks.csv`** (1,921 rows)
   - Citation flows between regions, self-citation rates, knowledge lags
   - Key finding: China faster absorption (3-4 years) vs US/EU (5-6 years); lowest self-citation (35.7%)

7. **SQL Queries**: Documented in `sql/` directory and `patent_analysis_feedback_response.md`

### Chapter Structure and Completion

**Completed Sections** ✅:
- **Section 1: Introduction** (~1,200 words) - Complete
- **Section 2: Theoretical Framework** (~900 words) - Complete, 37 academic references
- **Section 3: The Five-Region Race** (~3,500 words) - ✅ **COMPLETE (2025-10-12)**
  - Figure 1: Overall Patent Share Evolution (5 regions)
  - Figure 2: Technology Domain Analysis (7 domains, small multiples)
  - Figure 3: EU Competitive Position (heatmap)
  - Theory-driven interpretations with Box 1 on Korea-China battery paradox
  - **Status**: Publication-ready (A- grade, 92/100 after improvements)

**Pending Sections** 🟡:
- **Section 4**: Cross-Border Collaboration (0 words, planned 1,000)
- **Section 5**: Patent Quality Analysis (0 words, planned 2,100)
- **Section 6**: Knowledge Flow Networks (0 words, planned 900)
- **Section 7**: China Case Study updates (~1,500 existing + 300 new)
- **Section 8**: EU Strategic Recommendations (~1,500 existing + 1,100 new)
- **Section 9**: Conclusion updates (~500 existing + revision)
- **Appendix B**: Glossary (pending)

### Recent Work Completed (2025-10-12)

**Section 3 Editorial Improvements** - Task 2.1 ✅ COMPLETE

Based on critical review (graded A-, 92/100), implemented three changes:

1. **Enhanced Title** (line 162)
   - Changed from: `"# Competition Analysis"`
   - Changed to: `"# The Five-Region Race: Patent Competition Across EV Technology Domains"`

2. **Added Introductory Paragraph** (lines 166-173)
   - 170 words previewing section structure
   - Establishes scope: 5 regions, 2014-2024, 7 technology domains
   - Preview: Figure 1 → Figure 2 → Figure 3
   - Connects to theoretical framework from Section 2

3. **Fixed Visualization Consistency** (line 421)
   - Changed Figure 2 legend from hollow to solid filled markers
   - Now matches Figure 1 legend style
   - Change: `mark_point(size=100)` → `mark_point(size=100, filled=True)`

**Result**: Section 3 is publication-ready and requires no further edits.

### Work Remaining (~13 hours)

**Phase 2: Analysis & Visualization** - 20% complete (7.5 hours remaining)
- ✅ Task 2.1: Section 3 improvements (COMPLETE)
- 🟡 Task 2.2: Section 4 collaboration analysis (2 hours)
- 🟡 Task 2.3: Section 5.1 citation quality (1.5 hours)
- 🟡 Task 2.4: Section 5.2 lifecycle analysis (1.5 hours)
- 🟡 Task 2.5: Section 5.3 generality/originality (1.5 hours)
- 🟡 Task 2.6: Section 6 knowledge flows (2 hours)
- 🟡 Task 2.7: Section 7 China updates (1 hour)

**Phase 3: Writing Additions** - 40% complete (4 hours remaining)
- ✅ Task 3.1: Theoretical framework (complete)
- ✅ Task 3.2: Literature review (complete)
- 🟡 Task 3.3: Section 8 scenarios (2.5 hours)
- 🟡 Task 3.4: Section 9 conclusion (1 hour)
- 🟡 Task 3.5: Glossary (0.5 hours)

**Phase 4: Polish & Formatting** - 35% complete (1.5 hours remaining)
- ✅ Task 4.1: Section ordering (complete)
- ✅ Task 4.3: Section 3 title/intro (complete)
- 🟡 Task 4.2: Reduce subdivision levels (0.5 hours)
- 🟡 Task 4.4: Final proofread (1 hour)

### Next Immediate Step

**Task 2.2: Section 4 - Cross-Border Collaboration Analysis**
- **Data Ready**: `data/02_collaborative_patents.csv` (verified, 713 rows)
- **Deliverables**:
  - Bar charts showing collaboration patterns by region pairs
  - Time series of collaboration trends (2014-2024)
  - Domain breakdown: which technologies see most collaboration?
  - 1,000-word narrative analyzing EU as potential "innovation bridge"
- **Why Next**: Addresses critical feedback about missing collaboration analysis; natural progression from Section 3

### Key Methodological Decisions

1. **Assignee-Based Counting** (Critical)
   - Counts by assignee/inventor country, NOT patent office location
   - Automatically excludes Chinese utility models (CN office filings lack assignee data)
   - Captures "export-quality" innovation only
   - Result: Dataset contains only examined patents by design

2. **Theoretical Framework**: 5 complementary perspectives
   - Resource-Based View (RBV) - Barney (1991)
   - Disruptive Innovation - Christensen (1997)
   - National Innovation Systems - Freeman, Lundvall
   - Open Innovation - Chesbrough (2003)
   - Business Model Innovation - Teece, Zott & Amit

### Critical Findings from Data

1. **Korea's Battery Dominance**: 31-33% patent share (highest among 5 regions)
   - Creates paradox: China leads manufacturing (53%) but Korea leads innovation (33%)

2. **US Quality Advantage**: 2-3× higher forward citations
   - Generality 0.801, Originality 0.855 (highest scores)
   - Indicates foundational, cross-domain innovation

3. **China's Speed & Openness** (Surprising)
   - Faster knowledge absorption: 3-4 year citation lags vs. 5-6 for US/EU
   - Lowest self-citation rate: 35.7% (contradicts "insular innovation" narrative)

4. **EU's Systemic Erosion**: Patent share declined in 6 of 7 domains (2014-2023)
   - Only growth: Hybrid powertrains (+1.2pp) - declining market relevance
   - Steepest decline: Autonomous driving (-12.2pp)

### Important Notes for Continuing Work

- **Section 3 is complete** - Do not make further edits unless explicitly requested
- **All data verified** - CSV files are ready to use, no need to re-query
- **Visualization library**: Use Altair (not Plotly) - project switched from Plotly to Altair
- **Marimo reactive notebook** - Changes to cells auto-update dependent cells
- **Academic tone** - Maintain theory-driven, data-grounded analysis style established in Sections 1-3

### Detailed Planning Document

For comprehensive project planning, status tracking, and implementation details, see:
- **`patent_analysis_feedback_response.md`** - Full feedback response plan with query details, task breakdowns, and timeline
