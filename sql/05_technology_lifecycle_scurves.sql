-- Query 5: Technology Life Cycle Analysis (S-Curves)
-- Purpose: Calculate growth rates, acceleration, and lifecycle stages for each technology domain
-- Stages: Emergence → Growth → Maturity → Decline

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

-- Base data: patent counts by domain, region, and year
patent_data_by_domain AS (
  SELECT
    pdr.region,
    cm.application_area,
    CAST(pdr.filing_date / 10000 AS INT64) AS year,
    COUNT(DISTINCT pdr.publication_number) AS patent_count
  FROM patent_data_regional pdr
  JOIN cpc_mapping cm ON pdr.cpc_code = cm.symbol
  WHERE cm.application_area IS NOT NULL
    AND pdr.region IS NOT NULL
  GROUP BY region, application_area, year
),

-- Calculate year-over-year growth rates
yearly_growth AS (
  SELECT
    application_area,
    region,
    year,
    patent_count,
    LAG(patent_count) OVER (PARTITION BY region, application_area ORDER BY year) as prev_year_count,
    (patent_count - LAG(patent_count) OVER (PARTITION BY region, application_area ORDER BY year))
      / NULLIF(LAG(patent_count) OVER (PARTITION BY region, application_area ORDER BY year), 0) as growth_rate
  FROM patent_data_by_domain
),

-- Calculate acceleration (second derivative) and classify lifecycle stages
growth_acceleration AS (
  SELECT
    *,
    growth_rate - LAG(growth_rate) OVER (PARTITION BY region, application_area ORDER BY year) as acceleration,
    CASE
      WHEN growth_rate > 0.15 AND (growth_rate - LAG(growth_rate) OVER (PARTITION BY region, application_area ORDER BY year)) > 0 THEN 'Emergence'
      WHEN growth_rate > 0.10 AND (growth_rate - LAG(growth_rate) OVER (PARTITION BY region, application_area ORDER BY year)) <= 0 THEN 'Growth'
      WHEN growth_rate BETWEEN 0.03 AND 0.10 THEN 'Maturity'
      WHEN growth_rate < 0.03 THEN 'Decline'
      ELSE 'Uncertain'
    END as lifecycle_stage
  FROM yearly_growth
)

SELECT
  application_area,
  region,
  year,
  patent_count,
  prev_year_count,
  ROUND(IFNULL(growth_rate * 100, 0), 2) as growth_rate_pct,
  ROUND(IFNULL(acceleration * 100, 0), 2) as acceleration_pct,
  lifecycle_stage
FROM growth_acceleration
ORDER BY application_area, region, year;
