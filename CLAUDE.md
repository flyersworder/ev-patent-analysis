# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Project Overview

EV (Electric Vehicle) patent analysis research project analyzing patent filing patterns across five regions (US, China, EU, Japan, South Korea) from 2014-2024. The analysis focuses on seven core EV technology domains using Google's Public Patent Dataset via BigQuery.

**Current Status**: Publication-ready academic book chapter (~10,165 words, EU-centric focus)

## Tech Stack & Environment

- **Python**: >=3.12 (managed with `uv`)
- **Package Manager**: `uv` (see pyproject.toml)
- **Key Dependencies**:
  - `marimo` (>=0.16.5) - Interactive notebook framework
  - `pandas` (>=2.3.3) - Data analysis
  - `altair` - Visualization library (switched from Plotly)

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

### PDF Export Workflow

```bash
# Make the script executable (first time only)
chmod +x export_pdf_workflow.sh

# Run the complete workflow
./export_pdf_workflow.sh
```

**Workflow**: Exports to Jupyter → Converts Vega-Lite to PNG → Renders PDF with Quarto → Cleanup

**Requirements**: Quarto installed, `_quarto.yml` in project root, all dependencies synced

**Output**: A4 paper, 300 DPI figures (7"×5"), hidden code cells, numbered sections

## Project Architecture

### Core Analysis Flow

1. **Data Source**: Google BigQuery `patents-public-data.patents.publications`
2. **Data Processing**: 7 CSV files from BigQuery queries in `data/` directory
3. **Analysis**: Patent data by region, year, and technology domain (5 regions × 11 years × 7 domains)
4. **Visualization**: Altair charts with interactive elements

### Key Files

- **`patent_analysis_chapter.py`**: Main marimo notebook (EU-centric book chapter, ~10,165 words)
- **`patent_analysis_paper.py`**: Backup of original 5-region comparative manuscript (~13,650 words)
- **`EU_CENTRIC_REVISION_PLAN_V2.md`**: Revision strategy for EU-centric transformation

### Technology Domain Categories

1. **Battery Technology** (H01M, H01G11)
2. **EV Propulsion & Charging** (B60L, H02K, H02P, H02J7, H02M)
3. **Autonomous Driving** (B60W, G05D1)
4. **Hybrid & Energy Management** (B60K6, B60W20, F02D)
5. **Safety & ADAS** (B60R, B60Q, G08G)
6. **Thermal Management** (B60H, F28D)
7. **Infotainment & Connectivity** (B60K35, B60K37, H04W4, G07C5, H04N7/18)

### Data Assets (7 CSV files)

1. `01_global_context_5regions.csv` - Patent counts by region/year/domain
2. `02_collaborative_patents.csv` - Cross-regional collaboration patterns
3. `03_patent_quality_citations.csv` - Forward citation counts
4. `05_technology_lifecycle_scurves.csv` - Growth rates and lifecycle stages
5. `06_generality_originality_indices.csv` - Hall-Jaffe-Trajtenberg quality indices
6. `07_knowledge_flow_networks.csv` - Citation flows, self-citation rates, knowledge lags
7. SQL queries documented in `sql/` directory

## Marimo-Specific Conventions

### Core Principles
- **Reactive execution**: Cells auto-run when dependencies change
- **DAG structure**: Avoid circular dependencies
- **No variable redeclaration**: Variables cannot be redeclared across cells
- **Local variables**: Prefix with underscore (`_variable`) to keep cell-local
- **Return values**: Return variables to make them available to dependent cells

### Cell Structure
```python
@app.cell
def _():
    data = load_data()
    processed = process(data)
    return data, processed  # Make available to other cells
```

### Visualization Best Practices
- **Altair charts**: Return chart object directly as last expression
- **Markdown cells**: Use `@app.cell(hide_code=True)` with `mo.md(r""" ... """)`
- **Interactive elements**: Altair charts are already interactive

### Data Processing Pattern
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
- Automatically excludes Chinese utility models (captures "export-quality" innovation only)
- All percentages represent share **among five regions** (US, China, EU, Japan, Korea)

### Data Specifics
- 2024 data is incomplete (partial year) - marked with asterisk (*)
- EU region aggregates all 27 current member states
- Analysis period: 2014-2024 (11 years)
- Citation cohort for quality analysis: 2014-2018 (to allow citation maturity)

### Theoretical Framework (5 perspectives)
- Resource-Based View (RBV) - Barney (1991)
- Disruptive Innovation - Christensen (1997)
- National Innovation Systems - Freeman, Lundvall
- Open Innovation - Chesbrough (2003)
- Business Model Innovation - Teece, Zott & Amit

## Critical Findings from Data

### Regional Patterns
- **EU paradox**: 2nd in patent volume (24.9%, 2014-2018 cohort), last in citation quality (2.58 vs. US 9.97)
- **Korea's battery dominance**: 31-33% patent share (highest among 5 regions)
- **US quality advantage**: 2-3× higher forward citations, generality 0.801, originality 0.855
- **China's openness**: Lowest self-citation rate (21.2%), minimal citation lags (1.54 years)

### Geopolitical Dynamics
- **US-China collaboration collapse**: -76% (562→135 patents, 2020→2023)
- **US-China knowledge flows**: -64% to -70% decline after 2021 peak
- **EU as knowledge bridge**: EU-US dominant axis (13,139 citations in 2023)

### EU Competitive Position
- **Patent share decline**: 26.3% → 17.3% (2014-2024), erosion in 6 of 7 domains
- **Legacy trap**: Only growth in hybrid powertrains (+1.2pp), a declining technology
- **Defensive strengths**: Thermal management (44% share), safety systems (47% share)

### Socioeconomic Data Integration
- **R&D Intensity (2022)**: Korea 5.21% (highest), US 3.59%, Germany 3.13%, China 2.56% (lowest)
- **Manufacturing Value Added (2022)**: China 28.59% (highest), Korea 26.69%, Germany 20.29%, US 10.70%

## Important Notes for Ongoing Work

### Writing & Analysis
- **Maintain academic tone**: Theory-driven, data-grounded, formal language
- **Data accuracy critical**: Always verify numbers against CSV files before writing
- **EU-centric focus**: Current chapter emphasizes EU competitive positioning
- **Citation consistency**: Use 2014-2018 cohort for citation quality metrics

### Technical Details
- **Visualization library**: Use Altair (not Plotly)
- **Marimo reactive notebook**: Changes to cells auto-update dependent cells
- **Check formatting**: Run `marimo check --fix` to catch issues

### Reference Documents
- **`COMPREHENSIVE_REVIEW_FINDINGS.md`**: 4-part review (January 2025) with detailed findings
- **`patent_analysis_feedback_response.md`**: Full feedback response plan with query details
- **`LITERATURE_REVIEW_2020-2025.md`**: Comprehensive literature review (60+ papers)
- **`EU_CENTRIC_REVISION_PLAN_V2.md`**: Revision strategy and word count targets

### Research Context
- **Main finding**: EU patent share declined while China surged; EU last in quality despite 2nd in volume
- **Key insight**: China treats EVs as consumer electronics (rapid iteration), EU relies on traditional auto engineering
- **Strategic recommendation**: EU should pursue "Premium Sustainable Mobility" positioning

---

**Version**: Updated 2025-01-25 (post EU-centric revision, ~10,165 words)
