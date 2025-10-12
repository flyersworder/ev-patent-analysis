import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---
    title: "The Great Electric Vehicle Innovation Race: A Patent Analysis of US, China, and EU Competition (2014-2024)"
    author: "Qing Ye"
    date: "2025-10-06"
    abstract: |
      This chapter examines the competitive landscape of electric vehicle (EV) innovation through a comprehensive patent analysis spanning 2014-2024. By analyzing patent filings across seven core EV technology domains—Battery Technology, EV Propulsion & Charging, Autonomous Driving, Hybrid & Energy Management, Safety & ADAS, Thermal Management, and Infotainment & Connectivity—we uncover distinct strategic approaches among the United States, China, and the European Union. Our findings reveal a shifting power dynamic: while the EU commanded 42.2% of patent share in 2014, this declined to 33.5% by 2023 and 28.4% in 2024 (partial year). Meanwhile, China surged from 8.7% to 25.0%, demonstrating a dual strategy of battery dominance (42.1% share in 2024) and digital experience focus (24.2% in infotainment). The US maintained leadership at 44-49% share, particularly in autonomous driving (55%) and infotainment (60%). We argue that these patterns reflect fundamentally different visions: China treating EVs as consumer electronics with rapid iteration cycles, the US pursuing technology-driven disruption, and the EU leveraging traditional automotive engineering excellence. The chapter concludes with strategic recommendations for EU competitiveness, emphasizing the need to close software gaps while capitalizing on strengths in thermal management, safety systems, and sustainable manufacturing. All patent share calculations represent proportions among these three regions only, excluding other major automotive nations.
    keywords: ["electric vehicles", "patent analysis", "innovation competition", "China EV strategy", "EU automotive policy", "battery technology", "autonomous driving"]
    ---
    """
    )
    return


@app.cell
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

    ## Europe's Automotive Legacy at a Crossroads

    For more than a century, Europe has been synonymous with automotive excellence. From Karl Benz's 1885 Motorwagen to today's sophisticated vehicles from BMW, Mercedes-Benz, Volkswagen, and Renault, European engineering has defined what it means to build quality automobiles. The European automotive sector currently employs 14 million people, represents 7% of EU GDP, and generates a €400 billion annual trade surplus.

    Yet this legacy now faces its most profound challenge since the invention of the automobile itself.

    The transition to electric vehicles (EVs)—cars powered by batteries rather than internal combustion engines—represents not merely a change in powertrain technology, but a fundamental restructuring of automotive value creation. As vehicles evolve from mechanical machines into "computers on wheels," competitive advantage is shifting from traditional engineering domains toward software capabilities (autonomous driving, digital experiences) and battery technology.

    This chapter presents a troubling reality: **Europe's patent share in core EV technologies declined from 42% in 2014 to just 28% in 2024, while China surged from 9% to 25% over the same period.** This 14-percentage-point erosion in innovation leadership signals a competitive crisis demanding urgent strategic response.

    ## Why Patents Matter

    Patents are leading indicators of future competitiveness. When companies file patents, they reveal where they're investing R&D resources and which capabilities they're developing for tomorrow's markets. Patent activity predicts market outcomes by 5-10 years: today's patents become tomorrow's products and competitive advantages. The region that leads in EV patents today will likely dominate EV markets in 2030-2035—when EVs are projected to represent 50-60% of global vehicle sales.

    Consider Nokia in 2010: it dominated mobile phone sales but was losing the smartphone patent race to Apple and Samsung. By 2013, Nokia's phone business had collapsed. Patents revealed the strategic shift before it appeared in sales figures.

    ## Three Competing Visions for Electric Mobility

    Our analysis examines innovation competition among three major economic regions, each pursuing distinct strategies:

    **The United States** treats EVs as technology platforms, emphasizing software and autonomy. Led by Tesla, Waymo, and Silicon Valley entrants, the US holds 44-47% of patent share, with dominance in autonomous driving (55%) and infotainment systems (60%).

    **China** pursues a dual strategy treating EVs as both industrial policy priority and consumer electronics product. Through massive government support and a "smartphone playbook" emphasizing rapid iteration, China grew from 9% (2014) to 25% (2024) patent share, achieving dominance in battery technology (42%) and significant infotainment capabilities (24%).

    **The European Union** leverages traditional automotive engineering excellence but faces critical gaps in software-defined vehicle technologies. While maintaining leadership in thermal management (44%), safety systems (47%), and hybrid technologies (50%), Europe lags in autonomous driving (31%) and infotainment (16%)—the very technologies increasingly defining consumer purchase decisions.

    ## The Stakes

    The outcome of the EV innovation race will determine: which regions capture value in the €5+ trillion global automotive market; where high-skilled engineering jobs locate; whether Europe depends on US software and Chinese batteries or maintains technological sovereignty; and whether European automotive excellence continues into the electric era or becomes a historical artifact of the internal combustion age.

    ## Research Questions and Contributions

    This chapter addresses three central questions from a European policy perspective:

    1. **Where does Europe stand?** How has patent share distribution evolved among the US, China, and EU from 2014 to 2024 across different EV technology domains?

    2. **What are competitors doing differently?** What distinct strategic approaches do the US and China demonstrate, and what can Europe learn from them?

    3. **What should Europe do?** What policy interventions and business strategies can revitalize European competitiveness in the EV innovation race?

    We provide European policymakers and industry leaders with: comprehensive diagnosis of where Europe leads and lags across seven core EV technology domains; strategic context understanding China's "consumer electronics" approach that challenges traditional automotive business models; and actionable recommendations focusing on realistic pathways that leverage existing strengths while addressing critical gaps.

    ## Methodology Overview

    Our analysis draws from Google's Public Patent Dataset, examining over 270,000 patents filed between 2014 and 2024 by companies and inventors from the US, China, and 27 EU member states. We categorize patents into seven core EV technology domains: Battery Technology, EV Propulsion & Charging, Autonomous Driving & ADAS (Advanced Driver Assistance Systems), Hybrid Powertrains, Vehicle Safety Systems, Thermal Management, and Infotainment & Connectivity.

    **Critical methodological distinction**: We count patents by **assignee/inventor country** (where the innovating company is located), not by patent office location (where patents are filed). Chinese companies file 93.7% of their patents domestically, while US and EU companies file 45-60% internationally—traditional patent office statistics thus systematically misrepresent competitive positioning.

    **Scope note**: The primary analysis focuses on US-China-EU "trilateral competition." We also examine Japan and South Korea's roles—particularly Korea's battery dominance and Japan's hybrid leadership—in the global context section. All patent share percentages represent proportions among the regions discussed in each section. Complete methodology details are provided in Appendix A; a glossary of technical terms appears in Appendix B.

    ## Chapter Structure

    Section 2 presents empirical findings revealing the shifting landscape of EV innovation. Section 3 examines Europe's competitive position, identifying strengths and weaknesses. Section 4 provides a case study of China's "EVs as consumer electronics" strategy. Section 5 presents strategic recommendations for European policymakers and industry leaders. Section 6 concludes with reflections on implementation and urgency.

    The window for strategic repositioning remains open, but is closing rapidly. The next five years will determine whether European automotive leadership—built over more than a century—continues into the electric era.
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

    Our three regions exhibit contrasting innovation systems: China's state-directed approach combines government subsidies, SOE coordination, and domestic market protection to rapidly scale targeted technologies like batteries. The US market-driven system relies on venture capital, university-industry linkages, and entrepreneurial firm entry (Tesla, Rivian). The EU's coordinated market economy emphasizes standards-setting, collaborative R&D programs (Horizon 2020), and incremental innovation by established firms. These institutional differences explain not just patent volume differences but also strategic orientations—China's top-down battery focus, US bottom-up software experimentation, EU consensus-based hybrid strategies.

    ## Open Innovation and Cross-Border Knowledge Flows

    Chesbrough's (2003) open innovation paradigm challenges closed, vertically-integrated R&D models, arguing that firms increasingly source external knowledge and license internal technologies. In global innovation competition, regions function as open innovation hubs with varying degrees of international collaboration.

    Our collaborative patent analysis examines knowledge flows among US, China, and EU innovation systems. The extent of cross-border co-invention reveals whether regions operate as isolated silos or integrated networks. EU-US collaboration patterns may reflect transatlantic technology alliances, while EU-China joint ventures in automotive manufacturing could generate collaborative patents. These flows have strategic implications: regions heavily dependent on external knowledge face vulnerability, while those serving as knowledge sources gain influence.

    ## Business Model Innovation: EVs as Consumer Electronics

    Teece (2010) and Zott & Amit (2010) demonstrate that competitive advantage increasingly stems from business model innovation—new approaches to value creation, delivery, and capture—rather than pure technological superiority. China's "EVs as consumer electronics" strategy represents business model innovation: rapid product cycles (smartphone-style annual releases), ecosystem integration (apps, services, connectivity), and volume-based cost reduction.

    This contrasts fundamentally with traditional automotive business models emphasizing long development cycles, mechanical reliability, and premium pricing. The China case study examines how this alternative business model—enabled by digital technologies but not requiring technological superiority—challenges European and US competitors even in domains where they maintain patent leadership.

    ## Synthesis: Multiple Lenses, Integrated Insights

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
    mo.md(
        r"""
    This section presents the empirical foundation of our analysis, examining patent filing patterns across five major regions (United States, China, European Union, Japan, and South Korea) from 2014-2024. We first analyze aggregate trends showing the overall competitive landscape (Figure 1), then examine domain-specific patterns across seven core EV technologies (Figure 2), before focusing on the EU's competitive position and its decline across technology domains (Figure 3). These patent data reveal not merely different innovation speeds but fundamentally distinct strategic approaches—reflecting the theoretical frameworks of resource-based capabilities, national innovation systems, and disruptive innovation dynamics discussed earlier.
    """
    )
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
def _(mo):
    mo.md(
        rf"""
    ## Interpreting the Global Patent Landscape: Resource Endowments, Disruption, and Strategic Divergence

    The patterns revealed in Figures 1 and 2 illustrate the theoretical frameworks outlined earlier in concrete form. Through the lens of Resource-Based View, National Innovation Systems, and disruptive innovation theory, we can interpret these patent trajectories as manifestations of distinct regional capabilities, institutional arrangements, and strategic responses to technological transition.

    ### Overall Competitive Dynamics: A Five-Region Race

    Figure 1 reveals a complex competitive landscape characterized by sustained US leadership (27-31% share across the decade), gradual EU decline (26% to 20%), steady Chinese growth (6% to 14%), Japanese stability with recent volatility (18-23%), and Korea's remarkable ascent (15% to 22% by 2022). Three patterns demand theoretical interpretation.

    **First, Korea's emergence as a peer competitor**: Korea's patent share overtook Japan in 2021 (19.0% vs. 18.7%) and surged to 21.6% in 2022, nearly matching the EU's 21.5%. By 2023, Korea maintained near-parity with the EU (20.5% vs. 20.2%). This trajectory reflects Korea's National Innovation System—characterized by concentrated industrial policy (targeting batteries), chaebols' capacity for rapid capability building (Samsung SDI, LG Energy Solution), and strategic focus on specific high-value domains rather than comprehensive automotive coverage. The Resource-Based View explains Korea's success: deliberate accumulation of battery manufacturing capabilities—rare, valuable, and difficult to imitate—provides sustainable competitive advantage in the EV value chain's most critical component.

    **Second, the US patent share anomaly of 2021-2023**: US share declined from 27.8% (2021) to 25.5% (2022) before recovering to 27.1% (2023) and surging to 29.3% in partial-year 2024 data. This U-shaped pattern contradicts narratives of consistent US dominance. We interpret this as evidence of technology S-curve dynamics in autonomous driving and infotainment—domains where the US concentrates investment. The 2022 dip likely reflects a consolidation phase following rapid patent growth in 2019-2021 (the "hype cycle" in autonomous driving), with subsequent recovery indicating maturation of commercially viable technologies. This pattern illustrates how disruptive innovation trajectories exhibit non-linear dynamics distinct from sustaining innovation's predictable progression.

    **Third, China's persistent 13-16% share**: Despite policy prioritization and massive subsidies, China's overall patent share remains modest (13.4% in 2021, 14.2% in 2023), contradicting expectations of rapid dominance. This apparent paradox resolves when examining domain-specific patterns (Figure 2), revealing China's strategic selectivity—overwhelming focus on batteries rather than comprehensive coverage. This reflects China's state-directed National Innovation System: concentrated resource deployment in targeted domains (batteries, where China reached 21% share by 2023) rather than distributed investment across all EV technologies. The consumer electronics business model—emphasizing rapid iteration and cost reduction over technological breadth—prioritizes commercialization speed in selected domains over patent leadership across the board.

    ### Domain-Level Analysis: Explaining the Aggregates

    The domain breakdown (Figure 2) provides essential context for interpreting overall trends, revealing how aggregate patterns emerge from distinct technology-specific trajectories shaped by regional resource endowments.

    **Battery Technology: Korea's Hidden Dominance and China's Acceleration**

    Korea's battery patents constitute 29-33% global share (2020-2023)—the highest among all five regions—explaining Korea's overall patent share surge. This dominance reflects decades of capability accumulation in consumer electronics batteries (Samsung, LG), transferred to EV applications through complementary asset deployment (Teece, 2010). China's battery share grew from 16% (2020) to 21% (2023), representing state-directed capability building through subsidized gigafactories (CATL, BYD) and raw material supply chain control. These patterns support the Resource-Based View: battery capabilities are path-dependent, accumulated over decades, and not easily replicated—explaining why US (15-16%) and EU (13-15%) struggle despite recent policy focus.

    The EU-Korea battery gap (33% vs. 13% in 2023) is particularly concerning from a European policy perspective. While the EU possessed comparable battery share to Korea in 2014-2016, Korea's focused industrial policy—concentrating R&D in battery chemistry, manufacturing processes, and cost reduction—generated capabilities the EU's fragmented, multi-country approach could not match. This exemplifies how National Innovation Systems' institutional coherence (Korea's coordinated chaebol-government model) can outperform larger but fragmented systems (EU's 27 national programs).

    **Box 1: Patents vs. Market Share—The Korea-China Battery Paradox**

    Korea's 31-33% battery patent share contrasts sharply with its manufacturing market position. In 2023 global EV battery installations, Chinese manufacturers dominated with CATL (36.8% market share) and BYD (15.8%), totaling approximately 53% combined market share. Korean battery makers—LG Energy Solution (13.6%), SK On (4.9%), and Samsung SDI (4.6%)—held approximately 23% combined (CnEVPost, 2024; SNE Research, 2024). China thus leads battery *production* (53% vs. 23%) while Korea leads battery *innovation* (33% vs. 21% patent share).

    This patent-market gap illustrates the distinction between innovation leadership (R&D capabilities, technological advancement) and commercialization dominance (manufacturing scale, cost reduction). Patents are leading indicators of future competitiveness—today's R&D investments become tomorrow's products, typically with 5-10 year lag times. Korea's patent advantage reflects decades of consumer electronics battery expertise (LG Chem, Samsung SDI) systematically transferred to EV applications, with Korean firms accounting for 29% of the top-10 battery patent holders' total strength (IAM Media, 2023).

    However, China rapidly closes the innovation gap. Chinese battery patent share surged from 16% (2020) to 21% (2023)—a 5-percentage-point gain in three years driven by CATL and BYD's massive R&D investments (each receiving $2+ billion annually in state support). If this acceleration continues, China could challenge Korea's patent leadership by 2027-2028, potentially translating manufacturing dominance into innovation leadership. This presents a future strategic challenge for Korean battery makers: maintaining R&D advantage becomes critical for premium positioning and next-generation technology leadership (solid-state batteries, silicon anodes) as Chinese competitors scale both production *and* innovation capabilities simultaneously.

    The Korea-China battery dynamic thus exemplifies business model competition: Korea's R&D-intensive model (high patent output, premium products, smaller scale) versus China's state-directed scaling model (lower patent intensity but massive manufacturing, rapid catch-up in R&D). The crucial question: Can Korea's innovation advantage sustain competitive positioning as China masters both cost leadership *and* technological advancement?

    **Autonomous Driving: US Software Dominance and the EU-Japan Paradox**

    US autonomous driving leadership (32-35%) reflects Silicon Valley's software engineering ecosystem—university-industry linkages (Stanford-Waymo), venture capital availability, and AI talent concentration. China's persistent weakness (8-9%) contradicts industrial policy narratives, suggesting autonomous driving requires software capabilities distinct from batteries' manufacturing-intensive model. Japan's stable 20-21% share—comparable to the EU's 20-22%—despite Japan's traditional automotive strength, reveals that mechanical engineering excellence does not automatically translate to software-defined vehicle competencies. This pattern exemplifies Christensen's (1997) innovator's dilemma: incumbent capabilities in ICE vehicles provide limited advantage in autonomous systems requiring different knowledge bases.

    **Infotainment: Korea's Surge and the Digital Divide**

    Korea's infotainment patent share surged from 16% (2020) to 21% (2022), likely reflecting Samsung's and LG's consumer electronics DNA—treating vehicle dashboards as smartphone-derived product categories. The US maintains dominance (35-38%), but Korea's rapid growth suggests successful capability transfer from consumer electronics. China's stability (14-16%) and the EU's weakness (14%) reveal strategic positioning differences: Korea and China treat infotainment as extension of existing consumer electronics capabilities, while EU automakers view it as subsidiary to core vehicle engineering—a framing that disadvantages them in software-defined vehicle competition.

    ### Institutional Explanations: Why Regions Diverge

    These patent patterns reflect fundamentally different National Innovation Systems responding to EV transition:

    **Korea's focused excellence model**: Concentrated industrial policy targets specific high-value domains (batteries, displays), with chaebol coordination enabling rapid capability building. Success in batteries and infotainment illustrates this approach's effectiveness, while weakness in autonomous driving (15-16%) reveals its selectivity. Korea demonstrates that smaller innovation systems can achieve peer-competitor status through strategic focus rather than comprehensive coverage.

    **China's dual-track strategy**: State-directed battery dominance (infrastructure control) combined with consumer electronics-inspired infotainment focus (user experience differentiation), while accepting weakness in autonomous driving (8-9%). This reflects business model innovation—treating EVs as fast-moving consumer goods requiring battery supply chains and digital experiences, not comprehensive automotive engineering. The modest overall patent share (13-14%) masks strategic selectivity: China prioritizes commercialization and cost reduction over patent breadth.

    **US software-first positioning**: Market-driven innovation system concentrates resources in software domains (autonomous, infotainment) where venture capital and tech talent provide advantage, while accepting battery gap (15-16%). The 2022 patent share dip suggests technology maturation cycles in software domains exhibit different dynamics than manufacturing-intensive technologies.

    **EU's incumbent challenge**: Fragmented 27-country innovation system struggles to concentrate resources, leading to moderate positions across most domains (20-22%) but excellence in traditional engineering (thermal management, safety). This pattern exemplifies the innovator's dilemma: existing capabilities create organizational and institutional resistance to radical resource reallocation toward software domains.

    **Japan's hybrid identity**: Maintaining comparable patent shares to the EU across most domains (autonomous 21%, infotainment 15%, batteries 18%) despite smaller industrial base suggests persistent automotive engineering excellence. However, similarity to EU patterns—strength in traditional domains, weakness in software—indicates shared incumbent challenges during disruption.

    ### Strategic Implications: Resource Endowments and Competitive Positioning

    These patterns reveal that regional competitiveness in the EV era depends not on aggregate patent volumes but on strategic alignment between resource endowments, institutional capabilities, and technology domain prioritization:

    - **Korea's success** demonstrates that focused capability building in high-value domains (batteries) can generate peer-competitor status despite smaller overall innovation systems
    - **China's approach** shows that consumer electronics business models—rapid iteration, cost focus, selective technology investment—can challenge automotive incumbents even without comprehensive patent leadership
    - **US volatility** suggests software-defined vehicle technologies exhibit different innovation dynamics than mechanical engineering, requiring different policy approaches
    - **EU's dilemma** illustrates how excellence in declining technologies (hybrids, thermal management) can coexist with dangerous gaps in emerging domains (software, batteries), demanding urgent strategic reorientation
    - **Japan's trajectory** mirrors EU challenges, suggesting shared incumbent disadvantages during disruptive transitions

    The critical insight for European policymakers: aggregate patent share (EU's 20%) matters less than domain-specific positioning. Korea's focused battery dominance (33%) generates more strategic value than the EU's moderate capabilities across multiple domains. The five-region competition reveals that EV leadership requires strategic selectivity—concentrating resources in high-leverage domains aligned with institutional capabilities—rather than attempting comprehensive coverage across all technology categories.
    """
    )
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
        r"""
    ## EU's Systemic Erosion: Beyond Software Gaps to Comprehensive Decline

    Figure 3's domain-level heatmap reveals a crisis more profound than selective weakness in emerging technologies: the EU experiences patent share erosion across virtually all domains. This pattern—contrasting sharply with Korea's focused excellence and China's selective strength documented in Figures 1-2—illustrates how institutional fragmentation can undermine even established capabilities during technological transitions.

    **The erosion is comprehensive, not selective**. Between 2014 and 2023, EU patent share declined in six of seven technology domains: autonomous driving (-12.2 percentage points, from 32.4% to 20.2%), thermal management (-7.3pp, from 40.5% to 33.2%), infotainment (-5.2pp, from 18.7% to 13.5%), battery technology (-5.1pp, from 17.8% to 12.7%), safety systems (-3.8pp, from 35.9% to 32.1%), and propulsion (-2.9pp, from 28.3% to 25.4%). Only hybrid powertrains grew modestly (+1.2pp, from 32.2% to 33.4%)—precisely the domain with declining market relevance as the industry shifts from hybrid to pure electric vehicles.

    This pattern exemplifies Christensen's (1997) innovator's dilemma in stark form. The EU's sole growth domain—hybrids—represents sustaining innovation in declining technology, while competitors capture emerging domains. The EU strengthens capabilities the market is abandoning while losing ground in technologies defining future competitiveness. Thermal management—often cited as European strength—declined from 40.5% (2014) to 33.2% (2023), demonstrating that even path-dependent, difficult-to-replicate capabilities (Barney, 1991) erode without strategic investment during disruptive transitions.

    **Contrasting the EU's diffuse decline with Korea's targeted ascent** (analyzed in Figures 1-2) reveals the cost of institutional fragmentation. Korea's National Innovation System—coordinating chaebols, government, and research institutions—concentrated resources in batteries (achieving 32-33% share) and infotainment (surging to 21%), accepting weakness in autonomous driving (15-16%). This strategic selectivity generated peer-competitor status despite Korea's smaller industrial base. The EU's 27 fragmented national programs, conversely, spread resources thinly across domains, achieving moderate capabilities nowhere and excellence only in declining technologies.

    The autonomous driving collapse (-12.2pp, the steepest decline) particularly exemplifies National Innovation Systems' divergent responses to software-intensive technologies. The US market-driven system (venture capital, university-industry linkages) achieved 32-35% autonomous driving share through bottom-up experimentation. China's state-directed approach struggled (8-9%) despite industrial policy, revealing that command-and-control systems excel at manufacturing-intensive domains (batteries) but not software innovation requiring decentralized creativity. The EU's coordinated market economy—relying on consensus among established automakers—proves especially ill-suited: fragmented across 27 countries, lacking pan-European platforms, and constrained by incumbent resistance to radical resource reallocation away from mechanical engineering toward software capabilities.

    **Connecting to earlier analysis**: Figures 1-2 demonstrated that Korea's focused battery dominance (33%) generates more strategic value than the EU's moderate capabilities across multiple domains (20-25%). Figure 3 reveals why: the EU's multi-domain approach dilutes resources without achieving critical mass in any single high-value domain. While Korea deliberately built rare, valuable, inimitable capabilities in batteries (Resource-Based View), the EU's fragmented system prevents such concentration. The result resembles neither focused excellence (Korea) nor selective strategic positioning (China's dual battery-infotainment strategy) but rather slow erosion across the board—a coordination failure characteristic of fragmented National Innovation Systems during rapid technological transitions.

    The policy implication transcends "closing software gaps." The EU faces systemic capability erosion requiring fundamental institutional reform. Korea's chaebol-government coordination and China's state direction—however problematic in other respects—enable resource concentration the EU's consensus-based, 27-country fragmentation cannot match. Without pan-European platforms, unified digital mobility strategies, and mechanisms to override national fragmentation, even traditionally strong domains (thermal management, safety) will continue eroding as competitors concentrate resources more effectively.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""# Cross-Border Collaboration and Knowledge Flows in EV Innovation""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    While the previous section documented regional patent shares and domain-specific competencies, it tells only part of the story. Innovation in complex technological systems like electric vehicles increasingly depends on cross-border collaboration and knowledge flows. This section examines collaborative patent patterns—patents with co-inventors or co-assignees from multiple regions—to reveal the structure of global innovation networks and assess whether regions operate as isolated silos or integrated innovation ecosystems.

    The Open Innovation framework (Chesbrough, 2003) predicts that firms and regions increasingly source external knowledge and collaborate internationally. However, National Innovation Systems theory suggests institutional differences may facilitate or constrain cross-border collaboration. Our analysis addresses three empirical questions: (1) What is the overall rate of international collaboration in EV innovation? (2) Which region pairs collaborate most intensively? (3) Do collaboration patterns vary across technology domains? These patterns have strategic implications: regions serving as collaboration hubs gain influence and access to complementary knowledge, while isolated regions risk technological lock-in.

    **Methodological Note**: We measure collaboration as patents with assignees/inventors from multiple regions among our five focal regions (US, China, EU, Japan, Korea). This definition excludes within-region international collaboration (e.g., Germany-France partnerships within the EU) and collaborations involving countries outside these five regions. Patents involving three or more regions (0.01% of total patents) are classified by their first bilateral pair match and thus represent a subset of bilateral collaboration patterns.
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
    # Figure 4A: Overall Collaboration Rate Trend (2014-2024)
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

    fig4a = (_rate_solid + _rate_dashed).properties(
        width=700,
        height=300,
        title=alt.Title(
            'Figure 4A: EV Patent Collaboration Rate (2014-2024)',
            subtitle='Percentage of patents with co-inventors/assignees from multiple regions. Dashed line indicates incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig4a
    return


@app.cell(hide_code=True)
def _(alt, collab_pairs_by_year_top):
    # Figure 4B: Major Collaboration Pairs Over Time
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

    fig4b = (_pairs_solid + _pairs_dashed).properties(
        width=700,
        height=350,
        title=alt.Title(
            'Figure 4B: Top Cross-Border Collaboration Pairs (2014-2024)',
            subtitle='Patents with co-assignees/inventors from multiple regions. Six largest pairs by total volume. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig4b
    return


@app.cell(hide_code=True)
def _(alt, collab_data):
    def _():
        # Figure 4C: Collaboration Rate by Technology Domain (Small Multiples)
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
        _domain_labels_fig4c = {
            'Battery Technology': 'Battery Tech',
            'EV Propulsion & Charging': 'Propulsion',
            'Autonomous Driving & ADAS': 'Autonomous',
            'Hybrid Powertrains': 'Hybrid',
            'Vehicle Safety Systems': 'Safety',
            'Thermal Management': 'Thermal',
            'Infotainment & Connectivity': 'Infotainment'
        }
        domain_collab['domain_short'] = domain_collab['application_area'].map(_domain_labels_fig4c)
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

        fig4c = alt.vconcat(_row1_collab, _row2_collab, _row3_collab).properties(
            title=alt.Title(
                'Figure 4C: Collaboration Rate by Technology Domain (2014-2024)',
                subtitle='Percentage of patents with cross-border collaboration in each domain. Dashed lines indicate incomplete 2024 data.',
                fontSize=14,
                anchor='start'
            )
        ).configure_view(strokeWidth=0)
        return fig4c


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## The Paradox of Insularity: Low Collaboration in a Global Industry

    Figures 4A-C reveal a striking pattern: **EV innovation remains overwhelmingly insular despite globalization narratives**. Across the 2014-2024 period, collaborative patents (those with co-inventors or assignees from multiple regions) constitute only **0.65-1.28% of total patents** (Figure 4A). The collaboration rate peaked at 1.28% in 2018, declined to 0.87% by 2021, recovered slightly to 0.93% in 2022, then declined to 0.89% in 2023 and 0.65% in partial-year 2024 data. This contrasts sharply with Open Innovation theory's prediction of increasing cross-border knowledge flows in complex technological systems (Chesbrough, 2003).

    Three explanations emerge from our theoretical frameworks:

    **First, National Innovation Systems' institutional divergence** (Freeman, 1987; Lundvall, 1992) creates friction for collaboration. China's state-directed system, the US market-driven venture capital model, and the EU's coordinated market economy operate under fundamentally different R&D funding mechanisms, intellectual property norms, and industry-government relationships. Cross-border collaboration requires bridging these institutional gaps—a transaction cost that may exceed collaboration benefits for most patent-generating activities.

    **Second, strategic competition** in EV technologies—particularly batteries and software—generates incentives for proprietary knowledge protection rather than open sharing. The Resource-Based View (Barney, 1991) predicts that firms protect rare, valuable, inimitable capabilities. With battery technology determining supply chain control and software defining consumer experiences, regions treat EV innovation as strategically sensitive, limiting collaboration with potential competitors.

    **Third, technology complexity may not require collaboration** when regions possess comprehensive capabilities. Korea's focused battery excellence and the US software dominance reflect self-sufficient capability concentrations. Only when complementary capabilities reside in different regions (e.g., EU thermal management + Korean batteries) does collaboration become strategically necessary.

    ### EU as Collaboration Hub: Structural Position vs. Strategic Value

    Despite low overall collaboration, Figure 4B reveals that **the EU participates in the two largest collaboration pairs**: EU-JP (5,410 patents total 2014-2024) and EU-US (4,966 patents total), together accounting for the majority of all cross-border collaboration. In 2023, EU-JP collaboration yielded 172 patents and EU-US totaled 215 patents. The EU also maintains significant partnerships with China (EU-CN: 2,167 total). The EU thus appears as a "collaboration hub"—engaging intensively with both US software capabilities and Asian battery/electronics expertise.

    However, interpreting this positively requires caution. **The EU's high collaboration rate may reflect weakness rather than strength**. Network theory distinguishes between hub position (many connections) and knowledge brokerage (controlling information flows between otherwise disconnected actors). The EU collaborates with US, Japan, and China, but these regions increasingly collaborate bilaterally: US-JP partnerships remained significant (328 patents in 2014, peaking at 453 in 2019, declining to 299 in 2023); US-CN collaboration surged from 273 (2014) to a peak of 562 (2020) before geopolitical tensions drove collapse to 135 (2023), a 76% decline from peak.

    **The EU's collaboration patterns reflect complementary capability needs**: EU automakers partner with US tech firms for software (EU-US) and Japanese suppliers for hybrid/safety systems (EU-JP, the largest collaboration pair globally). China-Japan collaboration (CN-JP: 1,274 total patents) also features prominently, particularly in infotainment technologies. The EU's multi-directional dependency—engaging with both US and Asian partners across multiple technology domains—contrasts with more selective bilateral patterns elsewhere. The EU's hub position thus signals fragmented capabilities requiring external partnerships, while competitors' selectivity reflects self-sufficiency in core domains.

    ### Domain-Specific Collaboration: Where Openness Emerges

    Figure 4C's domain analysis reveals that **collaboration rates vary dramatically across technologies**, supporting the Resource-Based View's prediction that firms collaborate when complementary capabilities reside in different regions:

    **Battery Technology** shows the highest collaboration rate among all domains, peaking at 1.80% in 2016 and averaging around 1.4-1.6% in recent years. This reflects geographic separation of battery value chain components: Korean and Japanese firms lead cell manufacturing, European companies excel in thermal management systems, and US firms contribute battery management software. Collaborative patents in batteries often involve EU-Korean partnerships (188 patents in 2014, stabilizing around 40-60 in recent years) combining European safety engineering with Korean cell technology.

    **Autonomous Driving** shows the second-highest collaboration rate, peaking at 1.71% in 2018, concentrated in EU-US partnerships (58-103 patents across most years) and EU-JP collaboration (surge to 269 patents in 2019). The US dominance in autonomous driving (32-35% patent share) creates natural collaboration patterns where EU and Japanese automakers partner with US tech firms (Waymo, Mobileye) for self-driving systems. Japan's EU-JP collaboration surge in 2018-2019 (246-269 patents) likely reflects established automotive relationships adapting to ADAS integration.

    **Infotainment & Connectivity** exhibits moderate collaboration rates, peaking at 1.49% in 2018, especially notable given software's typically proprietary nature. The EU-US collaboration in infotainment (333 patents in 2014, declining but still 127 in 2020) suggests European automakers source digital experience capabilities from US tech firms. The decline from 333 (2014) to 127 (2020) to 39 (2023) may indicate either: (1) European capability building reducing dependence, or (2) strategic shift toward proprietary platforms (e.g., Volkswagen's VW.OS, Mercedes' MBOS).

    **Thermal Management, Safety, and Hybrid Powertrains** exhibit the lowest collaboration rates, all below 1.5%. Safety systems peaked at 1.21% (2022), hybrid powertrains at 1.10% (2017), and thermal management at 0.96% (2018). These mature engineering domains with established supply chains generate minimal cross-border co-invention. Thermal management's low collaboration despite EU leadership suggests European capabilities are self-sufficient. Safety systems' insularity reflects standardization—once regulatory requirements are defined, regional innovation becomes independent.

    ### The US-China Collaboration Collapse: Geopolitics Overriding Complementarity

    The most dramatic temporal pattern in Figure 4B is the **US-CN collaboration trajectory**: rising from 273 patents (2014) to 562 (2020)—a 106% increase—before collapsing to 135 (2023), a 76% decline from peak. This collapse occurred despite strong complementary capabilities: China's battery manufacturing and cost engineering combined with US software and system integration should generate collaboration incentives.

    The 2018-2023 decline coincides precisely with US-China trade tensions, Trump administration tariffs, and Biden administration export controls on semiconductor technology. This provides quasi-experimental evidence that **geopolitical factors can override economic complementarity** in shaping innovation networks. The National Innovation Systems perspective (Freeman, 1987) emphasizes institutional context—but Figure 4B demonstrates that state-level geopolitical strategy can fragment otherwise efficient innovation networks.

    Notably, EU-CN collaboration did not collapse equivalently: it peaked at 292 patents (2019), declined to 227 (2020), rebounded to 268 (2021), then declined to 162 (2023), and dropped to 40 (partial 2024). While showing decline, the EU-CN drop (45% from peak to 2023) is far less severe than US-CN collapse (76%). This differential suggests EU policy maintains technological engagement with China even as US policy seeks decoupling. The strategic implication: the EU's intermediate position allows hedging between US alliance and Chinese market access.

    ### Strategic Implications: Collaboration as Competitive Advantage?

    Our findings challenge simplistic narratives equating collaboration with innovation leadership. The data reveal three distinct collaboration strategies:

    **Korea's selective excellence**: Minimal collaboration outside batteries (primarily EU-KR), reflecting self-sufficient capabilities in chosen domains. Collaboration rate remains below 2% overall, concentrated in battery partnerships. This supports strategic focus—Korea collaborates only when accessing complementary capabilities (EU thermal management), not broadly.

    **China's decreasing openness**: Despite rhetoric of "open innovation," China's collaboration rate declined from 2.5% (2016) to 1.8% (2023). The US-CN collapse dominates this trend, but EU-CN and CN-JP also declined. This suggests China's growing self-sufficiency: as battery and infotainment capabilities matured, dependence on external knowledge decreased. The consumer electronics business model emphasizes rapid internal iteration over collaborative development.

    **EU's dependent openness**: Highest absolute collaboration volumes (EU-US, EU-JP, EU-KR all in top 6 pairs), but this reflects fragmented capabilities requiring external partnerships. The EU collaborates in batteries (EU-KR), software (EU-US), and hybrid systems (EU-JP)—precisely the domains where it lags in independent patent share. This pattern illustrates Christensen's (1997) innovator's dilemma: established automotive players seek partnerships to access disruptive capabilities they failed to develop internally.

    **US strategic ambivalence**: Historically collaborative (EU-US, US-JP, US-CN all major pairs), but the China decoupling reveals willingness to sacrifice collaboration for geopolitical objectives. Post-2020 data suggest the US increasingly relies on domestic software capabilities (Silicon Valley ecosystem) while selectively partnering with allies (EU, Japan, Korea) for hardware/manufacturing.

    ### The Open Innovation Paradox: Why EVs Remain Closed

    The low collaboration rates (0.65-1.28%) documented in Figure 4A contradict Chesbrough's (2003) Open Innovation prediction that complex technologies drive external knowledge sourcing. Three factors explain this paradox:

    1. **Winner-take-all dynamics**: EV technologies (batteries, software) exhibit increasing returns to scale. Firms compete for dominant platforms (Tesla's Supercharger network, China's CATL battery hegemony) rather than sharing knowledge. Collaboration risks creating competitors.

    2. **Institutional barriers**: National security reviews (CFIUS in US, EU merger control), export controls, and intellectual property disputes raise collaboration costs. The 18-month patent publication delay creates asymmetric information—partners may exploit knowledge before protection.

    3. **Vertical integration strategies**: Tesla's model of in-house batteries, software, and manufacturing directly contradicts open innovation. Chinese EV makers (BYD, NIO) similarly pursue vertical integration. This suggests EV business models favor control over collaboration.

    The theoretical insight: **Open Innovation may apply within regions (clusters, ecosystems) but not between competing National Innovation Systems**. Silicon Valley exhibits open innovation through talent mobility and startup collaboration, but US-China knowledge flows face state-imposed barriers. The nation-state remains the relevant unit of analysis for EV innovation competition.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Case Study: China's "EVs as Consumer Electronics" Strategy

    ## The Smartphone-on-Wheels Paradigm Shift

    Our patent data reveals a critical strategic divergence: **China is treating EVs as consumer electronics, not traditional automobiles**. This explains both their patent patterns and competitive positioning.

    ### China's Dual Strategy: Battery Dominance + Digital Experience

    #### Battery Technology: Steady Growth to Market Leadership

    China's battery patent share trajectory (among three regions):
    - **2014**: 7.3% (minor player)
    - **2018**: 17.4% (emerging)
    - **2020**: 30.0% (parity)
    - **2023**: 37.9% (leading)
    - **2024***: 42.1% (dominant)

    **Pattern**: Consistent, aggressive growth—treating batteries as core infrastructure (like semiconductors in phones)

    #### Infotainment & Connectivity: Strategic Focus

    China's infotainment patent share (among three regions):
    - **2014**: 15.0% (baseline)
    - **2017**: 18.1% (accelerating)
    - **2020**: 24.1% (major push)
    - **2022**: 25.4% (peak)
    - **2023-2024***: ~24% (stabilizing at high level)

    **Key Insight**: China grew infotainment share from 15% → 24% while US held steady at ~60% and EU declined from 23% → 16%

    ### The Consumer Electronics Business Model

    Evidence from industry trends:

    **Rapid Model Cycles** (like smartphone releases):
    - BYD: 19 new models (2017-2023)
    - NIO: 9 new models
    - XPeng: 6 new models
    - Tesla: 5 models (for comparison)

    **Consumer Electronics Features**:
    - **Multiple screens**: 2-3 displays standard (like tablets)
    - **AR glasses**: NIO's $350 AR headset integration
    - **Smartphone integration**: XPeng's phone-to-car ecosystem
    - **Karaoke systems**: Entertainment-first mindset
    - **OTA updates**: Continuous software improvement (like iOS updates)

    **Cost Reduction Focus**:
    - XPeng SEPA 2.0: 70% cost reduction in ADAS, 85% in infotainment
    - Focus on volume and affordability over premium pricing

    ### Physical Customization: Patent Evidence Supporting the Consumer Electronics Approach

    Beyond software and digital experiences, China's consumer electronics strategy extends to physical vehicle customization—a defining characteristic of modern consumer products like smartphones. Exploratory patent analysis of modular design and customization domains (CPC codes B60N seats/interiors, B60J windows/doors, B62D29 chassis/body structure) reveals striking patterns supporting this thesis.

    **China's Strategic Growth in Modular Design Patents**:

    Among five major regions (US, China, EU, Japan, South Korea), China's modular design patent share evolved dramatically:
    - **2014**: 1.8% (214 patents) - negligible presence
    - **2018**: 4.4% (433 patents) - emerging focus
    - **2022**: 5.1% (480 patents) - sustained growth
    - **2023**: 8.3% (476 patents) - **quadrupled from 2014**

    China is the **only major region showing growth** in this domain. Competitors experienced decline or stagnation:
    - **EU**: 43.3% → 34.3% (-9pp decline, from 5,222 to 1,960 patents)
    - **US**: 24.4% → 27.9% (modest gain, but absolute decline from 2,946 to 1,591 patents)
    - **Japan**: 18.2% → 13.9% (-4.3pp decline, collapsed from 2,193 to 795 patents)
    - **Korea**: 12.3% → 15.5% (share gain, but absolute stagnation around 1,500-1,960 patents)

    **Interpretation**: This pattern mirrors China's smartphone-industry playbook. Just as Xiaomi, Oppo, and Huawei offer extensive color options, material choices, and accessory ecosystems, Chinese EV makers (NIO, BYD, XPeng) emphasize configurability. NIO's modular interior systems, BYD's 19 model variants in 6 years, and industry-wide emphasis on build-to-order customization all reflect consumer electronics DNA.

    China's **122% absolute growth** (214 → 476 patents) while incumbents decline signals strategic intent: treating EVs as mass-customizable products rather than standardized industrial goods. This contrasts sharply with traditional automotive approaches emphasizing platform standardization and limited variation (the "Ford Model T" paradigm).

    **Important Caveat**: The overall category declined 53% across all regions (12,055 patents in 2014 → 5,708 in 2023), suggesting either technological maturation or—more likely—that key manufacturing innovations are protected as trade secrets rather than patents. China's modular design patents remain modest in absolute terms (476) compared to core technologies like batteries (2,567 in 2024). The CPC codes capture broad vehicle design elements (seats, windows, chassis) extending beyond EV-specific customization.

    Nonetheless, China's countercyclical growth—patenting more while others patent less—provides tangible evidence for the "EVs as consumer electronics" thesis. Where traditional automakers reduce investment in physical modularity (viewing it as mature technology), Chinese firms increase patenting activity, treating configurability as strategic differentiation. This pattern, combined with battery dominance and infotainment focus, reveals a comprehensive consumer electronics approach spanning hardware, software, and manufacturing flexibility.

    ### Strategic Implications: Different Race, Different Rules

    **Traditional Auto Model (EU/US)**:
    - Long development cycles (5-7 years)
    - Emphasis on mechanical excellence
    - Premium pricing for quality
    - Safety and durability first
    - Slower software innovation

    **Consumer Electronics Model (China)**:
    - Rapid iteration (1-2 year cycles)
    - Software/digital experience focus
    - Aggressive pricing
    - Feature-rich for consumer appeal
    - Quality/profitability trade-offs

    ### What 2024* Data Reveals (Incomplete Year)

    Despite incomplete data, 2024 shows (share among three regions):

    **Overall Patent Distribution**:
    - US: 46.6% (12,605 patents)
    - EU: 28.4% (7,675 patents)
    - CN: 25.0% (6,777 patents)

    **Infotainment Specific**:
    - US: 59.5% (3,616 patents)
    - CN: 24.2% (1,472 patents)
    - EU: 16.3% (989 patents)

    **Battery Technology**:
    - **CN: 42.1% (2,567 patents)** - Highest share among three regions
    - US: 32.6% (1,989 patents)
    - EU: 25.3% (1,541 patents)

    ### Critical Observation

    China maintains high infotainment focus (~24%) **while simultaneously dominating batteries (42%)**. This dual strategy is unique:
    - **Hardware foundation**: Battery dominance ensures supply chain control
    - **Software differentiation**: Infotainment focus drives consumer preference
    - **Ecosystem play**: Like Apple's hardware + software integration

    ### Market Reality Check: The Profitability Challenge

    Despite patent activity, Chinese EV startups face financial challenges:

    **Financial Struggles**:
    - NIO: $3 billion net loss (2023)
    - NIO, XPeng, Great Wall: Missed sales targets 2 years running
    - Response: Launching cheaper mass-market brands (2024)

    **Why the disconnect?**
    - Patents ≠ Profitability
    - Consumer electronics model requires massive scale
    - Price competition eroding margins
    - Market consolidation likely

    ### EU Response Strategy: Don't Play China's Game

    **What EU Should NOT Do:**
    - Race China on rapid model cycles (plays to their strength)
    - Compete on lowest-cost infotainment (loses quality advantage)
    - Treat EVs as disposable consumer goods (contradicts European values)

    **What EU SHOULD Do:**

    1. **Reframe the Competition**
       - Position EVs as "Premium Sustainable Mobility" not gadgets
       - Emphasize durability, repairability, lifecycle value
       - European quality vs. Chinese quantity

    2. **Selective Digital Investment**
       - Do invest in safety-critical software (autonomous driving, ADAS)
       - Do invest in privacy-first connectivity (European values)
       - Don't copy multi-screen excess
       - Focus on user experience quality over feature quantity

    3. **Leverage Sustainability Advantage**
       - Circular economy expertise (battery recycling)
       - Thermal management leadership = longer battery life = less waste
       - Appeal to environmentally conscious consumers globally

    4. **Premium Positioning**
       - Combine thermal management + battery tech = superior systems
       - Market "10-year lifespan" vs. "3-year upgrade cycle"
       - Target premium segment (like European watches vs. smartwatches)

    ### Two Different Futures

    The patent data reveals **two fundamentally different visions** for EVs:

    **Chinese Vision**: Fast-moving consumer goods
    - Rapid refresh cycles
    - Digital experience paramount
    - Volume and affordability
    - Ecosystem lock-in (apps, services, connectivity)

    **European Opportunity**: Sustainable premium mobility
    - Long-life products
    - Engineering excellence
    - Quality and safety
    - Environmental responsibility

    The EU doesn't need to become China. It needs to offer a **compelling alternative** that appeals to consumers who value:
    - Products that last beyond 3 years
    - Privacy and data security
    - Environmental sustainability
    - Engineering quality over feature bloat

    **The Critical Question**: Can the EU move fast enough to execute this differentiated strategy before market share erosion becomes irreversible?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Strategic Recommendations for EU Competitiveness



    Building on the empirical findings and China case study insights, this section presents actionable strategies for EU policymakers and industry leaders to revitalize European competitiveness in the global EV race.



    ## The EU's Strategic Imperative



    The data reveals three concurrent challenges:

    1. **Declining patent share**: 42% (2014) → 28%* (2024)

    2. **Software gap**: Lagging in autonomous driving (31%) and infotainment (16%)

    3. **Strategic fragmentation**: 27 different national approaches undermining collective competitiveness



    Yet the EU retains crucial advantages: world-class engineering heritage, leadership in thermal management (44%) and safety (47%), strong industrial base, and a unified market of 450M people.



    ## Priority 1: Close the Software & Digital Gap



    **Problem**: EU losing the software-defined vehicle race



    **Recommended Actions**:



    1. **Create an EU Digital Mobility Alliance**

       - Pool resources from BMW, Mercedes, Stellantis, VW for common software platform

       - Partner with European tech champions (SAP, Siemens, Bosch Software)

       - Counter Tesla's vertical integration advantage through collective action



    2. **Accelerate Autonomous Driving R&D**

       - Establish pan-European testing corridors

       - Increase funding for AI and sensor fusion research

       - Partner with universities and startups (Wayve, Oxbotica)

       - Target 40% patent share in autonomous driving by 2030



    3. **Develop Compelling Digital Experiences**

       - Build EU infotainment platforms competitive with Tesla/Rivian

       - Focus on privacy-first, user-centric design (European values as differentiator)

       - Integrate with EU green mobility ecosystems



    ## Priority 2: Leverage Existing Strengths



    **Thermal Management & Safety Leadership** (45-50% patent share)



    **Recommended Actions**:



    1. **Battery System Integration**

       - Combine thermal management expertise with battery technology

       - Create superior battery systems (longer life, faster charging, safer)

       - Market "European Quality" as premium positioning globally



    2. **Safety as Global Standard**

       - Maintain regulatory leadership in vehicle safety

       - Innovate in crashworthiness for heavy EV batteries

       - Export EU safety standards to emerging markets



    3. **Hybrid Technology Bridge**

       - Leverage 50% hybrid patent share to fund pure EV R&D

       - Don't abandon transitional technology prematurely

       - Use hybrid revenue to finance software investments



    ## Priority 3: Secure Battery Supply Chain



    **Current Position**: 30% (2023) → 25%* (2024), competing with China's 38% → 42%*



    **Recommended Actions**:



    1. **Scale European Battery Manufacturing**

       - Accelerate support for Northvolt, Freyr, ACC (Stellantis/Mercedes JV)

       - Attract Asian battery makers to manufacture in EU with regulatory incentives

       - Target 40% global battery patent share by 2030



    2. **Next-Generation Chemistry Leadership**

       - Invest in solid-state batteries (QuantumScape European partnerships)

       - Sodium-ion for affordable EVs

       - Silicon anode technology for range improvements



    3. **Circular Economy Advantage**

       - Lead global innovation in battery recycling technology

       - Create closed-loop battery supply chains

       - Leverage regulatory advantage in sustainability as market differentiator



    ## Priority 4: Coordinated EU Industrial Policy



    **Problem**: Fragmentation undermining collective competitiveness



    **Recommended Actions**:



    1. **EU-Wide EV Moonshot Program**

       - €100B over 10 years (matching US IRA, China subsidies)

       - Focus on software, batteries, charging infrastructure

       - Coordinate national programs (Germany, France, Italy) under unified framework



    2. **Regulatory Harmonization**

       - Single EU market for EV testing and approval

       - Unified charging standards and grid integration

       - Streamlined permitting for gigafactories (reduce from years to months)



    3. **Protect & Nurture Innovation Ecosystem**

       - European DARPA for mobility innovation

       - Easier access to capital for EV/battery startups

       - Prevent brain drain to US/China through competitive funding



    ## Differentiated Positioning: The European Alternative



    **Don't compete on China's consumer electronics playbook**. Instead, position European EVs as **"Premium Sustainable Mobility"**:



    - **Durability**: 10-year lifespan vs 3-year upgrade cycles

    - **Privacy**: Data security and European values

    - **Safety**: Uncompromising standards

    - **Environmental responsibility**: Circular economy leadership

    - **Engineering quality**: Precision over feature bloat



    This positioning appeals to consumers who value longevity, privacy, sustainability, and quality—a substantial global market segment underserved by the Chinese volume approach.



    ## Implementation Roadmap: 2025-2030



    ### Phase 1: Stabilize (2025-2026)

    - Stop patent share erosion

    - Launch EU Digital Mobility Alliance

    - Defend leadership in thermal management & safety



    ### Phase 2: Compete (2027-2029)

    - Reach 40% patent share among three regions

    - Competitive autonomous driving platforms in production

    - European battery gigafactories at scale (500 GWh capacity)



    ### Phase 3: Lead (2030+)

    - Define next-generation EV standards globally

    - Export EU technology and regulatory frameworks

    - Establish sustainable competitive advantage



    ## Summary



    The data shows **the EU has not lost the EV race**, but stands at a critical decision point. The next five years will determine whether European automotive leadership—built over more than a century—continues into the electric era.



    **The Path Forward**: EU can reclaim leadership by:

    1. Playing to strengths (thermal, safety, quality engineering)

    2. Fixing critical gaps (software, autonomy, digital experience)

    3. Coordinated action (pan-European programs, not 27 separate strategies)

    4. Speed (move faster than traditional automotive timelines)



    The window remains open, but is closing rapidly.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Conclusion and Policy Implications

    This chapter's patent analysis of US, China, and EU electric vehicle innovation from 2014-2024 reveals a dynamic, rapidly shifting competitive landscape with profound implications for industrial policy, corporate strategy, and the future of automotive manufacturing.

    ## Key Findings Summary

    1. **Regional Divergence**: The three regions pursue fundamentally different innovation strategies:
       - **US**: Software and autonomy leadership (55% autonomous driving, 60% infotainment)
       - **China**: Dual strategy of battery dominance (42%) and digital experience (24% infotainment)
       - **EU**: Traditional engineering excellence (50% thermal management, 47% safety) but software gaps

    2. **EU's Concerning Trajectory**: European patent share declined from 42.2% (2014) to 28.4% (2024*), with particular weakness in software-defined vehicle technologies crucial for future competitiveness.

    3. **China's Strategic Success**: Patent share grew from 5.9% to 25.0%, demonstrating successful execution of a smartphone-industry playbook applied to automotive: control batteries (hardware), invest in infotainment (software), pursue rapid iteration.

    4. **The Software Imperative**: Across all three regions, digital technologies (autonomous driving, infotainment, connectivity) increasingly differentiate competitive positioning—areas where the EU significantly lags.

    ## Theoretical Contributions

    This analysis contributes to innovation studies and industrial policy literature in three ways:

    **First**, we demonstrate the importance of **measuring innovation by inventor/assignee country** rather than patent office location. Chinese companies file 93.7% domestically while US/EU companies file 45-60% internationally—traditional patent metrics thus systematically misrepresent competitive positioning.

    **Second**, we identify **distinct innovation strategies** reflecting different industrial paradigms: China's consumer electronics approach (rapid iteration, volume, affordability) versus the EU's automotive engineering paradigm (quality, safety, longevity). These aren't just different speeds—they represent fundamentally different theories of value creation.

    **Third**, we highlight the **strategic coordination gap** as a critical EU weakness. While individual European companies maintain technical excellence, fragmented national policies and lack of pan-European platforms (especially in software) undermine collective competitiveness.

    ## Policy Recommendations

    ### For the European Union:

    1. **Urgent Software Investment**: Create a €20-30B EU Digital Mobility Alliance pooling resources from major OEMs, tech companies, and research institutions. Focus on autonomous driving, infotainment platforms, and V2X connectivity.

    2. **Battery Supply Chain Security**: Accelerate support for European battery manufacturing (Northvolt, ACC, Freyr) while investing in next-generation chemistry (solid-state, sodium-ion). Target 40% global patent share by 2030.

    3. **Regulatory Harmonization**: Eliminate fragmentation through single EU market for EV testing, approval, and charging infrastructure. Fast-track permitting for gigafactories.

    4. **Differentiated Positioning**: Don't compete on China's consumer electronics playbook. Instead, position European EVs as "Premium Sustainable Mobility"—emphasizing durability, privacy, safety, and environmental responsibility.

    5. **Coordinated Industrial Policy**: Launch €100B EU EV Moonshot Program (2025-2035) matching US IRA and Chinese subsidies, with coordinated national programs rather than 27 separate strategies.

    ### For the United States:

    1. **Maintain Software Leadership**: Continue investment in autonomous driving and AI while ensuring talent pipeline through immigration and STEM education.

    2. **Address Battery Gap**: While US companies lead in battery patents (33%), manufacturing capacity lags China significantly. The IRA's battery manufacturing incentives must accelerate.

    3. **Strengthen Supply Chains**: Reduce dependence on Chinese battery materials and components through domestic mining, processing, and manufacturing.

    ### For China:

    1. **Path to Profitability**: Patent leadership doesn't guarantee business success—Chinese EV startups face consolidation pressure. Focus must shift from pure innovation to sustainable business models.

    2. **Quality over Quantity**: As China moves upmarket, the rapid-iteration consumer electronics model may need refinement to address safety, durability, and premium positioning.

    ## Limitations and Future Research

    This analysis has several limitations suggesting future research directions:

    **First**, patent counts measure innovation inputs, not commercialization success. Future research should link patent patterns to market outcomes, manufacturing capacity, and firm profitability.

    **Second**, we exclude other major automotive nations (Japan, South Korea) to focus on US-China-EU competition. Comprehensive global analysis would provide additional context.

    **Third**, 2024 data is incomplete. Future updates will reveal whether observed trends (China's battery acceleration, EU's infotainment decline) continue.

    **Fourth**, patent quality varies—counting treats all patents equally. Citation analysis and patent value metrics could refine these findings.

    **Fifth**, technology domains overlap (autonomous driving requires batteries, infotainment, sensors). Network analysis could reveal integration capabilities across domains.

    ## Final Reflection

    The electric vehicle revolution represents more than automotive electrification—it embodies a fundamental reshaping of value creation, competitive advantage, and industrial leadership in the 21st century economy.

    **The EU faces a moment of truth**: Either adapt rapidly to software-defined mobility while leveraging traditional strengths, or risk becoming a premium manufacturer in a market increasingly defined by Chinese volume and American software.

    **China's challenge** is converting patent and manufacturing leadership into sustainable profitability and global brand equity.

    **The US must** maintain software advantages while addressing hardware (battery) gaps that could undermine competitiveness.

    The window for strategic repositioning remains open, but is closing. The next five years will determine whether European automotive leadership—built over more than a century—continues into the electric era, or becomes a historical artifact of the internal combustion age.

    The data is clear: **the race is not over, but the EU must run faster and smarter to stay in it.**

    ---

    **Important Notes**:
    1. **Patent Share Calculation**: All percentages represent patent share **among these three regions only** (US, China, EU)—not global patent share. Other countries (Japan, South Korea, etc.) are excluded from this analysis.
    2. **Patent vs. Market Share**: This analysis focuses on patent activity as a proxy for innovation leadership. Patent share does not directly equal market share—Chinese companies may have lower patent counts but higher vehicle sales due to domestic market advantages. However, long-term competitiveness requires both innovation (patents) and commercialization (market share).
    3. **2024 Data**: Marked with asterisk (*) throughout to indicate incomplete year—percentages will shift as full-year data becomes available.
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

    **IMPORTANT**: This query counts patents by **assignee/inventor country** rather than patent office location, providing accurate attribution of innovation to regions.

    ### Key Methodological Decisions:

    1. **Assignee Country vs. Patent Office**: We use `assignee_harmonized.country_code` instead of `p.country_code` to count who filed patents, not where they were filed. This addresses the bias where Chinese companies file 93.7% domestically while US/EU companies file 45-60% internationally.

    2. **EU Aggregation**: All 27 current EU member states are mapped to single "EU" region for comparative analysis.

    3. **Time Period**: 2014-2024, with 2024 data incomplete as of analysis date.

    4. **Technology Domains**: Seven categories using CPC classification codes (see below).

    ### Technical Implementation

    Data was queried from Google BigQuery's `patents-public-data.patents.publications` table using SQL, joining with CPC classification definitions to categorize patents. The complete query implementation and source code are available in the project repository.
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

    **Category 1: Battery Technology** (Energy Storage for BEVs)
       - H01M 4: Electrodes for batteries
       - H01M 6: Primary cells (non-rechargeable)
       - H01M 10: Secondary cells/accumulators (Li-ion, etc.)
       - H01M 12: Hybrid cells
       - H01M 50: Constructional details, casings, battery packs
       - H01G11: Hybrid capacitors (supercapacitors)

       **Rationale**: Explicitly excludes H01M 8 (fuel cells) as fuel cell vehicles (FCVs)
       represent a fundamentally different technology trajectory from battery electric vehicles
       (BEVs). FCVs have negligible market share (~0.14% of BEV volume) and different competitive
       landscape (dominated by Toyota/Hyundai). Including fuel cells would conflate distinct
       innovation strategies.

    **Category 2: EV Propulsion & Charging** (Motors, Power Electronics, Charging)
       - B60L: Electric propulsion of vehicles
       - H02K: Rotating electric machines (motors/generators)
       - H02P: Control or regulation of electric motors
       - H02J7: Charging or depolarizing batteries/supercapacitors
       - H02M: Power conversion apparatus (inverters, converters)

    **Category 3: Autonomous Driving & ADAS** (Self-Driving and Advanced Assistance)
       - B60W: Conjoint control of vehicle sub-units (THE primary ADAS classification)
       - G05D1: Control of position, course, altitude for autonomous vehicles

       **Rationale**: "ADAS" (Advanced Driver Assistance Systems) refers to autonomous driving
       capabilities, NOT safety. This category focuses on automation and active control during
       driving (adaptive cruise control, lane keeping, collision avoidance, autonomous navigation).

    **Category 4: Hybrid Powertrains** (Hybrid Power Management)
       - B60K6: Hybrid vehicle arrangements and components
       - F02D: Controlling combustion engines (hybrid integration)

       **Note**: B60W20 (hybrid control systems) was removed to avoid overlap with B60W (Category 3).

    **Category 5: Vehicle Safety Systems** (Occupant Protection and Visibility)
       - B60R: Vehicles arrangements and fittings (airbags, seatbelts, crash protection)
       - B60Q: Lighting and signaling devices (headlights, brake lights, turn signals)

       **Rationale**: This category covers passive safety (protection during/after crashes) and
       visibility systems, distinct from ADAS active control. B60R focuses on structural protection
       and restraint systems, while B60Q ensures vehicle visibility to other road users.

    **Category 6: Thermal Management** (Cooling and Heat Management)
       - B60H: Heating, cooling, ventilation, air-conditioning in vehicles
       - F28D: Heat exchangers (radiators, coolant systems)

       **Importance**: Critical for battery longevity, fast-charging capability, and overall EV
       performance. EU leadership in this domain provides defensible competitive advantages.

    **Category 7: Infotainment & Connectivity** (Digital Experience and V2X)
       - B60K35: Instruments, dashboards, displays for vehicles
       - B60K37: Dashboard arrangements
       - H04W4: Services specifically adapted for wireless communication networks
       - G07C5: Registering or indicating vehicle operation (telematics)
       - H04N7/18: Closed-circuit television systems (backup cameras, surround view)
       - G08G: Traffic control systems (V2X communication, vehicle-to-infrastructure)

       **Note**: G08G placed here (not in Safety) as it primarily concerns connectivity and
       communication infrastructure rather than occupant protection.
    ```

    ### Key Design Principles

    1. **Mutual Exclusivity**: Categories designed to avoid overlaps (e.g., B60W20 removed, G08G placed in Infotainment)

    2. **BEV Focus**: Fuel cells (H01M 8) excluded to maintain focus on battery electric vehicle innovation

    3. **Conceptual Clarity**: "ADAS" refers to autonomous driving (Category 3), not safety protection (Category 5)

    4. **Comprehensive Coverage**: Seven categories span all major EV innovation areas from hardware (batteries, motors) to software (autonomy, infotainment)

    5. **Validated Against USPTO Definitions**: All CPC code assignments verified through official USPTO CPC scheme documentation

    ## Data Processing Notes

    - **Filing date format**: Stored as integer YYYYMMDD, divided by 10000 to extract year
    - **EU member states**: All 27 current EU countries included (as of 2024)
    - **Multiple assignees**: Patents with co-inventors from different regions counted for each region (realistic for collaborative R&D)
    - **Global filing capture**: Counts patents filed anywhere in world by companies from these regions, not just domestic filings
    - **No "Others" category**: Patents not matching specific categories excluded entirely to maintain focus on core EV technologies

    ## Data Limitations

    1. **2024 incomplete**: Partial year data as of publication date
    2. **Patent lag**: 18-month publication delay means recent filings may not yet appear
    3. **Regional exclusions**: Japan, South Korea, and other automotive nations excluded to focus on trilateral competition
    4. **Patent quality**: All patents weighted equally; citation analysis could refine
    5. **Technology overlaps**: Some patents may fit multiple categories; CPC codes assigned hierarchically

    ## Reproducibility

    This analysis is fully reproducible using Google BigQuery's public patent dataset. The complete SQL query, data processing code, and visualization functions are provided in this notebook. Data was extracted on [insert date] and reflects patent publications available as of that date.

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

    ## Patent Analysis Methodology

    Alcácer, J., & Gittelman, M. (2006). Patent citations as a measure of knowledge flows: The influence of examiner citations. *Review of Economics and Statistics*, 88(4), 774-779. https://doi.org/10.1162/rest.88.4.774

    Breschi, S., & Lissoni, F. (2009). Mobility of skilled workers and co-invention networks: An anatomy of localized knowledge flows. *Journal of Economic Geography*, 9(4), 439-468. https://doi.org/10.1093/jeg/lbp008

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

    Boeing, P., & Mueller, E. (2019). Measuring China's patent quality: Development and validation of ISR indices. *China Economic Review*, 57, 101331. https://doi.org/10.1016/j.chieco.2019.101331

    Li, X. (2012). Behind the recent surge of Chinese patenting: An institutional view. *Research Policy*, 41(1), 236-249. https://doi.org/10.1016/j.respol.2011.07.003

    ## Scenario Planning and Strategic Foresight

    Schwartz, P. (1991). *The Art of the Long View: Planning for the Future in an Uncertain World*. Currency Doubleday.

    van der Heijden, K. (2005). *Scenarios: The Art of Strategic Conversation* (2nd ed.). Wiley.

    ## EV Market and Policy

    European Commission. (2020). *Horizon 2020: The EU Framework Programme for Research and Innovation*. https://ec.europa.eu/programmes/horizon2020/

    European Commission. *CORDIS: Community Research and Development Information Service*. https://cordis.europa.eu/

    Howell, S. T. (2017). Financing innovation: Evidence from R&D grants. *American Economic Review*, 107(4), 1136-1164. https://doi.org/10.1257/aer.20150808

    IEA. (2023). *Global EV Outlook 2023: Catching up with climate ambitions*. International Energy Agency. https://www.iea.org/reports/global-ev-outlook-2023

    WIPO. (2019). *World Intellectual Property Report 2019: The Geography of Innovation - Local Hotspots, Global Networks*. World Intellectual Property Organization. https://www.wipo.int/publications/en/details.jsp?id=4467

    ## Patent Data Sources

    Google. (2024). Public Patent Dataset. *BigQuery*. patents-public-data.patents.publications. https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/google-patents-public-data

    ## China EV Industry and Strategy

    Bloomberg. (2024, March 10). China EV Makers Woo Buyers With In-Car Beds, Kitchens, and Karaoke. *Bloomberg News*. https://www.bloomberg.com/news/articles/2024-03-10/5-unusual-electric-car-features-in-china-from-gaming-system-to-full-sized-beds

    Digital Creative. (2024). Top 10 User-Centric HMI Designs: How China Is Leading The Way. https://digitalcreative.cn/blog/latest-automotive-hmi-design-trends

    Mixed News. (2022). Augmented Reality: Nreal & Nio show new AR headset. https://mixed-news.com/en/augmented-reality-nreal-nio-show-new-ar-headset/

    NIO Inc. (2024, March 5). NIO Inc. Reports Unaudited Fourth Quarter and Full Year 2023 Financial Results. *Investor Relations News Release*. https://ir.nio.com/news-releases/news-release-details/nio-inc-reports-unaudited-fourth-quarter-and-full-year-2023/

    Research in China. (2024). China Passenger Car Cockpit Multi/Dual Display Research Report, 2023-2024. http://www.researchinchina.com/Htmls/Report/2024/74971.html

    TechCrunch. (2023, April 16). XPeng unveils new EV platform designed to cut production costs. https://techcrunch.com/2023/04/16/xpeng-unveils-new-ev-platform-designed-to-cut-production-costs/

    Wikipedia. (2024). List of BYD Auto vehicles. https://en.wikipedia.org/wiki/List_of_BYD_Auto_vehicles

    Wikipedia. (2024). Nio Inc. https://en.wikipedia.org/wiki/Nio_Inc.

    Wikipedia. (2024). XPeng. https://en.wikipedia.org/wiki/XPeng

    XPeng Inc. (2023, April 16). XPENG Presents Next-Gen Technology Architecture – SEPA2.0. *Investor Relations News Release*. https://ir.xiaopeng.com/news-releases/news-release-details/xpeng-presents-next-gen-technology-architecture-sepa20

    ---
    """
    )
    return


if __name__ == "__main__":
    app.run()
