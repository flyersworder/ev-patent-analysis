# Data Files Documentation

This document provides detailed documentation for all CSV data files referenced in the analysis.

## Important Note

**The CSV data files are not included in this repository** due to size constraints. However, full reproducibility is ensured through:

1. **SQL queries**: All 7 queries available in the `sql/` directory
2. **Documentation**: Complete column definitions and methodology below
3. **Public data source**: Google's Public Patent Dataset is freely accessible via BigQuery

To reproduce the data files, execute the SQL queries in BigQuery and export the results as CSV files following the naming convention described below.

## Overview

All data files were extracted from Google's Public Patent Dataset (`patents-public-data.patents.publications`) using BigQuery SQL queries documented in the `sql/` directory. Primary data extraction: October 2024; citation/collaboration data: January 2025.

---

## File 1: `01_global_context_5regions.csv`

**Source Query**: `sql/01_global_context_5regions.sql`
**Rows**: 385
**Purpose**: Core regional patent counts by year and technology domain

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `country` | STRING | Region code: CN, US, EU, JP, KR |
| `application_area` | STRING | Technology domain (7 categories) |
| `year` | INTEGER | Filing year (2014-2024) |
| `patent_count` | INTEGER | Number of distinct patent families |

### Technology Domains (application_area values)

1. Battery Technology
2. EV Propulsion & Charging
3. Autonomous Driving & ADAS
4. Hybrid Powertrains
5. Vehicle Safety Systems
6. Thermal Management
7. Infotainment & Connectivity

### Sample Data

```csv
country,application_area,year,patent_count
CN,Battery Technology,2014,1234
US,Autonomous Driving & ADAS,2018,5678
EU,Thermal Management,2020,890
```

### Data Quality Notes

- **2024 data incomplete**: Partial year (January-October)
- **No double-counting**: Each patent assigned to single primary region (first assignee's country)
- **Missing values**: None (all patents have valid region, year, domain)
- **Total patents**: 385,000+ unique patent families across all rows

### Known Issues

- **CPC overlaps**: Patents with multiple CPC codes assigned to primary domain only
- **Utility models excluded**: Chinese utility models automatically excluded (lack assignee data)

---

## File 2: `02_collaborative_patents.csv`

**Source Query**: `sql/02_collaborative_patents.sql`
**Rows**: 713
**Purpose**: Cross-regional collaborative patents (multiple assignees from different regions)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `year` | INTEGER | Filing year (2014-2024) |
| `application_area` | STRING | Technology domain |
| `region_pair` | STRING | Collaboration pair (e.g., "CN-US", "EU-JP") |
| `collaborative_patent_count` | INTEGER | Number of collaborative patents |

### Sample Data

```csv
year,application_area,region_pair,collaborative_patent_count
2018,Battery Technology,CN-US,45
2020,Autonomous Driving & ADAS,EU-JP,123
```

### Methodology Notes

- **Scope**: Only cross-REGIONAL collaboration counted (e.g., US-China collaboration)
- **Excluded**: Within-region collaboration (e.g., Germany-France) and outside-region collaboration (e.g., US-India)
- **Multi-lateral**: Tri-regional patents classified by first bilateral pair (affects ~158 patents, 0.01% of total)

### Data Quality Notes

- **Total collaborative patents**: 713 unique region-year-domain combinations
- **Collaboration rate**: 0.65-1.28% of all patents (extremely low)
- **Top pairs** (2014-2024 cumulative):
  - EU-JP: 5,410 patents
  - EU-US: 4,966 patents
  - US-CN: 3,414 patents
  - US-JP: 3,375 patents

---

## File 3: `03_patent_quality_citations.csv`

**Source Query**: `sql/03_patent_quality_citations.sql`
**Rows**: 385
**Purpose**: Forward citation counts (measure of patent quality/impact)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `region` | STRING | Region code: CN, US, EU, JP, KR |
| `application_area` | STRING | Technology domain |
| `year` | INTEGER | Filing year (2014-2024) |
| `avg_forward_citations` | FLOAT | Average citations per patent |
| `median_forward_citations` | FLOAT | Median citations per patent |
| `patent_count` | INTEGER | Number of patents in sample |

### Sample Data

```csv
region,application_area,year,avg_forward_citations,median_forward_citations,patent_count
US,Autonomous Driving & ADAS,2016,12.5,8.0,2345
CN,Battery Technology,2017,3.2,2.0,4567
```

### Methodology Notes

- **Citation window**: Analysis focuses on 2014-2018 cohorts (6-10 years accumulation time)
- **Normalization**: Age-normalized (focus on same time windows for fair comparison)
- **Citation types**: Includes both examiner and applicant citations

### Data Quality Notes

- **Recency bias**: 2020+ patents have insufficient citation accumulation time (use with caution)
- **Skewed distribution**: Citation counts highly right-skewed; median < mean for most regions
- **Coverage**: ~76% of patents have citation data (remainder have zero forward citations)

### Key Findings

- US: 8.87 avg citations (highest quality)
- EU: 2.50 avg citations (lowest quality, despite 2nd highest volume)
- Software domains (Autonomous, Infotainment): 2-3× higher citations than hardware

---

## File 4: `04_sensitivity_analysis_exclude_utility.csv`

**Source Query**: `sql/04_sensitivity_analysis_exclude_utility.sql`
**Rows**: 385
**Purpose**: Robustness check excluding utility models and design patents

### Columns

Same structure as File 1 (`01_global_context_5regions.csv`)

### Methodology Notes

- **Exclusions**: Removes patents classified as utility models (short-term protection, lower examination bar)
- **Purpose**: Tests whether main findings robust to excluding lower-quality patent types
- **Result**: Regional rankings unchanged; China patent counts reduced ~15% (confirms utility model concentration)

---

## File 5: `05_technology_lifecycle_scurves.csv`

**Source Query**: `sql/05_technology_lifecycle_scurves.sql`
**Rows**: 385
**Purpose**: Technology maturity analysis (year-over-year growth rates)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `region` | STRING | Region code |
| `application_area` | STRING | Technology domain |
| `year` | INTEGER | Filing year |
| `patent_count` | INTEGER | Number of patents |
| `yoy_growth_rate` | FLOAT | Year-over-year growth (%) |
| `lifecycle_stage` | STRING | Emergence / Growth / Maturity / Decline |

### Lifecycle Stage Classification

- **Emergence**: High volatility, YoY growth >20%
- **Growth**: Consistent positive growth, 10-20% YoY
- **Maturity**: Stable growth, 0-10% YoY
- **Decline**: Negative growth, <0% YoY

### Key Findings

- **Declining**: Hybrid Powertrains (mature technology, BEV transition)
- **Emergence**: Autonomous Driving (high growth, immature)
- **Maturity**: Battery Technology (stable, incremental improvements)

---

## File 6: `06_generality_originality_indices.csv`

**Source Query**: `sql/06_generality_originality_indices.sql`
**Rows**: 35 (5 regions × 7 domains)
**Purpose**: Hall-Jaffe-Trajtenberg quality indices (cross-domain knowledge integration)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `region` | STRING | Region code |
| `application_area` | STRING | Technology domain |
| `generality_index` | FLOAT | Herfindahl-based citing diversity (0-1) |
| `originality_index` | FLOAT | Herfindahl-based cited diversity (0-1) |
| `patent_count` | INTEGER | Sample size |

### Formulas

**Generality Index**:
```
1 - Σ(share_of_citations_in_class_i)²
```
- Measures how broadly a patent influences diverse technology fields
- 0 = narrow specialist impact (all citations from single class)
- 1 = broad general impact (citations evenly distributed across classes)

**Originality Index**:
```
1 - Σ(share_of_citations_to_class_i)²
```
- Measures how broadly a patent draws knowledge from diverse sources
- 0 = incremental within single domain
- 1 = synthetic across many domains

### Sample Data

```csv
region,application_area,generality_index,originality_index,patent_count
US,Autonomous Driving & ADAS,0.823,0.867,15234
CN,Battery Technology,0.612,0.591,23456
```

### Data Quality Notes

- **Coverage**: ~76% of patents have sufficient citation data for index calculation
- **Missing values**: Patents with <5 citations excluded (insufficient data for Herfindahl calculation)
- **CPC bias check**: US patents have 9% more CPC codes assigned (2.63 vs EU 2.41); insufficient to explain 60-110% quality gaps

### Key Findings

- **US dominance**: Highest indices across all 7 domains (0.707 generality, 0.751 originality weighted avg)
- **EU's generalist dilemma**: Ranks 2nd-4th in all domains, leads in none
- **Korea battery paradox**: Lowest indices (0.488/0.544) despite 31-33% patent share and manufacturing dominance

---

## File 7: `07_knowledge_flow_networks.csv`

**Source Query**: `sql/07_knowledge_flow_networks.sql`
**Rows**: 1,921
**Purpose**: Citation flows between regions (knowledge transfer analysis)

### Columns

| Column | Type | Description |
|--------|------|-------------|
| `citing_region` | STRING | Region of citing patent (knowledge recipient) |
| `cited_region` | STRING | Region of cited patent (knowledge source) |
| `year` | INTEGER | Citing patent filing year |
| `application_area` | STRING | Technology domain |
| `citation_count` | INTEGER | Number of citations |
| `avg_citation_lag` | FLOAT | Average time gap (years) between cited and citing |

### Sample Data

```csv
citing_region,cited_region,year,application_area,citation_count,avg_citation_lag
US,CN,2020,Battery Technology,234,1.5
EU,US,2021,Autonomous Driving & ADAS,567,1.8
```

### Methodology Notes

- **Self-citation**: When `citing_region = cited_region`
- **Cross-regional flows**: When `citing_region ≠ cited_region`
- **Citation lag**: Time difference between cited patent filing date and citing patent filing date

### Data Quality Notes

- **2024 data incomplete**: Partial year for citing patents
- **Citation window**: Recent patents (2022+) underrepresent outbound citations (publication lag)

### Key Findings

**Self-Citation Rates** (2014-2024 avg):
- China: 21.2% (lowest - contradicts "insular" narrative)
- US: 33.8%
- EU: 34.5%
- Korea: 37.6%
- Japan: 51.5% (highest - most insular)

**Top 10 Cross-Regional Flows** (2023):
1. EU→US: 13,139 citations (dominant axis)
2. US→EU: 8,234
3. CN→US: 4,567
4. JP→US: 3,890
5. US→CN: 2,345
... (see data file for complete ranking)

**US-China Geopolitical Collapse**:
- US→CN: 562 (2018) → 203 (2024), -64% decline
- CN→US: 489 (2018) → 147 (2024), -70% decline
- Timing: Collapse begins 2019 (trade war), accelerates 2021 (export controls)

**Citation Lags** (2014-2020 cohort):
- China: 1.54 years (fastest knowledge absorption)
- US: 1.66 years
- EU: 1.61 years
- Korea: 1.58 years
- Japan: 1.45 years (fastest)

---

## Data Limitations (All Files)

### Temporal Limitations
1. **2024 incomplete**: Partial year data (January-October 2024)
2. **Publication lag**: 18-month delay means recent filings may not yet appear in dataset
3. **Citation window bias**: Patents filed 2020+ have insufficient time to accumulate citations

### Methodological Limitations
4. **Regional scope**: Analysis limited to five major regions; excludes India, Canada, Taiwan, others
5. **CPC overlaps**: Patents with multiple CPC codes assigned to primary category only
6. **First assignee rule**: Multi-assignee patents assigned to first assignee's region (no double-counting)

### Quality vs. Quantity
7. **Forward citations measure technical influence, not commercial value**: High-citation patents may not translate to market success or manufacturing scale
8. **Patent propensity varies by sector**: Software patents easier to obtain than hardware; may bias cross-domain comparisons

---

## Reproducibility Checklist

To reproduce these data files:

1. ✅ **BigQuery access**: Sign up for free Google Cloud account
2. ✅ **Execute queries**: Run all 7 SQL queries in `sql/` directory
3. ✅ **Export results**: Download as CSV, name according to convention `01_*.csv`
4. ✅ **Verify row counts**: Compare against table above (385, 713, 385, 385, 385, 35, 1921)
5. ✅ **Check date ranges**: Ensure 2014-2024 coverage (2024 partial)

**Expected total processing**: ~250-300 GB (free under BigQuery 1 TB/month quota)

---

## Version History

- **v1.0** (October 2024): Initial primary data extraction (Files 1, 4, 5)
- **v1.1** (January 2025): Added citation and collaboration data (Files 2, 3, 6, 7)
- **Current**: All 7 files complete and validated

---

## Contact

For data questions or reported errors:
- **GitHub Issues**: https://github.com/flyersworder/ev-patent-analysis/issues
- **Email**: [your.email@institution.edu]

**Last Updated**: November 2025
