-- Query 2: Collaborative Patents Analysis
-- Purpose: Identify patents with co-inventors from multiple regions
-- Analyzes EU-US, EU-CN, US-CN, and other collaboration patterns

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

patent_assignees AS (
  SELECT
    p.publication_number,
    p.filing_date,
    cpc_code.code AS cpc_code_str,
    ARRAY_AGG(DISTINCT
      CASE
        WHEN assignee.country_code = 'CN' THEN 'CN'
        WHEN assignee.country_code = 'US' THEN 'US'
        WHEN assignee.country_code IN (SELECT country_code FROM eu_countries) THEN 'EU'
        WHEN assignee.country_code = 'JP' THEN 'JP'
        WHEN assignee.country_code = 'KR' THEN 'KR'
        ELSE NULL
      END
      IGNORE NULLS
    ) as regions
  FROM `patents-public-data.patents.publications` p,
    UNNEST(p.cpc) AS cpc_code,
    UNNEST(p.assignee_harmonized) AS assignee
  WHERE p.filing_date >= 20140101 AND p.filing_date <= 20241231
  GROUP BY p.publication_number, p.filing_date, cpc_code_str
),

collaborative_patents AS (
  SELECT
    publication_number,
    filing_date,
    cpc_code_str,
    regions,
    ARRAY_LENGTH(regions) as region_count,
    CASE
      WHEN 'EU' IN UNNEST(regions) AND 'US' IN UNNEST(regions) THEN 'EU-US'
      WHEN 'EU' IN UNNEST(regions) AND 'CN' IN UNNEST(regions) THEN 'EU-CN'
      WHEN 'US' IN UNNEST(regions) AND 'CN' IN UNNEST(regions) THEN 'US-CN'
      WHEN 'EU' IN UNNEST(regions) AND 'JP' IN UNNEST(regions) THEN 'EU-JP'
      WHEN 'EU' IN UNNEST(regions) AND 'KR' IN UNNEST(regions) THEN 'EU-KR'
      WHEN 'US' IN UNNEST(regions) AND 'JP' IN UNNEST(regions) THEN 'US-JP'
      WHEN 'US' IN UNNEST(regions) AND 'KR' IN UNNEST(regions) THEN 'US-KR'
      WHEN 'CN' IN UNNEST(regions) AND 'JP' IN UNNEST(regions) THEN 'CN-JP'
      WHEN 'CN' IN UNNEST(regions) AND 'KR' IN UNNEST(regions) THEN 'CN-KR'
      WHEN 'JP' IN UNNEST(regions) AND 'KR' IN UNNEST(regions) THEN 'JP-KR'
      WHEN ARRAY_LENGTH(regions) > 2 THEN 'Multi-lateral'
      ELSE 'Single-region'
    END as collaboration_type
  FROM patent_assignees
  WHERE ARRAY_LENGTH(regions) > 0
)

SELECT
  CAST(filing_date / 10000 AS INT64) AS year,
  cm.application_area,
  cp.collaboration_type,
  COUNT(DISTINCT cp.publication_number) as patent_count
FROM collaborative_patents cp
JOIN cpc_mapping cm ON cp.cpc_code_str = cm.symbol
WHERE cm.application_area IS NOT NULL
  AND cp.region_count >= 1
GROUP BY year, application_area, collaboration_type
ORDER BY year, application_area, collaboration_type;
