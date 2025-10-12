-- Query 6: Generality & Originality Indices (Hall-Jaffe-Trajtenberg Method)
-- Purpose: Calculate patent quality metrics beyond simple citation counts
-- Generality: Breadth of impact (diversity of CPC classes citing this patent)
-- Originality: Breadth of knowledge sources (diversity of CPC classes cited by this patent)
-- Formula: Index = 1 - Σ(share in each CPC class)² (Herfindahl-based)

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
    AND p.filing_date <= 20231231  -- Exclude 2024 for citation maturity
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

-- Generality: Diversity of CPC classes in patents that cite this patent
citing_cpc_shares AS (
  SELECT
    cited_pub.publication_number,
    cited_pub.region,
    cm_cited.application_area,
    SUBSTR(citing_cpc.code, 1, 4) as citing_cpc_class,  -- Use 4-digit CPC class
    COUNT(*) as cite_count,
    COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY cited_pub.publication_number) as class_share
  FROM `patents-public-data.patents.publications` citing_p,
    UNNEST(citing_p.citation) as citation_struct,
    UNNEST(citing_p.cpc) as citing_cpc
  JOIN patent_data_regional cited_pub ON citation_struct.publication_number = cited_pub.publication_number
  JOIN cpc_mapping cm_cited ON cited_pub.cpc_code = cm_cited.symbol
  WHERE citing_p.filing_date >= 20140101
    AND citation_struct.publication_number IS NOT NULL
    AND cm_cited.application_area IS NOT NULL
  GROUP BY cited_pub.publication_number, cited_pub.region, cm_cited.application_area, citing_cpc_class
),

generality_per_patent AS (
  SELECT
    publication_number,
    region,
    application_area,
    1 - SUM(POW(class_share, 2)) as generality_index,
    COUNT(DISTINCT citing_cpc_class) as num_citing_classes
  FROM citing_cpc_shares
  GROUP BY publication_number, region, application_area
),

-- Originality: Diversity of CPC classes in patents cited by this patent
cited_cpc_shares AS (
  SELECT
    citing_pub.publication_number,
    citing_pub.region,
    cm_citing.application_area,
    SUBSTR(cited_cpc.code, 1, 4) as cited_cpc_class,  -- Use 4-digit CPC class
    COUNT(*) as cited_count,
    COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY citing_pub.publication_number) as class_share
  FROM `patents-public-data.patents.publications` citing_p
  JOIN patent_data_regional citing_pub ON citing_p.publication_number = citing_pub.publication_number
  JOIN cpc_mapping cm_citing ON citing_pub.cpc_code = cm_citing.symbol,
    UNNEST(citing_p.citation) as citation_struct
  JOIN `patents-public-data.patents.publications` cited_p ON citation_struct.publication_number = cited_p.publication_number,
    UNNEST(cited_p.cpc) as cited_cpc
  WHERE citing_p.filing_date >= 20140101
    AND citation_struct.publication_number IS NOT NULL
    AND cm_citing.application_area IS NOT NULL
  GROUP BY citing_pub.publication_number, citing_pub.region, cm_citing.application_area, cited_cpc_class
),

originality_per_patent AS (
  SELECT
    publication_number,
    region,
    application_area,
    1 - SUM(POW(class_share, 2)) as originality_index,
    COUNT(DISTINCT cited_cpc_class) as num_cited_classes
  FROM cited_cpc_shares
  GROUP BY publication_number, region, application_area
)

-- Aggregate by region and application area
SELECT
  COALESCE(g.region, o.region) as region,
  COALESCE(g.application_area, o.application_area) as application_area,
  COUNT(DISTINCT COALESCE(g.publication_number, o.publication_number)) as patent_count,
  ROUND(AVG(g.generality_index), 3) as avg_generality,
  ROUND(AVG(o.originality_index), 3) as avg_originality,
  ROUND(APPROX_QUANTILES(g.generality_index, 100)[OFFSET(50)], 3) as median_generality,
  ROUND(APPROX_QUANTILES(o.originality_index, 100)[OFFSET(50)], 3) as median_originality,
  ROUND(AVG(g.num_citing_classes), 1) as avg_citing_classes,
  ROUND(AVG(o.num_cited_classes), 1) as avg_cited_classes
FROM generality_per_patent g
FULL OUTER JOIN originality_per_patent o ON g.publication_number = o.publication_number
WHERE COALESCE(g.region, o.region) IS NOT NULL
  AND COALESCE(g.application_area, o.application_area) IS NOT NULL
GROUP BY region, application_area
ORDER BY region, application_area;
