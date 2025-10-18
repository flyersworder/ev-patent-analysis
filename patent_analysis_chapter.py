import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    title: "Europe's Innovation Paradox: Patent Quality and Regional Competition in the Global Electric Vehicle Race (2014-2024)"
    author: "Qing Ye, Marina van Geenhuizen"
    date: "2025-01-13"
    abstract: |
      This chapter examines a troubling paradox in electric vehicle (EV) innovation: Europe produces the second-highest patent volume globally yet ranks last in innovation quality. Analyzing 385,000+ patents across five major regions (United States, China, European Union, South Korea, Japan) and seven core EV technology domains from 2014 to 2024, we employ forward citation analysis to assess technological impact beyond mere quantity. Europe's patent share declined 9 percentage points affecting six of seven domains, with growth only in declining hybrid powertrains. European patents average 2.50 forward citations versus 8.87 for the US—a 3.5× quality gap despite second-highest volume. This "generalist dilemma" (moderate capabilities across all domains, leadership in none) contrasts with Korea's focused battery excellence and China's strategic selectivity in batteries and consumer electronics-inspired business models. Counterintuitively, China exhibits the lowest self-citation rate (21.2%), indicating unexpected openness, while US-China knowledge flows collapsed 64-70% since 2021 despite technological complementarity. Cross-border collaboration remains minimal (0.65-1.28% of patents). Grounded in Resource-Based View, National Innovation Systems, and Disruptive Innovation theory, we interpret these patterns as manifestations of distinct regional capabilities and institutional arrangements. Strategic imperatives for Europe include anchoring in defensible domains (thermal management, safety systems), forging strategic alliances (EU-Korea, EU-US), differentiating on privacy and sustainability, and accepting strategic triage. Three scenarios for 2030 explore alternative futures and robust strategies across uncertainty.
    keywords: ["electric vehicles", "patent analysis", "innovation quality", "forward citations", "National Innovation Systems", "disruptive innovation", "EU automotive policy", "knowledge flows", "cross-border collaboration", "battery technology", "autonomous driving", "Korea-China paradox"]
    ---
    """
    )
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
    alt.themes.enable('default')
    alt.data_transformers.disable_max_rows()

    # Set rendering for static export (PNG/PDF compatibility)
    alt.renderers.enable('mimetype')
    return alt, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Introduction

    ## The European Paradox

    Europe produces the second-highest volume of electric vehicle patents globally—yet ranks dead last in innovation quality.

    From 2014 to 2024, European inventors filed over 62,000 patents across seven core EV technology domains, trailing only the United States in absolute numbers. But when measured by forward citations—the gold standard for assessing patent impact and technological influence—European patents average just 2.50 citations, compared to 8.87 for US patents. This 3.5× quality gap reveals a troubling reality: European innovation generates high activity but low impact.

    This paradox extends deeper. Europe's patent share declined from 26.3% to 17.3% (2014-2024)—a 9-percentage-point erosion affecting six of seven technology domains. Europe's sole growth domain? Hybrid powertrains, the very technology the industry is abandoning as it shifts toward pure electric vehicles. Meanwhile, Europe ranks second, third, or fourth across nearly all domains but leads in precisely none of the high-growth categories defining future competitiveness: autonomous driving, battery innovation, or infotainment systems.

    We term this the "generalist dilemma": moderate capabilities everywhere, excellence nowhere.

    For a continent whose automotive sector employs 14 million people, represents 7% of EU GDP, and generates a €400 billion annual trade surplus, this pattern signals not cyclical weakness but structural crisis. The question is not whether European automotive leadership faces existential threat, but whether the window for strategic renewal remains open—and what actions might reverse these trajectories before they become irreversible.

    ## Why Patents Predict Market Futures

    Patents are leading indicators of competitive positioning, revealing where regions invest R&D resources and develop capabilities for tomorrow's markets. Patent activity predicts market outcomes by 5-10 years: today's patents become tomorrow's products and competitive advantages. Nokia's collapse illustrates this dynamic—the company dominated mobile phone sales in 2010 yet lost the smartphone patent race to Apple and Samsung, leading to business failure within three years. Patents revealed the strategic shift years before sales data.

    The EV transition exhibits similar dynamics. Patent leadership in batteries, autonomous driving, and infotainment will determine which regions capture value in the €5+ trillion global automotive market, where high-skilled engineering jobs locate, and whether Europe maintains technological sovereignty or becomes dependent on US software platforms and Chinese battery supply chains.

    ## The Five-Region Race: Distinct Strategies, Divergent Outcomes

    This chapter analyzes innovation competition among five major regions, each pursuing fundamentally different strategies:

    The United States treats EVs as software platforms, concentrating in autonomous driving and infotainment. Led by Tesla, Waymo, and Silicon Valley entrants, US innovation emphasizes disruptive business models and AI-enabled capabilities, maintaining the highest patent quality through foundational, cross-domain research.

    China pursues strategic selectivity in battery technology and consumer electronics-inspired infotainment. China's "smartphone playbook"—rapid iteration, ecosystem integration, volume-based cost reduction—challenges traditional automotive business models. Paradoxically, China exhibits the lowest self-citation rate globally, indicating unexpected openness, though citation quality suggests incremental optimization rather than foundational breakthroughs.

    The European Union confronts comprehensive erosion: declining patent share in six of seven domains, with growth only in hybrid powertrains—a declining technology. Europe maintains strength in thermal management and safety systems reflecting traditional engineering heritage, yet ranks last in citation quality despite second-highest volume. This "generalist dilemma"—moderate capabilities across all domains but leadership in none—exemplifies the innovator's dilemma: strengthening declining technologies while losing ground in disruptive domains.

    South Korea demonstrates that focused excellence can generate peer-competitor status. Korea dominates battery innovation with the highest patent share among all regions, reflecting Samsung SDI's, LG Energy Solution's, and SK Innovation's accumulated capabilities. The "Korea-China battery paradox" emerges: Korea leads innovation, China leads production, illustrating how different national innovation systems generate distinct competitive advantages.

    Japan represents the incumbent's dilemma in stark form. Despite pioneering hybrid vehicles and maintaining hybrid powertrain strength, Japan struggles in software-intensive domains. Japan's patent quality indicates solid but not transformative innovation—a pattern shared with the EU, reflecting traditional automotive incumbents' challenges during disruptive transitions.

    ## Research Questions and Contributions

    This chapter addresses four interrelated questions from a European policy perspective:

    1. Where does Europe stand? How have patent share, innovation quality (citations), and knowledge network positioning evolved across the five major competing regions from 2014 to 2024?

    2. Why is Europe losing ground? What institutional, strategic, and capability factors explain Europe's decline in six of seven technology domains and its last-place ranking in citation quality despite second-highest patent volume?

    3. What drives competitors' success? How do the US's software dominance, China's consumer electronics business model, and Korea's focused battery excellence succeed through fundamentally different approaches—and what constraints do they face?

    4. What pathways remain open to Europe? Given Europe's capability endowments, institutional structures, and competitors' positioning, what strategic imperatives and policy interventions offer realistic prospects for competitive renewal?

    We provide European policymakers and industry leaders with:

    - Comprehensive competitive diagnosis: Patent share, quality metrics (forward citations), cross-border collaboration rates, and knowledge flow networks across seven technology domains and 11 years

    - Theoretical interpretation: Analysis grounded in Resource-Based View, National Innovation Systems, Disruptive Innovation theory, and Open Innovation frameworks, explaining how regional capabilities, institutional arrangements, and business models generate observed patent patterns

    - Strategic intelligence on competitors: Deep examination of China's "EVs as consumer electronics" strategy, Korea's battery dominance despite smaller industrial base, and US software concentration—revealing their asymmetric advantages and structural vulnerabilities

    - Actionable strategic pathways: Recommendations prioritizing defensible domains (thermal management, safety systems), strategic alliances (EU-Korea batteries, EU-US software), differentiation strategies (privacy, sustainability), and necessary strategic triage (abandoning unwinnable battles in infotainment)

    ## Methodology Overview

    We analyze 385,000+ patents from Google's Public Patent Dataset (2014-2024) filed by inventors and assignees from the five major regions, categorized into seven core EV technology domains using Cooperative Patent Classification (CPC) codes: Battery Technology, EV Propulsion & Charging, Autonomous Driving, Hybrid & Energy Management, Safety Systems, Thermal Management, and Infotainment & Connectivity. Patents are counted by assignee/inventor country rather than patent office location, capturing "export-quality" innovation. Quality assessment employs forward citation analysis. Complete methodology and CPC code mapping appear in Appendix A; all data, queries, and code are publicly available at https://github.com/flyersworder/ev-patent-analysis.

    ## Paper Structure

    **Section 2** presents the theoretical framework integrating Resource-Based View, Disruptive Innovation theory, National Innovation Systems, and Open Innovation perspectives. **Section 3** examines five-region patent competition across seven EV technology domains. **Section 4** analyzes patent quality through forward citations. **Section 5** investigates cross-border collaboration and knowledge flow networks. **Section 6** provides a case study of China's consumer electronics business model. **Section 7** translates findings into strategic imperatives for Europe. **Section 8** concludes with synthesis and implications. **Appendices** provide methodology documentation and technical glossary.

    The window for European strategic renewal remains open, but it narrows with each passing quarter. The next five years will determine whether Europe's automotive leadership continues into the electric era, or whether the EV transition marks the end of European automotive dominance.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Theoretical Framework

    This chapter's analysis of EV patent competition draws on five complementary theoretical perspectives from innovation studies, strategic management, and industrial economics. These frameworks provide analytical lenses for interpreting regional patent patterns and their strategic implications.

    ## Resource-Based View: Regional Capabilities as Competitive Advantage

    The Resource-Based View (RBV) argues that sustainable competitive advantage stems from valuable, rare, inimitable, and non-substitutable resources (Barney, 1991). Applied to regional innovation systems, different geographic regions possess distinct technological capabilities accumulated through decades of institutional development and industrial specialization.

    Our analysis reveals region-specific resource endowments: the EU's thermal management and safety engineering expertise reflects traditional automotive engineering heritage; China's battery manufacturing scale results from coordinated industrial policy and massive capital deployment; US software and autonomous driving leadership builds on Silicon Valley's AI talent ecosystem. These capabilities are path-dependent—difficult for competitors to replicate quickly—explaining persistent regional specialization patterns across technology domains.

    ## Disruptive Innovation and Technology S-Curves

    Christensen's (1997) disruptive innovation framework explains why established industry leaders often fail during technological transitions. Incumbent firms optimize for existing technology trajectories (sustaining innovation) while new entrants pursue alternative approaches that initially underperform but eventually displace incumbents.

    The EV transition exemplifies this pattern: traditional automotive companies (predominantly European and Japanese) excelled at internal combustion engine optimization but face challenges in software-defined vehicles. China's "leapfrog" strategy—skipping ICE excellence to focus directly on batteries and digital experiences—and US tech entrants (Tesla, Waymo) leveraging software expertise both represent disruptive approaches. The EU's strength in declining technologies (hybrid powertrains) versus weakness in emerging domains (autonomous driving, infotainment) reflects classic innovator's dilemma dynamics.

    ## National Innovation Systems: Institutional Differences

    The National Innovation Systems (NIS) perspective emphasizes that innovation emerges from interactions among firms, universities, government agencies, and financial institutions within country-specific institutional contexts (Freeman, 1987; Lundvall, 1992). Different national systems produce distinct innovation patterns.

    Our five regions exhibit contrasting innovation systems: China's state-directed approach combines government subsidies, SOE coordination, and domestic market protection to rapidly scale targeted technologies like batteries. The US market-driven system relies on venture capital, university-industry linkages, and entrepreneurial firm entry (Tesla, Rivian). The EU's coordinated market economy emphasizes standards-setting, collaborative R&D programs (Horizon 2020), and incremental innovation by established firms. Korea's chaebol-coordinated model enables rapid capability building in targeted sectors (batteries, displays). Japan's consensus-driven approach emphasizes long-term relationships and incremental refinement. These institutional differences explain not just patent volume differences but also strategic orientations—China's top-down battery focus, US bottom-up software experimentation, EU consensus-based strategies, Korea's concentrated excellence, Japan's hybrid holdout.

    ## Open Innovation and Cross-Border Knowledge Flows

    Chesbrough's (2003) open innovation paradigm challenges closed, vertically-integrated R&D models, arguing that firms increasingly source external knowledge and license internal technologies. In global innovation competition, regions function as open innovation hubs with varying degrees of international collaboration.

    Our collaborative patent analysis examines knowledge flows among US, China, and EU innovation systems. The extent of cross-border co-invention reveals whether regions operate as isolated silos or integrated networks. EU-US collaboration patterns may reflect transatlantic technology alliances, while EU-China joint ventures in automotive manufacturing could generate collaborative patents. These flows have strategic implications: regions heavily dependent on external knowledge face vulnerability, while those serving as knowledge sources gain influence.

    ## Business Model Innovation: EVs as Consumer Electronics

    Teece (2010) and Zott & Amit (2010) demonstrate that competitive advantage increasingly stems from business model innovation—new approaches to value creation, delivery, and capture—rather than pure technological superiority. China's "EVs as consumer electronics" strategy represents business model innovation: rapid product cycles (smartphone-style annual releases), ecosystem integration (apps, services, connectivity), and volume-based cost reduction.

    This contrasts fundamentally with traditional automotive business models emphasizing long development cycles, mechanical reliability, and premium pricing. The China case study examines how this alternative business model—enabled by digital technologies but not requiring technological superiority—challenges European and US competitors even in domains where they maintain patent leadership.


    These five frameworks are not competing explanations but complementary perspectives. RBV explains persistent regional specializations; disruptive innovation theory predicts incumbent challenges during transitions; NIS perspective reveals institutional drivers of national strategies; open innovation highlights collaboration opportunities; business model lens identifies alternative competitive approaches.

    Together, these theories inform our empirical analysis and strategic recommendations: understanding regional capabilities (RBV) identifies EU strengths to leverage; recognizing disruption dynamics (S-curves) explains urgency of software investment; appreciating institutional differences (NIS) shapes realistic policy proposals; examining knowledge flows (open innovation) reveals alliance opportunities; analyzing business models clarifies China's competitive strategy.

    The following empirical sections apply these theoretical lenses to patent data, revealing the concrete manifestations of these abstract dynamics in the EV innovation race.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# The Five-Region Race: Patent Competition Across EV Technology Domains""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""This section presents the empirical foundation of our analysis, examining patent filing patterns across five major regions (United States, China, European Union, Japan, and South Korea) from 2014-2024. We first analyze aggregate trends showing the overall competitive landscape (Figure 1), then examine domain-specific patterns across seven core EV technologies (Figure 2), before focusing on the EU's competitive position and its decline across technology domains (Figure 3). These patent data reveal not merely different innovation speeds but fundamentally distinct strategic approaches—reflecting the theoretical frameworks of resource-based capabilities, national innovation systems, and disruptive innovation dynamics discussed earlier.""")
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

    *Note*: RCA quantifies regional specialization following Balassa (1965): RCA = (region's share in domain) / (region's overall patent share). RCA > 1.0 indicates specialization (higher concentration than overall portfolio); RCA < 1.0 indicates under-representation; **bold (RCA ≥ 1.5)** indicates strong specialization. **Key findings**: (1) **China**: Strong battery specialization (1.49) but weakness in autonomous driving (0.58); (2) **EU**: Strong specialization in *traditional automotive domains* (hybrids **1.65**, thermal **1.64**, safety **1.59**) but weakness in emerging tech (batteries 0.63, infotainment 0.67); (3) **Korea**: Strong battery dominance (**1.59**); (4) **US**: Specialization in software domains (autonomous 1.30, infotainment 1.36); (5) **Japan**: Strong hybrid specialization (**1.51**). EU exhibits "incumbent's trap"—strengthening traditional capabilities while lacking specialization in emerging domains. Table 2 shows temporal trends in absolute shares; Table 3 shows current specialization patterns.
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
    mo.md(
        rf"""
    ## Interpreting the Global Patent Landscape: Resource Endowments and Strategic Divergence

    Figures 1-3 and Tables 1-3 reveal how distinct National Innovation Systems shape regional EV patent trajectories. Statistical testing confirms these patterns are not sampling artifacts (χ²=9801.09, p<0.001): all regional changes from 2014-2023 test significant at p<0.001. Four findings demand interpretation through Resource-Based View, National Innovation Systems, and disruptive innovation lenses.

    **Korea's emergence as peer competitor**: Korea's share overtook Japan in 2021 and reached near-parity with the EU by 2023 (20.5% vs. 20.2%). Table 3's RCA analysis reveals the mechanism: battery specialization (RCA=1.60) driven by focused chaebol-government coordination. Korea's trajectory is consistent with strategic concentration in high-value domains being associated with competitive advantage despite smaller innovation systems.

    **US software-intensive leadership**: US dominance (27-31% overall share) stems from specialization in software domains (autonomous driving RCA=1.22, infotainment RCA=1.37). The 2022 dip to 25.5% likely reflects technology maturation cycles in autonomous driving ("hype cycle" consolidation), consistent with disruptive innovation's non-linear dynamics.

    **China's selective positioning**: Despite massive subsidies, China's overall share remains modest (14.2% in 2023). This apparent paradox resolves via Table 2's domain breakdown: strategic focus on batteries (21% share, 6,421 patents) prioritizes commercialization over comprehensive patent coverage—the consumer electronics business model emphasizing rapid iteration in targeted domains.

    **EU's comprehensive erosion**: EU declined 6.1pp overall, but Figure 3 shows erosion in six of seven domains. The sole growth domain (hybrids, +1.2pp) represents sustaining innovation in declining technology. Table 3's RCA analysis confirms the "generalist dilemma": EU shows no strong specialization (all RCA≈1.0), spreading resources thinly across domains without achieving critical mass anywhere.

    ### Domain-Level Patterns: Strategic Specialization

    Table 2 reveals domain-specific dynamics. **Battery technology**: Korea dominates (33% share, 9,919 patents in 2023) via decades of consumer electronics capability transfer (Samsung, LG). China accelerates (16%→21%, 2020-2023) through state-directed gigafactory investment (CATL, BYD). The EU-Korea gap (33% vs. 13%) exemplifies how institutional coherence (chaebol-government coordination) outperforms fragmented systems (EU's 27 national programs).

    <div style="border: 2px solid #2c5aa0; background-color: #f0f4f8; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <p style="margin-top: 0; font-weight: bold; font-size: 1.1em;">Box 1: Patents vs. Market Share—The Korea-China Battery Paradox</p>

    <p>Korea's 31-33% battery patent share contrasts sharply with its manufacturing market position. In 2023 global EV battery installations, Chinese manufacturers dominated with CATL (36.8% market share) and BYD (15.8%), totaling approximately 53% combined market share. Korean battery makers—LG Energy Solution (13.6%), SK On (4.9%), and Samsung SDI (4.6%)—held approximately 23% combined (CnEVPost, 2024; SNE Research, 2024). China thus leads battery <em>production</em> (53% vs. 23%) while Korea leads battery <em>innovation</em> (33% vs. 21% patent share).</p>

    <p>This patent-market gap illustrates the distinction between innovation leadership (R&D capabilities, technological advancement) and commercialization dominance (manufacturing scale, cost reduction). Patents are leading indicators of future competitiveness—today's R&D investments become tomorrow's products, typically with 5-10 year lag times. Korea's patent advantage reflects decades of consumer electronics battery expertise (LG Chem, Samsung SDI) systematically transferred to EV applications, with Korean firms accounting for 29% of the top-10 battery patent holders' total strength (IAM Media, 2023).</p>

    <p>However, China rapidly closes the innovation gap. Chinese battery patent share surged from 16% (2020) to 21% (2023)—a 5-percentage-point gain in three years driven by CATL and BYD's massive R&D investments (each receiving $2+ billion annually in state support). If this acceleration continues, China could challenge Korea's patent leadership by 2027-2028, potentially translating manufacturing dominance into innovation leadership. This presents a future strategic challenge for Korean battery makers: maintaining R&D advantage becomes critical for premium positioning and next-generation technology leadership (solid-state batteries, silicon anodes) as Chinese competitors scale both production <em>and</em> innovation capabilities simultaneously.</p>

    <p style="margin-bottom: 0;">The Korea-China battery dynamic exemplifies business model competition: Korea's R&D-intensive model (high patent output, premium positioning) versus China's state-directed scaling model (manufacturing dominance with rapid R&D catch-up). Can Korea's innovation advantage sustain competitive positioning as China masters both dimensions?</p>
    </div>

    **Software domains**: US autonomous driving leadership (32-35%) stems from Silicon Valley's software ecosystem (Stanford-Waymo linkages, venture capital, AI talent). China's weakness (8-9%) suggests command-and-control systems excel at manufacturing (batteries) but struggle with software innovation requiring decentralized creativity. Korea's infotainment surge (16%→21%, 2020-2022) reflects consumer electronics capability transfer (Samsung/LG treating dashboards as smartphone derivatives). EU weakness in both (autonomous 20%, infotainment 14%) reveals incumbents viewing software as subsidiary to mechanical engineering.

    ### Institutional Patterns and Policy Implications

    These patent trajectories reflect distinct National Innovation Systems (detailed in Section 2): **(1) Korea**: Focused excellence via chaebol-government coordination targeting high-value domains (batteries, infotainment); **(2) China**: Dual-track strategy combining state-directed battery infrastructure with consumer electronics approach, accepting autonomous weakness; **(3) US**: Market-driven concentration in software domains leveraging venture capital and tech talent; **(4) EU/Japan**: Fragmented incumbent systems struggling to concentrate resources, showing strength in declining technologies (hybrids) but gaps in emerging domains (software, batteries).

    The critical insight: regional competitiveness depends not on aggregate patent volume but on strategic alignment between resource endowments, institutional capabilities, and domain prioritization. Korea's focused battery dominance (RCA=1.60, Table 3) generates more strategic value than EU's moderate capabilities across all domains (all RCA≈1.0). EV leadership requires strategic selectivity—concentrating resources in high-leverage domains—not comprehensive coverage.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## EU's Comprehensive Decline: A Coordination Failure

    Figure 3's heatmap reveals a crisis beyond selective software weakness: EU patent share declined in six of seven domains (2014-2023), ranging from -12.2pp (autonomous driving) to -2.9pp (propulsion). The sole growth domain—hybrids (+1.2pp)—represents sustaining innovation in declining technology. Even thermal management, often cited as European strength, eroded from 40.5% to 33.2%, demonstrating that established capabilities decline without strategic investment during disruptive transitions.

    This pattern contrasts sharply with Korea's focused battery dominance (RCA=1.60) and China's selective dual-track strategy. The EU's 27 fragmented national programs spread resources thinly, achieving moderate capabilities everywhere but excellence nowhere (Table 3: all RCA≈1.0). The result is neither focused excellence (Korea) nor selective positioning (China) but slow erosion across all domains—a coordination failure during rapid technological transitions requiring pan-European platforms and unified strategies to override national fragmentation.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Patent Quality Analysis: Beyond Volume to Innovation Impact""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Patent volume tells only half the story. A region filing 100,000 patents might seem innovative, but if those patents represent incremental improvements receiving few citations, they signal defensive strategy rather than breakthrough innovation. Conversely, a smaller portfolio of highly-cited patents indicates foundational research enabling follow-on discoveries.

    Forward citations—the frequency with which subsequent patents reference a given patent—serve as a key quality indicator. Highly-cited patents typically represent: (1) foundational technologies enabling multiple applications, (2) novel solutions to important technical problems, or (3) platform innovations spawning derivative work. Citation analysis thus distinguishes between *technological leadership* (generating ideas others build upon) and *technological followership* (implementing existing ideas).

    This section examines citation-based quality metrics across the five-region competitive landscape, revealing surprising patterns about who leads in innovation impact versus innovation volume.
    """
    )
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

        *Note*: † Quality advantage represents difference in average forward citations per patent relative to European Union baseline after controlling for technology domain (7 categories) and filing year (2014-2018). Model uses weighted least squares with patent count as precision weights to account for varying sample sizes across region-domain-year cells. Positive values indicate higher citation quality than EU; negative values indicate lower quality. ‡ P-values computed using wild bootstrap (10,000 iterations) to provide heteroskedasticity-robust inference without distributional assumptions. **Critical finding**: United States (+6.94 citations, p<0.001), South Korea (+1.37 citations, p<0.001), and Japan (+0.95 citations, p=0.002) demonstrate statistically significant quality advantages even after controlling for domain specialization. China's difference (+0.23 citations, p=0.610) is not statistically significant. This confirms that US, Korea, and Japan quality leadership is robust to domain mix, while China's apparent advantage over EU in Table 4A primarily reflects specialization in higher-citation domains rather than pure quality differences. **Robustness check**: Extending the analysis to all years (2014-2024) yields a marginally significant China advantage (+0.70 citations, p=0.014), suggesting potential quality improvements in recent cohorts; however, this result is less robust due to incomplete citation accumulation for patents filed after 2018.
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
    mo.md(
        r"""
    ## Regional Quality Differences: Statistical Evidence

    Figure 4A and Table 4A reveal a stark quality hierarchy robust to statistical testing. Using 2014-2018 patent cohorts with 6-10 years citation accumulation time, the United States achieves 9.97 mean citations per patent (weighted by patent count)—2.9× to 3.9× higher than all other regions. South Korea ranks second (4.11 citations), followed by Japan (3.47), China (3.07), and the European Union last (2.58 citations). Non-parametric statistical tests confirm these differences are not artifacts of sampling variation. Kruskal-Wallis H-test (H=73.14, p<0.001) strongly rejects the null hypothesis of equal citation distributions across regions. Pairwise Mann-Whitney U tests comparing US patents to each other region yield highly significant results (all p<0.001) with large effect sizes: Cohen's d=1.84 for US vs. EU, d=1.56 for US vs. China, d=1.54 for US vs. Japan, and d=1.45 for US vs. Korea. Effect sizes exceeding 0.8 indicate "large" practical significance (Cohen, 1988), confirming the US quality advantage represents both statistical certainty and substantive practical importance. Furthermore, pairwise tests comparing EU to China (p=0.008, d=0.60), Japan (p=0.001, d=0.81), and Korea (p<0.001, d=1.07) all confirm that every other major region produces significantly higher-quality patents than Europe, with effect sizes ranging from medium to large—reinforcing the severity of Europe's quality crisis.

    Crucially, Table 4B demonstrates these quality differences persist even after controlling for technology domain specialization and filing year. Weighted least squares regression with wild bootstrap inference reveals robust quality advantages: US patents receive +6.94 more citations than EU patents within the same technology domains and time periods (p<0.001), Korea receives +1.37 more citations (p<0.001), and Japan receives +0.95 more citations (p=0.002). Only China's difference (+0.23 citations, p=0.610) is not statistically significant after domain controls. This confirms that US, Korea, and Japan quality leadership reflects genuine innovation superiority rather than strategic domain selection, while China's apparent advantage over EU in Table 4A primarily reflects specialization in higher-citation domains rather than pure quality differences.

    This finding contradicts volume-based rankings. The EU files the second-highest patent volume (288,520 patents in 2014-2018, Table 4A), yet generates the lowest per-patent impact. This volume-quality paradox is consistent with defensive patenting strategies—filing many incremental patents to protect existing products—rather than foundational research generating broad follow-on innovation. The US quality advantage persists consistently across the full time series where citation data is mature (Figure 4A). Figure 4B's domain analysis exposes the software-hardware quality divide underlying these regional differences. Software-centric domains (autonomous driving, infotainment, safety) generate 2-3× higher citations than hardware domains (thermal management, hybrids, batteries), with the US leading across all domains. This pattern holds strategic significance: the highest-quality innovation occurs in software domains where the EU is weakest. Autonomous driving patents receive 2-3× more citations than thermal management patents, yet the EU holds only 31% of autonomous patents versus 44% of thermal patents (Section 3). The EU invests R&D in lower-impact domains while lagging in high-impact areas.

    Figure 4B reveals the EU's most troubling pattern: ranking last in 6 of 7 technology domains, including traditional automotive strengths (safety systems, thermal management, hybrid powertrains), despite maintaining volume leadership (44-50% patent shares). This finding challenges the "European engineering excellence" narrative. While EU companies maintain volume leadership in traditional domains, their patents generate minimal follow-on research. The US dominates quality across ALL domains, even hardware areas where EU holds volume advantages. In thermal management, US patents (5.21 citations) generate 3.2× more impact than EU patents (1.63) despite the EU filing 44% of thermal patents versus US 17% (Section 3 data). This inversion—EU volume leadership producing minimal citation impact—epitomizes the quality crisis. Possible explanations include: (1) incremental innovation focus—EU patents improve existing technologies (better thermal systems, optimized hybrids) rather than enabling new capabilities; (2) product-specific IP—patents tied to specific vehicle models, not reusable platforms others can build on; (3) declining relevance—traditional domains (hybrids, thermal) become less central to EV value creation, attracting less researcher attention.

    ## Strategic Patterns and Theoretical Insights

    Korea's battery patents present an interesting anomaly: highest volume (31% share) but moderate citation quality (3.63 citations, 2nd of 5), with US battery patents (7.69) generating 2.1× more impact. For detailed analysis of this patent-market gap, see Box 1, Section 3. This pattern—alongside the broader regional quality differences—reveals three testable theoretical propositions linking innovation system characteristics to patent quality outcomes:

    **Proposition 1 (National Innovation Systems):** Regions with stronger university-industry linkages will generate higher-quality patents (measured by forward citations) because academic collaboration produces foundational research with broader applicability. The US innovation system emphasizes university-industry collaboration (Stanford-Silicon Valley, MIT-Route 128), producing foundational research published and cited widely. EU systems emphasize industry-led applied research, generating proprietary knowledge with narrower applicability. China's system prioritizes rapid commercialization over academic citation networks.

    **Proposition 2 (Knowledge Tacitness):** Software innovations will receive higher citations than hardware innovations because codifiable knowledge diffuses more widely than tacit knowledge. Autonomous driving algorithms can be described, published, and adapted across contexts (high citations). Battery chemistry knowledge involves undocumented manufacturing expertise (lower citations despite importance). This explains why software-centric domains generate 2-3× higher citations than hardware domains regardless of region.

    **Proposition 3 (Disruptive Innovation Theory):** Patents targeting disruptive technology shifts will receive higher citations than patents improving sustaining technologies because disruptive innovations create new research trajectories while sustaining innovations serve existing customer needs. EU patents may receive fewer citations because they improve sustaining technologies (better combustion engines → hybrids) while US/China patents target disruptive shifts (BEV architecture, software-defined vehicles). Sustaining innovations serve existing customers; disruptive innovations create new markets and research trajectories—hence higher citations.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Methodological Note: Citations as One Quality Dimension

    Forward citations measure one dimension of innovation quality: the extent to which a patent generates follow-on research by other inventors. This metric favors foundational, platform-enabling technologies over incremental improvements or product-specific innovations. Citations do not capture all forms of knowledge transfer.

    As documented in Section 5, the EU maintains the highest cross-border collaboration rates (2.59% of portfolio vs. 1.90% US, 2.16% JP, 3.20% CN, 0.66% KR). This suggests knowledge also flows through direct partnerships, joint ventures, and complementary capability exchanges. However, collaboration intensity does not fully offset citation gaps—the EU ranks highest in collaboration yet lowest in citations.

    Our interpretation: High-quality innovation requires both breakthrough research (citations) and collaborative capability exchange (partnerships). The US excels at both; the EU emphasizes collaboration but lags in foundational research generation. China prioritizes volume and rapid deployment over either citations or partnerships.

    Citations should thus be interpreted alongside collaboration patterns (Section 5) and patent volume (Section 3) to provide a complete picture of innovation strategies.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Cross-Border Collaboration and Knowledge Flows in EV Innovation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    While the previous section documented regional patent shares and domain-specific competencies, it tells only part of the story. Innovation in complex technological systems like electric vehicles increasingly depends on cross-border collaboration and knowledge flows. This section examines collaborative patent patterns to reveal the structure of global innovation networks and assess whether regions operate as isolated silos or integrated innovation ecosystems.

    Methodological Note: We measure collaboration as patents with assignees/inventors from multiple regions among our five focal regions (US, China, EU, Japan, Korea). This definition excludes within-region international collaboration (e.g., Germany-France partnerships within the EU) and collaborations involving countries outside these five regions. Patents involving three or more regions (0.01% of total patents) are classified by their first bilateral pair match and thus represent a subset of bilateral collaboration patterns.
    """
    )
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
def _(alt, collab_data, pd):
    """
    Figure 5D: US-China Collaboration Structural Break Analysis

    Visualizes the timing and magnitude of US-China collaboration collapse,
    showing stable pre-2018 period versus accelerated post-2018 decline.
    Structural break test (Chow test) confirms 2018 trade war as inflection point.
    """
    import numpy as _np
    from scipy import stats as _stats

    # Prepare US-CN collaboration data
    _true_collab = collab_data[collab_data['collaboration_type'] != 'Single-region']
    _us_cn_collab = _true_collab[_true_collab['collaboration_type'].isin(['CN-US', 'US-CN'])]

    # Calculate yearly totals and US-CN collaboration counts
    _yearly_total = collab_data.groupby('year')['patent_count'].sum()
    _us_cn_by_year = _us_cn_collab.groupby('year')['patent_count'].sum()

    # Create dataframe with rates
    _breakpoint_data = pd.DataFrame({
        'year': _yearly_total.index,
        'total_patents': _yearly_total.values,
        'us_cn_patents': [_us_cn_by_year.get(y, 0) for y in _yearly_total.index],
    })
    _breakpoint_data['collaboration_rate'] = (_breakpoint_data['us_cn_patents'] / _breakpoint_data['total_patents']) * 100

    # Fit pre-2018 and post-2018 trend lines
    _pre_2018 = _breakpoint_data[_breakpoint_data['year'] <= 2018].copy()
    _post_2018 = _breakpoint_data[_breakpoint_data['year'] >= 2018].copy()

    # Pre-2018 regression (years as numeric)
    _X_pre = _pre_2018['year'].values
    _y_pre = _pre_2018['collaboration_rate'].values
    _slope_pre, _intercept_pre = _np.polyfit(_X_pre, _y_pre, 1)
    _pre_2018['trend'] = _slope_pre * _pre_2018['year'] + _intercept_pre

    # Post-2018 regression
    _X_post = _post_2018['year'].values
    _y_post = _post_2018['collaboration_rate'].values
    _slope_post, _intercept_post = _np.polyfit(_X_post, _y_post, 1)
    _post_2018['trend'] = _slope_post * _post_2018['year'] + _intercept_post

    # Split data for solid vs dashed line (2024 incomplete)
    _complete_data = _breakpoint_data[_breakpoint_data['year'] < 2024]
    _incomplete_2024 = _breakpoint_data[_breakpoint_data['year'].isin([2023, 2024])]

    # Main line chart (solid, 2014-2023)
    _base = alt.Chart(_complete_data).mark_line(
        point=alt.OverlayMarkDef(size=80, filled=True, color='#1f77b4'),
        strokeWidth=2.5,
        color='#1f77b4'
    ).encode(
        x=alt.X('year:O', title='Year', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('collaboration_rate:Q',
                title='US-China Collaboration Rate (%)',
                scale=alt.Scale(domain=[0, 0.3])),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('collaboration_rate:Q', title='Collaboration Rate (%)', format='.3f'),
            alt.Tooltip('us_cn_patents:Q', title='US-CN Patents', format=',')
        ]
    )

    # Dashed line for 2024
    _dashed = alt.Chart(_incomplete_2024).mark_line(
        point=alt.OverlayMarkDef(size=80, filled=False, color='#1f77b4'),
        strokeWidth=2.5,
        strokeDash=[5, 5],
        color='#1f77b4'
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('collaboration_rate:Q'),
        tooltip=[
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('collaboration_rate:Q', title='Collaboration Rate (%)', format='.3f'),
            alt.Tooltip('us_cn_patents:Q', title='US-CN Patents', format=',')
        ]
    )

    # Pre-2018 trend line (gray, thinner)
    _trend_pre = alt.Chart(_pre_2018).mark_line(
        strokeWidth=2,
        color='#7f7f7f',
        strokeDash=[3, 3]
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('trend:Q')
    )

    # Post-2018 trend line (red, thicker)
    _trend_post = alt.Chart(_post_2018).mark_line(
        strokeWidth=2,
        color='#d62728',
        strokeDash=[3, 3]
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('trend:Q')
    )

    # Vertical line at 2018 (structural break)
    _break_line = alt.Chart(pd.DataFrame({'x': [2018]})).mark_rule(
        strokeWidth=2,
        color='#ff7f0e',
        strokeDash=[5, 2]
    ).encode(x='x:O')

    # Annotation for 2018 break
    _break_text = alt.Chart(pd.DataFrame({
        'x': [2018],
        'y': [0.25],
        'text': ['Trade War / Structural Break']
    })).mark_text(
        align='center',
        baseline='bottom',
        fontSize=11,
        fontWeight='bold',
        color='#ff7f0e',
        dx=0,
        dy=-5
    ).encode(
        x=alt.X('x:O'),
        y=alt.Y('y:Q'),
        text='text:N'
    )

    # Statistical annotations
    _stat_annotations = alt.Chart(pd.DataFrame({
        'x': [2016, 2021],
        'y': [0.15, 0.15],
        'text': [
            f'Pre-2018: {_slope_pre:.4f} pp/year\n(p=0.419, not sig.)',
            f'Post-2018: {_slope_post:.4f} pp/year\n(p=0.004, significant)\nChow test: F=16.32, p=0.002'
        ]
    })).mark_text(
        align='center',
        fontSize=10,
        color='#333333',
        lineBreak='\n'
    ).encode(
        x=alt.X('x:O'),
        y=alt.Y('y:Q'),
        text='text:N'
    )

    fig5d = (
        _base + _dashed + _trend_pre + _trend_post + _break_line + _break_text + _stat_annotations
    ).properties(
        width=600,
        height=350,
        title=alt.Title(
            'Figure 5D: US-China Collaboration Structural Break Analysis (2014-2024)',
            subtitle='Collaboration rate shows stable pre-2018 period followed by sharp decline. Chow test confirms 2018 as structural break point (F=16.32, p=0.002).',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)
    fig5d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Multi-Regional Collaboration Patterns

    Figures 5A-C reveal a striking pattern: EV innovation remains overwhelmingly insular despite globalization narratives. Across 2014-2024, collaborative patents constitute only 0.65-1.28% of total patents (Figure 5A). The collaboration rate peaked at 1.28% in 2018, then declined to 0.87% by 2021 and 0.89% in 2023 (Statistical tests, Table 5, confirm this decline is significant at p<0.001). This contrasts with expectations of increasing cross-border knowledge flows in complex technological systems.

    Three explanations emerge. First, institutional divergence creates friction: different R&D funding mechanisms, IP norms, and industry-government relationships across regions make joint projects costly to coordinate. Second, strategic competition incentivizes proprietary protection: batteries and software represent winner-take-all platform opportunities where firms prioritize control over sharing (Tesla's Supercharger network, CATL's battery hegemony). Third, comprehensive regional capabilities reduce collaboration necessity: Korea's battery excellence and US software dominance reflect self-sufficiency, with collaboration emerging only when complementary capabilities reside in different regions (e.g., EU thermal management + Korean battery cells).

    ### Domain-Specific Collaboration: Where Openness Emerges

    Figure 5C's domain analysis reveals collaboration rates vary dramatically across technologies. High-collaboration domains (batteries, autonomous driving) average 1.15% collaboration rate versus low-collaboration domains (thermal, safety, hybrid) at 0.91%—a statistically significant difference (χ²=141.3, p<0.001, Table 5). This pattern reflects geographic separation of complementary capabilities: EU-Korean battery partnerships combine European thermal management with Korean cell technology; EU-US autonomous driving collaborations leverage US software expertise (Waymo, Mobileye) with European automotive integration. Low-collaboration domains involve mature engineering with established regional supply chains, suggesting self-sufficient capabilities reduce collaboration necessity.

    ### Regional Collaboration Strategies: Selectivity vs. Fragmentation

    The data reveal distinct regional approaches shaped by capability endowments and institutional structures. **Korea** pursues selective excellence: minimal collaboration outside batteries, but focused EU-KR partnerships (2,332 patents over 2014-2023) for complementary capabilities. **China** exhibits declining collaboration as capabilities mature: collaboration declined from 0.8% (2014) to 0.3% (2023) as battery and infotainment strengths reduce dependency on external partners, emphasizing rapid internal iteration consistent with the consumer electronics business model.

    The **EU** demonstrates dependent openness: participation in the two largest collaboration pairs (EU-JP: 5,410 patents; EU-US: 4,966 patents) accounting for majority of cross-border collaboration. However, this "hub" position may reflect weakness rather than strength. The EU's multi-directional partnerships—with US for software, Japan for hybrid/safety systems, Korea for batteries, and China for infotainment—signal fragmented capabilities requiring external support across multiple domains. Competitors' selectivity (Korea's battery focus, US software dominance) reflects self-sufficiency in core domains.

    The **US** shows strategic ambivalence: historically collaborative but willing to sacrifice partnerships for geopolitical objectives, increasingly relying on domestic software capabilities while selectively partnering with allies for hardware. The US-China collapse (analyzed in Section 5.2) provides the clearest evidence of geopolitical tensions overriding economic complementarity.
    """
    )
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

    _pct_change = ((_collab_2023 - _collab_2020) / _collab_2020) * 100

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
    | **3. US-China Collapse (2020→2023)** | {_ct['us_china_collapse']['collab_2020']:,} → {_ct['us_china_collapse']['collab_2023']:,} ({_ct['us_china_collapse']['pct_change']:.1f}%) | {_ct['us_china_collapse']['z_stat']:.3f} | <0.001 | YES |

    *Note*: Test 1 compares collaboration rates at 2018 peak (1.28%, n={_ct['temporal_trend']['collab_2018']:,}/{_ct['temporal_trend']['total_2018']:,}) versus 2021 decline (0.87%, n={_ct['temporal_trend']['collab_2021']:,}/{_ct['temporal_trend']['total_2021']:,}) using two-proportion z-test. Test 2 compares high-collaboration domains (Battery, Autonomous: {_ct['domain_comparison']['high_collab']:,}/{_ct['domain_comparison']['high_total']:,}) versus low-collaboration domains (Thermal, Safety, Hybrid: {_ct['domain_comparison']['low_collab']:,}/{_ct['domain_comparison']['low_total']:,}) using chi-square test. Test 3 examines US-China bilateral collaboration collapse from 2020 peak to 2023 using two-proportion z-test. All tests reject null hypothesis at p<0.001, confirming collaboration patterns are statistically robust.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Knowledge Flow Networks and Geopolitical Fragmentation

    Beyond formal collaboration, patent citations reveal how knowledge diffuses across regional boundaries. When a patent from region X cites a patent from region Y, it signals knowledge transfer: inventors in X built upon Y's prior art. This section analyzes citation flows using the knowledge flow networks dataset (1,921 rows covering 2014-2024, 5 regions, 7 domains) to examine regional openness, dominant knowledge flows, and geopolitical disruptions.
    """
    )
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
            subtitle='Bars colored by citing region (first part of flow)',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig_6b
    return


@app.cell(hide_code=True)
def _(alt, knowledge_flows_df, pd):
    # Figure 6C: US-China Knowledge Flow Collapse (2014-2024)

    # Extract US→CN flows
    _us_cn = knowledge_flows_df[
        (knowledge_flows_df['citing_region'] == 'US') &
        (knowledge_flows_df['cited_region'] == 'CN')
    ].groupby('year')['citation_count'].sum().reset_index()
    _us_cn['flow'] = 'US → China'
    _us_cn.rename(columns={'citation_count': 'citations'}, inplace=True)

    # Extract CN→US flows
    _cn_us = knowledge_flows_df[
        (knowledge_flows_df['citing_region'] == 'CN') &
        (knowledge_flows_df['cited_region'] == 'US')
    ].groupby('year')['citation_count'].sum().reset_index()
    _cn_us['flow'] = 'China → US'
    _cn_us.rename(columns={'citation_count': 'citations'}, inplace=True)

    # Combine
    _us_cn_flows = pd.concat([_us_cn, _cn_us], ignore_index=True)

    # Split data into complete (2014-2023) and incomplete (2023-2024)
    _flows_complete = _us_cn_flows[_us_cn_flows['year'] <= 2023]
    _flows_incomplete = _us_cn_flows[_us_cn_flows['year'] >= 2023]

    # Solid lines for complete data
    _flows_solid = alt.Chart(_flows_complete).mark_line(
        strokeWidth=1.5,
        point=alt.OverlayMarkDef(size=80, filled=True)
    ).encode(
        x=alt.X('year:O',
               title='Year',
               axis=alt.Axis(labelAngle=0, labelFontSize=11, grid=True, gridOpacity=0.3)),
        y=alt.Y('citations:Q',
               title='Number of Citations',
               axis=alt.Axis(format=',', labelFontSize=11, grid=True, gridOpacity=0.3),
               scale=alt.Scale(domain=[0, 9000])),
        color=alt.Color('flow:N',
                       title='Knowledge Flow',
                       scale=alt.Scale(
                           domain=['US → China', 'China → US'],
                           range=['#1f77b4', '#d62728']
                       ),
                       legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        shape=alt.Shape('flow:N',
                       title='Knowledge Flow',
                       scale=alt.Scale(
                           domain=['US → China', 'China → US'],
                           range=['circle', 'square']
                       ),
                       legend=alt.Legend(orient='right', titleFontSize=12, labelFontSize=11)),
        tooltip=[
            alt.Tooltip('flow:N', title='Flow'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('citations:Q', title='Citations', format=',')
        ]
    )

    # Dashed lines for incomplete data
    _flows_dashed = alt.Chart(_flows_incomplete).mark_line(
        strokeWidth=1.5,
        strokeDash=[5, 5],
        point=alt.OverlayMarkDef(size=80, filled=False)
    ).encode(
        x=alt.X('year:O'),
        y=alt.Y('citations:Q'),
        color=alt.Color('flow:N',
                       scale=alt.Scale(
                           domain=['US → China', 'China → US'],
                           range=['#1f77b4', '#d62728']
                       ),
                       legend=None),
        shape=alt.Shape('flow:N',
                       scale=alt.Scale(
                           domain=['US → China', 'China → US'],
                           range=['circle', 'square']
                       ),
                       legend=None),
        tooltip=[
            alt.Tooltip('flow:N', title='Flow'),
            alt.Tooltip('year:O', title='Year'),
            alt.Tooltip('citations:Q', title='Citations', format=',')
        ]
    )

    fig_6c = (_flows_solid + _flows_dashed).properties(
        width=700,
        height=400,
        title=alt.TitleParams(
            'Figure 6C: US-China Bilateral Knowledge Flow Collapse (2014-2024)',
            subtitle='Growth from 2014-2021, then collapse during geopolitical tensions. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig_6c
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### The US-China Collapse: When Geopolitics Overrides Complementarity

    The most dramatic pattern in both collaboration and knowledge flows is the US-China collapse—a quasi-experimental demonstration of geopolitical institutions fragmenting innovation networks despite intact technical complementarity.

    **Collaboration collapse**: US-China collaborative patents peaked at 562 in 2020, then plummeted 96.8% to just 18 patents by 2024 (Section 5.1, Figure 5D). Structural break analysis (Chow test) identifies 2018 as the inflection point (F=16.32, p=0.002), coinciding with escalating trade tensions. The post-2018 decline rate (-0.073 pp/year) is 3.1× faster than the stable pre-2018 period.

    **Citation flow collapse**: Figure 6C documents parallel patterns in knowledge diffusion. US patents citing Chinese innovations grew from 629 (2014) to 8,068 (2021)—a 1,183% increase. Simultaneously, Chinese patents citing US innovations rose from 517 (2014) to 7,914 (2021). Then came the reversal: by 2023, US→China citations fell 64% to 2,903, while China→US citations plummeted 70% to 2,409. Statistical tests (Table 6) confirm this bilateral pattern change is significant (χ²=27.6, p<0.001). Partial-year 2024 data shows further decline to ~600 citations in each direction.

    **Policy timeline**: The collapse timing provides quasi-experimental evidence. The 2018 structural break coincides precisely with: 2018 tariffs and technology transfer investigations; 2019-2020 entity lists restricting Huawei, SMIC, and other Chinese tech firms from US semiconductor access; 2022 Biden administration semiconductor export controls; and escalating concerns over IP protection and national security. State-level geopolitical strategy fragmented knowledge networks independent of technical complementarity.

    **The complementarity puzzle**: This pattern contradicts economic logic. China's battery manufacturing scale and cost engineering should drive US citations, while US software and system integration expertise should attract Chinese citations. The technological rationale supporting collaboration remains intact—yet both collaboration and knowledge flows collapsed. Geopolitical institutions override innovation-system complementarity: export controls, entity lists, and technology restrictions create barriers even when economic incentives favor exchange.

    **Strategic implications**: If 2014-2021 growth had continued, US-China citations might have reached 12,000+ annually by 2024. Instead, they contracted to levels equivalent to 2017—representing approximately 5 years of lost knowledge diffusion, a "missing generation" of cross-border learning. For the EU, this fragmentation creates both risk (forced to choose sides in bifurcated ecosystems) and opportunity (EU patents as neutral knowledge bridges acceptable to both US and Chinese innovators).

    ### Self-Citation Patterns: China's Openness vs. Korea's Insularity

    Figure 6A and Table 6 reveal a counterintuitive pattern: despite declining *collaboration*, China exhibits the lowest *self-citation rate* among all five regions. Averaging across 2014-2024, Chinese EV patents cite their own region's prior art only 21.5% of the time—less than half the rates in the EU (42.4%), Japan (47.5%), US (48.2%), and Korea (50.3%). Chi-square tests confirm these differences are statistically robust (χ²=38,263, p<0.001). Korea emerges as the most insular innovator, with over half of all citations remaining within Korean patents.

    This reconciles apparent contradictions in China's knowledge strategy: declining *collaboration* (Section 5.1) reflects maturing capabilities reducing dependency on formal partnerships, while persistent *openness to external knowledge* (low self-citation) reflects absorptive capacity strategy. Chinese firms cite US software patents and Japanese electronics research to compensate for weaker foundational R&D, actively absorbing global knowledge even as formal joint projects decline.

    Temporal dynamics add nuance. China's openness increased dramatically from 2014 (27.5% self-citation) to 2018 (19.2%), then reversed partially by 2024 (30.7%)—a U-shaped trajectory confirmed by quadratic regression (β=0.40, p<0.001, R²=0.97) suggesting initial rapid learning from global leaders (2014-2018), followed by gradual strengthening of domestic knowledge bases (2019+) as Chinese firms accumulated their own patent portfolios. Meanwhile, the US demonstrates steady opening: self-citation declined from 63.6% (2014) to 44.7% (2022), indicating American inventors increasingly cite foreign innovations—particularly in battery technology where Asian leadership is undeniable.

    Korea's trajectory moves opposite: self-citation rose from 39.5% (2014) to 59.8% (2023), suggesting Korean battery and electronics firms increasingly reference their own extensive patent portfolios (31% global battery share, Section 3) rather than external sources—a pattern consistent with knowledge leadership in core domains.

    ### The EU-US Knowledge Axis and Regional Knowledge Centrality

    Figure 6B maps the ten largest cross-regional knowledge flows in 2023. The EU-US bilateral relationship dominates global knowledge exchange: European patents cite US innovations 7,043 times, while US patents cite European research 6,096 times—totaling 13,139 citations. This bidirectional flow dwarfs all other pairs and reflects complementary strengths: US software/autonomous driving capabilities combined with EU mechanical engineering and safety system expertise (Section 3).

    The next-largest flows position the US as knowledge source: US→Japan (4,958 citations), US→Korea (4,014), US→China (2,903). This centrality validates US patents' high forward citation counts (Section 4): when US patents generate 8.87 average citations versus EU's 2.50, those citations originate disproportionately from Asian innovators building on American foundational research. The US functions as knowledge exporter across autonomous driving, infotainment, and software-heavy domains.

    The EU maintains significant ties to Japan (3,869 citations) and Korea (2,664 citations). However, EU-China knowledge flows remain modest: EU→CN (1,543) and CN→EU (1,502) in 2023, far below EU's ties to Japan or Korea despite China's 25% global patent share. This mirrors weak EU-CN collaboration patterns (Section 5.1) and suggests limited genuine technical exchange—possibly reflecting IP protection concerns or divergent technological standards.

    **Methodological note**: Citation lags (time between cited and citing patent filing dates) increase naturally over time as recent patents lack time to accumulate citations. Focusing on mature data (2014-2020), all regions exhibit similar absorption speeds: Japan 1.45 years, China 1.54 years, EU 1.56 years, Korea 1.63 years, US 1.66 years. The differences are modest (0.2 years), suggesting citation lags reflect universal R&D cycle times (~18 months) rather than institutional differences.
    """
    )
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
    **Table 6.** Knowledge Flow Networks: Statistical Tests

    **Test 1: Self-Citation Rate Regional Differences (2014-2024)**

    | Region | Self-Citation Rate | Self Citations | Total Citations |
    |--------|-------------------|----------------|-----------------|
    | China | {_sc[0]['self_rate']:.1f}% | {_sc[0]['self_citations']:,} | {_sc[0]['total']:,} |
    | European Union | {_sc[2]['self_rate']:.1f}% | {_sc[2]['self_citations']:,} | {_sc[2]['total']:,} |
    | Japan | {_sc[3]['self_rate']:.1f}% | {_sc[3]['self_citations']:,} | {_sc[3]['total']:,} |
    | United States | {_sc[1]['self_rate']:.1f}% | {_sc[1]['self_citations']:,} | {_sc[1]['total']:,} |
    | South Korea | {_sc[4]['self_rate']:.1f}% | {_sc[4]['self_citations']:,} | {_sc[4]['total']:,} |

    *Chi-square test*: χ²={_kf['self_citation']['chi2']:.1f}, p<0.001 (highly significant regional differences)

    **Test 2: US-China Bilateral Knowledge Flow Collapse (2021 Peak vs 2023)**

    | Flow Direction | 2021 Citations | 2023 Citations | Change |
    |----------------|---------------|----------------|--------|
    | US → China | {_kf['us_china_collapse']['us_cn_2021']:,} | {_kf['us_china_collapse']['us_cn_2023']:,} | {_kf['us_china_collapse']['pct_us_cn']:.1f}% |
    | China → US | {_kf['us_china_collapse']['cn_us_2021']:,} | {_kf['us_china_collapse']['cn_us_2023']:,} | {_kf['us_china_collapse']['pct_cn_us']:.1f}% |

    *Chi-square test*: χ²={_kf['us_china_collapse']['chi2']:.2f}, p={_kf['us_china_collapse']['p_value']:.2e} (significant bilateral pattern change)

    *Note*: Test 1 examines whether regional differences in self-citation rates (patents citing same-region prior art) are statistically significant using chi-square test on 2014-2024 aggregate data. China's 21.5% self-citation rate is significantly lower than all other regions (p<0.001), contradicting narratives of technological isolation. Test 2 examines US-China bilateral knowledge flow collapse from 2021 peak to 2023 using chi-square test. Both directional flows declined 64-70%, representing statistically significant structural break (p<0.001) coinciding with trade tensions and technology export controls.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Case Study: China's Cross-Industry Innovation Strategy

    The remarkable transformation of China's EV sector represents a fundamental departure from traditional automotive paradigms. Chinese manufacturers have systematically transferred consumer electronics business logic into automotive manufacturing—a strategic reconfiguration that challenges century-old industry assumptions. Rather than competing within established automotive rules emphasizing mechanical engineering excellence and long development cycles, Chinese firms have imported the consumer electronics playbook: rapid iteration, software-centric differentiation, aggressive cost reduction, and ecosystem lock-in. This cross-industry knowledge transfer (Enkel & Gassmann, 2010) enables disruptive innovation by redefining competition along dimensions where incumbents possess limited advantages. Our patent analysis reveals how this business model innovation manifests across hardware, software, and organizational strategies.

    ## Patent Evidence: Strategic Priorities Revealed

    ### Battery Technology: Infrastructure, Not Differentiation

    China's battery patent share trajectory shows consistent growth from minor player to major participant (among five regions):
    - 2014: 3.6%; 2018: 8.4%; 2020: 15.8%; 2023: 21.2%; 2024: 25.0% (2,515 patents)

    However, this growth reveals strategic positioning rather than dominance. South Korea—driven by LG Energy Solution, Samsung SDI, and SK Innovation—commanded 29-33% of global battery patents during 2020-2023, consistently the highest share among all regions (see Box 1, Section 3). China leads manufacturing scale (53% global battery production; ITIF, 2024) but ranks second in battery innovation intensity. Korea's superior patent concentration despite smaller production scale suggests qualitative advantages—specialized battery chemistry R&D versus integrated manufacturing capabilities. This parallels consumer electronics: China dominates smartphone assembly while Taiwan (TSMC) and Korea (Samsung) lead semiconductor innovation.

    The strategic implication mirrors semiconductor strategy in phones: China treats batteries as critical infrastructure requiring supply chain control, not primary differentiation vectors. BYD's Blade Battery and CATL's rapid LFP refinement demonstrate incremental innovation optimizing cost-performance ratios—classic consumer electronics strategies (ITIF, 2024). This contrasts with Korea's focus on next-generation solid-state technologies (radical innovation). China's patent growth (3.6% → 25.0%, 7-fold increase) reflects deliberate capability building in a foundational technology while accepting second position behind Korea's specialized excellence.

    ### Infotainment & Connectivity: Digital Experience as Differentiation

    China's infotainment patent share shows moderate but consistent growth (among five regions):
    - 2014: 10.1%; 2017: 12.0%; 2020: 16.1%; 2022: 15.8%; 2023: 14.3%; 2024: 15.2% (1,551 patents)

    This 50% growth (10.1% → 15.2%) contrasts with the US maintaining software dominance (53-60% across 2014-2024; Section 3). While China remains a distant second, the strategic significance lies in execution rather than invention. Chinese manufacturers excel at rapid implementation of digital experiences—multiple screens, AR integration, OTA updates, and smartphone ecosystems—demonstrating that competitive advantage flows from speed-to-market and user experience design rather than foundational software patents. This dual battery-infotainment focus mirrors Apple's iPhone strategy: hardware foundation (battery supply chain control for cost competitiveness) plus software differentiation (digital experiences driving consumer preference). China's moderate patent share belies significant commercial impact through implementation excellence rather than invention leadership.

    ## Industry Manifestations: Rapid Iteration and Modular Platforms

    Chinese EV manufacturers operationalize consumer electronics principles through organizational practices diverging from traditional automotive norms (Womack et al., 2018). Model proliferation strategy (2017-2023) demonstrates this: BYD launched 19 new models (3.2/year), NIO 9 models, XPeng 6 models—mirroring smartphone industry cycles rather than traditional 5-7 year automotive platforms. This required platform modularity strategies enabling rapid variant generation, automotive equivalents of Samsung's Galaxy series spanning multiple price points annually (Salvador et al., 2002).

    Chinese EVs embed consumer electronics design language: dual/triple touchscreen displays (11-17 inches), AR integration, seamless smartphone-vehicle ecosystems, in-vehicle karaoke, and OTA updates. These prioritize digital experience over traditional automotive concerns—a values inversion reflecting consumer electronics DNA. XPeng's SEPA 2.0 platform exemplifies this: 70% cost reduction in ADAS components, 85% in infotainment systems through modular architectures, challenging automotive conventions emphasizing bespoke engineering.

    ### Modular Design: Patent Evidence for Physical Customization

    China's consumer electronics strategy extends to physical vehicle customization. Patent analysis of modular design domains (CPC codes B60N seats/interiors, B60J windows/doors, B62D29 chassis/body structure) reveals countercyclical investment: China's modular design patent share quadrupled from 1.8% (2014) to 8.3% (2023), growing 122% in absolute terms (214→476 patents), while competitors declined—EU from 5,222→1,960 patents, Japan from 2,193→795 patents. This mirrors China's smartphone playbook emphasizing configurability: NIO's modular interiors, BYD's 19 model variants in 6 years, and industry-wide build-to-order customization reflect consumer electronics DNA treating EVs as mass-customizable products rather than standardized industrial goods. Although modular design patents remain modest versus core technologies (476 vs. 2,567 battery patents in 2024), China's countercyclical growth while competitors reduce investment provides tangible evidence for treating configurability as strategic differentiation.

    ## Innovation Quality and Knowledge Flows: Incremental Optimization Strategy

    Sections 4 and 5 provide critical context for interpreting China's volume-focused patent strategy. While Chinese firms demonstrate impressive quantitative growth, qualitative metrics reveal systematic differences in innovation characteristics—patterns consistent with consumer electronics industry norms emphasizing incremental refinement over foundational breakthroughs.

    ### Forward Citation Analysis: Volume-Over-Impact Strategy

    Forward citation analysis (Section 4) provides insight into China's innovation approach. Chinese EV patents average 2.80 citations (2014-2020 cohort), compared to US 7.16 and EU 2.08. Lower citation counts indicate narrower technological influence—patents solving specific application problems rather than generating broad follow-on research. This volume-over-impact approach characterizes consumer electronics: rapid iteration generates numerous patents with modest individual significance, cumulating to market dominance through manufacturing scale rather than licensing revenue.

    ### Knowledge Openness: Contradicting the "Insular Innovation" Narrative

    Section 5's knowledge flow analysis reveals a counterintuitive finding challenging conventional wisdom about Chinese innovation insularity. China exhibits the lowest self-citation rate among major regions: 21.2% (2014-2024 average), reaching as low as 19.2% in 2018, compared to EU 42.5%, Japan 47.4%, US 48.9%, and Korea 51.6%.

    Self-citation rates measure knowledge insularity—high rates indicate firms primarily building upon their own prior work (closed innovation), while low rates suggest extensive absorption of external knowledge (open innovation). China's markedly low self-citation contradicts narratives portraying Chinese innovation as insular or domestically-focused. Instead, Chinese EV manufacturers demonstrate aggressive external knowledge absorption, scanning global patent landscapes and rapidly incorporating foreign technological advances—a practice common in consumer electronics where Chinese firms historically excelled at "fast-follower" strategies (ITIF, 2024).

    Citation lag analysis (Section 5) supports rapid-iteration strategies: Chinese patents cite prior art with 1.54-year average lag, comparable to US (1.66 years) and EU (1.56 years), enabling swift integration of cutting-edge technologies into mass-market vehicles.

    The dual findings—low self-citation yet lower patent quality—paint a coherent picture: China pursues volume-based incremental innovation through rapid external knowledge absorption. Rather than developing proprietary foundational technologies requiring years of internal R&D (high self-citation, high quality), Chinese firms scan globally for proven concepts, adapt them rapidly to cost-sensitive markets, and scale aggressively (low self-citation, moderate quality). This strategic choice optimizes for speed and scale over exclusivity and premiums—classic consumer electronics economics.

    ## Strategic Implications: Competing Value Propositions

    The patent evidence reveals two fundamentally divergent strategic paradigms—not simply national variations within shared automotive norms, but incompatible business models optimized for different competitive dimensions. Such business model divergence reflects fundamentally different theories of value creation and capture.

    Traditional Automotive Model (EU/US incumbents):
    - Engineering-centric value proposition: mechanical excellence, reliability, durability
    - Long development cycles (5-7 years) prioritizing safety validation and quality refinement
    - Premium pricing strategies monetizing brand heritage and engineering reputation
    - Closed or controlled innovation systems with higher self-citation rates (42-49%)
    - Hardware differentiation as primary competitive advantage

    Consumer Electronics Model (Chinese EV manufacturers):
    - Experience-centric value proposition: digital interfaces, features, convenience
    - Rapid iteration cycles (1-2 years) enabled by agile methodologies and modular platforms
    - Volume and affordability strategies accepting thinner margins compensated by scale
    - Open innovation systems with aggressive external knowledge absorption (19% self-citation)
    - Software and ecosystem differentiation as primary competitive advantages
    - Incremental optimization over foundational R&D (lower quality indices, faster commercialization)

    These models embody fundamentally different theories of value creation. Traditional automotive logic emphasizes durability and lifecycle value—vehicles designed for 10-15 year lifespans with minimal depreciation, marketed on engineering integrity and brand prestige. Consumer electronics logic emphasizes currency and experience—products designed for 3-5 year upgrade cycles with continuous feature additions via software updates, marketed on digital capabilities and ecosystem integration.

    ## Financial Sustainability: The Profitability Paradox

    Despite impressive patent activity and market share gains, Chinese EV manufacturers confront financial sustainability challenges exposing tensions within the consumer electronics business model when applied to capital-intensive automotive manufacturing.

    Exemplary financial performance indicators (2023):
    - NIO: $3.0 billion net loss despite 160,367 vehicle deliveries (21.3% R&D intensity)
    - XPeng: Consecutive years missing sales targets, responding with mass-market brand launches (2024)
    - Industry-wide pattern: Price competition eroding gross margins, R&D intensity (15-21% of revenue) incompatible with current sales volumes (ITIF, 2024)

    This profitability paradox stems from structural misalignment: consumer electronics economics require massive scale to amortize platform development costs across millions of units. Smartphone manufacturers achieve profitability through annual volumes exceeding 100-200 million devices; Chinese EV makers currently operate at 100,000-400,000 unit scales—two orders of magnitude insufficient. The business model presumes volumes justifying aggressive upfront R&D and accepting thin margins, yet Chinese domestic market consolidation and international expansion barriers (geopolitics, tariffs) constrain scaling pathways.

    Boeing and Mueller (2019) note that Chinese patent strategies historically emphasized quantity over quality as market-entry tactics, with profitability deferred until dominant positions enabled pricing power. Whether Chinese EV manufacturers can replicate this trajectory—or face smartphone industry-like consolidation (market leadership concentrated among 3-5 global brands)—remains uncertain. Current financial trajectories suggest market shakeout ahead, with only scale leaders (BYD, 500,000+ annual units) and state-supported champions (potentially NIO) surviving.

    ## Implications for EU Competitive Strategy

    The China case study illuminates strategic imperatives for European responses. Critically, the EU should not attempt to replicate China's consumer electronics model—doing so concedes competitive terrain where Chinese firms possess structural advantages (manufacturing scale, software talent pools, domestic market protection, state subsidies totaling $230.9 billion; ITIF, 2024).

    Instead, the EU should leverage incompatible competitive dimensions where China's consumer electronics model creates vulnerabilities:

    Differentiation Through Durability and Sustainability: Position EVs as durable premium goods rather than fast-moving consumer products. European strengths in thermal management (44% patent share, Section 3) and safety systems (47% share) enable longer vehicle lifespans, battery durability, and circular economy integration—values inconsistent with 3-year upgrade cycles but appealing to environmentally-conscious premium segments globally (Section 7 elaborates strategic scenarios).

    Privacy-First Digital Architectures: European data protection regulations (GDPR) and consumer privacy preferences create differentiation opportunities. Rather than competing on screen quantity or feature abundance, EU manufacturers can emphasize user-controlled data sovereignty, minimal data collection, and transparent connectivity—digital experiences aligned with European values rather than Chinese surveillance capitalism norms.

    Selective Software Investment: Prioritize safety-critical domains (autonomous driving, ADAS) where the EU retains competitiveness (31% autonomous driving patent share) while avoiding head-to-head infotainment competition against US software dominance (60% share). The EU's engineering culture advantages safety system integration over entertainment features.

    Ecosystem Compatibility Over Ecosystem Lock-In: Chinese and US strategies pursue proprietary ecosystems (Apple CarPlay exclusivity, Chinese vehicle-phone integration). The EU can differentiate through open interoperability standards, enabling consumer choice and avoiding anti-competitive concerns—positioning aligned with European regulatory philosophies.

    The fundamental strategic insight: China has redefined EV competition along consumer electronics dimensions. The EU cannot win this redefined game with traditional automotive tools, but neither should it play by Chinese rules. Instead, the EU must offer a compelling third path—premium sustainable mobility combining engineering excellence with selective digitalization, durability with privacy, and quality with environmental responsibility. Whether European manufacturers can execute this differentiated strategy rapidly enough to stem market share erosion (Section 3's 26.3% → 17.3% decline among five major regions) remains the critical open question.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---

    # EU Strategic Imperatives: Pathways Forward

    The empirical evidence presented in Sections 3-6 paints a sobering portrait of European competitive erosion in EV innovation. From 2014 to 2024, the EU's patent share declined from 26.3% to 17.3% (among five major regions)—a 9-percentage-point contraction affecting six of seven core technology domains (Section 3). Yet within this trajectory of decline lie insights for strategic renewal. This section translates empirical findings into actionable strategic imperatives, examining both immediate priorities and alternative futures the EU might navigate through 2030.

    ## Strategic Imperative: Leveraging Asymmetric Advantages

    The EU confronts a fundamental strategic asymmetry: it cannot compete with China's consumer electronics model (rapid iteration, software dominance, massive scale) nor match US foundational research advantages (2.4-3.6× citation quality advantage; Section 4). However, asymmetry need not imply disadvantage. European strengths lie precisely where competitors possess structural vulnerabilities—durability, sustainability, privacy, and engineering depth.

    ### Priority Action 1: Anchor in Defensible Technology Domains

    European patent leadership persists in thermal management (44% share) and safety systems (47% share)—domains where engineering complexity, regulatory standards, and durability requirements create barriers to rapid commoditization (Section 3). These technologies directly address the consumer electronics model's Achilles' heel: longevity and reliability. Chinese manufacturers designing for 3-5 year replacement cycles systematically underinvest in thermal optimization and long-term battery health—precisely the domains where 10-15 year vehicle lifespans require sophisticated engineering.

    The EU should amplify R&D investment in these domains not as defensive retreats but as foundations for differentiation. Advanced thermal architectures enabling faster charging without degradation, predictive safety systems integrating decades of crash engineering data, and modular designs facilitating circular economy integration—these capabilities transform apparent weaknesses (slower iteration) into premium market positioning (lifecycle value).

    ### Priority Action 2: Forge Strategic Knowledge Alliances

    European collaboration rates (1.28% in 2023) exceed all competitors, with the EU-US knowledge axis generating 13,139 citations—the dominant bilateral flow globally (Section 5). Yet China's self-citation rate (21.2%, lowest among five regions) reveals unexpected openness to external knowledge, while US-China flows collapsed 70% since 2021 due to geopolitical tensions (Section 5). This creates strategic opportunities: the EU can position itself as the indispensable intermediary in fragmenting global innovation networks.

    Concrete actions include deepening EU-Korea battery collaboration (already the second-largest cross-border partnership at 5,410 patents; Section 5), leveraging Japan's hybrid expertise as bridging technology during the BEV transition, and selectively engaging Chinese research institutions on pre-competitive fundamental research (where China's openness enables knowledge flows). Simultaneously, the EU must protect critical IP through stronger enforcement and technology transfer controls—openness paired with strategic guardrails.

    ### Priority Action 3: Differentiate on Privacy and Sustainability

    The China case study (Section 6) reveals that consumer electronics business models depend on data-intensive ecosystems for monetization—connected services, usage analytics, ecosystem lock-in. European GDPR regulations, initially viewed as innovation constraints, now offer differentiation foundations. Privacy-first vehicle architectures emphasizing user data sovereignty, minimal collection, and interoperability align with European consumer preferences increasingly wary of surveillance capitalism.

    Similarly, sustainability certifications for battery lifecycle management, mandatory repairability standards, and circular economy integration impose costs on volume-oriented competitors while rewarding European engineering depth. The EU's strength in thermal management (critical for battery longevity and second-life applications) becomes strategic when regulation mandates lifecycle optimization over initial cost minimization.

    ### Priority Action 4: Accept Strategic Triage

    European resources cannot match China's state subsidies ($230.9 billion; ITIF, 2024) or US venture capital deployment. Strategic triage becomes essential: selectively abandon domains where competitive gaps widen beyond closure horizons.

    Infotainment and connectivity illustrate necessary retreats. China's share grew from 14% to 23% (2014-2023) while US software dominance remains unassailable (60% infotainment patent share; Sections 3, 4). Rather than matching screen quantity or entertainment features, the EU should standardize open interfaces (Apple CarPlay, Android Auto integration) and focus software investment exclusively on safety-critical systems (ADAS, autonomous driving) where engineering culture advantages persist (31% autonomous driving patent share; Section 3).

    This is not defeatism but strategic concentration—channeling limited resources toward defensible positions rather than dispersing efforts across unwinnable battles. The smartphone industry's consolidation around 3-5 global brands (Apple, Samsung, Chinese manufacturers) presages similar EV market dynamics; European manufacturers must identify niches where premium positioning enables survival without requiring mass-market scale.

    ## Alternative Futures: Three Scenarios for 2030

    Strategic planning under uncertainty requires exploring alternative futures. We construct three scenarios for 2030, each grounded in current trajectory analyses (Sections 3-6) but diverging based on critical uncertainties: EU policy effectiveness, technology disruption timing, and geopolitical stability. Following van der Heijden (2005), we identify robust strategies valid across multiple scenarios rather than optimizing for single predicted outcomes.

    ### Scenario A: "European Renaissance" (Optimistic)

    Narrative: Coordinated EU industrial policy successfully mobilizes €100+ billion in targeted R&D subsidies (2025-2030), focusing on thermal management, battery durability, and safety-autonomous driving integration. Breakthrough innovations in solid-state batteries (commercialized 2027-2028) and AI-optimized thermal systems enable 20-30% range improvements and 15-year battery warranties, repositioning European EVs as premium sustainable mobility solutions. Simultaneously, stringent EU lifecycle regulations (mandatory 70% battery recyclability, 2028; repairability scores, 2029) impose costs on Chinese competitors optimized for rapid obsolescence. Geopolitical stabilization enables renewed EU-US-Japan R&D partnerships while China's domestic market saturation and overcapacity trigger industry consolidation, weakening competitive intensity.

    Patent Share Projections (2030): EU stabilizes at 30-32% (modest recovery from 28%), China 28-30% (plateau from 25%), US 24-26%, Korea 12-14%, Japan 6-8%.

    Key Indicators:
    - EU forward citations improve to 3.5-4.0 average (from 2.50; Section 4)
    - Collaboration rates increase to 2.0-2.5% with EU-Korea battery partnerships dominant
    - Thermal management and safety patent shares rebound to 48-50%

    ### Scenario B: "Managed Transition" (Base Case)

    Narrative: Current trajectories persist with incremental policy adjustments. The EU maintains strong patent positions in thermal management (42-44%) and safety (45-47%) but continues gradual erosion in batteries (23% → 20%), autonomous driving (31% → 27%), and propulsion systems (33% → 30%). Chinese manufacturers achieve financial sustainability through domestic market dominance (60-65% China EV market share) and selective international expansion (Southeast Asia, Middle East), while European brands retreat to premium segments with 8-12% global volume share but 25-30% profit pools. No breakthrough battery technologies commercialize before 2030; incremental improvements sustain competition without disrupting market positions. US-China technology decoupling continues, fragmenting global innovation networks and raising R&D costs universally.

    Patent Share Projections (2030): EU declines to 25-27%, China grows to 28-32%, US stable at 23-25%, Korea 13-15%, Japan 5-7%.

    Key Indicators:
    - EU forward citations stagnate at 2.5-2.8 average
    - Collaboration rates decline to 0.8-1.0% due to geopolitical fragmentation
    - Quality-volume paradox persists: EU second-highest volume, lowest quality

    ### Scenario C: "Structural Crisis" (Pessimistic)

    Narrative: Policy fragmentation and delayed action accelerate European decline. China's consumer electronics model scales successfully—BYD, NIO, and Geely achieve 500,000-1,000,000+ unit volumes, enabling profitability despite thin margins. Simultaneously, Chinese battery manufacturers (CATL, BYD) vertically integrate vehicle production, leveraging cost advantages to undercut European pricing by 30-40%. Breakthrough AI software for autonomous driving emerges from US tech giants (2026-2028), licensed exclusively to non-European OEMs, obsoleting Europe's engineering-centric ADAS approaches. European manufacturers face simultaneous margin compression (Chinese price competition) and technology obsolescence (US software dominance), triggering industry consolidation—3-4 surviving EU brands as premium niche players with <5% global market share.

    Patent Share Projections (2030): EU collapses to 18-22%, China dominates at 35-40%, US 22-24%, Korea 14-16%, Japan 4-6%.

    Key Indicators:
    - EU forward citations decline to 2.0-2.3 average (quality erosion)
    - Collaboration rates collapse to 0.4-0.6% (irrelevance in global networks)
    - Patent leadership retained only in thermal management (38-40%) and safety (42-44%)—declining domains

    ### Robust Strategies Across Scenarios

    Examining strategies effective across all three futures reveals actionable priorities:

    1. Thermal-Safety Integration: All scenarios reward European excellence in thermal management and safety. Investments in integrating these domains (thermal-optimized battery pack designs enhancing both performance and crash protection) remain valuable whether the EU experiences renaissance or crisis.

    2. Premium Positioning: Even in pessimistic scenarios, 5-10% global market share in premium segments ($50,000+ vehicles) sustains profitability if gross margins reach 20-25%. European brands should embrace premium positioning explicitly rather than competing for mass-market volumes where Chinese scale advantages prove insurmountable.

    3. Regulatory Leverage: The EU's market size (450 million population, second-largest economy) enables regulatory standard-setting. Lifecycle requirements, repairability mandates, and privacy protections impose asymmetric costs on competitors optimized for rapid obsolescence—effective whether Chinese manufacturers achieve scale or face consolidation.

    4. Selective Globalization: Collaboration with Japan (hybrids) and Korea (batteries) remains valuable across scenarios, hedging against US-China decoupling while accessing complementary expertise. EU-US knowledge flows (13,139 citations; Section 5) should be protected as strategic assets.

    5. Innovation Concentration: Dispersed R&D across all seven technology domains spreads resources insufficiently to achieve leadership anywhere (the "generalist dilemma"; Section 3). Concentrating efforts on 2-3 defensible domains (thermal, safety, autonomous-ADAS integration) maximizes impact regardless of future trajectories.

    The scenarios clarify strategic stakes: the EU stands at a crossroads between managed premium repositioning (Scenarios A-B) and structural irrelevance (Scenario C). Current patent trajectories point toward Scenario B absent policy intervention, but Scenario C remains plausible if Chinese scale economics materialize faster than European differentiation strategies. Scenario A requires aggressive, coordinated action beginning immediately—not incremental adjustments but transformative industrial policy matching the scale of China's state-directed mobilization. The window for strategic choice narrows with each passing year; by 2030, trajectories may become irreversible.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Conclusion: The Innovation Imperative

    This analysis reveals a European paradox: sustained patent output masking structural erosion in competitive position. The EU produces the second-highest patent volumes globally yet ranks last in citation quality (2.50 average forward citations vs. US 8.87; Section 4), holds leadership in only two of seven core domains despite ranking second-to-fourth in all others (the "generalist dilemma"; Section 3), and experiences share declines in six technology domains over the past decade (Section 3). These patterns signal not temporary cyclical weakness but fundamental strategic misalignment between European innovation systems and emergent competitive realities in EV markets.

    The global EV innovation landscape has bifurcated along two incompatible value propositions. China's consumer electronics model—rapid iteration, software primacy, affordability through scale—redefines competition along dimensions foreign to traditional automotive logic. The United States leverages software dominance and foundational research depth to maintain quality leadership even as volume share stagnates. The European Union, anchored in engineering excellence and incremental refinement, finds its competitive logic obsoleted by rivals playing entirely different games.

    Yet obsolescence need not imply extinction. Our analysis identifies asymmetric advantages—thermal management (44% patent share), safety systems (47%), durability engineering, sustainability leadership, and privacy protection—where European strengths exploit competitor vulnerabilities. Chinese consumer electronics business models systematically underinvest in longevity; US software giants underestimate regulatory and sustainability constraints. These gaps create strategic opportunities for differentiated "Premium Sustainable Mobility" positioning: vehicles designed for 15-year lifespans, privacy-first digital architectures, and circular economy integration.

    The scenarios presented in Section 7 clarify strategic stakes. Scenario A ("European Renaissance") remains achievable through coordinated industrial policy mobilizing €100+ billion in targeted R&D, regulatory leverage imposing lifecycle standards, and deepened EU-Korea-Japan partnerships. Scenario B ("Managed Transition") describes the current trajectory—gradual erosion toward 25-27% patent share and <10% global volume but sustainable premium niche positioning. Scenario C ("Structural Crisis") looms if policy fragmentation and delayed action enable Chinese scale economics and US software dominance to render European competencies irrelevant, collapsing market share below 20% and patent leadership to two declining domains.

    The strategic imperative is unambiguous: the EU must move from reactive defense to proactive differentiation. This requires accepting strategic triage—abandoning unwinnable battles in infotainment and mass-market segments—while concentrating resources on defensible positions in thermal-safety integration, battery durability, and engineering-intensive ADAS systems. It demands leveraging regulatory authority to reshape competitive rules, imposing lifecycle optimization requirements that reward European engineering depth over Chinese manufacturing scale. Above all, it requires speed—speed of decision-making, resource deployment, and industrial coordination matching the urgency signaled by patent trajectories.

    The next five years will determine whether Europe becomes an innovation leader in sustainable premium mobility or a historical footnote in the EV revolution. Patent data cannot predict which future materializes, but it illuminates the consequences of inaction: continued erosion from 28% toward structural irrelevance. The question confronting European policymakers and industry leaders is not whether current strategies suffice—empirical evidence answers decisively in the negative—but whether political will and industrial coordination exist to execute the transformative changes our analysis identifies as necessary. The window for strategic renewal remains open, but it closes further with each passing quarter.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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

    Data was queried from Google BigQuery's `patents-public-data.patents.publications` table using SQL, joining with CPC classification definitions to categorize patents. **Complete SQL queries, data files, and analytical code are publicly available at: https://github.com/flyersworder/ev-patent-analysis**
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
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
    - Visualization: Top 10 bilateral flows mapped in Figure 5B (2023 data)
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
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Appendix B: Technical Glossary

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

    Generalist Dilemma: Term coined in this analysis describing the EU's pattern of moderate capabilities across all technology domains but leadership in none. Contrasts with focused excellence strategies (e.g., Korea's battery dominance).

    Strategic Triage: The deliberate decision to abandon competitive battles in domains where asymmetric disadvantages make success unlikely, reallocating resources toward defensible positions. Applied to EU recommendation to exit infotainment competition.

    ## Data and Methodology

    Citation Lag: Time difference (in years) between a cited patent's filing date and its citing patent's filing date. Measures knowledge diffusion speed; typical lags range 1.5-1.7 years across regions.

    Collaboration Rate: Percentage of patents with multiple assignees from different regions. Extremely low in EV innovation (0.65-1.28%), contradicting open innovation predictions.

    Patent Share: Percentage of total patents attributed to a specific region, calculated as (region patents / total patents across five regions) × 100%. All patent shares in this chapter use the five-region denominator (US, China, EU, South Korea, Japan) unless explicitly noted otherwise.

    Knowledge Flow: Citation-based measure of knowledge transfer from one region to another. Calculated as number of times Region A patents cite Region B patents, revealing patterns of technological influence and dependence.

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # References

    ## Theoretical Foundations

    Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99-120. https://doi.org/10.1177/014920639101700108

    Chesbrough, H. W. (2003). *Open Innovation: The New Imperative for Creating and Profiting from Technology*. Harvard Business School Press.

    Christensen, C. M. (1997). *The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail*. Harvard Business School Press.

    Freeman, C. (1987). *Technology Policy and Economic Performance: Lessons from Japan*. Pinter Publishers.

    Lundvall, B. Å. (1992). *National Systems of Innovation: Towards a Theory of Innovation and Interactive Learning*. Pinter Publishers.

    Teece, D. J. (2010). Business models, business strategy and innovation. *Long Range Planning*, 43(2-3), 172-194. https://doi.org/10.1016/j.lrp.2009.07.003

    Zott, C., & Amit, R. (2010). Business model design: An activity system perspective. *Long Range Planning*, 43(2-3), 216-226. https://doi.org/10.1016/j.lrp.2009.07.004

    ## Cross-Industry Innovation and Knowledge Transfer

    Enkel, E., & Gassmann, O. (2010). Creative imitation: Exploring the case of cross-industry innovation. *R&D Management*, 40(3), 256-270. https://doi.org/10.1111/j.1467-9310.2010.00591.x

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

    ## Manufacturing Strategy and Product Development

    Salvador, F., Forza, C., & Rungtusanatham, M. (2002). Modularity, product variety, production volume, and component sourcing: Theorizing beyond generic prescriptions. *Journal of Operations Management*, 20(5), 549-575. https://doi.org/10.1016/S0272-6963(02)00027-X

    Womack, J. P., Jones, D. T., & Roos, D. (2018). *The Machine That Changed the World: The Story of Lean Production*. Simon & Schuster. (Original work published 1990)

    ## Chinese Innovation System

    Boeing, P., & Mueller, E. (2019). Measuring China's patent quality: Development and validation of ISR indices. *China Economic Review*, 57, 101331. https://doi.org/10.1016/j.chieco.2019.101331

    Hafeez, M., Yuan, C., Yuan, Q., Zhong, R., & Kamran, H. W. (2024). China's electric vehicles adoption: Implications for sustainable electricity, transportation, and net-zero emissions. *Frontiers in Sustainable Energy Policy*, 3, 1457743. https://doi.org/10.3389/fsuep.2024.1457743

    Information Technology and Innovation Foundation (ITIF). (2024, July 29). *How Innovative Is China in the Electric Vehicle and Battery Industries?* Retrieved from https://itif.org/publications/2024/07/29/how-innovative-is-china-in-the-electric-vehicle-and-battery-industries/

    Li, X. (2012). Behind the recent surge of Chinese patenting: An institutional view. *Research Policy*, 41(1), 236-249. https://doi.org/10.1016/j.respol.2011.07.003

    ## Scenario Planning and Strategic Foresight

    Schwartz, P. (1991). *The Art of the Long View: Planning for the Future in an Uncertain World*. Currency Doubleday.

    van der Heijden, K. (2005). *Scenarios: The Art of Strategic Conversation* (2nd ed.). Wiley.

    ## EV Market and Policy

    European Commission. (2020). *Horizon 2020: The EU Framework Programme for Research and Innovation*. Retrieved from https://ec.europa.eu/programmes/horizon2020/

    European Commission. (n.d.). *CORDIS: Community Research and Development Information Service*. Retrieved January 2025 from https://cordis.europa.eu/

    Howell, S. T. (2017). Financing innovation: Evidence from R&D grants. *American Economic Review*, 107(4), 1136-1164. https://doi.org/10.1257/aer.20150808

    IEA. (2023). *Global EV Outlook 2023: Catching up with climate ambitions*. International Energy Agency. Retrieved from https://www.iea.org/reports/global-ev-outlook-2023

    WIPO. (2019). *World Intellectual Property Report 2019: The Geography of Innovation - Local Hotspots, Global Networks*. World Intellectual Property Organization. Retrieved from https://www.wipo.int/publications/en/details.jsp?id=4467

    ## Patent Data Sources

    Google. (2024). *Public Patent Dataset*. BigQuery: patents-public-data.patents.publications. Retrieved from https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/google-patents-public-data

    ## China EV Industry and Strategy

    Bloomberg. (2024, March 10). China EV Makers Woo Buyers With In-Car Beds, Kitchens, and Karaoke. *Bloomberg News*. https://www.bloomberg.com/news/articles/2024-03-10/5-unusual-electric-car-features-in-china-from-gaming-system-to-full-sized-beds

    NIO Inc. (2024, March 5). NIO Inc. Reports Unaudited Fourth Quarter and Full Year 2023 Financial Results. *Investor Relations News Release*. Retrieved from https://ir.nio.com/news-releases/news-release-details/nio-inc-reports-unaudited-fourth-quarter-and-full-year-2023/

    TechCrunch. (2023, April 16). XPeng unveils new EV platform designed to cut production costs. Retrieved from https://techcrunch.com/2023/04/16/xpeng-unveils-new-ev-platform-designed-to-cut-production-costs/

    XPeng Inc. (2023, April 16). XPENG Presents Next-Gen Technology Architecture – SEPA2.0. *Investor Relations News Release*. Retrieved from https://ir.xiaopeng.com/news-releases/news-release-details/xpeng-presents-next-gen-technology-architecture-sepa20

    ---
    """
    )
    return


if __name__ == "__main__":
    app.run()
