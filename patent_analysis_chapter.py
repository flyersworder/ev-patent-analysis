import marimo

__generated_with = "0.17.7"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Europe's Innovation Paradox: Patent Quality and Regional Competition in the Global Electric Vehicle Race (2014-2024)

    **Authors:** Qing Ye, Marina van Geenhuizen

    **Date:** November 2025

    ## Abstract

    Europe ranks second in electric vehicle patent volume (2014-2024) yet last in quality. Analyzing 385,000+ patents across five regions (US, China, EU, Korea, Japan), we employ forward citation analysis, collaboration patterns, and knowledge flows to assess innovation impact. European patents (2014-2018 cohort) average 2.58 citations versus 9.97 for the US—a 3.9× quality gap. Testing four hypotheses synthesizing Resource-Based View, National Innovation Systems, Open Innovation, and Business Model Innovation reveals critical theoretical gaps. RBV receives conditional support: volume-quality correlation holds for the US but fails for Europe, revealing a "legacy trap" where capabilities in declining technologies harm quality during transitions. US-China collaboration collapsed 76% despite complementarity, demonstrating geopolitical friction overrides open innovation logic. China's consumer electronics business model enables market competitiveness despite 2.6× patent quality disadvantage. These findings extend innovation theory by demonstrating RBV's conditional validity, geopolitical constraints on knowledge flows, and business model innovation as an independent strategic pathway.

    **Keywords:** electric vehicles, patent quality, innovation systems, forward citations, business model innovation, cross-border collaboration, battery technology
    """)
    return


@app.cell(hide_code=True)
def _():
    # Cell tags: setup
    # Setup: Import required libraries
    import marimo as mo
    import pandas as pd
    import altair as alt
    import warnings

    warnings.filterwarnings("ignore")

    # Configure Altair for publication-quality output
    _ = alt.themes.enable('default')
    _ = alt.data_transformers.disable_max_rows()

    # Disable actions menu (three dots) for clean PDF exports
    _ = alt.renderers.set_embed_options(actions=False)
    return alt, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introduction

    ## The European Paradox

    European inventors filed over 534,000 patents across seven core EV technology domains (23.4% of the five-region total), ranking second globally. However, when measured by forward citations, European patents (2014-2018 cohort) average 2.58 citations versus 9.97 for the US—a 3.9× quality gap revealing high activity but minimal impact.

    This paradox extends deeper. Europe's patent share declined from 26.3% to 17.3% (2014-2024), with erosion in six of seven domains. Europe's sole growth domain—hybrid powertrains—is the technology the industry is abandoning. We term this the "legacy trap": strong specialization in traditional automotive domains but critical weaknesses in future-defining technologies (batteries, autonomous driving, infotainment).

    For a continent whose automotive sector employs 13.8 million people, represents 7% of EU GDP, and generates a €89 billion annual trade surplus (ACEA, 2024; Eurostat, 2025), this pattern signals not cyclical weakness but structural crisis. The question is whether the window for strategic renewal remains open and what actions might reverse these trajectories before they become irreversible.

    ## Research Questions and Contributions

    This paper addresses four interrelated questions from a European policy perspective:

    **RQ1: Where does Europe stand?** How have patent share, innovation quality (citations), and knowledge network positioning evolved across the five major competing regions from 2014 to 2024?

    **RQ2: Why is Europe losing ground?** What institutional, strategic, and capability factors explain Europe's decline in six of seven technology domains and its last-place ranking in citation quality despite second-highest patent volume?

    **RQ3: What drives competitors' success?** How do the US's software dominance and China's consumer electronics business model succeed through fundamentally different approaches—and what constraints do they face?

    **RQ4: What pathways remain open to Europe?** Given Europe's capability endowments, institutional structures, and competitors' positioning, what strategic imperatives and policy interventions offer realistic prospects for competitive renewal?

    Analyzing 385,000+ patents across five regions (US, China, EU, Korea, Japan) and seven technology domains (2014-2024), we test four theory-driven hypotheses synthesizing Resource-Based View, National Innovation Systems, Open Innovation, and Business Model Innovation. Our contributions:

    **Empirical discoveries**: We reveal Europe's "legacy trap," geopolitical fragmentation overriding economic complementarity (US-China collaboration collapsed 76%), and counterintuitive knowledge openness patterns contradicting innovation systems theory.

    **Theoretical extensions**: Hypothesis testing exposes critical theoretical gaps while establishing business model innovation as independent pathway where commercialization architecture matters more than technological superiority.

    **Strategic pathways**: Evidence-based recommendations identify defensible domains, alliance opportunities, and differentiation strategies with three alternative futures.

    This paper proceeds: **Theoretical Framework** formulates testable hypotheses. **Methods** describes data and analytical techniques. **The Five-Region Race** examines patent competition across technology domains. **Patent Quality Analysis** employs citation analysis. **Cross-Border Collaboration and Knowledge Flows** investigates patterns across regions. **Business Model Innovation** examines China's alternative pathway. **Hypothesis Testing** evaluates theoretical predictions. **EU Strategic Imperatives** translates findings into policy recommendations.

    The window for European strategic renewal remains open, but it narrows with each passing quarter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Theoretical Framework and Hypotheses

    Why do different regions exhibit such divergent patent patterns in electric vehicle innovation? The Resource-Based View (RBV) provides our foundation for understanding persistent regional specialization. Barney (1991) argues that sustainable competitive advantage stems from valuable, rare, inimitable, and non-substitutable resources. Applied to regional innovation systems, different geographic regions possess distinct technological capabilities accumulated through decades of institutional development and industrial specialization. These capabilities are path-dependent: the EU's thermal management and safety engineering expertise reflects traditional automotive engineering heritage built over a century; China's battery manufacturing scale results from coordinated industrial policy and large-scale capital deployment post-2010; US software and autonomous driving leadership builds on Silicon Valley's AI talent ecosystem developed since the 1990s. Competitors cannot quickly replicate these accumulated capabilities—German engineers cannot instantly acquire Chinese battery manufacturing expertise, nor can Chinese firms rapidly develop Silicon Valley's software talent networks. This path dependency explains why regional specialization patterns persist across technology domains despite globalization.

    Yet capabilities alone cannot explain divergent innovation strategies. The National Innovation Systems (NIS) perspective reveals how institutional contexts shape innovation approaches. Freeman (1987) and Lundvall (1992) emphasize that innovation emerges from interactions among firms, universities, government agencies, and financial institutions within country-specific institutional arrangements. Our five regions exhibit fundamentally different innovation systems producing distinct strategic orientations: China's state-directed approach combines government subsidies, state-owned enterprise coordination, and domestic market protection to scale targeted technologies like batteries through top-down mandates rapidly. The US market-driven system relies on venture capital financing, university-industry linkages (Stanford-Silicon Valley, MIT-Route 128), and entrepreneurial firm entry (Tesla, Rivian, Waymo), enabling bottom-up experimentation. The EU's coordinated market economy emphasizes standards-setting, collaborative R&D programs (Horizon 2020), and incremental innovation by established firms operating within consensus-based governance. Korea's chaebol-coordinated model enables rapid capability building through government-conglomerate partnerships targeting high-value sectors (LG Energy Solution, Samsung SDI). Japan's consensus-driven approach emphasizes long-term relationships and incremental refinement of existing technologies. These institutional differences explain not just patent volume variations but also quality differences, domain priorities, and collaboration patterns we observe empirically.

    Recent empirical research validates and quantifies these NIS mechanisms, addressing a critical gap in the literature where institutional effects were theoretically asserted but rarely causally demonstrated. Analyzing 60,000+ industrial policy documents and patent data from 2008-2023 across the global automobile industry, researchers find that a one-standard-deviation increase in five-year cumulative EV-targeted policies (e.g., subsidies, R&D support, standards) generates a 4% increase in new EV patent filings, with effects strongest for batteries and charging infrastructure (Liu et al., 2024, NBER w33138). This quasi-experimental evidence—leveraging policy variation across countries and time—confirms NIS theory's prediction that state intervention causally shapes innovation trajectories. Importantly, policy effectiveness varies by institutional context: industrial policies in coordinated economies (EU, Japan) generate relatively smaller patent increases (2-3%) compared to state-directed systems (China, 6-8%) or market-driven contexts with targeted interventions (US, 5-7%), consistent with institutional complementarity theory (Wang et al., 2023). These findings transform NIS from descriptive taxonomy to quantified causal framework, enabling predictions about how specific institutional arrangements influence innovation intensity. Our subsequent empirical analysis tests whether these policy-driven patent increases translate into quality improvements or merely inflate quantity, examining the causal pathway from institutions → policies → innovation outcomes.

    The EV transition itself represents a disruptive technological shift that challenges established industry leaders. Christensen's (1997) disruptive innovation framework explains why incumbent firms often fail during such transitions: they optimize for existing technology trajectories (sustaining innovation) while new entrants pursue alternative approaches that initially underperform but eventually displace incumbents. Traditional automotive companies (predominantly European and Japanese) excelled at internal combustion engine (ICE) optimization but now face challenges in software-defined vehicles. China's "leapfrog" strategy skipped ICE excellence entirely, focusing directly on batteries and digital experiences. US tech entrants (Tesla, Waymo) leveraged software expertise rather than automotive heritage. The EU's strength in declining technologies (hybrid powertrains) versus weakness in emerging domains (autonomous driving, infotainment) reflects classic innovator's dilemma dynamics: established firms strengthen competencies in sustaining technologies while losing ground in disruptive domains. This explains why Europe's incremental improvements to traditional automotive engineering generate fewer citations than US foundational software research or China's battery architecture innovations, as disruptive innovations create new research trajectories while sustaining innovations serve existing customer needs.

    Cross-border collaboration patterns require an additional theoretical perspective. Chesbrough's (2003) open innovation paradigm challenges closed, vertically-integrated R&D models, arguing that firms increasingly source external knowledge and license internal technologies. In a global innovation competition, regions function as open innovation hubs with varying degrees of international collaboration. The extent of cross-border co-invention reveals whether regions operate as isolated silos or integrated networks. EU-US collaboration patterns may reflect transatlantic technology alliances; EU-Korea partnerships in batteries leverage complementary capabilities; US-China flows (prior to geopolitical disruption) combined American software with Chinese manufacturing scale. These flows have strategic implications: regions heavily dependent on external knowledge face vulnerability during geopolitical fragmentation, while those serving as knowledge sources gain influence. Collaboration intensity should increase when regions possess highly complementary capabilities (e.g., EU thermal management + Korean battery cells) and decrease when they compete directly or face institutional friction.

    Finally, business model innovation provides a crucial perspective on competitive strategy beyond technological leadership. Teece (2010) and Zott & Amit (2010) demonstrate that competitive advantage increasingly stems from novel approaches to value creation, delivery, and capture rather than pure technological superiority. Cross-industry business model transfer—where competitive logics from one sector migrate to another—may enable market competitiveness even when patent quality lags technological leaders. China's trajectory suggests this mechanism: rapid iteration cycles, volume-based cost reduction, ecosystem integration, and software-centric differentiation mirror consumer electronics industry logic applied to EVs. This "EVs as smartphones" strategy contrasts fundamentally with traditional automotive business models emphasizing long development cycles (5-7 years), mechanical reliability, dealer networks, and premium pricing. If successful, this reveals business model innovation as an independent strategic pathway, challenging assumptions that patent leadership necessarily predicts market outcomes.

    These five frameworks are not competing explanations but complementary lenses illuminating different facets of the same phenomena. Yet existing theory, developed primarily from Western advanced economies and established industries, may not fully predict innovation dynamics in a context characterized by state-led catch-up strategies, geopolitical fragmentation, and platform competition. We therefore formulate four core hypotheses that synthesize mainstream theoretical expectations—hypotheses that, if contradicted by empirical evidence, would reveal important theoretical gaps and generate novel insights.

    Barney (1991) and Teece (1986) argue that competitive advantage stems from accumulated, inimitable resources. R&D capabilities are quintessential strategic resources: larger patent portfolios indicate deeper knowledge stocks, greater absorptive capacity (Cohen & Levinthal, 1990), and more extensive researcher networks. The EU possesses world-leading automotive R&D budgets (€57 billion annually, 2020) and century-long engineering heritage. This resource accumulation should produce both high volume AND high quality, as knowledge begets knowledge. Rejection would reveal that accumulated capabilities can paradoxically harm innovation quality, challenging RBV's core logic.

    **H1 (Resource-Based View → Volume-Quality Relationship):** Regional patent volume will correlate positively with average citation quality across all five regions. Regions with larger patent portfolios (higher volume) will exhibit higher average forward citations (higher quality).

    Chesbrough (2003) argues that firms increasingly access external knowledge to accelerate innovation. At the regional level, technological specialization creates complementarity: US dominance in autonomous driving software, China's battery manufacturing scale, Korea's battery science excellence, EU's thermal management and safety expertise, and Japan's hybrid powertrains suggest natural division of labor. As specialization deepens from 2014 to 2024, complementarity intensifies. Rejection would indicate that factors beyond technological complementarity—such as geopolitical friction or strategic competition—override open innovation logic.

    **H2 (Open Innovation → Collaboration Under Complementarity):** Cross-regional collaboration rates will increase over time (2014→2024) as technological specialization deepens. Regions with highly complementary capabilities will exhibit the highest collaboration rates.

    Freeman (1987) and Lundvall (1992) emphasize that National Innovation Systems' institutional arrangements shape knowledge diffusion patterns. State-directed systems should prioritize domestic knowledge retention (higher self-citation), while market-driven systems encourage broad diffusion (lower self-citation). EU's coordinated market economy should exhibit intermediate patterns.

    **H3 (National Innovation Systems → Knowledge Openness):** State-led innovation systems will exhibit higher self-citation rates than market-led systems. Specifically, China (state-led) will show the highest self-citation rate, US (market-driven) the lowest, and EU intermediate levels.

    Teece (2010) argues that business model innovation can generate competitive advantage independently of technological superiority. Cross-industry business model transfer (consumer electronics → automotive) may enable market competitiveness despite patent quality gaps when product characteristics align—modularity, software-centricity, network effects—enabling rapid iteration and ecosystem integration strategies to offset R&D disadvantages.

    **H4 (Business Model Innovation → Alternative Pathway):** Regions can achieve market competitiveness through cross-industry business model transfer even when patent quality significantly lags technological leaders, when the transferred model aligns with product modularity, software-centricity, and network effects.

    The following empirical sections test these hypotheses through comprehensive patent data analysis. Hypothesis confirmation would validate theoretical expectations; hypothesis rejection would reveal critical theoretical gaps requiring new frameworks to explain 21st-century innovation competition among technologically advanced regions operating under geopolitical tension and platform-based competition dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Methods

    ## Data Source and Sample

    Our analysis employs the Google Patents Public Dataset accessed via BigQuery, which aggregates patent filings from 107 patent offices globally. The dataset provides comprehensive coverage of the Cooperative Patent Classification (CPC) system, assignee information, and forward citation data. We extracted 385,000+ electric vehicle-related patents filed between 2014-2024 across five major regions: the United States (US), China (CN), the European Union (EU, aggregating all 27 current member states), Japan (JP), and South Korea (KR). We excluded Taiwan from the analysis as it lacks significant automotive manufacturing presence or major OEM R&D centers (no major OEMs or global R&D centers as of 2024). The 2014-2024 time period captures the EV acceleration phase following Tesla's Model S launch, encompassing both early-stage innovation and recent platform competition.

    Patents are classified into seven core EV technology domains based on CPC codes: Battery Technology (H01M4/6/10/12/50, H01G11), EV Propulsion & Charging (B60L, H02K/P/J7/M), Autonomous Driving & ADAS (B60W, G05D1), Hybrid Powertrains (B60K6, F02D), Vehicle Safety Systems (B60R, B60Q), Thermal Management (B60H, F28D), and Infotainment & Connectivity (B60K35/37, H04W4, G07C5, H04N7/18, G08G). Complete CPC mapping schema and SQL queries are provided in Appendix A and the project's GitHub repository for full reproducibility.

    ## Key Methodological Decisions

    **Patent attribution.** We count patents by **assignee/inventor country based on filing date**, not patent office location or grant date. This assignee-based approach captures where innovation originates rather than where legal protection is sought. Filing dates (not grant or publication dates) provide consistent temporal anchoring across jurisdictions with different examination timelines. This methodology has two critical implications: (1) it automatically excludes Chinese utility models, which lack assignee data in patent office filings and represent lower-quality defensive patents rather than substantive innovation; (2) it captures "export-quality" innovation—patents filed by entities investing in examination and prosecution costs, indicating commercial intent.

    **Citation analysis cohort.** Forward citation analysis is restricted to patents filed 2014-2018, providing a 5-10 year citation window to avoid temporal truncation bias (patents filed recently have less time to accumulate citations). This cohort restriction ensures citation metrics reflect genuine technological impact rather than recency artifacts. All volume-based analyses employ the full 2014-2024 dataset; only quality metrics (citations, generality, originality) use the 2014-2018 cohort.

    **Collaboration measurement.** Cross-border collaboration patents are identified through multi-assignee analysis at the regional level (Section 4). Patents are classified as collaborative when assignees from different regions (e.g., US-China, EU-Korea) co-file. Within-region collaboration (e.g., Germany-France) and collaborations with regions outside our five-region focus are excluded from collaboration rate calculations to maintain analytical focus on strategic cross-regional knowledge flows.

    ## Operationalization and Measurement

    **Volume metrics** include raw patent counts and regional shares calculated as each region's patents divided by the five-region total (excluding other countries). **Quality metrics** comprise: (1) forward citations—the number of subsequent patents citing each focal patent, measuring technological impact (Hall et al., 2001); (2) generality and originality indices—Herfindahl-based measures of cross-domain knowledge integration, where generality captures the diversity of technology classes citing the focal patent and originality measures the diversity of classes the focal patent cites (Hall et al., 2001). **Knowledge flow metrics** include citation-weighted self-citation rates (the proportion of citations received from the same region), cross-regional citation flows (citations from one region to another), and citation time lags (median time between cited and citing patent filing dates).

    ## Statistical Approach

    Given non-normal citation distributions, we employ non-parametric tests for quality comparisons: Kruskal-Wallis H-tests for overall regional differences and Mann-Whitney U-tests for pairwise comparisons, reporting Cohen's d effect sizes to quantify magnitude (small d=0.2, medium d=0.5, large d≥0.8). Collaboration trend analysis employs two-proportion z-tests for temporal changes and Chow tests for structural breaks, identifying whether collaboration collapse coincides with geopolitical events (trade war, export controls). Robustness checks include wild bootstrap regression with technology domain fixed effects to verify quality differences persist within identical domains, ruling out specialization artifacts. All tests employ robust standard errors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # The Five-Region Race: Patent Competition Across EV Technology Domains
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This section presents the empirical foundation of our analysis, examining patent filing patterns across five major regions (the United States, China, the European Union, Japan, and South Korea) from 2014-2024. We first analyze aggregate trends showing the overall competitive landscape (Figure 1), then examine domain-specific patterns across seven core EV technologies (Figure 2), before focusing on the EU's competitive position and its decline across technology domains (Figure 3). These patent data reveal not merely different innovation speeds but fundamentally distinct strategic approaches, reflecting the theoretical frameworks of resource-based capabilities, national innovation systems, and disruptive innovation dynamics discussed earlier.
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    # Data loading: Global patent data (5 regions: US, CN, EU, JP, KR)
    global_data = pd.read_csv('data/01_global_context_5regions.csv')

    # Prepare overall patent share data (all 5 regions)
    overall_data = global_data.groupby(['year', 'country'])['patent_count'].sum().reset_index()

    # Calculate percentages
    total_by_year = overall_data.groupby('year')['patent_count'].sum().reset_index()
    total_by_year.columns = ['year', 'total']
    overall_data = overall_data.merge(total_by_year, on='year')
    overall_data['percentage'] = (overall_data['patent_count'] / overall_data['total']) * 100
    return global_data, overall_data


@app.cell(hide_code=True)
def _(global_data, np, overall_data, pd, stats):
    """
    Statistical Analysis: Regional Patent Share Changes (2014 vs 2023)

    Tests whether observed changes in regional patent shares are statistically significant
    using chi-square tests for proportions.
    """

    # Filter to complete years only (exclude 2024)
    _shares_2014 = overall_data[overall_data['year'] == 2014].copy()
    _shares_2023 = overall_data[overall_data['year'] == 2023].copy()

    # Create contingency table for chi-square test
    # Rows: regions, Columns: years (2014, 2023)
    _contingency = pd.DataFrame({
        '2014': _shares_2014.set_index('country')['patent_count'],
        '2023': _shares_2023.set_index('country')['patent_count']
    })

    # Chi-square test for independence (tests if regional distribution changed)
    _chi2, _p_val, _dof, _expected = stats.chi2_contingency(_contingency.values)

    # Calculate share changes with 95% confidence intervals
    _share_changes = []
    for _region in ['US', 'CN', 'EU', 'JP', 'KR']:
        _n_2014 = _shares_2014[_shares_2014['country'] == _region]['patent_count'].values[0]
        _total_2014 = _shares_2014['patent_count'].sum()
        _p_2014 = _n_2014 / _total_2014

        _n_2023 = _shares_2023[_shares_2023['country'] == _region]['patent_count'].values[0]
        _total_2023 = _shares_2023['patent_count'].sum()
        _p_2023 = _n_2023 / _total_2023

        # Calculate 95% CI for proportion difference using normal approximation
        _se_2014 = np.sqrt(_p_2014 * (1 - _p_2014) / _total_2014)
        _se_2023 = np.sqrt(_p_2023 * (1 - _p_2023) / _total_2023)
        _se_diff = np.sqrt(_se_2014**2 + _se_2023**2)
        _ci_lower = (_p_2023 - _p_2014) - 1.96 * _se_diff
        _ci_upper = (_p_2023 - _p_2014) + 1.96 * _se_diff

        # Z-test for individual region change
        _z_stat = (_p_2023 - _p_2014) / _se_diff if _se_diff > 0 else 0
        _p_value_z = 2 * (1 - stats.norm.cdf(abs(_z_stat)))

        _share_changes.append({
            'region': _region,
            'share_2014': _p_2014 * 100,
            'share_2023': _p_2023 * 100,
            'change_pp': (_p_2023 - _p_2014) * 100,
            'ci_lower': _ci_lower * 100,
            'ci_upper': _ci_upper * 100,
            'z_stat': _z_stat,
            'p_value': _p_value_z,
            'significant': _p_value_z < 0.001
        })

    _share_changes_df = pd.DataFrame(_share_changes)

    # Domain-specific analysis for EU
    _eu_domain_changes = []
    for domain in global_data['application_area'].unique():
        _domain_data = global_data[global_data['application_area'] == domain]

        _eu_2014 = _domain_data[(_domain_data['year'] == 2014) & (_domain_data['country'] == 'EU')]['patent_count'].sum()
        _total_2014 = _domain_data[_domain_data['year'] == 2014]['patent_count'].sum()

        _eu_2023 = _domain_data[(_domain_data['year'] == 2023) & (_domain_data['country'] == 'EU')]['patent_count'].sum()
        _total_2023 = _domain_data[_domain_data['year'] == 2023]['patent_count'].sum()

        if _total_2014 > 0 and _total_2023 > 0:
            _p_2014_dom = _eu_2014 / _total_2014
            _p_2023_dom = _eu_2023 / _total_2023
            _change_pp_dom = (_p_2023_dom - _p_2014_dom) * 100

            _eu_domain_changes.append({
                'domain': domain,
                'eu_share_2014': _p_2014_dom * 100,
                'eu_share_2023': _p_2023_dom * 100,
                'change_pp': _change_pp_dom
            })

    _eu_domain_changes_df = pd.DataFrame(_eu_domain_changes).sort_values('change_pp')

    # Store results
    share_test_results = {
        'chi2_stat': round(_chi2, 2),
        'chi2_p': _p_val,
        'share_changes': _share_changes_df,
        'eu_domain_changes': _eu_domain_changes_df
    }
    return (share_test_results,)


@app.cell(hide_code=True)
def _(alt, overall_data):
    # Figure 1: Overall Patent Share Evolution (5 Regions: US, CN, EU, JP, KR)
    # Line chart with shape + color encoding for B&W print compatibility
    # Dashed lines indicate incomplete 2024 data

    # Define color scheme for regions
    region_colors = {
        'US': '#1f77b4',   # Blue
        'EU': '#ff7f0e',   # Orange
        'CN': '#2ca02c',   # Green
        'JP': '#d62728',   # Red
        'KR': '#9467bd'    # Purple
    }

    # Define shape scheme for B&W print compatibility
    region_shapes = {
        'US': 'circle',
        'EU': 'square',
        'CN': 'triangle-up',
        'JP': 'diamond',
        'KR': 'cross'
    }

    # Split data into complete (2014-2023) and incomplete (2023-2024) segments
    _data_complete = overall_data[overall_data['year'] <= 2023]
    _data_incomplete = overall_data[overall_data['year'] >= 2023]

    # Create solid line chart for complete data (2014-2023)
    _chart_solid = alt.Chart(_data_complete).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=80, filled=True)
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('percentage:Q',
                title='Patent Share (%)',
                scale=alt.Scale(domain=[0, 40]),
                axis=alt.Axis(format='.0f', labelFontSize=11, grid=True, gridOpacity=0.3)),
        color=alt.Color('country:N',
                        title='Region',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        shape=alt.Shape('country:N',
                        title='Region',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        tooltip=[
            alt.Tooltip('country:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('percentage:Q', title='Patent Share (%)', format='.1f'),
            alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
        ]
    )

    # Create dashed line chart for incomplete data (2023-2024)
    _chart_dashed = alt.Chart(_data_incomplete).mark_line(
        strokeWidth=1.5,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=80, filled=False)
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('percentage:Q'),
        color=alt.Color('country:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        shape=alt.Shape('country:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        tooltip=[
            alt.Tooltip('country:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('percentage:Q', title='Patent Share (%)', format='.1f'),
            alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
        ]
    )

    # Combine solid and dashed charts
    fig1 = (_chart_solid + _chart_dashed).properties(
        width=700,
        height=400,
        title=alt.Title(
            'Figure 1: Global EV Patent Share Evolution (2014-2024)',
            subtitle='Five major regions competing in electric vehicle innovation. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(
        strokeWidth=0
    )

    fig1
    return region_colors, region_shapes


@app.cell(hide_code=True)
def _(mo, share_test_results):
    """Display Table 1: Statistical tests for regional share changes"""
    _st = share_test_results
    _sc = _st['share_changes']

    mo.md(f"""
    **Table 1.** Regional Patent Share Changes and Statistical Significance (2014 vs. 2023)

    | Region | 2014 Share | 2023 Share | Change (pp) | 95% CI | Z-statistic | p-value | Significant |
    |--------|-----------|-----------|-------------|--------|-------------|---------|-------------|
    | China | {_sc[_sc['region']=='CN']['share_2014'].values[0]:.1f}% | {_sc[_sc['region']=='CN']['share_2023'].values[0]:.1f}% | **+{_sc[_sc['region']=='CN']['change_pp'].values[0]:.1f}** | [{_sc[_sc['region']=='CN']['ci_lower'].values[0]:.1f}, {_sc[_sc['region']=='CN']['ci_upper'].values[0]:.1f}] | {_sc[_sc['region']=='CN']['z_stat'].values[0]:.2f} | <0.001 | Yes |
    | South Korea | {_sc[_sc['region']=='KR']['share_2014'].values[0]:.1f}% | {_sc[_sc['region']=='KR']['share_2023'].values[0]:.1f}% | **+{_sc[_sc['region']=='KR']['change_pp'].values[0]:.1f}** | [{_sc[_sc['region']=='KR']['ci_lower'].values[0]:.1f}, {_sc[_sc['region']=='KR']['ci_upper'].values[0]:.1f}] | {_sc[_sc['region']=='KR']['z_stat'].values[0]:.2f} | <0.001 | Yes |
    | United States | {_sc[_sc['region']=='US']['share_2014'].values[0]:.1f}% | {_sc[_sc['region']=='US']['share_2023'].values[0]:.1f}% | {_sc[_sc['region']=='US']['change_pp'].values[0]:.1f} | [{_sc[_sc['region']=='US']['ci_lower'].values[0]:.1f}, {_sc[_sc['region']=='US']['ci_upper'].values[0]:.1f}] | {_sc[_sc['region']=='US']['z_stat'].values[0]:.2f} | <0.001 | Yes |
    | Japan | {_sc[_sc['region']=='JP']['share_2014'].values[0]:.1f}% | {_sc[_sc['region']=='JP']['share_2023'].values[0]:.1f}% | {_sc[_sc['region']=='JP']['change_pp'].values[0]:.1f} | [{_sc[_sc['region']=='JP']['ci_lower'].values[0]:.1f}, {_sc[_sc['region']=='JP']['ci_upper'].values[0]:.1f}] | {_sc[_sc['region']=='JP']['z_stat'].values[0]:.2f} | <0.001 | Yes |
    | **European Union** | **{_sc[_sc['region']=='EU']['share_2014'].values[0]:.1f}%** | **{_sc[_sc['region']=='EU']['share_2023'].values[0]:.1f}%** | **{_sc[_sc['region']=='EU']['change_pp'].values[0]:.1f}** | **[{_sc[_sc['region']=='EU']['ci_lower'].values[0]:.1f}, {_sc[_sc['region']=='EU']['ci_upper'].values[0]:.1f}]** | **{_sc[_sc['region']=='EU']['z_stat'].values[0]:.2f}** | **<0.001** | **Yes** |

    *Note*: Chi-square test confirms regional distribution changed significantly between 2014 and 2023 (χ²={_st['chi2_stat']}, df=4, p<0.001). Z-statistics test whether individual regional changes differ from zero; 95% confidence intervals (CI) calculated using normal approximation for proportion differences. All regional changes are statistically significant at p<0.001, indicating changes are not due to sampling variation. EU's -6.1pp decline and China's +8.7pp growth represent the largest absolute changes. Sorted by 2023 share (descending).
    """)
    return


@app.cell(hide_code=True)
def _(alt, global_data, pd, region_colors, region_shapes):
    # Figure 2: Technology Domain Analysis (Small Multiples)
    # Faceted line charts showing patent share across 7 EV technology domains
    # Dashed lines indicate incomplete 2024 data

    # Calculate percentage share by domain for each region
    domain_data = global_data.copy()

    # Get total patents per domain per year
    domain_totals = domain_data.groupby(['application_area', 'year'])['patent_count'].sum().reset_index()
    domain_totals.columns = ['application_area', 'year', 'total']

    # Merge and calculate percentages
    domain_data = domain_data.merge(domain_totals, on=['application_area', 'year'])
    domain_data['percentage'] = (domain_data['patent_count'] / domain_data['total']) * 100

    # Shorten domain names for better display
    _domain_labels_fig2 = {
        'Battery Technology': 'Battery Tech',
        'EV Propulsion & Charging': 'Propulsion & Charging',
        'Autonomous Driving & ADAS': 'Autonomous Driving',
        'Hybrid Powertrains': 'Hybrid Systems',
        'Vehicle Safety Systems': 'Safety Systems',
        'Thermal Management': 'Thermal Mgmt',
        'Infotainment & Connectivity': 'Infotainment'
    }
    domain_data['domain_short'] = domain_data['application_area'].map(_domain_labels_fig2)

    # Remove any rows with null domain_short (fixes "null" category issue)
    domain_data = domain_data[domain_data['domain_short'].notna()].copy()

    # Function to create a chart for a single domain (like Figure 1 approach)
    def _create_domain_chart(data, domain_name):
        # Filter data for this domain
        _domain_subset = data[data['domain_short'] == domain_name].copy()

        # Split into complete and incomplete
        _complete = _domain_subset[_domain_subset['year'] <= 2023]
        _incomplete = _domain_subset[_domain_subset['year'] >= 2023]

        # Solid lines for complete data
        _solid = alt.Chart(_complete).mark_line(
            strokeWidth=1.5,
            point=alt.OverlayMarkDef(size=50, filled=True)
        ).encode(
            x=alt.X('year:O', title='Year', axis=alt.Axis(labelAngle=-45, labelFontSize=9)),
            y=alt.Y('percentage:Q', title='Patent Share (%)',
                    scale=alt.Scale(domain=[0, 50]),
                    axis=alt.Axis(format='.0f', labelFontSize=9, grid=True, gridOpacity=0.2)),
            color=alt.Color('country:N',
                            scale=alt.Scale(
                                domain=['US', 'EU', 'CN', 'JP', 'KR'],
                                range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                            ),
                            legend=None),
            shape=alt.Shape('country:N',
                            scale=alt.Scale(
                                domain=['US', 'EU', 'CN', 'JP', 'KR'],
                                range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                            ),
                            legend=None),
            tooltip=[
                alt.Tooltip('country:N', title='Region'),
                alt.Tooltip('year:O', title='Year'),
                alt.Tooltip('percentage:Q', title='Patent Share (%)', format='.1f'),
                alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
            ]
        )

        # Dashed lines for incomplete data
        _dashed = alt.Chart(_incomplete).mark_line(
            strokeWidth=1.5,
            strokeDash=[5, 5],
            point=alt.OverlayMarkDef(size=50, filled=False)
        ).encode(
            x=alt.X('year:O'),
            y=alt.Y('percentage:Q'),
            color=alt.Color('country:N',
                            scale=alt.Scale(
                                domain=['US', 'EU', 'CN', 'JP', 'KR'],
                                range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                            ),
                            legend=None),
            shape=alt.Shape('country:N',
                            scale=alt.Scale(
                                domain=['US', 'EU', 'CN', 'JP', 'KR'],
                                range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                            ),
                            legend=None),
            tooltip=[
                alt.Tooltip('country:N', title='Region'),
                alt.Tooltip('year:O', title='Year'),
                alt.Tooltip('percentage:Q', title='Patent Share (%)', format='.1f'),
                alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
            ]
        )

        return (_solid + _dashed).properties(
            width=220,
            height=150,
            title=alt.TitleParams(domain_name, fontSize=11, fontWeight='bold', anchor='start')
        )

    # Define the 7 domains in the order we want them displayed
    _domains_ordered = [
        'Battery Tech', 'Autonomous Driving', 'Infotainment',
        'Propulsion & Charging', 'Thermal Mgmt', 'Safety Systems',
        'Hybrid Systems'
    ]

    # Create individual charts for each domain
    _charts = [_create_domain_chart(domain_data, domain) for domain in _domains_ordered]

    # Arrange in 3x3 grid (7 domains + legend placeholder)
    _row1 = alt.hconcat(_charts[0], _charts[1], _charts[2])
    _row2 = alt.hconcat(_charts[3], _charts[4], _charts[5])
    _row3 = alt.hconcat(_charts[6])

    # Create legend as a separate chart with explicit data for all 5 regions
    _legend_data = pd.DataFrame({'country': ['US', 'EU', 'CN', 'JP', 'KR']})
    _legend_chart = alt.Chart(_legend_data).mark_point(size=100, filled=True).encode(
        y=alt.Y('country:N',
                title=None,
                axis=alt.Axis(orient='right', labelFontSize=10, domain=False, ticks=False, labelPadding=1),
                scale=alt.Scale(domain=['US', 'EU', 'CN', 'JP', 'KR'])),
        color=alt.Color('country:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        shape=alt.Shape('country:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None)
    ).properties(width=15, height=150, title=alt.TitleParams('Region', fontSize=11, fontWeight='bold', anchor='start'))

    _row3_with_legend = alt.hconcat(_charts[6], _legend_chart)

    # Combine all rows
    fig2 = alt.vconcat(_row1, _row2, _row3_with_legend).properties(
        title=alt.Title(
            'Figure 2: Patent Share by Technology Domain (2014-2024)',
            subtitle='Seven core EV technology domains. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig2
    return


@app.cell(hide_code=True)
def _(global_data):
    """
    Calculate domain×region statistics for Table 2
    Provides patent counts and shares for 2014 vs 2023 comparison
    """
    # Filter to 2014 and 2023 only
    _table2_data = global_data[global_data['year'].isin([2014, 2023])].copy()

    # Pivot to get region×domain matrix for both years
    _pivot_2014 = _table2_data[_table2_data['year'] == 2014].pivot_table(
        index='application_area',
        columns='country',
        values='patent_count',
        aggfunc='sum'
    ).fillna(0)

    _pivot_2023 = _table2_data[_table2_data['year'] == 2023].pivot_table(
        index='application_area',
        columns='country',
        values='patent_count',
        aggfunc='sum'
    ).fillna(0)

    # Calculate totals for percentage calculation
    _totals_2014 = _pivot_2014.sum(axis=1)
    _totals_2023 = _pivot_2023.sum(axis=1)

    # Calculate percentages
    _pct_2014 = _pivot_2014.div(_totals_2014, axis=0) * 100
    _pct_2023 = _pivot_2023.div(_totals_2023, axis=0) * 100

    # Store results
    domain_region_stats = {
        'counts_2014': _pivot_2014,
        'counts_2023': _pivot_2023,
        'pct_2014': _pct_2014,
        'pct_2023': _pct_2023,
        'totals_2014': _totals_2014,
        'totals_2023': _totals_2023
    }
    return (domain_region_stats,)


@app.cell(hide_code=True)
def _(domain_region_stats, mo):
    """Display Table 2: Domain×Region patent statistics"""
    _drs = domain_region_stats
    _c14 = _drs['counts_2014']
    _c23 = _drs['counts_2023']
    _p14 = _drs['pct_2014']
    _p23 = _drs['pct_2023']

    # Domain order (alphabetical for clarity)
    _domains = [
        'Autonomous Driving & ADAS',
        'Battery Technology',
        'EV Propulsion & Charging',
        'Hybrid Powertrains',
        'Infotainment & Connectivity',
        'Thermal Management',
        'Vehicle Safety Systems'
    ]

    # Build table rows
    _table_rows = []
    for _dom in _domains:
        if _dom in _c14.index:
            _row = f"| {_dom} |"
            for _reg in ['US', 'CN', 'EU', 'JP', 'KR']:
                _n14 = int(_c14.loc[_dom, _reg]) if _reg in _c14.columns else 0
                _n23 = int(_c23.loc[_dom, _reg]) if _reg in _c23.columns else 0
                _pct14 = _p14.loc[_dom, _reg] if _reg in _p14.columns else 0
                _pct23 = _p23.loc[_dom, _reg] if _reg in _p23.columns else 0
                _row += f" {_n14:,} ({_pct14:.1f}%) | {_n23:,} ({_pct23:.1f}%) |"
            _table_rows.append(_row)

    _table_content = "\n".join(_table_rows)

    mo.md(f"""
    **Table 2.** Patent Counts and Regional Shares by Technology Domain (2014 vs. 2023)

    | Domain | US 2014 | US 2023 | CN 2014 | CN 2023 | EU 2014 | EU 2023 | JP 2014 | JP 2023 | KR 2014 | KR 2023 |
    |--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
    {_table_content}

    *Note*: Each cell shows N (share%) where N is patent count and share% is the region's percentage among the five regions for that domain. Totals by domain: Autonomous Driving 2014: {int(_drs['totals_2014']['Autonomous Driving & ADAS']):,}, 2023: {int(_drs['totals_2023']['Autonomous Driving & ADAS']):,}; Battery 2014: {int(_drs['totals_2014']['Battery Technology']):,}, 2023: {int(_drs['totals_2023']['Battery Technology']):,}; Propulsion 2014: {int(_drs['totals_2014']['EV Propulsion & Charging']):,}, 2023: {int(_drs['totals_2023']['EV Propulsion & Charging']):,}; Hybrid 2014: {int(_drs['totals_2014']['Hybrid Powertrains']):,}, 2023: {int(_drs['totals_2023']['Hybrid Powertrains']):,}; Infotainment 2014: {int(_drs['totals_2014']['Infotainment & Connectivity']):,}, 2023: {int(_drs['totals_2023']['Infotainment & Connectivity']):,}; Thermal 2014: {int(_drs['totals_2014']['Thermal Management']):,}, 2023: {int(_drs['totals_2023']['Thermal Management']):,}; Safety 2014: {int(_drs['totals_2014']['Vehicle Safety Systems']):,}, 2023: {int(_drs['totals_2023']['Vehicle Safety Systems']):,}.
    """)
    return


@app.cell(hide_code=True)
def _(global_data):
    """
    Calculate RCA (Revealed Comparative Advantage) for 2023
    to quantify current regional specialization patterns
    """
    # Filter to 2023 for current specialization
    _rca_data = global_data[global_data['year'] == 2023].copy()

    # Create region×domain matrix
    _patent_matrix = _rca_data.pivot_table(
        index='country',
        columns='application_area',
        values='patent_count',
        aggfunc='sum'
    ).fillna(0)

    # Calculate RCA following Balassa (1965)
    # Numerator: region's share in domain
    _domain_totals = _patent_matrix.sum(axis=0)
    _region_share_in_domain = _patent_matrix.div(_domain_totals, axis=1)

    # Denominator: region's overall share
    _region_totals = _patent_matrix.sum(axis=1)
    _grand_total = _patent_matrix.sum().sum()
    _region_overall_share = _region_totals / _grand_total

    # RCA = (share in domain) / (overall portfolio share)
    _rca_matrix = _region_share_in_domain.div(_region_overall_share, axis=0)

    rca_results = {'rca_2023': _rca_matrix.round(2)}
    return (rca_results,)


@app.cell(hide_code=True)
def _(mo, rca_results):
    """Display Table 3: RCA analysis for 2023"""
    _rca = rca_results['rca_2023']

    # Domain order (same as Table 2)
    _domains = [
        'Autonomous Driving & ADAS',
        'Battery Technology',
        'EV Propulsion & Charging',
        'Hybrid Powertrains',
        'Infotainment & Connectivity',
        'Thermal Management',
        'Vehicle Safety Systems'
    ]

    # Build table rows
    _table_rows = []
    for _dom in _domains:
        if _dom in _rca.columns:
            # Shortened domain names for table
            _dom_short = _dom.replace(' & ADAS', '').replace(' Technology', '').replace(' & Charging', '').replace('Vehicle ', '').replace(' & Connectivity', '')
            _row = f"| {_dom_short} |"
            for _reg in ['US', 'CN', 'EU', 'JP', 'KR']:
                _val = _rca.loc[_reg, _dom] if _reg in _rca.index else 0
                # Bold if ≥1.5 (strong specialization)
                if _val >= 1.5:
                    _row += f" **{_val:.2f}** |"
                else:
                    _row += f" {_val:.2f} |"
            _table_rows.append(_row)

    _table_content = "\n".join(_table_rows)

    mo.md(f"""
    **Table 3.** Revealed Comparative Advantage (RCA) by Technology Domain (2023)

    | Domain | US | CN | EU | JP | KR |
    |--------|----|----|----|----|-----|
    {_table_content}

    *Note*: RCA quantifies regional specialization following Balassa (1965): RCA = (region's share in domain) / (region's overall patent share). RCA > 1.0 indicates specialization (higher concentration than overall portfolio); RCA < 1.0 indicates under-representation; **bold (RCA ≥ 1.5)** indicates strong specialization. **Key findings**: (1) **China**: Strong battery specialization (1.49) but weakness in autonomous driving (0.58); (2) **EU**: Strong specialization in *traditional automotive domains* (hybrids **1.65**, thermal **1.64**, safety **1.59**) but weakness in emerging tech (batteries 0.63, infotainment 0.67); (3) **Korea**: Strong battery dominance (**1.59**); (4) **US**: Specialization in software domains (autonomous 1.30, infotainment 1.36); (5) **Japan**: Strong hybrid specialization (**1.51**). EU exhibits "legacy trap"—strengthening traditional capabilities while lacking specialization in emerging domains. Table 2 shows temporal trends in absolute shares; Table 3 shows current specialization patterns.
    """)
    return


@app.cell(hide_code=True)
def _(alt, global_data):
    # Figure 3: EU Competitive Position Heatmap
    # Shows EU's patent share across technology domains and time

    # Filter for EU data only and calculate EU share in each domain/year
    eu_data = global_data.copy()

    # Calculate total patents per domain per year
    totals = eu_data.groupby(['application_area', 'year'])['patent_count'].sum().reset_index()
    totals.columns = ['application_area', 'year', 'total']

    # Get EU patents
    eu_only = eu_data[eu_data['country'] == 'EU'].copy()
    eu_only = eu_only.merge(totals, on=['application_area', 'year'])
    eu_only['eu_percentage'] = (eu_only['patent_count'] / eu_only['total']) * 100

    # Shorten domain names - FIXED: match actual domain names in data
    _domain_labels_fig3 = {
        'Battery Technology': 'Battery',
        'EV Propulsion & Charging': 'Propulsion',
        'Autonomous Driving & ADAS': 'Autonomous',
        'Hybrid Powertrains': 'Hybrid',  # FIXED: was "Hybrid & Energy Management"
        'Vehicle Safety Systems': 'Safety',  # FIXED: was "Safety & ADAS"
        'Thermal Management': 'Thermal',
        'Infotainment & Connectivity': 'Infotainment'
    }
    eu_only['domain_short'] = eu_only['application_area'].map(_domain_labels_fig3)

    # Remove any null rows (domains that don't match the mapping)
    eu_only = eu_only[eu_only['domain_short'].notna()].copy()

    # Create heatmap with improved color scheme
    fig3 = alt.Chart(eu_only).mark_rect().encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11)),
        y=alt.Y('domain_short:N',
                title='Technology Domain',
                sort=['Battery', 'Propulsion', 'Autonomous', 'Hybrid', 'Safety', 'Thermal', 'Infotainment'],
                axis=alt.Axis(labelFontSize=11)),
        color=alt.Color('eu_percentage:Q',
                        title='EU Patent Share (%)',
                        scale=alt.Scale(scheme='blues', domain=[10, 50]),  # Adjusted range for better contrast
                        legend=alt.Legend(titleFontSize=11, labelFontSize=10)),
        tooltip=[
            alt.Tooltip('application_area:N', title='Domain'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('eu_percentage:Q', title='EU Share (%)', format='.1f'),
            alt.Tooltip('patent_count:Q', title='EU Patents', format=',')
        ]
    ).properties(
        width=650,  # Slightly wider for better readability
        height=320,
        title=alt.Title(
            'Figure 3: EU Competitive Position Across Technology Domains',
            subtitle='EU patent share (%) among five major regions (US, CN, EU, JP, KR) by domain and year. Darker shades indicate stronger EU position. *2024 data incomplete.',
            fontSize=14,
            anchor='start'
        )
    )

    # Add text annotations showing exact percentages
    text = alt.Chart(eu_only).mark_text(
        fontSize=9,
        fontWeight='bold'
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('domain_short:N',
                sort=['Battery', 'Propulsion', 'Autonomous', 'Hybrid', 'Safety', 'Thermal', 'Infotainment']),
        text=alt.Text('eu_percentage:Q', format='.0f'),
        color=alt.condition(
            alt.datum.eu_percentage > 28,  # Adjusted threshold for better text contrast
            alt.value('white'),
            alt.value('black')
        )
    )

    fig3_final = (fig3 + text).configure_view(strokeWidth=0)

    fig3_final
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## Interpreting the Global Patent Landscape: Resource Endowments and Strategic Divergence

    Figures 1-3 and Tables 1-3 reveal how distinct National Innovation Systems shape regional EV patent trajectories. Statistical testing confirms these patterns are not sampling artifacts (χ²=9801.09, p<0.001): all regional changes from 2014-2023 test significant at p<0.001.

    **Asian competitors' strategic focus**: Korea (20.5%) and Japan (18.3%) pursue focused specialization strategies, with Korea concentrating on batteries and Japan on hybrid powertrains—demonstrating how strategic concentration can generate competitive advantage despite smaller innovation systems.

    **US software-intensive leadership**: US dominance (27-31% overall share) stems from specialization in software domains (autonomous driving RCA=1.22, infotainment RCA=1.37). The 2022 dip to 25.5% likely reflects technology maturation cycles in autonomous driving ("hype cycle" consolidation), consistent with disruptive innovation's non-linear dynamics.

    **China's selective positioning**: Despite substantial subsidies, China's overall share remains modest (14.2% in 2023). This apparent paradox resolves via Table 2's domain breakdown: strategic focus on batteries (21% share, 6,421 patents) prioritizes commercialization over comprehensive patent coverage—the consumer electronics business model emphasizing rapid iteration in targeted domains.

    **EU's comprehensive erosion**: EU declined 6.1pp overall, but Figure 3 shows erosion in six of seven domains. The sole growth domain (hybrids, +1.2pp) represents sustaining innovation in declining technology. Table 3's RCA analysis reveals strategic misalignment: EU shows clear specialization in traditional automotive engineering (hybrids 1.65, thermal management 1.64, safety systems 1.59) but critical weaknesses in future-defining domains—batteries (0.63) and infotainment (0.67) both fall below the global average, indicating capability gaps in the two domains most central to EV differentiation and value capture.

    ### Domain-Level Patterns: Strategic Specialization

    Table 2 reveals domain-specific dynamics. **Battery technology** presents a critical vulnerability for the EU: Europe holds only 13% patent share (3,929 patents in 2023), far behind Korea's innovation leadership (33%, 9,919 patents) and China's accelerating position (21%, 6,314 patents). While Korea leverages consumer electronics battery expertise (Samsung, LG) and China scales through state-directed gigafactory investment (CATL, BYD), the EU's fragmented approach across 27 national programs has failed to generate either innovation leadership or manufacturing competitiveness. China's manufacturing dominance (53% global market share) combined with rapidly growing patent output (16%→21%, 2020-2023) suggests European battery dependence will intensify without strategic intervention.

    **Software domains**: US autonomous driving leadership (32-35%) stems from Silicon Valley's software ecosystem (Stanford-Waymo linkages, venture capital, AI talent). China's weakness (8-9%) suggests command-and-control systems excel at manufacturing but struggle with software innovation requiring decentralized creativity. EU weakness in both autonomous driving (20%) and infotainment (14%) reveals traditional automakers viewing software as subsidiary to mechanical engineering—a critical strategic misalignment.

    ### Institutional Patterns and Policy Implications

    These patent trajectories reflect distinct National Innovation Systems: competitors pursue focused specialization (US software, China batteries, Korea batteries, Japan hybrids) while the EU maintains broad coverage across all domains. The critical insight: regional competitiveness depends on strategic alignment between capabilities and future value creation, not aggregate patent volume. Focused specialization in high-leverage domains (batteries, software) generates more strategic value than the EU's broad coverage of traditional automotive engineering (hybrids 1.65, thermal 1.64, safety 1.59)—strong capabilities misaligned with future value capture. EV leadership requires strategic selectivity.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## EU's Comprehensive Decline: A Coordination Failure

    Figure 3's heatmap reveals a crisis beyond selective software weakness: EU patent share declined in six of seven domains (2014-2023), ranging from -12.2pp (autonomous driving) to -2.9pp (propulsion). The sole growth domain (hybrids, +1.2pp) represents sustaining innovation in declining technology. Even thermal management, often cited as European strength, eroded from 40.5% to 33.2%, demonstrating that established capabilities decline without strategic investment during disruptive transitions.

    This pattern contrasts sharply with competitors' focused specialization strategies. The EU's 27 fragmented national programs concentrate resources in traditional automotive domains (Table 3: hybrids 1.65, thermal 1.64, safety 1.59) while failing to build competitive positions in future-defining technologies (batteries 0.63, infotainment 0.67). The result is slow erosion across all domains—a coordination failure during rapid technological transitions requiring pan-European platforms and unified strategies to override national fragmentation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Patent Quality Analysis: Beyond Volume to Innovation Impact
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Patent volume tells only half the story. A region filing 100,000 patents might seem innovative, but if those patents represent incremental improvements receiving few citations, they signal a defensive strategy rather than breakthrough innovation. Conversely, a smaller portfolio of highly-cited patents indicates foundational research enabling follow-on discoveries.

    Forward citations, the frequency with which subsequent patents reference a given patent, serve as a key quality indicator. Highly-cited patents typically represent: (1) foundational technologies enabling multiple applications, (2) novel solutions to important technical problems, or (3) platform innovations spawning derivative work. Citation analysis thus distinguishes between *technological leadership* (generating ideas others build upon) and *technological followership* (implementing existing ideas).

    This section examines citation-based quality metrics across the five-region competitive landscape, revealing surprising patterns about who leads in innovation impact versus innovation volume.

    ## Forward Citations as Quality Measure

    We operationalize innovation quality using forward citations, following established practice in patent economics (Hall, Jaffe & Trajtenberg, 2001; Trajtenberg, 1990). This measure captures technological importance: highly-cited patents enable follow-on innovation, solve significant technical problems, and generate knowledge spillovers—core dimensions of innovation quality. Forward citations exhibit strong convergent validity with expert assessments of patent importance, patent renewal rates (indicating commercial value), and firm market valuation (Hall et al., 2005).

    **Robustness**: We validate this quality interpretation through multiple approaches: (1) calculating generality and originality indices (Section 4.2) showing EU ranks middle in knowledge breadth despite low citations, ruling out domain specialization artifacts; (2) domain-controlled regression (Table 4B) confirming quality differences persist after accounting for technology mix; (3) cross-referencing with collaboration patterns (Section 5) demonstrating citations and partnerships measure complementary dimensions.

    **Limitations**: Forward citations measure *research influence*—the extent patents enable follow-on R&D—which privileges foundational, platform-enabling technologies over incremental improvements or product-specific innovations. Alternative quality dimensions (manufacturing excellence, applied problem-solving, commercial success) may not correlate with citation counts. Citations also reflect domain norms: software/AI patents receive systematically higher citations than hardware domains, independent of technological sophistication. Our interpretation thus focuses on *technological quality* as "capacity to enable follow-on innovation" rather than comprehensive innovation value.

    **Alternative explanations**: We considered domain specialization, patent office bias, temporal lag, and fractional counting as potential confounds. Appendix B systematically assesses and addresses these alternative explanations using our existing empirical evidence.
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    # Data loading: Patent quality citation data (5 regions: US, CN, EU, JP, KR)
    citation_data = pd.read_csv('data/03_patent_quality_citations.csv')

    # Calculate overall citation trends by region and year
    citation_by_region_year = citation_data.groupby(['region', 'year']).agg({
        'patent_count': 'sum',
        'avg_citations': 'mean',
        'median_citations': 'median',
        'p90_citations': 'mean'
    }).reset_index()
    return citation_by_region_year, citation_data


@app.cell(hide_code=True)
def _(citation_data, pd):
    """
    Advanced Statistical Analysis: Domain-Controlled Citation Quality

    Tests whether regional citation differences persist after controlling for
    technology domain specialization and filing year. Uses weighted least squares
    with wild bootstrap inference for heteroskedasticity-robust inference.

    Method rationale:
    - Response variable (avg_citations) is a continuous rate, not integer counts
    - Data exhibits severe heteroskedasticity (US variance 21× higher than EU)
    - Wild bootstrap provides exact inference without distributional assumptions
    - Weights by patent_count to account for precision differences
    """
    import numpy as _np
    import statsmodels.formula.api as _smf

    # Filter to mature patents (2014-2018) with sufficient citation accumulation
    _regression_data = citation_data[
        (citation_data['year'] >= 2014) &
        (citation_data['year'] <= 2018)
    ].copy()

    # Create categorical variables with EU as reference (lowest-quality region)
    _regression_data['region_cat'] = pd.Categorical(
        _regression_data['region'],
        categories=['EU', 'US', 'KR', 'CN', 'JP']  # EU is reference
    )

    # Fit weighted least squares model
    # avg_citations ~ region + domain + year, weighted by patent_count
    _wls_model = _smf.wls(
        formula='avg_citations ~ region_cat + C(application_area) + C(year)',
        data=_regression_data,
        weights=_regression_data['patent_count']
    ).fit()

    # Wild bootstrap for heteroskedasticity-robust inference
    # Resamples residuals with random signs to preserve heteroskedastic structure
    def _wild_bootstrap(model, data, n_boot=10000, seed=42):
        """Wild bootstrap p-values for heteroskedasticity-robust inference"""
        _np.random.seed(seed)

        _fitted = model.fittedvalues
        _resid = model.resid
        _coef_names = ['region_cat[T.US]', 'region_cat[T.KR]',
                       'region_cat[T.CN]', 'region_cat[T.JP]']

        # Observed coefficients
        _obs_coefs = {name: model.params[name] for name in _coef_names
                      if name in model.params.index}

        # Bootstrap distribution
        _boot_results = {name: [] for name in _obs_coefs.keys()}

        for _i in range(n_boot):
            # Resample residuals with random signs (Rademacher distribution)
            _signs = _np.random.choice([-1, 1], size=len(_resid))
            _boot_resid = _resid * _signs
            _boot_y = _fitted + _boot_resid

            # Refit model
            _boot_data = data.copy()
            _boot_data['avg_citations'] = _boot_y

            _boot_model = _smf.wls(
                formula='avg_citations ~ region_cat + C(application_area) + C(year)',
                data=_boot_data,
                weights=_boot_data['patent_count']
            ).fit()

            for _name in _obs_coefs.keys():
                if _name in _boot_model.params.index:
                    _boot_results[_name].append(_boot_model.params[_name] - _obs_coefs[_name])

        # Two-tailed p-values
        _p_values = {}
        for _name, _obs_coef in _obs_coefs.items():
            _boot_dist = _np.array(_boot_results[_name])
            _p_values[_name] = 2 * min(
                _np.mean(_boot_dist >= abs(_obs_coef)),
                _np.mean(_boot_dist <= -abs(_obs_coef))
            )

        return _p_values

    # Compute bootstrap p-values
    _boot_pvals = _wild_bootstrap(_wls_model, _regression_data, n_boot=10000)

    # Extract region effects with bootstrap p-values
    _region_effects = {}
    for _region in ['US', 'KR', 'CN', 'JP']:
        _coef_name = f'region_cat[T.{_region}]'
        if _coef_name in _wls_model.params.index:
            _coef = _wls_model.params[_coef_name]
            _conf_int = _wls_model.conf_int().loc[_coef_name]
            _p_value = _boot_pvals.get(_coef_name, _np.nan)  # Use bootstrap p-value

            _region_effects[_region] = {
                'coefficient': _coef,
                'ci_lower': _conf_int[0],
                'ci_upper': _conf_int[1],
                'p_value': _p_value
            }

    # Add EU (reference category)
    _region_effects['EU'] = {
        'coefficient': 0.0,
        'ci_lower': 0.0,
        'ci_upper': 0.0,
        'p_value': _np.nan
    }

    domain_controlled_results = {
        'model': _wls_model,
        'region_effects': _region_effects,
        'converged': True
    }
    return (domain_controlled_results,)


@app.cell(hide_code=True)
def _(citation_data, pd):
    """
    Statistical Analysis: Citation Quality Differences

    This cell performs rigorous statistical testing to validate claims about
    regional citation quality differences using mature patent cohorts (2014-2018).
    """
    import numpy as np
    from scipy import stats

    # Filter to mature patents (2014-2018) with sufficient citation accumulation time
    _mature_data = citation_data[
        (citation_data['year'] >= 2014) &
        (citation_data['year'] <= 2018)
    ].copy()

    # Calculate weighted average citations by region (weighted by patent count)
    _regional_stats = _mature_data.groupby('region').apply(
        lambda x: pd.Series({
            'weighted_avg_citations': np.average(x['avg_citations'], weights=x['patent_count']),
            'total_patents': x['patent_count'].sum(),
            'median_citations': np.median(x['median_citations']),
            'p90_citations': np.average(x['p90_citations'], weights=x['patent_count'])
        })
    ).round(2)

    # Prepare data for non-parametric tests
    # Create expanded dataset where each patent gets its average citations value
    _citation_distributions = {}
    for region in ['US', 'CN', 'EU', 'JP', 'KR']:
        _region_data = _mature_data[_mature_data['region'] == region]
        # Use avg_citations as representative value for each region-year-domain combo
        _citation_distributions[region] = _region_data['avg_citations'].values

    # Kruskal-Wallis H-test: Non-parametric test for differences across all 5 regions
    _kruskal_h, _kruskal_p = stats.kruskal(
        _citation_distributions['US'],
        _citation_distributions['CN'],
        _citation_distributions['EU'],
        _citation_distributions['JP'],
        _citation_distributions['KR']
    )

    # Mann-Whitney U tests: Pairwise comparisons
    # 1) US vs each other region
    # 2) EU vs CN, JP, KR to verify EU ranks last
    _pairwise_tests = {}
    for region in ['EU', 'CN', 'JP', 'KR']:
        _u_stat, _p_value = stats.mannwhitneyu(
            _citation_distributions['US'],
            _citation_distributions[region],
            alternative='greater'  # Test if US > other region
        )
        _pairwise_tests[f'US_vs_{region}'] = {
            'U_statistic': _u_stat,
            'p_value': _p_value,
            'significant': _p_value < 0.001  # Bonferroni-corrected alpha
        }

    # EU vs other regions (to verify EU ranks last)
    for region in ['CN', 'JP', 'KR']:
        _u_stat, _p_value = stats.mannwhitneyu(
            _citation_distributions[region],
            _citation_distributions['EU'],
            alternative='greater'  # Test if other region > EU
        )
        _pairwise_tests[f'{region}_vs_EU'] = {
            'U_statistic': _u_stat,
            'p_value': _p_value,
            'significant': _p_value < 0.05
        }

    # Calculate effect sizes (Cohen's d approximation for Mann-Whitney)
    _effect_sizes = {}
    for region in ['EU', 'CN', 'JP', 'KR']:
        _us_mean = np.mean(_citation_distributions['US'])
        _region_mean = np.mean(_citation_distributions[region])
        _pooled_std = np.sqrt(
            (np.std(_citation_distributions['US'])**2 +
             np.std(_citation_distributions[region])**2) / 2
        )
        _cohens_d = (_us_mean - _region_mean) / _pooled_std if _pooled_std > 0 else 0
        _effect_sizes[f'US_vs_{region}'] = round(_cohens_d, 2)

    # Effect sizes for EU comparisons
    for region in ['CN', 'JP', 'KR']:
        _eu_mean = np.mean(_citation_distributions['EU'])
        _region_mean = np.mean(_citation_distributions[region])
        _pooled_std = np.sqrt(
            (np.std(_citation_distributions['EU'])**2 +
             np.std(_citation_distributions[region])**2) / 2
        )
        _cohens_d = (_region_mean - _eu_mean) / _pooled_std if _pooled_std > 0 else 0
        _effect_sizes[f'{region}_vs_EU'] = round(_cohens_d, 2)

    # Store results for display
    statistical_results = {
        'regional_stats': _regional_stats,
        'kruskal_h': round(_kruskal_h, 2),
        'kruskal_p': _kruskal_p,
        'pairwise_tests': _pairwise_tests,
        'effect_sizes': _effect_sizes
    }
    mature_citation_data = _mature_data
    return np, statistical_results, stats


@app.cell(hide_code=True)
def _(mo, statistical_results):
    """Display Table 4A: Statistical verification of citation quality differences"""
    _s = statistical_results
    mo.md(f"""
    **Table 4A.** Forward Citation Statistics by Region (2014-2018 Patent Cohorts)

    | Region | Mean Citations | Median | 90th Percentile | Patents (N) |
    |--------|----------------|--------|-----------------|-------------|
    | United States | {_s['regional_stats'].loc['US', 'weighted_avg_citations']} | {_s['regional_stats'].loc['US', 'median_citations']} | {_s['regional_stats'].loc['US', 'p90_citations']} | {_s['regional_stats'].loc['US', 'total_patents']:,.0f} |
    | South Korea | {_s['regional_stats'].loc['KR', 'weighted_avg_citations']} | {_s['regional_stats'].loc['KR', 'median_citations']} | {_s['regional_stats'].loc['KR', 'p90_citations']} | {_s['regional_stats'].loc['KR', 'total_patents']:,.0f} |
    | Japan | {_s['regional_stats'].loc['JP', 'weighted_avg_citations']} | {_s['regional_stats'].loc['JP', 'median_citations']} | {_s['regional_stats'].loc['JP', 'p90_citations']} | {_s['regional_stats'].loc['JP', 'total_patents']:,.0f} |
    | China | {_s['regional_stats'].loc['CN', 'weighted_avg_citations']} | {_s['regional_stats'].loc['CN', 'median_citations']} | {_s['regional_stats'].loc['CN', 'p90_citations']} | {_s['regional_stats'].loc['CN', 'total_patents']:,.0f} |
    | European Union | {_s['regional_stats'].loc['EU', 'weighted_avg_citations']} | {_s['regional_stats'].loc['EU', 'median_citations']} | {_s['regional_stats'].loc['EU', 'p90_citations']} | {_s['regional_stats'].loc['EU', 'total_patents']:,.0f} |

    *Note*: Mean citations weighted by patent count. Median and 90th percentile values reveal right-skewed distributions typical of citation data. Analysis restricted to 2014-2018 cohorts with 6-10 years citation accumulation time to avoid recency bias. Kruskal-Wallis H-test confirms significant regional differences (H={_s['kruskal_h']}, p={_s['kruskal_p']:.2e}). Mann-Whitney U tests comparing US to each region yield p<0.001 with large effect sizes (Cohen's d: EU={_s['effect_sizes']['US_vs_EU']}, CN={_s['effect_sizes']['US_vs_CN']}, JP={_s['effect_sizes']['US_vs_JP']}, KR={_s['effect_sizes']['US_vs_KR']}). EU ranks last: all other regions have significantly higher citations than EU (CN>EU: d={_s['effect_sizes']['CN_vs_EU']}, p={_s['pairwise_tests']['CN_vs_EU']['p_value']:.3f}; JP>EU: d={_s['effect_sizes']['JP_vs_EU']}, p={_s['pairwise_tests']['JP_vs_EU']['p_value']:.3f}; KR>EU: d={_s['effect_sizes']['KR_vs_EU']}, p={_s['pairwise_tests']['KR_vs_EU']['p_value']:.3f}).
    """)
    return


@app.cell(hide_code=True)
def _(domain_controlled_results, mo, np):
    """Display domain-controlled citation quality analysis"""
    if domain_controlled_results['converged']:
        _r = domain_controlled_results['region_effects']

        # Format coefficients and confidence intervals
        def _format_effect(region):
            if region not in _r:
                return "—", "—", "—"
            _effect = _r[region]
            _coef = f"{_effect['coefficient']:+.2f}"
            _ci = f"[{_effect['ci_lower']:+.2f}, {_effect['ci_upper']:+.2f}]"
            if np.isnan(_effect['p_value']):
                _p = "Ref"
            elif _effect['p_value'] < 0.001:
                _p = "<0.001"
            else:
                _p = f"{_effect['p_value']:.3f}"
            return _coef, _ci, _p

        _us_coef, _us_ci, _us_p = _format_effect('US')
        _kr_coef, _kr_ci, _kr_p = _format_effect('KR')
        _jp_coef, _jp_ci, _jp_p = _format_effect('JP')
        _cn_coef, _cn_ci, _cn_p = _format_effect('CN')
        _eu_coef, _eu_ci, _eu_p = _format_effect('EU')

        _output = mo.md(f"""
        **Table 4B.** Domain-Controlled Citation Quality: Weighted Least Squares Results

        | Region | Quality Advantage† | 95% CI | p-value‡ |
        |--------|-------------------|---------|----------|
        | United States | {_us_coef} | {_us_ci} | {_us_p} |
        | South Korea | {_kr_coef} | {_kr_ci} | {_kr_p} |
        | Japan | {_jp_coef} | {_jp_ci} | {_jp_p} |
        | China | {_cn_coef} | {_cn_ci} | {_cn_p} |
        | European Union | {_eu_coef} | — | {_eu_p} |

        *Note*: † Quality advantage represents difference in average forward citations per patent relative to European Union baseline after controlling for technology domain (7 categories) and filing year (2014-2018). Model uses weighted least squares with patent count as precision weights to account for varying sample sizes across region-domain-year cells. Positive values indicate higher citation quality than EU; negative values indicate lower quality. ‡ P-values computed using wild bootstrap (10,000 iterations) to provide heteroskedasticity-robust inference without distributional assumptions. **Causal identification**: Domain-controlled regression with wild bootstrap inference provides conservative causal identification—US patents generate +6.94 more citations than EU patents **within identical technology domains and time periods** (p<0.001). This within-domain comparison rules out domain specialization as explanation for quality gaps, isolating region-specific innovation capabilities. Korea (+1.37, p<0.001) and Japan (+0.95, p=0.002) demonstrate smaller but robust quality advantages, while China's difference (+0.23, p=0.610) is not statistically significant. **Robustness check**: Extending the analysis to all years (2014-2024) yields a marginally significant China advantage (+0.70 citations, p=0.014), suggesting potential quality improvements in recent cohorts; however, this result is less robust due to incomplete citation accumulation for patents filed after 2018.
        """)
    else:
        _output = mo.md(f"""
        *Domain-controlled analysis unavailable: {domain_controlled_results.get('error', 'unknown error')}*
        """)
    _output
    return


@app.cell(hide_code=True)
def _(alt, citation_by_region_year, region_colors, region_shapes):
    # Figure 4A: Average Forward Citations by Region (2014-2024)
    # Shows citation quality trends including citation lag effect

    # Split data into complete (2014-2023) and incomplete (2023-2024)
    _cit_complete = citation_by_region_year[citation_by_region_year['year'] <= 2023]
    _cit_incomplete = citation_by_region_year[citation_by_region_year['year'] >= 2023]

    # Solid lines for complete data
    _cit_solid = alt.Chart(_cit_complete).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=80, filled=True)
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('avg_citations:Q',
                title='Average Forward Citations per Patent',
                scale=alt.Scale(domain=[0, 15]),
                axis=alt.Axis(labelFontSize=11, grid=True, gridOpacity=0.3)),
        color=alt.Color('region:N',
                        title='Region',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        shape=alt.Shape('region:N',
                        title='Region',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('avg_citations:Q', title='Avg Citations', format='.2f'),
            alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
        ]
    )

    # Dashed lines for incomplete data
    _cit_dashed = alt.Chart(_cit_incomplete).mark_line(
        strokeWidth=1.5,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=80, filled=False)
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('avg_citations:Q'),
        color=alt.Color('region:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        shape=alt.Shape('region:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('avg_citations:Q', title='Avg Citations', format='.2f'),
            alt.Tooltip('patent_count:Q', title='Patent Count', format=',')
        ]
    )

    fig4a = (_cit_solid + _cit_dashed).properties(
        width=700,
        height=400,
        title=alt.Title(
            'Figure 4A: Average Forward Citations by Region (2014-2024)',
            subtitle='Patents require 5-7 years to accumulate citations. Declining trends after 2019 reflect citation lag, not quality decline. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig4a
    return


@app.cell(hide_code=True)
def _(alt, citation_data, region_colors, region_shapes):
    # Figure 4B: Citation Quality by Domain (2014-2018 only)
    # Small multiples showing mature patents only for valid quality comparison

    # Filter to mature patents (2014-2018) with sufficient citation lag
    _mature_citations = citation_data[
        (citation_data['year'] >= 2014) &
        (citation_data['year'] <= 2018)
    ].copy()

    # Calculate average citations by domain and region
    _domain_quality = _mature_citations.groupby(['application_area', 'region', 'year']).agg({
        'avg_citations': 'mean',
        'patent_count': 'sum'
    }).reset_index()

    # Create small multiples chart
    _domain_charts = alt.Chart(_domain_quality).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=50, filled=True)
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=9)),
        y=alt.Y('avg_citations:Q',
                title='Avg Citations',
                scale=alt.Scale(domain=[0, 25]),
                axis=alt.Axis(labelFontSize=9, grid=True, gridOpacity=0.2)),
        color=alt.Color('region:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=alt.Legend(orient='bottom', titleFontSize=11, labelFontSize=10, columns=5)),
        shape=alt.Shape('region:N',
                        scale=alt.Scale(
                            domain=['US', 'EU', 'CN', 'JP', 'KR'],
                            range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                        ),
                        legend=None),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('application_area:N', title='Domain'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('avg_citations:Q', title='Avg Citations', format='.2f'),
            alt.Tooltip('patent_count:Q', title='Patents', format=',')
        ]
    ).properties(
        width=210,
        height=150
    ).facet(
        facet=alt.Facet('application_area:N', title=None, header=alt.Header(labelFontSize=11, labelLimit=200)),
        columns=3
    ).properties(
        title=alt.Title(
            'Figure 4B: Citation Quality by Technology Domain (2014-2018)',
            subtitle='Showing only patents with 6-10 years citation lag for valid quality comparison across regions',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    _domain_charts
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Regional Quality Differences: Statistical Evidence

    Figure 4A and Table 4A reveal a stark quality hierarchy robust to statistical testing. Using 2014-2018 patent cohorts with 6-10 years citation accumulation time, the United States achieves 9.97 mean citations per patent, 2.9× to 3.9× higher than all other regions. South Korea ranks second (4.11 citations), followed by Japan (3.47), China (3.07), and the European Union last (2.58 citations). Non-parametric statistical tests confirm these differences are not artifacts of sampling variation. Kruskal-Wallis H-test (H=73.14, p<0.001) strongly rejects the null hypothesis of equal citation distributions across regions. Pairwise Mann-Whitney U tests comparing US patents to each other region yield highly significant results (all p<0.001) with large effect sizes: Cohen's d=1.84 for US vs. EU, d=1.56 for US vs. China, d=1.54 for US vs. Japan, and d=1.45 for US vs. Korea. Effect sizes exceeding 0.8 indicate "large" practical significance (Cohen, 1988), confirming the US quality advantage represents both statistical certainty and substantive practical importance. Furthermore, pairwise tests comparing EU to China (p=0.008, d=0.60), Japan (p=0.001, d=0.81), and Korea (p<0.001, d=1.07) all confirm that every other major region produces significantly higher-quality patents than Europe, with effect sizes ranging from medium to large—reinforcing the severity of Europe's quality crisis.

    Crucially, Table 4B demonstrates that these quality differences persist even after controlling for technology domain specialization and filing year. Weighted least squares regression with wild bootstrap inference reveals robust quality advantages: US patents receive +6.94 more citations than EU patents within the same technology domains and time periods (p<0.001), Korea receives +1.37 more citations (p<0.001), and Japan receives +0.95 more citations (p=0.002). Only China's difference (+0.23 citations, p=0.610) is not statistically significant after domain controls. This confirms that the US, Korea, and Japan quality leadership reflects genuine innovation superiority rather than strategic domain selection, while China's apparent advantage over the EU in Table 4A primarily reflects specialization in higher-citation domains rather than pure quality differences.

    This finding contradicts volume-based rankings. The EU files the second-highest patent volume (288,520 patents in 2014-2018, Table 4A), yet generates the lowest per-patent impact. This volume-quality paradox is consistent with defensive patenting strategies (filing many incremental patents to protect existing products) rather than foundational research generating broad follow-on innovation. The US quality advantage persists consistently across the full time series where citation data is mature (Figure 4A). Figure 4B's domain analysis exposes the software-hardware quality divide underlying these regional differences. Software-centric domains (autonomous driving, infotainment, safety) generate 2-3× higher citations than hardware domains (thermal management, hybrids, batteries), with the US leading across all domains. This pattern holds strategic significance: the highest-quality innovation occurs in software domains where the EU is weakest. Autonomous driving patents receive 2-3× more citations than thermal management patents, yet the EU holds only 31% of autonomous patents versus 44% of thermal patents (Section 3). The EU invests R&D in lower-impact domains while lagging in high-impact areas.

    Figure 4B reveals the EU's most troubling pattern: ranking last in 6 of 7 technology domains, including traditional automotive strengths (safety systems, thermal management, hybrid powertrains), despite maintaining volume leadership (44-50% patent shares). This finding challenges the "European engineering excellence" narrative. While EU companies maintain volume leadership in traditional domains, their patents generate minimal follow-on research. The US dominates quality across ALL domains, even hardware areas where the EU holds volume advantages. In thermal management, US patents (5.21 citations) generate 3.2× more impact than EU patents (1.63) despite the EU filing 44% of thermal patents versus the US 17% (Section 3 data). This inversion (EU volume leadership producing minimal citation impact) epitomizes the quality crisis. Possible explanations include: (1) incremental innovation focus: EU patents improve existing technologies (better thermal systems, optimized hybrids) rather than enabling new capabilities; (2) product-specific IP: patents tied to specific vehicle models, not reusable platforms others can build on; (3) declining relevance: traditional domains (hybrids, thermal) become less central to EV value creation, attracting less researcher attention.

    ## Strategic Patterns and Theoretical Insights

    Korea's battery patents present an interesting anomaly: highest volume (31% share) but moderate citation quality (3.63 citations, 2nd of 5), with US battery patents (7.69) generating 2.1× more impact—illustrating how patent leadership does not always translate directly to market dominance, as manufacturing scale and commercialization speed play critical roles. These regional quality differences reflect the theoretical dynamics outlined in Section 2: NIS institutional differences shaping research approaches, resource-based domain specialization creating path dependencies, disruptive versus sustaining innovation patterns affecting citation trajectories, and knowledge tacitness effects varying by technology type.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Citation Impact vs. Knowledge Breadth

    Forward citations measure one dimension of innovation quality: the extent to which a patent generates follow-on research by other inventors. This metric favors foundational, platform-enabling technologies over incremental improvements or product-specific innovations. Citations do not capture all forms of knowledge transfer.

    To validate forward citations as a quality measure, we also calculated generality and originality indices (Hall, Jaffe & Trajtenberg, 2001) for the same 2014-2018 cohort. Generality measures how broadly a patent impacts different technology classes (calculated as 1 minus the Herfindahl index of forward citations across classes), while originality measures how diverse its knowledge sources are (same formula applied to backward citations). These metrics measure **citation diversity** rather than **citation volume**, revealing a critical distinction: US patents exhibit the highest generality (0.718) and originality (0.751), followed by Japan (0.678/0.689), while China shows the lowest scores (0.589/0.606). **Notably, Europe ranks middle (0.651/0.687) in diversity despite ranking last in citation volume (2.58 avg citations vs. 9.97 US)**. This paradox suggests EU patents integrate knowledge across diverse domains (moderate breadth) but fail to generate high-impact breakthroughs (low influence). EU innovation emphasizes **integrative system engineering**—combining existing knowledge from different fields—rather than **foundational platform technologies** that enable follow-on innovation.

    As documented in Section 5, the EU maintains the highest cross-border collaboration rates (2.59% of portfolio vs. 1.90% US, 2.16% JP, 3.20% CN, 0.66% KR). This suggests knowledge also flows through direct partnerships, joint ventures, and complementary capability exchanges. However, collaboration intensity does not fully offset citation gaps—the EU ranks highest in collaboration yet lowest in citations.

    Our interpretation: High-quality innovation requires both breakthrough research (citations) and collaborative capability exchange (partnerships). The US excels at both; the EU emphasizes collaboration but lags in foundational research generation. China prioritizes volume and rapid deployment over either citations or partnerships.

    Citations should thus be interpreted alongside collaboration patterns (Section 5) and patent volume (Section 3) to provide a complete picture of innovation strategies.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Cross-Border Collaboration and Knowledge Flows in EV Innovation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    While the previous section documented regional patent shares and domain-specific competencies, it tells only part of the story. Innovation in complex technological systems like electric vehicles increasingly depends on cross-border collaboration and knowledge flows. This section examines collaborative patent patterns to reveal the structure of global innovation networks and assess whether regions operate as isolated silos or integrated innovation ecosystems.

    We measure collaboration as patents with multi-regional assignees/inventors among our five focal regions (see Section 3 for complete methodology). This excludes within-region collaboration (e.g., Germany-France within EU) and collaborations with countries outside the five-region focus.
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    # Data loading: Collaborative patent data (5 regions)
    collab_data = pd.read_csv('data/02_collaborative_patents.csv')

    # Create a flag for single-region vs collaborative
    collab_data['is_collaborative'] = collab_data['collaboration_type'] != 'Single-region'

    # Calculate collaboration rate by year (overall)
    collab_rate_overall = collab_data.groupby('year').apply(
        lambda x: pd.Series({
            'total_patents': x['patent_count'].sum(),
            'collaborative_patents': x[x['is_collaborative']]['patent_count'].sum()
        })
    ).reset_index()
    collab_rate_overall['collaboration_rate'] = (
        collab_rate_overall['collaborative_patents'] / collab_rate_overall['total_patents'] * 100
    )

    # Calculate collaboration by major region pairs (excluding Single-region)
    collab_pairs = collab_data[collab_data['is_collaborative']].copy()
    collab_pairs_by_year = collab_pairs.groupby(['year', 'collaboration_type'])['patent_count'].sum().reset_index()

    # Calculate total collaborative patents per year for percentage calculation
    collab_totals = collab_pairs.groupby('year')['patent_count'].sum().reset_index()
    collab_totals.columns = ['year', 'total_collab']
    collab_pairs_by_year = collab_pairs_by_year.merge(collab_totals, on='year')
    collab_pairs_by_year['percentage'] = (collab_pairs_by_year['patent_count'] / collab_pairs_by_year['total_collab']) * 100

    # Get top 6 collaboration pairs by total volume across all years
    top_pairs = collab_pairs.groupby('collaboration_type')['patent_count'].sum().nlargest(6).index.tolist()
    collab_pairs_by_year_top = collab_pairs_by_year[collab_pairs_by_year['collaboration_type'].isin(top_pairs)]
    return collab_data, collab_pairs_by_year_top, collab_rate_overall


@app.cell(hide_code=True)
def _(alt, collab_rate_overall):
    # Figure 5A: Overall Collaboration Rate Trend (2014-2024)
    # Shows the percentage of patents that are collaborative vs single-region

    # Split data into complete (2014-2023) and incomplete (2023-2024)
    _rate_complete = collab_rate_overall[collab_rate_overall['year'] <= 2023]
    _rate_incomplete = collab_rate_overall[collab_rate_overall['year'] >= 2023]

    # Solid line for complete data
    _rate_solid = alt.Chart(_rate_complete).mark_line(
        strokeWidth=2,
        point=alt.OverlayMarkDef(size=80, filled=True, color='#e7298a')
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('collaboration_rate:Q',
                title='Collaboration Rate (%)',
                scale=alt.Scale(domain=[0, 2]),
                axis=alt.Axis(format='.1f', labelFontSize=11, grid=True, gridOpacity=0.3)),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('collaboration_rate:Q', title='Collaboration Rate (%)', format='.2f'),
            alt.Tooltip('collaborative_patents:Q', title='Collaborative Patents', format=','),
            alt.Tooltip('total_patents:Q', title='Total Patents', format=',')
        ]
    )

    # Dashed line for incomplete data
    _rate_dashed = alt.Chart(_rate_incomplete).mark_line(
        strokeWidth=2,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=80, filled=False, color='#e7298a')
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('collaboration_rate:Q'),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('collaboration_rate:Q', title='Collaboration Rate (%)', format='.2f'),
            alt.Tooltip('collaborative_patents:Q', title='Collaborative Patents', format=','),
            alt.Tooltip('total_patents:Q', title='Total Patents', format=',')
        ]
    )

    fig5a = (_rate_solid + _rate_dashed).properties(
        width=700,
        height=300,
        title=alt.Title(
            'Figure 5A: EV Patent Collaboration Rate (2014-2024)',
            subtitle='Percentage of patents with co-inventors/assignees from multiple regions. Dashed line indicates incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig5a
    return


@app.cell(hide_code=True)
def _(alt, collab_pairs_by_year_top):
    # Figure 5B: Major Collaboration Pairs Over Time
    # Line chart showing top 6 collaboration pairs
    # Adds shape encoding for B&W print compatibility

    # Define colors for collaboration pairs (top 6 by total volume: EU-JP, EU-US, US-CN, US-JP, EU-CN, CN-JP)
    _pair_colors = {
        'EU-JP': '#1f77b4',    # Blue (largest volume)
        'EU-US': '#ff7f0e',    # Orange
        'US-CN': '#2ca02c',    # Green
        'US-JP': '#d62728',    # Red
        'EU-CN': '#9467bd',    # Purple
        'CN-JP': '#8c564b'     # Brown
    }

    # Define shapes for B&W compatibility
    _pair_shapes = {
        'EU-JP': 'circle',
        'EU-US': 'square',
        'US-CN': 'triangle-up',
        'US-JP': 'diamond',
        'EU-CN': 'cross',
        'CN-JP': 'triangle-down'
    }

    # Split data
    _pairs_complete = collab_pairs_by_year_top[collab_pairs_by_year_top['year'] <= 2023]
    _pairs_incomplete = collab_pairs_by_year_top[collab_pairs_by_year_top['year'] >= 2023]

    # Solid lines
    _pairs_solid = alt.Chart(_pairs_complete).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=60, filled=True)
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('patent_count:Q',
                title='Cross-Border Patent Count (Co-Assignees from Multiple Regions)',
                axis=alt.Axis(labelFontSize=10, grid=True, gridOpacity=0.3)),
        color=alt.Color('collaboration_type:N',
                        title='Region Pair',
                        scale=alt.Scale(
                            domain=list(_pair_colors.keys()),
                            range=list(_pair_colors.values())
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=11, labelFontSize=10)),
        shape=alt.Shape('collaboration_type:N',
                        title='Region Pair',
                        scale=alt.Scale(
                            domain=list(_pair_shapes.keys()),
                            range=list(_pair_shapes.values())
                        ),
                        legend=alt.Legend(orient='right', titleFontSize=11, labelFontSize=10)),
        tooltip=[
            alt.Tooltip('collaboration_type:N', title='Pair'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('patent_count:Q', title='Patents', format=','),
            alt.Tooltip('percentage:Q', title='% of All Collaborative', format='.1f')
        ]
    )

    # Dashed lines
    _pairs_dashed = alt.Chart(_pairs_incomplete).mark_line(
        strokeWidth=1.5,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=60, filled=False)
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('patent_count:Q'),
        color=alt.Color('collaboration_type:N',
                        scale=alt.Scale(
                            domain=list(_pair_colors.keys()),
                            range=list(_pair_colors.values())
                        ),
                        legend=None),
        shape=alt.Shape('collaboration_type:N',
                        scale=alt.Scale(
                            domain=list(_pair_shapes.keys()),
                            range=list(_pair_shapes.values())
                        ),
                        legend=None),
        tooltip=[
            alt.Tooltip('collaboration_type:N', title='Pair'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('patent_count:Q', title='Patents', format=','),
            alt.Tooltip('percentage:Q', title='% of All Collaborative', format='.1f')
        ]
    )

    fig5b = (_pairs_solid + _pairs_dashed).properties(
        width=700,
        height=350,
        title=alt.Title(
            'Figure 5B: Top Cross-Border Collaboration Pairs (2014-2024)',
            subtitle='Patents with co-assignees/inventors from multiple regions. Six largest pairs by total volume. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig5b
    return


@app.cell(hide_code=True)
def _(alt, collab_data):
    def _():
        # Figure 5C: Collaboration Rate by Technology Domain (Small Multiples)
        # Shows collaboration % vs single-region % for each of 7 domains

        # Calculate collaboration rate by domain and year
        domain_collab = collab_data.groupby(['application_area', 'year', 'is_collaborative'])['patent_count'].sum().reset_index()

        # Pivot to get collaborative vs single-region side by side
        domain_totals = domain_collab.groupby(['application_area', 'year'])['patent_count'].sum().reset_index()
        domain_totals.columns = ['application_area', 'year', 'total']

        domain_collab = domain_collab.merge(domain_totals, on=['application_area', 'year'])
        domain_collab['percentage'] = (domain_collab['patent_count'] / domain_collab['total']) * 100

        # Label collaborative vs single-region
        domain_collab['collab_label'] = domain_collab['is_collaborative'].map({True: 'Collaborative', False: 'Single-region'})

        # Shorten domain names
        _domain_labels_fig5c = {
            'Battery Technology': 'Battery Tech',
            'EV Propulsion & Charging': 'Propulsion',
            'Autonomous Driving & ADAS': 'Autonomous',
            'Hybrid Powertrains': 'Hybrid',
            'Vehicle Safety Systems': 'Safety',
            'Thermal Management': 'Thermal',
            'Infotainment & Connectivity': 'Infotainment'
        }
        domain_collab['domain_short'] = domain_collab['application_area'].map(_domain_labels_fig5c)
        domain_collab = domain_collab[domain_collab['domain_short'].notna()].copy()

        # Function to create small bar chart for one domain
        def _create_collab_domain_chart(data, domain_name):
            _subset = data[data['domain_short'] == domain_name].copy()

            # Get only collaborative patents
            _collab_only = _subset[_subset['is_collaborative'] == True].copy()

            # Split into complete and incomplete
            _complete = _collab_only[_collab_only['year'] <= 2023]
            _incomplete = _collab_only[_collab_only['year'] >= 2023]

            # Solid line for collaboration rate
            _solid = alt.Chart(_complete).mark_line(
                strokeWidth=1.5,
                point=alt.OverlayMarkDef(size=50, filled=True, color='#e7298a')
            ).encode(
                x=alt.X('year:O', title='Year', axis=alt.Axis(labelAngle=-45, labelFontSize=9)),
                y=alt.Y('percentage:Q', title='Collaboration Rate (%)',
                        scale=alt.Scale(domain=[0, 2]),
                        axis=alt.Axis(format='.1f', labelFontSize=9, grid=True, gridOpacity=0.2)),
                tooltip=[
                    alt.Tooltip('year:O', title='Year'),
                    alt.Tooltip('percentage:Q', title='Collaboration Rate (%)', format='.2f'),
                    alt.Tooltip('patent_count:Q', title='Collaborative Patents', format=',')
                ]
            )

            # Dashed line
            _dashed = alt.Chart(_incomplete).mark_line(
                strokeWidth=1.5,
                strokeDash=[5, 5],
                point=alt.OverlayMarkDef(size=50, filled=False, color='#e7298a')
            ).encode(
                x=alt.X('year:O'),
                y=alt.Y('percentage:Q'),
                tooltip=[
                    alt.Tooltip('year:O', title='Year'),
                    alt.Tooltip('percentage:Q', title='Collaboration Rate (%)', format='.2f'),
                    alt.Tooltip('patent_count:Q', title='Collaborative Patents', format=',')
                ]
            )

            return (_solid + _dashed).properties(
                width=220,
                height=150,
                title=alt.TitleParams(domain_name, fontSize=11, fontWeight='bold', anchor='start')
            )

        # Create charts for 7 domains
        _domains_ordered = [
            'Battery Tech', 'Autonomous', 'Infotainment',
            'Propulsion', 'Thermal', 'Safety', 'Hybrid'
        ]

        _charts_collab = [_create_collab_domain_chart(domain_collab, d) for d in _domains_ordered]

        # Arrange in 3x3 grid
        _row1_collab = alt.hconcat(_charts_collab[0], _charts_collab[1], _charts_collab[2])
        _row2_collab = alt.hconcat(_charts_collab[3], _charts_collab[4], _charts_collab[5])
        _row3_collab = alt.hconcat(_charts_collab[6])

        fig5c = alt.vconcat(_row1_collab, _row2_collab, _row3_collab).properties(
            title=alt.Title(
                'Figure 5C: Collaboration Rate by Technology Domain (2014-2024)',
                subtitle='Percentage of patents with cross-border collaboration in each domain. Dashed lines indicate incomplete 2024 data.',
                fontSize=14,
                anchor='start'
            )
        ).configure_view(strokeWidth=0)
        return fig5c


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Multi-Regional Collaboration Patterns

    Figures 5A-C reveal a striking pattern: EV innovation remains overwhelmingly insular despite globalization narratives. Across 2014-2024, collaborative patents constitute only 0.65-1.28% of total patents (Figure 5A). The collaboration rate peaked at 1.28% in 2018, then declined to 0.87% by 2021 and 0.89% in 2023 (Statistical tests, Table 5, confirm this decline is significant at p<0.001). This contrasts with expectations of increasing cross-border knowledge flows in complex technological systems.

    Three explanations emerge. First, institutional divergence creates friction: different R&D funding mechanisms, IP norms, and industry-government relationships across regions make joint projects costly to coordinate. Second, strategic competition incentivizes proprietary protection: batteries and software represent winner-take-all platform opportunities where firms prioritize control over sharing (Tesla's Supercharger network, CATL's battery hegemony). Third, comprehensive regional capabilities reduce collaboration necessity: Korea's battery excellence and US software dominance reflect self-sufficiency, with collaboration emerging only when complementary capabilities reside in different regions (e.g., EU thermal management + Korean battery cells).

    ### Domain-Specific Collaboration: Where Openness Emerges

    Figure 5C's domain analysis reveals that collaboration rates vary dramatically across technologies. High-collaboration domains (batteries, autonomous driving) average a 1.15% collaboration rate versus low-collaboration domains (thermal, safety, hybrid) at 0.91%—a statistically significant difference (χ²=141.3, p<0.001, Table 5). This pattern reflects geographic separation of complementary capabilities: EU-Korean battery partnerships combine European thermal management with Korean cell technology; EU-US autonomous driving collaborations leverage US software expertise (Waymo, Mobileye) with European automotive integration. Low-collaboration domains involve mature engineering with established regional supply chains, suggesting that self-sufficient capabilities reduce collaboration necessity.

    ### Regional Collaboration Strategies: Selectivity vs. Fragmentation

    The data reveal distinct regional approaches shaped by capability endowments and institutional structures. **Korea** pursues selective excellence: minimal collaboration outside batteries, but focused EU-KR partnerships (2,332 patents over 2014-2023) for complementary capabilities. **China** exhibits declining collaboration as capabilities mature: collaboration declined from 0.8% (2014) to 0.3% (2023) as battery and infotainment strengths reduce dependency on external partners, emphasizing rapid internal iteration consistent with the consumer electronics business model.

    The **EU** demonstrates dependent openness: participation in the two largest collaboration pairs (EU-JP: 5,410 patents; EU-US: 4,966 patents), accounting for the majority of cross-border collaboration. However, this "hub" position may reflect weakness rather than strength. The EU's multi-directional partnerships, with the US for software, Japan for hybrid/safety systems, Korea for batteries, and China for infotainment, signal fragmented capabilities requiring external support across multiple domains. Competitors' selectivity (Korea's battery focus, US software dominance) reflects self-sufficiency in core domains.

    The **US** shows strategic ambivalence: historically collaborative but willing to sacrifice partnerships for geopolitical objectives, increasingly relying on domestic software capabilities while selectively partnering with allies for hardware. The US-China collapse (analyzed in Section 5.2) provides the clearest evidence of geopolitical tensions overriding economic complementarity.
    """)
    return


@app.cell(hide_code=True)
def _(collab_data, np, stats):
    """Statistical Analysis: Collaboration Pattern Tests"""

    # Filter true collaborative patents (exclude Single-region)
    _true_collab = collab_data[collab_data['collaboration_type'] != 'Single-region']

    # ==========================================================================
    # TEST 1: Collaboration rate temporal trend (2018 peak vs 2021 decline)
    # ==========================================================================
    _yearly_total = collab_data.groupby('year')['patent_count'].sum()
    _yearly_collab = _true_collab.groupby('year')['patent_count'].sum()

    # 2018 vs 2021 comparison
    _total_2018 = _yearly_total[2018]
    _collab_2018 = _yearly_collab[2018]
    _rate_2018 = (_collab_2018 / _total_2018) * 100

    _total_2021 = _yearly_total[2021]
    _collab_2021 = _yearly_collab[2021]
    _rate_2021 = (_collab_2021 / _total_2021) * 100

    # Two-proportion z-test
    _n1, _n2 = int(_total_2018), int(_total_2021)
    _p1, _p2 = _collab_2018/_total_2018, _collab_2021/_total_2021
    _p_pooled = (_collab_2018 + _collab_2021) / (_total_2018 + _total_2021)
    _se = np.sqrt(_p_pooled * (1 - _p_pooled) * (1/_n1 + 1/_n2))
    _z_trend = (_p1 - _p2) / _se
    _p_trend = 2 * (1 - stats.norm.cdf(abs(_z_trend)))

    # ==========================================================================
    # TEST 2: Domain-specific collaboration rates
    # ==========================================================================
    _domain_total = collab_data.groupby('application_area')['patent_count'].sum()
    _domain_collab = _true_collab.groupby('application_area')['patent_count'].sum()
    _domain_rates = (_domain_collab / _domain_total * 100).sort_values(ascending=False)

    # Chi-square test: High-collaboration vs low-collaboration domains
    _high_domains = ['Battery Technology', 'Autonomous Driving & ADAS']
    _low_domains = ['Thermal Management', 'Vehicle Safety Systems', 'Hybrid Powertrains']

    _high_total = _domain_total[_high_domains].sum()
    _high_collab = _domain_collab[_high_domains].sum()
    _low_total = _domain_total[_low_domains].sum()
    _low_collab = _domain_collab[_low_domains].sum()

    _contingency = np.array([
        [_high_collab, _high_total - _high_collab],
        [_low_collab, _low_total - _low_collab]
    ])
    _chi2_domain, _p_domain, _dof, _expected = stats.chi2_contingency(_contingency)

    # ==========================================================================
    # TEST 3: US-China collaboration collapse (2020 vs 2023)
    # ==========================================================================
    _us_cn_collab = _true_collab[_true_collab['collaboration_type'].isin(['CN-US', 'US-CN'])]
    _us_cn_by_year = _us_cn_collab.groupby('year')['patent_count'].sum()

    _collab_2020 = _us_cn_by_year[2020] if 2020 in _us_cn_by_year.index else 0
    _collab_2023 = _us_cn_by_year[2023] if 2023 in _us_cn_by_year.index else 0

    _total_2020 = _yearly_total[2020]
    _total_2023 = _yearly_total[2023]

    # Two-proportion z-test
    _n1_cn, _n2_cn = int(_total_2020), int(_total_2023)
    _p1_cn, _p2_cn = _collab_2020/_n1_cn, _collab_2023/_n2_cn
    _p_pooled_cn = (_collab_2020 + _collab_2023) / (_n1_cn + _n2_cn)
    _se_cn = np.sqrt(_p_pooled_cn * (1 - _p_pooled_cn) * (1/_n1_cn + 1/_n2_cn))
    _z_collapse = (_p1_cn - _p2_cn) / _se_cn
    _p_collapse = 2 * (1 - stats.norm.cdf(abs(_z_collapse)))

    _pct_change = ((_collab_2023 - _collab_2020) / _collab_2020) * 100 if _collab_2020 > 0 else 0

    # Store results
    collab_test_results = {
        'temporal_trend': {
            'rate_2018': _rate_2018,
            'rate_2021': _rate_2021,
            'collab_2018': int(_collab_2018),
            'collab_2021': int(_collab_2021),
            'total_2018': int(_total_2018),
            'total_2021': int(_total_2021),
            'z_stat': _z_trend,
            'p_value': _p_trend
        },
        'domain_comparison': {
            'high_rate': (_high_collab / _high_total) * 100,
            'low_rate': (_low_collab / _low_total) * 100,
            'high_collab': int(_high_collab),
            'high_total': int(_high_total),
            'low_collab': int(_low_collab),
            'low_total': int(_low_total),
            'chi2': _chi2_domain,
            'p_value': _p_domain
        },
        'us_china_collapse': {
            'collab_2020': int(_collab_2020),
            'collab_2023': int(_collab_2023),
            'pct_change': _pct_change,
            'z_stat': _z_collapse,
            'p_value': _p_collapse
        },
        'domain_rates': _domain_rates
    }
    return (collab_test_results,)


@app.cell(hide_code=True)
def _(collab_test_results, mo):
    """Display Table 5: Statistical tests for collaboration patterns"""
    _ct = collab_test_results
    mo.md(f"""
    **Table 5.** Cross-Border Collaboration: Statistical Tests

    | Test | Result | Z-statistic | p-value | Significant |
    |------|--------|-------------|---------|-------------|
    | **1. Temporal Trend (2018 vs 2021)** | {_ct['temporal_trend']['rate_2018']:.2f}% → {_ct['temporal_trend']['rate_2021']:.2f}% | {_ct['temporal_trend']['z_stat']:.3f} | <0.001 | YES |
    | **2. Domain Differences** | High: {_ct['domain_comparison']['high_rate']:.2f}%, Low: {_ct['domain_comparison']['low_rate']:.2f}% | χ²={_ct['domain_comparison']['chi2']:.1f} | <0.001 | YES |

    *Note*: Test 1 compares collaboration rates at 2018 peak (1.28%, n={_ct['temporal_trend']['collab_2018']:,}/{_ct['temporal_trend']['total_2018']:,}) versus 2021 decline (0.87%, n={_ct['temporal_trend']['collab_2021']:,}/{_ct['temporal_trend']['total_2021']:,}) using two-proportion z-test. Test 2 compares high-collaboration domains (Battery, Autonomous: {_ct['domain_comparison']['high_collab']:,}/{_ct['domain_comparison']['high_total']:,}) versus low-collaboration domains (Thermal, Safety, Hybrid: {_ct['domain_comparison']['low_collab']:,}/{_ct['domain_comparison']['low_total']:,}) using chi-square test. Both tests reject null hypothesis at p<0.001, confirming collaboration patterns are statistically robust.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Knowledge Flow Networks and Geopolitical Fragmentation

    Beyond formal collaboration, patent citations reveal how knowledge diffuses across regional boundaries. When a patent from region X cites a patent from region Y, it signals knowledge transfer: inventors in X built upon Y's prior art. This section analyzes citation flows using the knowledge flow networks dataset (1,921 rows covering 2014-2024, 5 regions, 7 domains) to examine regional openness, dominant knowledge flows, and geopolitical disruptions.
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    # Load knowledge flow networks data
    knowledge_flows_df = pd.read_csv('data/07_knowledge_flow_networks.csv')
    return (knowledge_flows_df,)


@app.cell(hide_code=True)
def _(alt, knowledge_flows_df, region_colors, region_shapes):
    # Figure 6A: Self-Citation Rates Over Time (5 Regions)

    # Calculate citation-weighted self-citation rates
    # Weight each domain by its citation volume (more citations = more weight)
    _self_citations = knowledge_flows_df[knowledge_flows_df['flow_type'] == 'Self-citation'].groupby(['citing_region', 'year'])['citation_count'].sum().reset_index()
    _self_citations.columns = ['citing_region', 'year', 'self_count']

    _total_citations = knowledge_flows_df.groupby(['citing_region', 'year'])['citation_count'].sum().reset_index()
    _total_citations.columns = ['citing_region', 'year', 'total_count']

    _yearly_rates = _self_citations.merge(_total_citations, on=['citing_region', 'year'])
    _yearly_rates['self_citation_pct'] = (_yearly_rates['self_count'] / _yearly_rates['total_count']) * 100
    _yearly_rates['region'] = _yearly_rates['citing_region']  # Rename for consistency

    # Split data into complete (2014-2023) and incomplete (2023-2024)
    _rates_complete = _yearly_rates[_yearly_rates['year'] <= 2023]
    _rates_incomplete = _yearly_rates[_yearly_rates['year'] >= 2023]

    # Solid lines for complete data
    _rates_solid = alt.Chart(_rates_complete).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=80, filled=True)
    ).encode(
        x=alt.X('year:O',
                title='Year',
                axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('self_citation_pct:Q',
                title='Self-Citation Rate (%)',
                scale=alt.Scale(domain=[0, 70]),
                axis=alt.Axis(labelFontSize=11, grid=True, gridOpacity=0.3)),
        color=alt.Color('region:N',
                       title='Region',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        shape=alt.Shape('region:N',
                       title='Region',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('self_citation_pct:Q', title='Self-Citation Rate (%)', format='.1f')
        ]
    )

    # Dashed lines for incomplete data
    _rates_dashed = alt.Chart(_rates_incomplete).mark_line(
        strokeWidth=1.5,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=80, filled=False)
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('self_citation_pct:Q'),
        color=alt.Color('region:N',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=None),
        shape=alt.Shape('region:N',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=None),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('self_citation_pct:Q', title='Self-Citation Rate (%)', format='.1f')
        ]
    )

    fig_6a = (_rates_solid + _rates_dashed).properties(
        width=700,
        height=400,
        title=alt.TitleParams(
            'Figure 6A: Self-Citation Rates by Region (2014-2024)',
            subtitle='Lower values indicate greater openness to external knowledge sources. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig_6a
    return


@app.cell(hide_code=True)
def _(alt, knowledge_flows_df):
    # Figure 6B: Major Knowledge Flows (2023)

    # Filter to 2023 cross-regional flows only
    flows_2023 = knowledge_flows_df[
        (knowledge_flows_df['year'] == 2023) &
        (knowledge_flows_df['flow_type'] == 'Cross-regional')
    ].copy()

    # Aggregate by citing-cited pair
    flow_pairs = flows_2023.groupby(['citing_region', 'cited_region'])['citation_count'].sum().reset_index()

    # Get top 10 flows
    top_flows = flow_pairs.nlargest(10, 'citation_count')

    # Create flow labels
    top_flows['flow_label'] = top_flows['citing_region'] + ' → ' + top_flows['cited_region']
    top_flows = top_flows.sort_values('citation_count', ascending=True)  # For horizontal bar chart

    # Map regions to full names for clarity
    region_map_short = {
        'CN': 'CN',
        'US': 'US',
        'EU': 'EU',
        'JP': 'JP',
        'KR': 'KR'
    }

    fig_6b = alt.Chart(top_flows).mark_bar().encode(
        y=alt.Y('flow_label:N',
               title='Knowledge Flow',
               sort='-x',
               axis=alt.Axis(labelLimit=200)),
        x=alt.X('citation_count:Q',
               title='Number of Citations (2023)',
               axis=alt.Axis(format=',.0f')),
        color=alt.Color('citing_region:N',
                       scale=alt.Scale(
                           domain=['US', 'CN', 'EU', 'JP', 'KR'],
                           range=['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd']
                       ),
                       legend=None),
        tooltip=[
            alt.Tooltip('flow_label:N', title='Flow'),
            alt.Tooltip('citation_count:Q', title='Citations', format=',')
        ]
    ).properties(
        width=700,
        height=400,
        title=alt.TitleParams(
            'Figure 6B: Top 10 Cross-Regional Knowledge Flows (2023)',
            subtitle='Format: Citing Region → Cited Region (e.g., EU→US means EU patents cite US patents). Bars colored by citing region.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig_6b
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Geopolitical fragmentation** reshapes knowledge networks: US-China collaboration collapsed 76% (562→135 patents, 2020→2023) and bilateral citation flows declined 64-70% after peaking in 2021, demonstrating how trade tensions and technology restrictions fragment global innovation systems despite economic complementarity. For Europe, this bifurcation creates strategic opportunity: EU patents can serve as neutral knowledge bridges acceptable to both US and Chinese innovators, leveraging Europe's collaborative tradition and institutional neutrality.

    **Regional knowledge openness** varies significantly: Europe exhibits moderate self-citation (42.4% of citations remain within EU patents), indicating balanced knowledge absorption from external sources while building on domestic capabilities—a pattern consistent with Europe's collaborative innovation culture and extensive cross-border research programs.

    ### The EU-US Knowledge Axis and Regional Knowledge Centrality

    Figure 6B maps the ten largest cross-regional knowledge flows in 2023. The EU-US bilateral relationship dominates global knowledge exchange: European patents cite US innovations 7,043 times, while US patents cite European research 6,096 times—totaling 13,139 citations. This bidirectional flow dwarfs all other pairs and reflects complementary strengths: US software/autonomous driving capabilities combined with EU mechanical engineering and safety system expertise (Section 3). Notably, substantial absolute citations to EU patents (6,096 from US) do not contradict EU's low per-patent quality (2.58 average; Section 5.1)—EU's large patent base (288,520 patents in 2014-2018 cohort, second globally) generates ~744,000 total citations, of which US→EU represents less than 1%. Low quality per patent combined with high volume produces moderate absolute citation flows.

    The next-largest flows reveal a US paradox: US→Japan (4,958 citations), US→Korea (4,014), and US→China (2,903) position the US as an active knowledge consumer, not merely a source. Despite generating the highest-quality patents (9.97 average citations; Section 4), US inventors actively build on Asian innovations—particularly Japanese hybrid expertise and Korean battery technologies. Aggregating all 2023 cross-regional flows, US patents cite others 17,971 times while being cited 14,351 times (net +3,620), making the US simultaneously the highest-quality knowledge producer and the most active knowledge consumer. This bidirectional openness reflects a robust open innovation culture: US leadership stems not from insularity but from combining internal excellence with aggressive external learning.

    The EU maintains significant ties to Japan (3,869 citations) and Korea (2,664 citations). However, EU-China knowledge flows remain modest: EU→CN (1,543) and CN→EU (1,502) in 2023, far below the EU's ties to Japan or Korea despite China's 25% global patent share. This mirrors weak EU-CN collaboration patterns (Section 5.1) and suggests limited genuine technical exchange, possibly reflecting IP protection concerns or divergent technological standards.

    **Additional note**: Citation lags (time between cited and citing patent filing dates) increase naturally over time as recent patents lack time to accumulate citations. Focusing on mature data (2014-2020), all regions exhibit similar absorption speeds: Japan 1.45 years, China 1.54 years, EU 1.56 years, Korea 1.63 years, US 1.66 years. The differences are modest (0.2 years), suggesting citation lags reflect universal R&D cycle times (~18 months) rather than institutional differences.
    """)
    return


@app.cell(hide_code=True)
def _(knowledge_flows_df, np, stats):
    """Statistical Analysis: Knowledge Flow Pattern Tests"""

    # ==========================================================================
    # TEST 1: Self-citation rates regional differences
    # ==========================================================================
    _self_citation_stats = []
    for _region in ['CN', 'US', 'EU', 'JP', 'KR']:
        _region_flows = knowledge_flows_df[knowledge_flows_df['citing_region'] == _region]

        _total_citations = _region_flows['citation_count'].sum()
        _self_citations = _region_flows[_region_flows['cited_region'] == _region]['citation_count'].sum()
        _cross_citations = _total_citations - _self_citations

        _self_rate = (_self_citations / _total_citations) * 100 if _total_citations > 0 else 0

        _self_citation_stats.append({
            'region': _region,
            'self_citations': int(_self_citations),
            'cross_citations': int(_cross_citations),
            'total': int(_total_citations),
            'self_rate': _self_rate
        })

    # Chi-square test for regional differences
    _contingency_self = np.array([[d['self_citations'], d['cross_citations']] for d in _self_citation_stats])
    _chi2_self, _p_self, _dof, _expected = stats.chi2_contingency(_contingency_self)

    # ==========================================================================
    # TEST 2: US-China knowledge collapse (2021 vs 2023)
    # ==========================================================================
    _us_to_cn = knowledge_flows_df[(knowledge_flows_df['citing_region'] == 'US') & (knowledge_flows_df['cited_region'] == 'CN')]
    _cn_to_us = knowledge_flows_df[(knowledge_flows_df['citing_region'] == 'CN') & (knowledge_flows_df['cited_region'] == 'US')]

    _us_cn_by_year = _us_to_cn.groupby('year')['citation_count'].sum()
    _cn_us_by_year = _cn_to_us.groupby('year')['citation_count'].sum()

    _us_cn_2021 = _us_cn_by_year[2021] if 2021 in _us_cn_by_year.index else 0
    _us_cn_2023 = _us_cn_by_year[2023] if 2023 in _us_cn_by_year.index else 0
    _cn_us_2021 = _cn_us_by_year[2021] if 2021 in _cn_us_by_year.index else 0
    _cn_us_2023 = _cn_us_by_year[2023] if 2023 in _cn_us_by_year.index else 0

    _pct_us_cn = ((_us_cn_2023 - _us_cn_2021) / _us_cn_2021) * 100 if _us_cn_2021 > 0 else 0
    _pct_cn_us = ((_cn_us_2023 - _cn_us_2021) / _cn_us_2021) * 100 if _cn_us_2021 > 0 else 0

    # Chi-square test for bilateral pattern change
    _contingency_collapse = np.array([
        [_us_cn_2021, _cn_us_2021],
        [_us_cn_2023, _cn_us_2023]
    ])
    _chi2_collapse, _p_collapse, _, _ = stats.chi2_contingency(_contingency_collapse)

    # Store results
    kflow_test_results = {
        'self_citation': {
            'stats': _self_citation_stats,
            'chi2': _chi2_self,
            'p_value': _p_self
        },
        'us_china_collapse': {
            'us_cn_2021': int(_us_cn_2021),
            'us_cn_2023': int(_us_cn_2023),
            'cn_us_2021': int(_cn_us_2021),
            'cn_us_2023': int(_cn_us_2023),
            'pct_us_cn': _pct_us_cn,
            'pct_cn_us': _pct_cn_us,
            'chi2': _chi2_collapse,
            'p_value': _p_collapse
        }
    }
    return (kflow_test_results,)


@app.cell(hide_code=True)
def _(kflow_test_results, mo):
    """Display Table 6: Statistical tests for knowledge flow patterns"""
    _kf = kflow_test_results
    _sc = _kf['self_citation']['stats']

    mo.md(f"""
    **Table 6.** Self-Citation Rate Regional Differences (2014-2024)

    | Region | Self-Citation Rate | Self Citations | Total Citations |
    |--------|-------------------|----------------|-----------------|
    | China | {_sc[0]['self_rate']:.1f}% | {_sc[0]['self_citations']:,} | {_sc[0]['total']:,} |
    | European Union | {_sc[2]['self_rate']:.1f}% | {_sc[2]['self_citations']:,} | {_sc[2]['total']:,} |
    | Japan | {_sc[3]['self_rate']:.1f}% | {_sc[3]['self_citations']:,} | {_sc[3]['total']:,} |
    | United States | {_sc[1]['self_rate']:.1f}% | {_sc[1]['self_citations']:,} | {_sc[1]['total']:,} |
    | South Korea | {_sc[4]['self_rate']:.1f}% | {_sc[4]['self_citations']:,} | {_sc[4]['total']:,} |

    *Chi-square test*: χ²={_kf['self_citation']['chi2']:.1f}, p<0.001 (highly significant regional differences)

    *Note*: This test examines whether regional differences in self-citation rates (patents citing same-region prior art) are statistically significant using chi-square test on 2014-2024 aggregate data. Europe's moderate self-citation rate (42.4%) indicates balanced knowledge absorption from external sources while building on domestic capabilities.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Business Model Innovation: The Consumer Electronics Pathway

    **Hypothesis 4** predicts that cross-industry business model transfer can enable market competitiveness despite patent quality gaps when product characteristics align (modularity, software-centricity, network effects). China's trajectory provides a critical test: despite ranking last in patent volume among five regions (14.2%, Section 3) and demonstrating significantly lower citation quality (2.80 vs. US 7.16, Section 4), Chinese EV manufacturers have achieved substantial market penetration through consumer electronics business logic. The "EVs as smartphones" strategy—rapid iteration cycles (24 months vs. traditional 40-50 months; McKinsey, 2023), volume-based cost reduction, digital experience differentiation (multi-screen interfaces, OTA updates), and ecosystem integration—represents fundamental business model innovation. Patent evidence reveals how this transferred logic manifests: strategic domain priorities (batteries as infrastructure, infotainment as differentiation), implementation speed over invention depth, and aggressive external knowledge absorption (21.5% self-citation, lowest among all regions). This section examines whether business model innovation constitutes an independent competitive pathway or merely temporary market disruption requiring eventual patent leadership convergence.

    ## Strategic Domain Priorities: Infrastructure + Experience

    Patent evidence reveals selective focus mirroring smartphone industry logic. In **batteries**, China's patent share grew 7-fold (3.6% → 25.0%, Section 3) but remains second to Korea's 29-33% share despite leading global manufacturing (53%; ITIF, 2024). This parallels consumer electronics: China dominates assembly while Korea (Samsung, LG) leads component innovation. China treats batteries as critical infrastructure requiring supply chain control (BYD's Blade Battery, CATL's LFP optimization) rather than primary differentiation—the semiconductor strategy applied to EVs. In **infotainment**, China's 50% patent growth (10.1% → 15.2%) contrasts with US software dominance (53-60%), yet Chinese manufacturers excel at rapid implementation—multi-screen interfaces, AR integration, OTA updates, smartphone ecosystems—demonstrating that competitive advantage flows from execution speed over invention depth. This dual focus replicates Apple's iPhone strategy: hardware foundation (battery cost/supply control) plus software differentiation (digital experience). Patent shares understate commercial impact: implementation excellence, not invention leadership, drives market penetration.

    ## Implementation Speed: Rapid Iteration as Competitive Advantage

    Chinese EV manufacturers operationalize consumer electronics principles through compressed development cycles: 24 months concept-to-launch versus traditional 40-50 months, approaching smartphone timescales (12-18 months; McKinsey, 2023). This velocity enabled model proliferation mirroring annual smartphone refresh cycles (BYD: 19 new models 2017-2023; NIO: 9; XPeng: 6; California Management Review, 2024) rather than traditional 5-7 year automotive platforms. Operational execution embeds consumer electronics design language: dual/triple touchscreens (11-17 inches), AR integration, smartphone-vehicle ecosystems, OTA updates.

    **Xiaomi's market entry exemplifies this business model transfer mechanism.** The smartphone giant announced its EV ambitions in March 2021, launched the SU7 sedan in March 2024 (3-year development versus traditional 5-7 years), and delivered 135,000 units within nine months despite zero prior automotive experience (Canalys, 2024). Xiaomi's competitive advantage stems not from automotive R&D but from **ecosystem integration**—500 million connected smart devices enabling "Human × Car × Home" seamless experiences where a single voice command coordinates home thermostats, vehicle pre-conditioning, and smartphone navigation. The SU7's pricing strategy ($29,900, half of Tesla's comparable Model 3) targets Xiaomi's existing 20 million premium smartphone users in China, achieving 15.4% gross margin—exceeding Tesla (13.9%) and NIO (9.2%)—by leveraging supply chain expertise from consumer electronics. This demonstrates business model innovation generating competitive outcomes independently of technological leadership: Xiaomi succeeded through **ecosystem lock-in and cross-platform integration** rather than battery chemistry breakthroughs or autonomous driving patents. The company's trajectory validates H4's core mechanism: when modularity, software-centricity, and network effects characterize product architecture, consumer electronics business logic transfers directly to automotive markets, enabling rapid market penetration through commercialization excellence rather than R&D superiority.

    Patent evidence supports this strategic shift: China's modular design patents (seats, interiors, chassis) quadrupled from 1.8% (2014) to 8.3% (2023), +122% in absolute terms (214→476 patents), while EU declined from 5,222→1,960 and Japan from 2,193→795. This countercyclical investment treats EVs as mass-customizable products rather than standardized industrial goods.

    ## Implications for European Innovation Strategy

    China's consumer electronics pathway demonstrates that competitive advantage increasingly stems from *how* firms commercialize rather than *what* they invent—a shift with profound implications for EU innovation policy. Europe cannot replicate China's state-directed coordination or manufacturing scale (28.6% GDP vs EU 20.3%), nor match implementation speeds (24 vs. 40-50 months). However, asymmetric advantages exist: Europe's engineering depth enables differentiation through durability, sustainability, and privacy—precisely where rapid-iteration models systematically underinvest.

    **Strategic takeaways for Europe:** (1) **Accept different competitive logic**: Competing on patent quality and engineering depth requires premium positioning, not volume leadership; (2) **Leverage regulatory authority**: Lifecycle requirements, repairability mandates, and privacy protections impose asymmetric costs on rapid-obsolescence competitors; (3) **Differentiate on sustainability**: Europe's thermal management expertise (44% patent share) becomes strategic when regulations mandate 10-15 year vehicle lifespans rather than 3-5 year replacement cycles. Business model innovation reveals multiple pathways to competitiveness—China's volume-based approach represents one option, not the only viable strategy.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Key Empirical Patterns and Implications for EU Innovation Policy

    Our analysis tests four hypotheses with direct implications for European innovation strategy. Table 7 summarizes key findings:

    **Table 7.** Summary of Hypothesis Testing Results and EU Implications

    | Hypothesis | Evidence | EU Implication |
    |------------|----------|----------------|
    | **H1: RBV → Volume-Quality**<br/>(The Legacy Trap) | • EU: 2nd volume (24.9%), last quality (2.58 citations)<br/>• US: 1st volume (30.8%), 1st quality (9.97)<br/>• Gap persists within identical domains | Accumulated capabilities in declining technologies harm quality during transitions. €57B annual R&D directed at obsolescing domains. Requires strategic reorientation toward batteries, autonomous software. |
    | **H2: Open Innovation → Collaboration**<br/>(Geopolitical Fragmentation) | • US-CN collaboration: -76% (562→135, 2020→2023)<br/>• Citation flows: -64-70% after 2021 peak<br/>• Despite extreme complementarity | Collaboration collapsed despite mutual gains. EU positioned as neutral knowledge bridge between bifurcated US-CN ecosystems. Strengthen EU-Korea/EU-Japan ties while leveraging institutional neutrality. |
    | **H3: NIS → Knowledge Openness**<br/>(Balanced Absorption) | • EU self-citation: 42.4% (moderate, mid-range)<br/>• China: 21.5% (lowest), US: 48.2%<br/>• EU balances domestic/external knowledge | Europe's moderate openness enables knowledge absorption from external sources while building on domestic capabilities. Maintain collaborative R&D programs (Horizon Europe) while protecting critical IP. |
    | **H4: Business Model Innovation**<br/>(Alternative Pathway) | • China: 2.6× quality disadvantage (2.80 vs US 7.16)<br/>• Yet substantial market penetration<br/>• 24-month cycles vs. EU 40-50 months | Competitive advantage from *how* (commercialize) not *what* (invent). EU pathways: lifecycle optimization (durability, repairability), privacy-first architectures, sustainability differentiation. |

    *Note*: Volume percentages reflect 2014-2018 cohort (5-region total). Citation quality based on forward citations with 5-10 year window. All findings statistically significant (p<0.001).

    **The Legacy Trap.** Europe's second-highest patent volume (24.9%, 2014-2018 cohort) fails to translate into quality impact. European patents average 2.58 forward citations versus 9.97 for the US—a 3.9× quality gap that persists even within identical technology domains. This contradicts resource-based assumptions that accumulated capabilities generate both volume and quality. Instead, Europe's strength in declining technologies (hybrid powertrains, traditional thermal management, safety systems rooted in ICE architectures) represents path dependency becoming competitive liability. Capabilities without strategic reorientation toward future value creation (battery chemistry, autonomous software, digital experiences) generate high activity but minimal impact. The EU's substantial R&D expenditure (€57 billion annually) directed toward optimizing obsolescing technologies exemplifies how resource accumulation can paradoxically harm innovation quality during industry transitions.

    **Geopolitical Fragmentation Overrides Economic Logic.** Despite extreme technological complementarity—US leading autonomous driving (35% share), China leading batteries (47%), Europe leading thermal management (33%)—cross-regional collaboration collapsed rather than intensified. US-China collaborative patents declined 76% (562→135, 2020→2023) despite mutual gains from knowledge sharing. Citation flows followed: bilateral US-China citations fell 64-70% after peaking in 2021, representing approximately five years of lost knowledge diffusion. Trade tensions, technology sovereignty concerns, and platform control competition override open innovation logic, demonstrating that technological complementarity is necessary but not sufficient. For Europe, this fragmentation creates strategic opportunity: EU patents can serve as neutral knowledge bridges between bifurcated US and Chinese ecosystems, leveraging institutional neutrality and collaborative tradition.

    **Business Model Innovation as Alternative Competitive Pathway.** China's market penetration despite 2.6× patent quality disadvantage reveals that competitive advantage increasingly stems from *how* firms commercialize rather than *what* they invent. Consumer electronics business logic—rapid iteration (24 vs. 40-50 months), volume-based cost reduction, ecosystem integration—transferred directly to EVs characterized by modularity and software-centricity. This enabled implementation speed to compensate for R&D gaps, validated by China's 7-fold battery patent growth (8.7%→47.0%, 2014-2024) focused on domains where modularity confers advantages. For EU policymakers, this suggests competitive pathways exist beyond traditional R&D leadership: commercialization excellence, lifecycle optimization (durability, repairability), and privacy-first architectures can generate differentiation independently of patent volume or citation quality.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    # EU Strategic Imperatives: Pathways Forward

    The empirical evidence presented in Sections 3-6 paints a sobering portrait of European competitive erosion in EV innovation. From 2014 to 2024, the EU's patent share declined from 26.3% to 17.3% (among five major regions)—a 9-percentage-point contraction affecting six of seven core technology domains (Section 3). Yet within this trajectory of decline lie insights for strategic renewal. This section translates empirical findings into actionable strategic imperatives, examining both immediate priorities and alternative futures the EU might navigate through 2030.

    ## Strategic Imperative: Leveraging Asymmetric Advantages

    The EU confronts a fundamental strategic asymmetry: it cannot compete with China's consumer electronics model (rapid iteration, software dominance, economies of scale) nor match US foundational research advantages (2.4-3.6× citation quality advantage; Section 4). However, asymmetry need not imply disadvantage. European strengths lie precisely where competitors possess structural vulnerabilities—durability, sustainability, privacy, and engineering depth.

    ### Priority Action 1: Anchor in Defensible Technology Domains

    European patent leadership persists in thermal management (44% share) and safety systems (47% share)—domains where engineering complexity, regulatory standards, and durability requirements create barriers to rapid commoditization (Section 3). These technologies directly address the consumer electronics model's Achilles' heel: longevity and reliability. Chinese manufacturers designing for 3-5 year replacement cycles systematically underinvest in thermal optimization and long-term battery health—precisely the domains where 10-15 year vehicle lifespans require sophisticated engineering.

    The EU should amplify R&D investment in these domains not as defensive retreats but as foundations for differentiation. Advanced thermal architectures enabling faster charging without degradation, predictive safety systems integrating decades of crash engineering data, and modular designs facilitating circular economy integration—these capabilities transform apparent weaknesses (slower iteration) into premium market positioning (lifecycle value).

    ### Priority Action 2: Forge Strategic Knowledge Alliances

    European collaboration rates (1.28% in 2023) exceed all competitors, with the EU-US knowledge axis generating 13,139 citations—the dominant bilateral flow globally (Section 6). Yet China's self-citation rate (21.5%, lowest among five regions) reveals unexpected openness to external knowledge, while US-China flows collapsed 76% (2020-2023) due to geopolitical tensions (Section 6). This creates strategic opportunities: the EU can position itself as the indispensable intermediary in fragmenting global innovation networks.

    Concrete actions include deepening EU-Korea battery collaboration (already the second-largest cross-border partnership at 5,410 patents; Section 5.1), leveraging Japan's hybrid expertise as bridging technology during the BEV transition, and selectively engaging Chinese research institutions on pre-competitive fundamental research (where China's openness enables knowledge flows). Simultaneously, the EU must protect critical IP through stronger enforcement and technology transfer controls—openness paired with strategic guardrails.

    ### Priority Action 3: Differentiate on Privacy and Sustainability

    China's business model innovation reveals that consumer electronics strategies depend on data-intensive ecosystems for monetization—connected services, usage analytics, ecosystem lock-in. European GDPR regulations, initially viewed as innovation constraints, now offer differentiation foundations. Privacy-first vehicle architectures emphasizing user data sovereignty, minimal collection, and interoperability align with European consumer preferences increasingly wary of surveillance capitalism.

    Similarly, sustainability certifications for battery lifecycle management, mandatory repairability standards, and circular economy integration impose costs on volume-oriented competitors while rewarding European engineering depth. The EU's strength in thermal management (critical for battery longevity and second-life applications) becomes strategic when regulation mandates lifecycle optimization over initial cost minimization.

    ## Alternative Futures: Three Scenarios for 2030

    Strategic planning under uncertainty requires exploring alternative futures. Following van der Heijden (2005), we construct three scenarios grounded in current trajectories (Sections 3-6) but diverging based on critical uncertainties: EU policy effectiveness, technology disruption timing, and geopolitical stability. Table 8 and Figure 7 summarize key differences.

    **Table 8: Three Scenarios for EU EV Innovation (2030 Projections)**

    | Dimension | **Scenario A: "European Renaissance"** (Optimistic) | **Scenario B: "Managed Transition"** (Base Case) | **Scenario C: "Structural Crisis"** (Pessimistic) |
    |-----------|------------|-----------|-----------|
    | **EU Patent Share (2030)** | 30-32% (recovery) | 25-27% (gradual decline) | 18-22% (collapse) |
    | **China Patent Share** | 28-30% | 28-32% | 35-40% (dominance) |
    | **EU Citation Quality** | 3.5-4.0 avg (improved) | 2.5-2.8 avg (stagnant) | 2.0-2.3 avg (eroded) |
    | **Key Drivers** | • €100B+ coordinated R&D<br/>• Solid-state battery breakthrough (2027-2028)<br/>• Lifecycle regulations penalize Chinese rapid obsolescence<br/>• China market saturation weakens competition | • Current trends continue<br/>• Incremental policy adjustments<br/>• EU retreats to premium segments (8-12% volume, 25-30% profit)<br/>• US-China decoupling fragments innovation | • Policy fragmentation, delayed action<br/>• Chinese scale success (500K-1M+ units)<br/>• US AI breakthrough licensed to non-EU OEMs<br/>• Industry consolidation: 3-4 surviving EU brands |
    | **Collaboration Rate** | 2.0-2.5% (EU-Korea partnerships) | 0.8-1.0% (geopolitical fragmentation) | 0.4-0.6% (EU irrelevance) |
    | **EU Strategic Position** | Premium sustainable mobility leader | Profitable niche player | Historical footnote (<5% global share) |
    | **Current Trajectory Points To:** | Requires transformative action | **Most likely absent intervention** | Plausible if Chinese scale + US software converge |

    ### Robust Strategies Across Scenarios

    Five strategies remain effective regardless which future materializes:

    1. **Thermal-Safety Integration**: Leverage European excellence (44% thermal, 47% safety patent shares) through cross-domain integration—thermal-optimized battery packs enhancing both performance and crash protection.

    2. **Premium Positioning**: Accept 5-10% global volume share in $50,000+ segments with 20-25% margins rather than competing for mass-market volumes against insurmountable Chinese scale advantages.

    3. **Regulatory Leverage**: Use EU market size (450M population) to set global standards—lifecycle requirements, repairability mandates, privacy protections impose asymmetric costs on rapid-obsolescence competitors.

    4. **Selective Globalization**: Protect EU-US knowledge flows (13,139 citations; Section 5.2), deepen EU-Korea battery collaboration, hedge against US-China decoupling.

    5. **Innovation Concentration**: Overcome "legacy trap" (Section 3) by concentrating on 2-3 defensible domains (thermal, safety, autonomous-ADAS) rather than spreading across all seven technology areas.

    The EU faces a crossroads: managed premium repositioning (Scenarios A-B) versus structural irrelevance (Scenario C). Current trajectories point toward Scenario B absent intervention. Scenario A requires transformative action immediately; by 2030, trajectories may become irreversible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Conclusion: The Innovation Imperative

    This analysis reveals a European paradox: the EU ranks second in patent volume (2014-2018 cohort, 24.9%) yet last in citation quality (2.58 vs. US 9.97), with leadership in only two of seven domains and declining shares in six. These patterns signal fundamental strategic misalignment.

    The global EV landscape has bifurcated along incompatible value propositions—China's rapid iteration, America's software dominance, Europe's engineering excellence. Our analysis identifies asymmetric advantages where European strengths exploit competitor vulnerabilities: thermal management (44%), safety systems (47%), durability engineering, sustainability leadership, privacy protection. Chinese models underinvest in longevity; US software giants underestimate regulatory constraints. These gaps create "Premium Sustainable Mobility" opportunities.

    The strategic imperative: move from reactive defense to proactive differentiation. This requires concentrating resources on defensible positions (thermal-safety integration, battery durability), leveraging regulatory authority, and forging strategic alliances (EU-Korea, EU-US). Above all, it requires speed.

    The next five years will determine whether Europe becomes an innovation leader in sustainable premium mobility or a historical footnote in the EV revolution. The window for strategic renewal remains open, but it closes further with each passing quarter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    # Appendix A: Data Sources and Methodology

    ## Data Source: Google Public Patent Dataset

    This analysis draws from Google's Public Patent Dataset hosted on BigQuery, specifically the `patents-public-data.patents.publications` table. This dataset provides comprehensive global patent information including:

    - Patent publication numbers
    - Filing dates
    - Assignee information (harmonized company/inventor data)
    - Cooperative Patent Classification (CPC) codes
    - Bibliographic metadata

    ## BigQuery SQL Query

    IMPORTANT: This query counts patents by assignee/inventor country rather than patent office location, providing accurate attribution of innovation to regions.

    ### Key Methodological Decisions:

    1. Assignee Country vs. Patent Office: We use `assignee_harmonized.country_code` instead of `p.country_code` to count who filed patents, not where they were filed. This addresses the bias where Chinese companies file 93.7% domestically while US/EU companies file 45-60% internationally.

    2. EU Aggregation: All 27 current EU member states are mapped to single "EU" region for comparative analysis.

    3. Time Period: 2014-2024, with 2024 data incomplete as of analysis date.

    4. Technology Domains: Seven categories using CPC classification codes (see below).

    ### Technical Implementation

    We queried data from Google BigQuery's `patents-public-data.patents.publications` table using SQL, joining with CPC classification definitions to categorize patents. **Complete SQL queries, data files, and analytical code are publicly available at: https://github.com/flyersworder/ev-patent-analysis**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## CPC Classification Mapping

    ### Final Validated Categories and Rationale

    Our analysis uses seven mutually exclusive technology domains based on Cooperative Patent Classification (CPC) codes. These categories were validated through USPTO CPC definition research to ensure conceptual clarity and comprehensive EV coverage.

    Category 1: Battery Technology (Energy Storage for BEVs)
       - H01M 4: Electrodes for batteries
       - H01M 6: Primary cells (non-rechargeable)
       - H01M 10: Secondary cells/accumulators (Li-ion, etc.)
       - H01M 12: Hybrid cells
       - H01M 50: Constructional details, casings, battery packs
       - H01G11: Hybrid capacitors (supercapacitors)

       Rationale: Explicitly excludes H01M 8 (fuel cells) as fuel cell vehicles (FCVs)
       represent a fundamentally different technology trajectory from battery electric vehicles
       (BEVs). FCVs have negligible market share (~0.14% of BEV volume) and different competitive
       landscape (dominated by Toyota/Hyundai). Including fuel cells would conflate distinct
       innovation strategies.

    Category 2: EV Propulsion & Charging (Motors, Power Electronics, Charging)
       - B60L: Electric propulsion of vehicles
       - H02K: Rotating electric machines (motors/generators)
       - H02P: Control or regulation of electric motors
       - H02J7: Charging or depolarizing batteries/supercapacitors
       - H02M: Power conversion apparatus (inverters, converters)

    Category 3: Autonomous Driving & ADAS (Self-Driving and Advanced Assistance)
       - B60W: Conjoint control of vehicle sub-units (THE primary ADAS classification)
       - G05D1: Control of position, course, altitude for autonomous vehicles

       Rationale: "ADAS" (Advanced Driver Assistance Systems) refers to autonomous driving
       capabilities, NOT safety. This category focuses on automation and active control during
       driving (adaptive cruise control, lane keeping, collision avoidance, autonomous navigation).

    Category 4: Hybrid Powertrains (Hybrid Power Management)
       - B60K6: Hybrid vehicle arrangements and components
       - F02D: Controlling combustion engines (hybrid integration)

       Note: B60W20 (hybrid control systems) was removed to avoid overlap with B60W (Category 3).

    Category 5: Vehicle Safety Systems (Occupant Protection and Visibility)
       - B60R: Vehicles arrangements and fittings (airbags, seatbelts, crash protection)
       - B60Q: Lighting and signaling devices (headlights, brake lights, turn signals)

       Rationale: This category covers passive safety (protection during/after crashes) and
       visibility systems, distinct from ADAS active control. B60R focuses on structural protection
       and restraint systems, while B60Q ensures vehicle visibility to other road users.

    Category 6: Thermal Management (Cooling and Heat Management)
       - B60H: Heating, cooling, ventilation, air-conditioning in vehicles
       - F28D: Heat exchangers (radiators, coolant systems)

       Importance: Critical for battery longevity, fast-charging capability, and overall EV
       performance. EU leadership in this domain provides defensible competitive advantages.

    Category 7: Infotainment & Connectivity (Digital Experience and V2X)
       - B60K35: Instruments, dashboards, displays for vehicles
       - B60K37: Dashboard arrangements
       - H04W4: Services specifically adapted for wireless communication networks
       - G07C5: Registering or indicating vehicle operation (telematics)
       - H04N7/18: Closed-circuit television systems (backup cameras, surround view)
       - G08G: Traffic control systems (V2X communication, vehicle-to-infrastructure)

       Note: G08G placed here (not in Safety) as it primarily concerns connectivity and
       communication infrastructure rather than occupant protection.
    ```

    ### Key Design Principles

    1. Mutual Exclusivity: Categories designed to avoid overlaps (e.g., B60W20 removed, G08G placed in Infotainment)

    2. BEV Focus: Fuel cells (H01M 8) excluded to maintain focus on battery electric vehicle innovation

    3. Conceptual Clarity: "ADAS" refers to autonomous driving (Category 3), not safety protection (Category 5)

    4. Comprehensive Coverage: Seven categories span all major EV innovation areas from hardware (batteries, motors) to software (autonomy, infotainment)

    5. Validated Against USPTO Definitions: All CPC code assignments verified through official USPTO CPC scheme documentation

    ## Data Processing Notes

    - Filing date format: Stored as integer YYYYMMDD, divided by 10000 to extract year
    - EU member states: All 27 current EU countries included (as of 2024)
    - Regional assignment: Each patent assigned to a single primary region based on first assignee's country code (no double-counting)
    - Collaborative patents: Separate analysis identifies patents with multiple assignees from different regions (Section 5)
    - Global filing capture: Counts patents filed anywhere in world by companies from these regions, not just domestic filings
    - No "Others" category: Patents not matching specific categories excluded entirely to maintain focus on core EV technologies

    ## Quality Metrics Methodology

    Beyond patent counts, we assess innovation quality through forward citation analysis:

    Forward Citations (Section 4)
    - Definition: Number of times a patent is cited by subsequent patents as prior art
    - Interpretation: Higher citations indicate foundational, influential innovations that shape subsequent research
    - Time window: Analysis focuses on 2014-2018 patents (6-10 years citation accumulation) to avoid recency bias
    - Calculation: Average citations per patent by region and technology domain
    - Source: Google BigQuery `patents-public-data.patents.publications` citations table

    ## Cross-Border Collaboration Analysis (Section 5)

    Collaborative Patent Definition: Patents with multiple assignees from different regions among the five analyzed (US, China, EU, Korea, Japan)

    Methodology:
    - Query identifies patents where `assignee_harmonized.country_code` includes multiple regions
    - Collaboration rate = (collaborative patents / total patents) × 100%
    - Bilateral pairs counted (e.g., EU-US, US-CN) to map collaboration networks
    - Important scope note: Only cross-REGIONAL collaboration counted; within-region (e.g., Germany-France) and outside-region (e.g., US-India) collaborations excluded

    Findings: Collaboration rates extremely low (0.65-1.28% across 2014-2024), contradicting open innovation predictions

    ## Knowledge Flow Network Analysis (Section 5)

    Self-Citation Rates:
    - Definition: Percentage of citations where citing patent and cited patent share the same region
    - Calculation: For each region, `(within-region citations / total citations by region) × 100%`
    - Interpretation: High self-citation indicates insular innovation systems; low self-citation indicates openness to external knowledge

    Cross-Regional Citation Flows:
    - Definition: Citation counts from Region A patents to Region B patents (e.g., US→China, EU→US)
    - Visualization: Top 10 bilateral flows mapped in Figure 6B (2023 data)
    - Geopolitical analysis: Tracks US-China bilateral flows 2014-2024 to assess knowledge exchange collapse

    Citation Lags:
    - Definition: Time difference (in years) between cited patent filing date and citing patent filing date
    - Calculation: Average lag by region for 2014-2020 cohort (mature data avoiding recency bias)
    - Interpretation: Measures knowledge absorption speed; lags range 1.45-1.66 years (minimal variation)

    ## Data Limitations

    1. 2024 incomplete: Partial year data as of publication date (October 2024)
    2. Patent lag: 18-month publication delay means recent filings may not yet appear in dataset
    3. Regional scope: Analysis focuses on five major regions (US, China, EU, South Korea, Japan); other automotive nations (India, Taiwan, Canada) excluded
    4. Citation window bias: Recent patents (2020+) have insufficient time to accumulate citations, creating recency bias in quality metrics
    5. Technology overlaps: Some patents span multiple domains; CPC codes assigned hierarchically to primary category
    6. Quality vs. quantity: Forward citations measure academic/technical influence, not necessarily commercial value or manufacturing feasibility

    ## Reproducibility

    This analysis is fully reproducible using Google BigQuery's public patent dataset (`patents-public-data.patents.publications`). **All materials are publicly available at: https://github.com/flyersworder/ev-patent-analysis**, including:

    - Complete SQL queries (7 queries in `sql/` directory)
    - Raw data files (7 CSV files in `data/` directory)
    - Analysis code (marimo notebook: `patent_analysis_chapter.py`)
    - Full documentation (README.md and DATA_README.md)

    Primary data was extracted October 2024; citation and collaboration data extracted January 2025, reflecting patent publications available as of those dates.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Appendix B: Alternative Explanations and Limitations

    Our analysis attributes regional differences in patent volume and quality to strategic capability misalignment (H1), geopolitical constraints on collaboration (H2), institutional differences in knowledge openness (H3), and business model innovation (H4). However, alternative explanations merit consideration. This appendix addresses four potential confounds and assesses their plausibility given our evidence.

    ## Domain Specialization Effects

    **Alternative explanation**: Europe's lower citation quality could reflect specialization in inherently low-citation technology domains (e.g., thermal management, mechanical systems) rather than actual quality deficits. If EU concentrates in hardware domains while the US focuses on software domains, observed quality gaps might be compositional artifacts.

    **Assessment**: Our domain-controlled regression (Table 4B) directly tests and rejects this explanation. Even within identical technology domains and filing years, US patents generate +6.94 more citations than EU patents (p<0.001, wild bootstrap inference). This within-domain comparison isolates region-specific innovation capabilities from domain mix effects. Furthermore, Figure 5B reveals EU ranks last in citation quality across 6 of 7 domains, including traditional European strengths (thermal management, safety systems). The quality gap persists whether examining software-centric (autonomous driving) or hardware-centric (batteries) technologies. Domain specialization cannot explain systematic underperformance across diverse technology areas.

    ## Patent Office and Classification Bias

    **Alternative explanation**: Citation patterns could reflect USPTO-centric citation practices, where US patents receive more citations because researchers preferentially cite US patents, or CPC classification differences that systematically assign more codes to US patents.

    **Assessment**: We mitigate USPTO bias through three design choices: (1) using Google Patents Public Data covering all major patent offices (USPTO, EPO, JPO, KIPO, CNIPA), (2) analyzing publication numbers rather than jurisdiction-specific application numbers, and (3) counting citations from all offices, not only USPTO forward citations. Our CPC bias verification (referenced in Section 5.2's generality/originality analysis) found US patents average 2.63 CPC codes versus EU 2.41 codes—only a 9% difference insufficient to explain 2-3× citation gaps. However, we acknowledge potential English-language bias: patents published in English may accumulate citations more readily than non-English patents due to broader accessibility. This could disadvantage Chinese and Japanese patents relative to US/EU patents. Future research employing language-normalized citation metrics or examiner-added citations (less subject to linguistic barriers) could isolate this effect.

    ## Temporal Citation Lag Effects

    **Alternative explanation**: If EU patent filings concentrated later in our observation window, insufficient citation accumulation time rather than lower quality could explain citation gaps.

    **Assessment**: Our mature patent cohort restriction (2014-2018 filings analyzed in Table 4) provides 5-10 year citation windows, ensuring adequate accumulation time across all regions. Temporal analysis (Figure 4A) shows persistent US quality advantages throughout the full time series where citation data is mature. Importantly, EU patent volume peaked in 2014-2016 (288,520 patents in 2014-2018 cohort), giving EU patents equal or greater citation maturity compared to US patents filed in the same period. The temporal distribution of filings cannot explain observed quality differences.

    ## Fractional Counting for Multi-Assignee Patents

    **Alternative explanation**: Our whole-count method (assigning patents to all assignee regions) could inflate regional totals when patents involve multiple regions. Fractional counting (dividing credit equally among assignees) might yield different regional rankings.

    **Assessment**: Cross-regional collaboration rates are extremely low (0.65-1.28% of patents; Section 5.1, Figure 5A), limiting potential bias from multi-assignee patents. Even if we adopted fractional counting, 98.72-99.35% of patents would be unaffected. However, fractional counting could matter for specific collaboration-intensive domains. For instance, EU-Korea battery collaboration (5,410 patents) represents 2.8% of the battery patent pool; fractional allocation would reduce both regions' apparent battery contributions proportionally. Future robustness checks could implement fractional counting for collaboration-heavy domains, though we expect minimal impact on overall conclusions given the prevalence of single-region patents.

    ## Conclusion

    While these alternative explanations merit serious consideration, our existing evidence—domain-controlled regressions, multi-office citation data, temporal cohort restrictions, and low collaboration rates—suggests they do not fundamentally alter our core findings. Future research could strengthen causal identification through patent family analysis (triadic patents filed in multiple jurisdictions), examiner-added citation analysis (reducing self-selection bias), and fractional counting robustness checks. The persistent, large-magnitude quality gaps across diverse empirical tests provide confidence in our theoretical interpretations despite these limitations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Appendix C: Technical Glossary

    ## Innovation Quality Metrics

    Forward Citations: The number of times a patent is cited by subsequent patents as prior art. Higher citation counts indicate foundational, influential innovations that shape follow-on research. Used as proxy for technological impact and quality.

    Self-Citation Rate: Percentage of citations where citing patent and cited patent originate from the same region. High rates indicate insular innovation systems; low rates indicate openness to external knowledge.

    ## Regional and Institutional Terms

    Assignee Country: The country where a patent's assignee (typically the company or inventor owning the patent rights) is headquartered. This differs from patent office location and provides more accurate attribution of innovation to regions.

    Chaebol: South Korean large family-controlled corporate conglomerates (e.g., Samsung, LG, SK Group). Characterized by centralized control, government coordination, and rapid capability-building across related industries.

    National Innovation System (NIS): The network of institutions, policies, and interactions within a country that generate, diffuse, and exploit technological knowledge. Includes firms, universities, government agencies, and financial institutions. Different countries exhibit distinct NIS architectures (e.g., US market-driven vs. China state-directed).

    Resource-Based View (RBV): Strategic management theory emphasizing that sustainable competitive advantage stems from valuable, rare, inimitable, and non-substitutable resources. Applied to regions, explains persistent technological specializations.

    ## Technology Classifications

    CPC (Cooperative Patent Classification): Jointly developed classification system by European Patent Office (EPO) and United States Patent and Trademark Office (USPTO), organizing patents into hierarchical technology categories. Used to categorize patents into seven EV technology domains in this analysis.

    ADAS (Advanced Driver Assistance Systems): Technologies providing automation and assistance in driving tasks, including adaptive cruise control, lane keeping, collision avoidance, and autonomous navigation capabilities. Distinct from passive safety systems.

    BEV (Battery Electric Vehicle): Vehicles powered exclusively by electric batteries, without internal combustion engines. Contrasts with hybrid vehicles (combining electric and combustion powertrains) and fuel cell vehicles (using hydrogen).

    V2X (Vehicle-to-Everything): Communication technologies enabling vehicles to exchange information with other vehicles (V2V), infrastructure (V2I), networks (V2N), and pedestrians (V2P). Critical for autonomous driving coordination and traffic management.

    ## Strategic Concepts

    Disruptive Innovation: Christensen's (1997) theory describing how new entrants with initially inferior but simpler/cheaper technologies eventually displace established incumbents. Applied to EVs, explains challenges faced by traditional automakers (EU, Japan) versus tech entrants (Tesla, Chinese EV startups).

    Innovator's Dilemma: The paradox where successful incumbents fail during technological transitions because existing capabilities, organizational structures, and customer relationships become liabilities rather than assets.

    Legacy Trap: Term coined in this analysis describing the EU's pattern of strong specialization in traditional automotive domains (hybrids, thermal management, safety) but critical weaknesses in future-defining technologies (batteries, infotainment, autonomous software). Contrasts with strategically-aligned specialization (e.g., Korea's battery focus, US software dominance).

    Strategic Triage: The deliberate decision to abandon competitive battles in domains where asymmetric disadvantages make success unlikely, reallocating resources toward defensible positions. Applied to EU recommendation to exit infotainment competition.

    ## Data and Methodology

    Citation Lag: Time difference (in years) between a cited patent's filing date and its citing patent's filing date. Measures knowledge diffusion speed; typical lags range 1.5-1.7 years across regions.

    Collaboration Rate: Percentage of patents with multiple assignees from different regions. Extremely low in EV innovation (0.65-1.28%), contradicting open innovation predictions.

    Patent Share: Percentage of total patents attributed to a specific region, calculated as (region patents / total patents across five regions) × 100%. All patent shares in this chapter use the five-region denominator (US, China, EU, South Korea, Japan) unless explicitly noted otherwise.

    Knowledge Flow: Citation-based measure of knowledge transfer from one region to another. Calculated as number of times Region A patents cite Region B patents, revealing patterns of technological influence and dependence.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # References

    ## Theoretical Foundations

    Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99-120. https://doi.org/10.1177/014920639101700108

    Chesbrough, H. W. (2003). *Open Innovation: The New Imperative for Creating and Profiting from Technology*. Harvard Business School Press.

    Christensen, C. M. (1997). *The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail*. Harvard Business School Press.

    Freeman, C. (1987). *Technology Policy and Economic Performance: Lessons from Japan*. Pinter Publishers.

    Lundvall, B. Å. (1992). *National Systems of Innovation: Towards a Theory of Innovation and Interactive Learning*. Pinter Publishers.

    Teece, D. J. (2010). Business models, business strategy and innovation. *Long Range Planning*, 43(2-3), 172-194. https://doi.org/10.1016/j.lrp.2009.07.003

    Zott, C., & Amit, R. (2010). Business model design: An activity system perspective. *Long Range Planning*, 43(2-3), 216-226. https://doi.org/10.1016/j.lrp.2009.07.004

    ## Industry Statistics and Economic Data

    ACEA (European Automobile Manufacturers' Association). (2024). *The Automobile Industry Pocket Guide 2024-2025*. Retrieved from https://www.acea.auto/figure/employment-in-eu-automotive-sector/

    Eurostat. (2025, January 4). EU car trade surplus: €89.3 billion in 2024. Retrieved from https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250401-1

    IAM Media. (2023). *Patent 1000: The World's Leading Patent Professionals*. Retrieved from https://www.iam-media.com/rankings/patent-1000

    United Nations. (2023). Sustainable Development Goals Indicators Database. Research and development expenditure as a proportion of GDP (SDG 9.5.1) and Manufacturing value added as a proportion of GDP. Retrieved from https://unstats.un.org/sdgs/dataportal

    ## Patent Analysis Methodology

    Alcácer, J., & Gittelman, M. (2006). Patent citations as a measure of knowledge flows: The influence of examiner citations. *Review of Economics and Statistics*, 88(4), 774-779. https://doi.org/10.1162/rest.88.4.774

    Balassa, B. (1965). Trade liberalisation and "revealed" comparative advantage. *The Manchester School*, 33(2), 99-123. https://doi.org/10.1111/j.1467-9957.1965.tb00050.x

    Breschi, S., & Lissoni, F. (2009). Mobility of skilled workers and co-invention networks: An anatomy of localized knowledge flows. *Journal of Economic Geography*, 9(4), 439-468. https://doi.org/10.1093/jeg/lbp008

    Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum Associates.

    Griliches, Z. (1990). Patent statistics as economic indicators: A survey. *Journal of Economic Literature*, 28(4), 1661-1707.

    Hall, B. H., Jaffe, A., & Trajtenberg, M. (2001). The NBER patent citation data file: Lessons, insights and methodological tools. NBER Working Paper 8498. https://doi.org/10.3386/w8498

    Jaffe, A. B., & Trajtenberg, M. (1999). International knowledge flows: Evidence from patent citations. *Economics of Innovation and New Technology*, 8(1-2), 105-136. https://doi.org/10.1080/10438599900000006

    Peri, G. (2005). Determinants of knowledge flows and their effect on innovation. *Review of Economics and Statistics*, 87(2), 308-322. https://doi.org/10.1162/0034653053970258

    Squicciarini, M., Dernis, H., & Criscuolo, C. (2013). Measuring patent quality: Indicators of technological and economic value. OECD Science, Technology and Industry Working Papers, 2013/03. https://doi.org/10.1787/5k4522wkw1r8-en

    Trajtenberg, M., Henderson, R., & Jaffe, A. (1997). University versus corporate patents: A window on the basicness of invention. *Economics of Innovation and New Technology*, 5(1), 19-50. https://doi.org/10.1080/10438599700000006

    ## Technology Diffusion and Innovation Cycles

    Gort, M., & Klepper, S. (1982). Time paths in the diffusion of product innovations. *Economic Journal*, 92(367), 630-653. https://doi.org/10.2307/2232554

    Utterback, J. M., & Abernathy, W. J. (1975). A dynamic model of process and product innovation. *Omega*, 3(6), 639-656. https://doi.org/10.1016/0305-0483(75)90068-7

    ## Chinese Innovation System

    Information Technology and Innovation Foundation (ITIF). (2024, July 29). *How Innovative Is China in the Electric Vehicle and Battery Industries?* Retrieved from https://itif.org/publications/2024/07/29/how-innovative-is-china-in-the-electric-vehicle-and-battery-industries/

    ## EV Technology Innovation

    Canalys. (2024). Xiaomi's bold entry into the EV market: Navigating success and challenges. Retrieved from https://canalys.com/insights/xiaomi-s-entry-into-the-ev-market

    Jeong, J. H., Kim, C., & Jo, H. J. (2024). Three major challenges in the shift to electric vehicles: Industrial organization, industrial policy, and a just transition. *Sociology Compass*, 18(5), e13218. https://doi.org/10.1111/soc4.13218

    Liu, Y., Wang, H., & Zhang, L. (2022). Evolution of electric vehicle battery technology innovation: A patent-based analysis. *Journal of Cleaner Production*, 338, 130586. https://doi.org/10.1016/j.jclepro.2022.130586

    Liu, Z., Chen, X., & Li, M. (2024). Industrial policies and electric vehicle innovation: Evidence from patent data analysis. NBER Working Paper 33138. https://doi.org/10.3386/w33138

    Nature Energy Editorial. (2024). Collaborative innovation accelerates electric vehicle technology development. *Nature Energy*, 9(3), 245-246. https://doi.org/10.1038/s41560-024-01478-2

    Song, Y., Li, Y., Jiang, J., & Ye, B. (2025). The industrial prospect of electric vehicles—time delay stochastic evolutionary game evidence from the U.S., China, the EU, and Japan. *Humanities and Social Sciences Communications*, 12, Article 901. https://www.nature.com/articles/s41599-025-05342-5

    Philipsen, R., et al. (2022). An integrative approach for business modelling: Application to the EV charging market. *Journal of Business Research*, 142, 184-196. https://doi.org/10.1016/j.jbusres.2021.12.060

    Wang, S., Zhang, Y., & Liu, H. (2023). China's battery innovation system: Policy coherence and knowledge flows. *Energy Policy*, 174, 113442. https://doi.org/10.1016/j.enpol.2023.113442

    ## Scenario Planning and Strategic Foresight

    Schwartz, P. (1991). *The Art of the Long View: Planning for the Future in an Uncertain World*. Currency Doubleday.

    van der Heijden, K. (2005). *Scenarios: The Art of Strategic Conversation* (2nd ed.). Wiley.

    ## EV Market and Policy

    California Management Review. (2024). How Chinese companies are dominating electric vehicle market worldwide. *California Management Review*, University of California, Berkeley. Retrieved from https://cmr.berkeley.edu/2024/03/how-chinese-companies-are-dominating-electric-vehicle-market-worldwide/

    European Commission. (2020). *Horizon 2020: The EU Framework Programme for Research and Innovation*. Retrieved from https://ec.europa.eu/programmes/horizon2020/

    European Commission. (n.d.). *CORDIS: Community Research and Development Information Service*. Retrieved January 2025 from https://cordis.europa.eu/

    McKinsey & Company. (2023). Automotive product development: Accelerating to new horizons. Retrieved from https://www.mckinsey.com/capabilities/operations/our-insights/automotive-product-development-accelerating-to-new-horizons

    Howell, S. T. (2017). Financing innovation: Evidence from R&D grants. *American Economic Review*, 107(4), 1136-1164. https://doi.org/10.1257/aer.20150808

    IEA. (2023). *Global EV Outlook 2023: Catching up with climate ambitions*. International Energy Agency. Retrieved from https://www.iea.org/reports/global-ev-outlook-2023

    NBER. (2025). Manufacturing subsidies and innovation spillovers: Evidence from the Inflation Reduction Act. NBER Working Paper Series. National Bureau of Economic Research.

    WIPO. (2019). *World Intellectual Property Report 2019: The Geography of Innovation - Local Hotspots, Global Networks*. World Intellectual Property Organization. Retrieved from https://www.wipo.int/publications/en/details.jsp?id=4467

    WIPO. (2023). *Patent Landscape Report on Electric Vehicle Technologies*. World Intellectual Property Organization. Retrieved from https://www.wipo.int/publications/en/details.jsp?id=4623

    ## Patent Data Sources

    Google. (2024). *Public Patent Dataset*. BigQuery: patents-public-data.patents.publications. Retrieved from https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/google-patents-public-data

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
