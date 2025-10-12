-- Query 7: Knowledge Flow Networks (Directional Citation Analysis)
-- Purpose: Analyze inter-regional knowledge flows through patent citations
-- Metrics: Citation flows (who cites whom), self-citation rates, network centrality, citation lags

WITH cpc_mapping AS (
  SELECT
    symbol,
    CASE
      -- Battery Technology (excluding fuel cells H01M8)
      WHEN symbol LIKE 'H01M4%' THEN 'Battery Technology'   -- Electrodes
      WHEN symbol LIKE 'H01M6%' THEN 'Battery Technology'   -- Primary cells
      WHEN symbol LIKE 'H01M10%' THEN 'Battery Technology'  -- Secondary cells (Li-ion, etc.)
      WHEN symbol LIKE 'H01M12%' THEN 'Battery Technology'  -- Hybrid cells
      WHEN symbol LIKE 'H01M50%' THEN 'Battery Technology'  -- Constructional details
      WHEN symbol LIKE 'H01G11%' THEN 'Battery Technology'  -- Supercapacitors

      -- EV Propulsion & Charging
      WHEN symbol LIKE 'B60L%' THEN 'EV Propulsion & Charging'
      WHEN symbol LIKE 'H02K%' THEN 'EV Propulsion & Charging'
      WHEN symbol LIKE 'H02P%' THEN 'EV Propulsion & Charging'
      WHEN symbol LIKE 'H02J7%' THEN 'EV Propulsion & Charging'
      WHEN symbol LIKE 'H02M%' THEN 'EV Propulsion & Charging'
      WHEN symbol LIKE 'B60W%' THEN 'Autonomous Driving & ADAS'
      WHEN symbol LIKE 'G05D1%' THEN 'Autonomous Driving & ADAS'
      WHEN symbol LIKE 'B60K6%' THEN 'Hybrid Powertrains'
      WHEN symbol LIKE 'F02D%' THEN 'Hybrid Powertrains'
      WHEN symbol LIKE 'B60R%' THEN 'Vehicle Safety Systems'
      WHEN symbol LIKE 'B60Q%' THEN 'Vehicle Safety Systems'
      WHEN symbol LIKE 'B60H%' THEN 'Thermal Management'
      WHEN symbol LIKE 'F28D%' THEN 'Thermal Management'
      WHEN symbol LIKE 'B60K35%' THEN 'Infotainment & Connectivity'
      WHEN symbol LIKE 'B60K37%' THEN 'Infotainment & Connectivity'
      WHEN symbol LIKE 'H04W4%' THEN 'Infotainment & Connectivity'
      WHEN symbol LIKE 'G07C5%' THEN 'Infotainment & Connectivity'
      WHEN symbol LIKE 'H04N7/18%' THEN 'Infotainment & Connectivity'
      WHEN symbol LIKE 'G08G%' THEN 'Infotainment & Connectivity'
      ELSE NULL
    END AS application_area
  FROM `patents-public-data.cpc.definition`
  WHERE symbol IS NOT NULL
),

eu_countries AS (
  SELECT country_code FROM UNNEST([
    'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR',
    'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL',
    'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
  ]) AS country_code
),

patent_data AS (
  SELECT
    p.publication_number,
    p.filing_date,
    p.publication_date,
    cpc_code.code AS cpc_code,
    assignee.country_code AS assignee_country
  FROM `patents-public-data.patents.publications` p,
    UNNEST(p.cpc) AS cpc_code,
    UNNEST(p.assignee_harmonized) AS assignee
  WHERE p.filing_date IS NOT NULL
    AND p.filing_date >= 20140101
    AND p.filing_date <= 20241231
    AND assignee.country_code IS NOT NULL
),

patent_data_regional AS (
  SELECT DISTINCT
    pd.publication_number,
    pd.filing_date,
    pd.publication_date,
    pd.cpc_code,
    CASE
      WHEN pd.assignee_country = 'CN' THEN 'CN'
      WHEN pd.assignee_country = 'US' THEN 'US'
      WHEN pd.assignee_country IN (SELECT country_code FROM eu_countries) THEN 'EU'
      WHEN pd.assignee_country = 'JP' THEN 'JP'
      WHEN pd.assignee_country = 'KR' THEN 'KR'
      ELSE NULL
    END AS region
  FROM patent_data pd
  WHERE pd.assignee_country IN ('CN', 'US', 'JP', 'KR')
     OR pd.assignee_country IN (SELECT country_code FROM eu_countries)
),

-- Cross-regional citation flows (who cites whom?)
citation_flows AS (
  SELECT
    citing_patent.region as citing_region,
    cited_patent.region as cited_region,
    cm.application_area,
    CAST(citing_patent.filing_date / 10000 AS INT64) as citing_year,
    COUNT(DISTINCT citing_patent.publication_number) as citation_count,
    AVG(
      DATE_DIFF(
        PARSE_DATE('%Y%m%d', CAST(citing_patent.filing_date AS STRING)),
        PARSE_DATE('%Y%m%d', CAST(cited_patent.filing_date AS STRING)),
        DAY
      )
    ) as avg_lag_days
  FROM `patents-public-data.patents.publications` citing_p
  JOIN patent_data_regional citing_patent ON citing_p.publication_number = citing_patent.publication_number
  JOIN cpc_mapping cm ON citing_patent.cpc_code = cm.symbol,
    UNNEST(citing_p.citation) as citation_struct
  JOIN patent_data_regional cited_patent ON citation_struct.publication_number = cited_patent.publication_number
  WHERE citing_patent.filing_date >= 20140101
    AND cited_patent.filing_date >= 20140101
    AND cm.application_area IS NOT NULL
    AND citing_patent.region IS NOT NULL
    AND cited_patent.region IS NOT NULL
    AND citation_struct.publication_number IS NOT NULL
  GROUP BY citing_region, cited_region, application_area, citing_year
),

-- Self-citation analysis (regional insularity)
self_citation_rates AS (
  SELECT
    citing_region,
    citing_year,
    application_area,
    SUM(CASE WHEN citing_region = cited_region THEN citation_count ELSE 0 END) as self_citations,
    SUM(citation_count) as total_citations,
    ROUND(SUM(CASE WHEN citing_region = cited_region THEN citation_count ELSE 0 END) / NULLIF(SUM(citation_count), 0), 3) as self_citation_rate
  FROM citation_flows
  GROUP BY citing_region, citing_year, application_area
)

-- Main output: Cross-regional flows with self-citation context
SELECT
  cf.citing_year as year,
  cf.citing_region,
  cf.cited_region,
  cf.application_area,
  cf.citation_count,
  ROUND(cf.avg_lag_days / 365.25, 1) as avg_lag_years,
  sc.self_citation_rate,
  CASE
    WHEN cf.citing_region = cf.cited_region THEN 'Self-citation'
    ELSE 'Cross-regional'
  END as flow_type
FROM citation_flows cf
LEFT JOIN self_citation_rates sc
  ON cf.citing_region = sc.citing_region
  AND cf.citing_year = sc.citing_year
  AND cf.application_area = sc.application_area
ORDER BY cf.citing_year, cf.application_area, cf.citation_count DESC;
