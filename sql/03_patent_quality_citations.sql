-- Query 3: Patent Quality Metrics - Forward Citations Analysis
-- Purpose: Calculate citation-based quality metrics by region and technology domain
-- Metrics: average citations, median citations, 90th percentile citations

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

-- Count forward citations for each patent
-- Optimized: filter citing patents by year and use UNNEST for better performance
citations_unnested AS (
  SELECT
    citing.publication_number as citing_pub,
    citation_struct.publication_number as cited_pub
  FROM `patents-public-data.patents.publications` citing,
    UNNEST(citing.citation) AS citation_struct
  WHERE citing.filing_date >= 20140101
    AND citing.filing_date <= 20241231
    AND citation_struct.publication_number IS NOT NULL
),

patent_citations AS (
  SELECT
    cited_pub AS publication_number,
    COUNT(DISTINCT citing_pub) as forward_citations
  FROM citations_unnested
  GROUP BY cited_pub
)

SELECT
  pdr.region,
  cm.application_area,
  CAST(pdr.filing_date / 10000 AS INT64) AS year,
  COUNT(DISTINCT pdr.publication_number) as patent_count,
  ROUND(AVG(IFNULL(pc.forward_citations, 0)), 2) as avg_citations,
  ROUND(APPROX_QUANTILES(IFNULL(pc.forward_citations, 0), 100)[OFFSET(50)], 2) as median_citations,
  ROUND(APPROX_QUANTILES(IFNULL(pc.forward_citations, 0), 100)[OFFSET(90)], 2) as p90_citations
FROM patent_data_regional pdr
LEFT JOIN patent_citations pc ON pdr.publication_number = pc.publication_number
JOIN cpc_mapping cm ON pdr.cpc_code = cm.symbol
WHERE cm.application_area IS NOT NULL
  AND pdr.region IS NOT NULL
GROUP BY pdr.region, cm.application_area, year
ORDER BY pdr.region, cm.application_area, year;
