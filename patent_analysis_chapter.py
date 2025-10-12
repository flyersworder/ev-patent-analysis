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
      This chapter examines a troubling paradox in electric vehicle (EV) innovation: Europe produces the second-highest patent volume globally yet ranks last in innovation quality. Analyzing 385,000+ patents across five major regions (United States, China, European Union, South Korea, and Japan) and seven core EV technology domains from 2014 to 2024, we employ advanced metrics—forward citations, generality indices, and originality indices—to assess not just innovation quantity but technological impact. Our findings challenge conventional narratives. Europe's patent share declined from 26.3% to 17.3% (2014-2024), a 9-percentage-point erosion affecting six of seven technology domains, with sole growth in declining hybrid powertrains. European patents average 2.50 forward citations compared to 8.87 for the US, ranking last despite second-highest volume. This "generalist dilemma"—moderate capabilities across all domains but leadership in none—contrasts sharply with Korea's focused battery excellence (31-33% domain share, highest globally) despite smaller industrial base. China exhibits counterintuitive openness (21.2% self-citation rate, lowest among five regions) yet modest quality (2.80 average citations), pursuing strategic selectivity in batteries and consumer electronics-inspired business models. Cross-border collaboration remains minimal (0.65-1.28% of patents), with US-China knowledge flows collapsing 64-70% since 2021 despite technological complementarity. Grounded in Resource-Based View, National Innovation Systems, and Disruptive Innovation theory, we interpret these patterns as manifestations of distinct regional capabilities, institutional arrangements, and strategic responses to technological transition. The chapter concludes with strategic imperatives for Europe: anchoring in defensible domains (thermal management, safety systems), forging strategic alliances (EU-Korea batteries, EU-US software), differentiating on privacy and sustainability, and accepting strategic triage in unwinnable battles. Three scenarios for 2030 explore alternative futures and robust strategies across uncertainty.
    keywords: ["electric vehicles", "patent analysis", "innovation quality", "forward citations", "generality index", "originality index", "National Innovation Systems", "disruptive innovation", "EU automotive policy", "knowledge flows", "cross-border collaboration", "battery technology", "autonomous driving", "Korea-China paradox"]
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

    ## The European Paradox

    Europe produces the second-highest volume of electric vehicle patents globally—yet ranks dead last in innovation quality.

    From 2014 to 2024, European inventors filed over 62,000 patents across seven core EV technology domains, trailing only the United States in absolute numbers. But when measured by forward citations—the gold standard for assessing patent impact and technological influence—European patents average just 2.50 citations, compared to 8.87 for US patents. This 3.5× quality gap reveals a troubling reality: European innovation generates high activity but low impact.

    This paradox extends deeper. Europe's patent share declined from 26.3% to 17.3% (2014-2024)—a 9-percentage-point erosion affecting six of seven technology domains. Europe's sole growth domain? Hybrid powertrains, the very technology the industry is abandoning as it shifts toward pure electric vehicles. Meanwhile, Europe ranks second, third, or fourth across nearly all domains but leads in precisely none of the high-growth categories defining future competitiveness: autonomous driving, battery innovation, or infotainment systems.

    We term this the "generalist dilemma": moderate capabilities everywhere, excellence nowhere.

    For a continent whose automotive sector employs 14 million people, represents 7% of EU GDP, and generates a €400 billion annual trade surplus, this pattern signals not cyclical weakness but structural crisis. The question is not whether European automotive leadership faces existential threat, but whether the window for strategic renewal remains open—and what actions might reverse these trajectories before they become irreversible.

    ## Why Patents Predict Market Futures

    Patents are leading indicators of competitive positioning, revealing where regions invest R&D resources and develop capabilities for tomorrow's markets. Patent activity predicts market outcomes by 5-10 years: today's patents become tomorrow's products, manufacturing processes, and competitive advantages. The region that leads in EV patents today will likely dominate EV markets in 2030-2035, when electric vehicles are projected to represent 50-60% of global sales and the automotive industry completes its most profound technological transition since the internal combustion engine displaced horses.

    Consider Nokia's collapse: in 2010, Nokia dominated global mobile phone sales yet was hemorrhaging position in the smartphone patent race to Apple and Samsung. Within three years, Nokia's phone business had collapsed, acquired by Microsoft for a fraction of its former value. Patents revealed the strategic shift years before it appeared in sales figures or financial statements.

    The EV transition exhibits similar dynamics. Patent leadership in batteries, autonomous driving software, and infotainment systems will determine which regions capture value in the €5+ trillion global automotive market, where high-skilled engineering jobs locate for the next half-century, and whether Europe maintains technological sovereignty or becomes dependent on US software platforms and Chinese battery supply chains.

    ## The Five-Region Race: Distinct Strategies, Divergent Outcomes

    This chapter analyzes innovation competition among five major regions, each pursuing fundamentally different strategies:

    The United States (27-29% patent share in five-region analysis) treats EVs as software platforms, concentrating resources in autonomous driving (32-35% domain share) and infotainment (35-38%). Led by Tesla, Waymo, and Silicon Valley entrants, US innovation emphasizes disruptive business models and AI-enabled capabilities. The US maintains the highest patent quality globally (8.87 average forward citations), with generality (0.801) and originality (0.855) indices indicating foundational, cross-domain innovation that draws from and contributes to diverse technology fields.

    China (13-16% overall share) pursues strategic selectivity, concentrating on battery technology (accelerating from 16% to 21% domain share, 2020-2023) and consumer electronics-inspired infotainment. China's "smartphone playbook"—rapid iteration cycles, ecosystem integration, volume-based cost reduction—challenges traditional automotive business models. Paradoxically, despite narratives of technological insularity, China exhibits the lowest self-citation rate globally (21.2%), indicating the most internationally open innovation system among all five regions. However, citation quality remains modest (2.80 average), suggesting incremental optimization rather than foundational breakthroughs.

    The European Union (20-22% share) confronts comprehensive erosion: declining patent share in six of seven domains between 2014 and 2023, with only hybrid powertrains growing (+1.2 percentage points). Europe maintains residual strength in thermal management (33% domain share by 2023) and safety systems (32%), reflecting traditional automotive engineering heritage. Yet Europe ranks last in citation quality (2.50 average) and exhibits the "generalist dilemma"—moderate capabilities across all domains but leadership in none of the high-growth categories. This pattern exemplifies the innovator's dilemma: strengthening capabilities in declining technologies while losing ground in disruptive domains.

    South Korea (20-22% share) demonstrates that focused excellence can generate peer-competitor status. Korea dominates battery innovation with 31-33% patent share—the highest among all five regions—reflecting Samsung SDI's, LG Energy Solution's, and SK Innovation's accumulated capabilities in lithium-ion chemistry and manufacturing. Korea's battery patent leadership contrasts sharply with China's battery manufacturing dominance (53% global EV battery installations), creating the "Korea-China battery paradox": Korea leads innovation, China leads production. This divergence between patent leadership and market share illustrates how different national innovation systems—Korea's chaebol-coordinated R&D versus China's state-subsidized manufacturing scale—generate distinct competitive advantages.

    Japan (16-21% share) represents the incumbent's dilemma in stark form. Despite pioneering hybrid vehicles (Toyota Prius, 1997) and maintaining strong positions in hybrid powertrains (27-30% domain share), Japan struggles in software-intensive domains: autonomous driving (20-21%) and infotainment (15%). Japan's patent quality (3.45 average citations) and moderate generality/originality indices indicate solid but not transformative innovation—a pattern shared with the EU, reflecting traditional automotive incumbents' challenges during disruptive technological transitions.

    ## Research Questions and Contributions

    This chapter addresses four interrelated questions from a European policy perspective:

    1. Where does Europe stand? How have patent share, innovation quality (citations, generality, originality), and knowledge network positioning evolved across the five major competing regions from 2014 to 2024?

    2. Why is Europe losing ground? What institutional, strategic, and capability factors explain Europe's decline in six of seven technology domains and its last-place ranking in citation quality despite second-highest patent volume?

    3. What drives competitors' success? How do the US's software dominance, China's consumer electronics business model, and Korea's focused battery excellence succeed through fundamentally different approaches—and what constraints do they face?

    4. What pathways remain open to Europe? Given Europe's capability endowments, institutional structures, and competitors' positioning, what strategic imperatives and policy interventions offer realistic prospects for competitive renewal?

    We provide European policymakers and industry leaders with:

    - Comprehensive competitive diagnosis: Patent share, quality metrics (forward citations, generality, originality indices), cross-border collaboration rates, and knowledge flow networks across seven technology domains and 11 years

    - Theoretical interpretation: Analysis grounded in Resource-Based View, National Innovation Systems, Disruptive Innovation theory, and Open Innovation frameworks, explaining how regional capabilities, institutional arrangements, and business models generate observed patent patterns

    - Strategic intelligence on competitors: Deep examination of China's "EVs as consumer electronics" strategy, Korea's battery dominance despite smaller industrial base, and US software concentration—revealing their asymmetric advantages and structural vulnerabilities

    - Actionable strategic pathways: Recommendations prioritizing defensible domains (thermal management, safety systems), strategic alliances (EU-Korea batteries, EU-US software), differentiation strategies (privacy, sustainability), and necessary strategic triage (abandoning unwinnable battles in infotainment)

    ## Methodology Overview

    Our analysis integrates multiple analytical approaches to construct a comprehensive portrait of EV innovation competition:

    Patent Data Foundation: We analyze Google's Public Patent Dataset, examining 385,000+ patents filed 2014-2024 by inventors and assignees from the five major regions. Patents are categorized into seven core EV technology domains using Cooperative Patent Classification (CPC) codes: Battery Technology (H01M, H01G11), EV Propulsion & Charging (B60L, H02K, H02P, H02J7, H02M), Autonomous Driving (B60W, G05D1), Hybrid & Energy Management (B60K6, B60W20, F02D), Safety & ADAS (B60R, B60Q, G08G), Thermal Management (B60H, F28D), and Infotainment & Connectivity (B60K35, B60K37, H04W4, G07C5, H04N7/18).

    Methodological Overview: We count patents by assignee/inventor country rather than patent office location, capturing "export-quality" innovation. We assess quality through forward citations, generality indices, and originality indices. We analyze cross-border collaborative patents and knowledge flow networks through citation patterns. Complete methodology details appear in Appendix A.

    ## Chapter Structure

    Following this Introduction, Section 2 presents the theoretical framework integrating Resource-Based View, Disruptive Innovation theory, National Innovation Systems, Open Innovation paradigms, and Business Model Innovation perspectives that inform our analysis.

    Section 3 examines the five-region patent race, analyzing aggregate trends and domain-specific patterns revealing distinct strategic approaches and Europe's comprehensive erosion across six of seven technology domains.

    Section 4 investigates cross-border collaboration, documenting the vanishingly low collaboration rates (0.65-1.28%) and the geopolitical collapse of US-China joint innovation.

    Section 5 analyzes patent quality through forward citations, generality, and originality indices, revealing Europe's last-place ranking despite second-highest volume and the software-hardware quality divide favoring US autonomous driving and infotainment patents.

    Section 6 maps knowledge flow networks via citation patterns, uncovering China's counterintuitive openness (21.2% self-citation), the EU-US dominant knowledge axis (13,139 citations in 2023), and the -64% to -70% US-China bilateral collapse since 2021.

    Section 7 provides a deep case study of China's "EVs as consumer electronics" strategy, examining how China's business model innovation—rapid iteration, ecosystem integration, volume-based cost reduction—challenges traditional automotive paradigms despite modest patent quality and selective domain focus.

    Section 8 translates empirical findings into strategic imperatives for Europe, identifying four priority actions (anchor in defensible domains, forge strategic alliances, differentiate on privacy/sustainability, accept strategic triage) and exploring three alternative futures for 2030 with robust strategies across scenarios.

    Section 9 concludes by synthesizing Europe's strategic positioning and the urgency of action. Appendices provide complete methodology documentation (Appendix A) and technical glossary (Appendix B).

    The window for European strategic renewal remains open, but it narrows with each passing quarter. The next five years will determine whether Europe's automotive leadership—built over more than a century—continues into the electric era, or whether the EV transition marks the end of European automotive dominance and the beginning of dependence on US software platforms and Asian battery supply chains.
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

    First, Korea's emergence as a peer competitor: Korea's patent share overtook Japan in 2021 (19.0% vs. 18.7%) and surged to 21.6% in 2022, nearly matching the EU's 21.5%. By 2023, Korea maintained near-parity with the EU (20.5% vs. 20.2%). This trajectory reflects concentrated industrial policy (targeting batteries), chaebols' capacity for rapid capability building (Samsung SDI, LG Energy Solution), and strategic focus on specific high-value domains rather than comprehensive automotive coverage. Deliberate accumulation of battery manufacturing capabilities—rare, valuable, and difficult to imitate—provides sustainable competitive advantage in the EV value chain's most critical component.

    Second, the US patent share anomaly of 2021-2023: US share declined from 27.8% (2021) to 25.5% (2022) before recovering to 27.1% (2023) and surging to 29.3% in partial-year 2024 data. This U-shaped pattern contradicts narratives of consistent US dominance. We interpret this as evidence of technology S-curve dynamics in autonomous driving and infotainment—domains where the US concentrates investment. The 2022 dip likely reflects a consolidation phase following rapid patent growth in 2019-2021 (the "hype cycle" in autonomous driving), with subsequent recovery indicating maturation of commercially viable technologies. This pattern illustrates how disruptive innovation trajectories exhibit non-linear dynamics distinct from sustaining innovation's predictable progression.

    Third, China's persistent 13-16% share: Despite policy prioritization and massive subsidies, China's overall patent share remains modest (13.4% in 2021, 14.2% in 2023), contradicting expectations of rapid dominance. This apparent paradox resolves when examining domain-specific patterns (Figure 2), revealing China's strategic selectivity—overwhelming focus on batteries rather than comprehensive coverage. This reflects state-directed concentrated resource deployment in targeted domains (batteries, where China reached 21% share by 2023) rather than distributed investment across all EV technologies. The consumer electronics business model—emphasizing rapid iteration and cost reduction over technological breadth—prioritizes commercialization speed in selected domains over patent leadership across the board.

    ### Domain-Level Analysis: Explaining the Aggregates

    The domain breakdown (Figure 2) provides essential context for interpreting overall trends, revealing how aggregate patterns emerge from distinct technology-specific trajectories shaped by regional resource endowments.

    Battery Technology: Korea's Hidden Dominance and China's Acceleration

    Korea's battery patents constitute 29-33% global share (2020-2023)—the highest among all five regions—explaining Korea's overall patent share surge. This dominance reflects decades of capability accumulation in consumer electronics batteries (Samsung, LG), transferred to EV applications through complementary asset deployment (Teece, 2010). China's battery share grew from 16% (2020) to 21% (2023), representing state-directed capability building through subsidized gigafactories (CATL, BYD) and raw material supply chain control. Battery capabilities are path-dependent, accumulated over decades, and not easily replicated—explaining why US (15-16%) and EU (13-15%) struggle despite recent policy focus.

    The EU-Korea battery gap (33% vs. 13% in 2023) is particularly concerning from a European policy perspective. While the EU possessed comparable battery share to Korea in 2014-2016, Korea's focused industrial policy—concentrating R&D in battery chemistry, manufacturing processes, and cost reduction—generated capabilities the EU's fragmented, multi-country approach could not match. This exemplifies how National Innovation Systems' institutional coherence (Korea's coordinated chaebol-government model) can outperform larger but fragmented systems (EU's 27 national programs).

    **Box 1: Patents vs. Market Share—The Korea-China Battery Paradox**

    Korea's 31-33% battery patent share contrasts sharply with its manufacturing market position. In 2023 global EV battery installations, Chinese manufacturers dominated with CATL (36.8% market share) and BYD (15.8%), totaling approximately 53% combined market share. Korean battery makers—LG Energy Solution (13.6%), SK On (4.9%), and Samsung SDI (4.6%)—held approximately 23% combined (CnEVPost, 2024; SNE Research, 2024). China thus leads battery *production* (53% vs. 23%) while Korea leads battery *innovation* (33% vs. 21% patent share).

    This patent-market gap illustrates the distinction between innovation leadership (R&D capabilities, technological advancement) and commercialization dominance (manufacturing scale, cost reduction). Patents are leading indicators of future competitiveness—today's R&D investments become tomorrow's products, typically with 5-10 year lag times. Korea's patent advantage reflects decades of consumer electronics battery expertise (LG Chem, Samsung SDI) systematically transferred to EV applications, with Korean firms accounting for 29% of the top-10 battery patent holders' total strength (IAM Media, 2023).

    However, China rapidly closes the innovation gap. Chinese battery patent share surged from 16% (2020) to 21% (2023)—a 5-percentage-point gain in three years driven by CATL and BYD's massive R&D investments (each receiving $2+ billion annually in state support). If this acceleration continues, China could challenge Korea's patent leadership by 2027-2028, potentially translating manufacturing dominance into innovation leadership. This presents a future strategic challenge for Korean battery makers: maintaining R&D advantage becomes critical for premium positioning and next-generation technology leadership (solid-state batteries, silicon anodes) as Chinese competitors scale both production *and* innovation capabilities simultaneously.

    The Korea-China battery dynamic thus exemplifies business model competition: Korea's R&D-intensive model (high patent output, premium products, smaller scale) versus China's state-directed scaling model (lower patent intensity but massive manufacturing, rapid catch-up in R&D). The crucial question: Can Korea's innovation advantage sustain competitive positioning as China masters both cost leadership *and* technological advancement?

    Autonomous Driving: US Software Dominance and the EU-Japan Paradox

    US autonomous driving leadership (32-35%) reflects Silicon Valley's software engineering ecosystem—university-industry linkages (Stanford-Waymo), venture capital availability, and AI talent concentration. China's persistent weakness (8-9%) contradicts industrial policy narratives, suggesting autonomous driving requires software capabilities distinct from batteries' manufacturing-intensive model. Japan's stable 20-21% share—comparable to the EU's 20-22%—despite Japan's traditional automotive strength, reveals that mechanical engineering excellence does not automatically translate to software-defined vehicle competencies. Incumbent capabilities in ICE vehicles provide limited advantage in autonomous systems requiring different knowledge bases.

    Infotainment: Korea's Surge and the Digital Divide

    Korea's infotainment patent share surged from 16% (2020) to 21% (2022), likely reflecting Samsung's and LG's consumer electronics DNA—treating vehicle dashboards as smartphone-derived product categories. The US maintains dominance (35-38%), but Korea's rapid growth suggests successful capability transfer from consumer electronics. China's stability (14-16%) and the EU's weakness (14%) reveal strategic positioning differences: Korea and China treat infotainment as extension of existing consumer electronics capabilities, while EU automakers view it as subsidiary to core vehicle engineering—a framing that disadvantages them in software-defined vehicle competition.

    ### Institutional Explanations: Why Regions Diverge

    These patent patterns reflect fundamentally different National Innovation Systems responding to EV transition:

    Korea's focused excellence model: Concentrated industrial policy targets specific high-value domains (batteries, displays), with chaebol coordination enabling rapid capability building. Success in batteries and infotainment illustrates this approach's effectiveness, while weakness in autonomous driving (15-16%) reveals its selectivity. Korea demonstrates that smaller innovation systems can achieve peer-competitor status through strategic focus rather than comprehensive coverage.

    China's dual-track strategy: State-directed battery dominance (infrastructure control) combined with consumer electronics-inspired infotainment focus (user experience differentiation), while accepting weakness in autonomous driving (8-9%). This reflects business model innovation—treating EVs as fast-moving consumer goods requiring battery supply chains and digital experiences, not comprehensive automotive engineering. The modest overall patent share (13-14%) masks strategic selectivity: China prioritizes commercialization and cost reduction over patent breadth.

    US software-first positioning: Market-driven innovation system concentrates resources in software domains (autonomous, infotainment) where venture capital and tech talent provide advantage, while accepting battery gap (15-16%). The 2022 patent share dip suggests technology maturation cycles in software domains exhibit different dynamics than manufacturing-intensive technologies.

    EU's incumbent challenge: Fragmented 27-country innovation system struggles to concentrate resources, leading to moderate positions across most domains (20-22%) but excellence in traditional engineering (thermal management, safety). This pattern exemplifies the innovator's dilemma: existing capabilities create organizational and institutional resistance to radical resource reallocation toward software domains.

    Japan's hybrid identity: Maintaining comparable patent shares to the EU across most domains (autonomous 21%, infotainment 15%, batteries 18%) despite smaller industrial base suggests persistent automotive engineering excellence. However, similarity to EU patterns—strength in traditional domains, weakness in software—indicates shared incumbent challenges during disruption.

    ### Strategic Implications: Resource Endowments and Competitive Positioning

    These patterns reveal that regional competitiveness in the EV era depends not on aggregate patent volumes but on strategic alignment between resource endowments, institutional capabilities, and technology domain prioritization:

    - Korea's success demonstrates that focused capability building in high-value domains (batteries) can generate peer-competitor status despite smaller overall innovation systems
    - China's approach shows that consumer electronics business models—rapid iteration, cost focus, selective technology investment—can challenge automotive incumbents even without comprehensive patent leadership
    - US volatility suggests software-defined vehicle technologies exhibit different innovation dynamics than mechanical engineering, requiring different policy approaches
    - EU's dilemma illustrates how excellence in declining technologies (hybrids, thermal management) can coexist with dangerous gaps in emerging domains (software, batteries), demanding urgent strategic reorientation
    - Japan's trajectory mirrors EU challenges, suggesting shared incumbent disadvantages during disruptive transitions

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

    The erosion is comprehensive, not selective. Between 2014 and 2023, EU patent share declined in six of seven technology domains: autonomous driving (-12.2 percentage points, from 32.4% to 20.2%), thermal management (-7.3pp, from 40.5% to 33.2%), infotainment (-5.2pp, from 18.7% to 13.5%), battery technology (-5.1pp, from 17.8% to 12.7%), safety systems (-3.8pp, from 35.9% to 32.1%), and propulsion (-2.9pp, from 28.3% to 25.4%). Only hybrid powertrains grew modestly (+1.2pp, from 32.2% to 33.4%)—precisely the domain with declining market relevance as the industry shifts from hybrid to pure electric vehicles.

    The EU's sole growth domain—hybrids—represents sustaining innovation in declining technology, while competitors capture emerging domains. The EU strengthens capabilities the market is abandoning while losing ground in technologies defining future competitiveness. Thermal management—often cited as European strength—declined from 40.5% (2014) to 33.2% (2023), demonstrating that even path-dependent, difficult-to-replicate capabilities (Barney, 1991) erode without strategic investment during disruptive transitions.

    Contrasting the EU's diffuse decline with Korea's targeted ascent (analyzed in Figures 1-2) reveals the cost of institutional fragmentation. Korea's coordinated system—chaebols, government, and research institutions—concentrated resources in batteries (achieving 32-33% share) and infotainment (surging to 21%), accepting weakness in autonomous driving (15-16%). This strategic selectivity generated peer-competitor status despite Korea's smaller industrial base. The EU's 27 fragmented national programs, conversely, spread resources thinly across domains, achieving moderate capabilities nowhere and excellence only in declining technologies.

    The autonomous driving collapse (-12.2pp, the steepest decline) reveals divergent responses to software-intensive technologies. The US market-driven system (venture capital, university-industry linkages) achieved 32-35% autonomous driving share through bottom-up experimentation. China's state-directed approach struggled (8-9%) despite industrial policy, revealing that command-and-control systems excel at manufacturing-intensive domains (batteries) but not software innovation requiring decentralized creativity. The EU's coordinated market economy—relying on consensus among established automakers—proves especially ill-suited: fragmented across 27 countries, lacking pan-European platforms, and constrained by incumbent resistance to radical resource reallocation away from mechanical engineering toward software capabilities.

    Connecting to earlier analysis: Figures 1-2 demonstrated that Korea's focused battery dominance (33%) generates more strategic value than the EU's moderate capabilities across multiple domains (20-25%). Figure 3 reveals why: the EU's multi-domain approach dilutes resources without achieving critical mass in any single high-value domain. While Korea deliberately built rare, valuable, inimitable capabilities in batteries, the EU's fragmented system prevents such concentration. The result resembles neither focused excellence (Korea) nor selective strategic positioning (China's dual battery-infotainment strategy) but rather slow erosion across the board—a coordination failure during rapid technological transitions.

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

    Figures 4A-C reveal a striking pattern: EV innovation remains overwhelmingly insular despite globalization narratives. Across the 2014-2024 period, collaborative patents (those with co-inventors or assignees from multiple regions) constitute only 0.65-1.28% of total patents (Figure 4A). The collaboration rate peaked at 1.28% in 2018, declined to 0.87% by 2021, recovered slightly to 0.93% in 2022, then declined to 0.89% in 2023 and 0.65% in partial-year 2024 data. This contrasts with expectations of increasing cross-border knowledge flows in complex technological systems.

    Three explanations emerge from our theoretical frameworks:

    First, institutional divergence creates friction for collaboration. China's state-directed system, the US market-driven venture capital model, and the EU's coordinated market economy operate under fundamentally different R&D funding mechanisms, intellectual property norms, and industry-government relationships. Cross-border collaboration requires bridging these institutional gaps—a transaction cost that may exceed collaboration benefits for most patent-generating activities.

    Second, strategic competition in EV technologies—particularly batteries and software—generates incentives for proprietary knowledge protection rather than open sharing. Firms protect rare, valuable, inimitable capabilities. With battery technology determining supply chain control and software defining consumer experiences, regions treat EV innovation as strategically sensitive, limiting collaboration with potential competitors.

    Third, technology complexity may not require collaboration when regions possess comprehensive capabilities. Korea's focused battery excellence and the US software dominance reflect self-sufficient capability concentrations. Only when complementary capabilities reside in different regions (e.g., EU thermal management + Korean batteries) does collaboration become strategically necessary.

    ### EU as Collaboration Hub: Structural Position vs. Strategic Value

    Despite low overall collaboration, Figure 4B reveals that the EU participates in the two largest collaboration pairs: EU-JP (5,410 patents total 2014-2024) and EU-US (4,966 patents total), together accounting for the majority of all cross-border collaboration. In 2023, EU-JP collaboration yielded 172 patents and EU-US totaled 215 patents. The EU also maintains significant partnerships with China (EU-CN: 2,167 total). The EU thus appears as a "collaboration hub"—engaging intensively with both US software capabilities and Asian battery/electronics expertise.

    However, interpreting this positively requires caution. The EU's high collaboration rate may reflect weakness rather than strength. Network theory distinguishes between hub position (many connections) and knowledge brokerage (controlling information flows between otherwise disconnected actors). The EU collaborates with US, Japan, and China, but these regions increasingly collaborate bilaterally: US-JP partnerships remained significant (328 patents in 2014, peaking at 453 in 2019, declining to 299 in 2023); US-CN collaboration surged from 273 (2014) to a peak of 562 (2020) before geopolitical tensions drove collapse to 135 (2023), a 76% decline from peak.

    The EU's collaboration patterns reflect complementary capability needs: EU automakers partner with US tech firms for software (EU-US) and Japanese suppliers for hybrid/safety systems (EU-JP, the largest collaboration pair globally). China-Japan collaboration (CN-JP: 1,274 total patents) also features prominently, particularly in infotainment technologies. The EU's multi-directional dependency—engaging with both US and Asian partners across multiple technology domains—contrasts with more selective bilateral patterns elsewhere. The EU's hub position thus signals fragmented capabilities requiring external partnerships, while competitors' selectivity reflects self-sufficiency in core domains.

    ### Domain-Specific Collaboration: Where Openness Emerges

    Figure 4C's domain analysis reveals that collaboration rates vary dramatically across technologies, supporting the Resource-Based View's prediction that firms collaborate when complementary capabilities reside in different regions:

    Battery Technology shows the highest collaboration rate among all domains, peaking at 1.80% in 2016 and averaging around 1.4-1.6% in recent years. This reflects geographic separation of battery value chain components: Korean and Japanese firms lead cell manufacturing, European companies excel in thermal management systems, and US firms contribute battery management software. Collaborative patents in batteries often involve EU-Korean partnerships (188 patents in 2014, stabilizing around 40-60 in recent years) combining European safety engineering with Korean cell technology.

    Autonomous Driving shows the second-highest collaboration rate, peaking at 1.71% in 2018, concentrated in EU-US partnerships (58-103 patents across most years) and EU-JP collaboration (surge to 269 patents in 2019). The US dominance in autonomous driving (32-35% patent share) creates natural collaboration patterns where EU and Japanese automakers partner with US tech firms (Waymo, Mobileye) for self-driving systems. Japan's EU-JP collaboration surge in 2018-2019 (246-269 patents) likely reflects established automotive relationships adapting to ADAS integration.

    Infotainment & Connectivity exhibits moderate collaboration rates, peaking at 1.49% in 2018, especially notable given software's typically proprietary nature. The EU-US collaboration in infotainment (333 patents in 2014, declining but still 127 in 2020) suggests European automakers source digital experience capabilities from US tech firms. The decline from 333 (2014) to 127 (2020) to 39 (2023) may indicate either: (1) European capability building reducing dependence, or (2) strategic shift toward proprietary platforms (e.g., Volkswagen's VW.OS, Mercedes' MBOS).

    Thermal Management, Safety, and Hybrid Powertrains exhibit the lowest collaboration rates, all below 1.5%. Safety systems peaked at 1.21% (2022), hybrid powertrains at 1.10% (2017), and thermal management at 0.96% (2018). These mature engineering domains with established supply chains generate minimal cross-border co-invention. Thermal management's low collaboration despite EU leadership suggests European capabilities are self-sufficient. Safety systems' insularity reflects standardization—once regulatory requirements are defined, regional innovation becomes independent.

    ### The US-China Collaboration Collapse: Geopolitics Overriding Complementarity

    The most dramatic pattern in Figure 4B is the US-CN collaboration collapse: rising from 273 patents (2014) to 562 (2020) before plummeting to 135 (2023)—a 76% decline coinciding with trade tensions and technology export controls. This collapse occurred despite strong complementary capabilities, providing evidence that geopolitical factors can override economic complementarity in shaping innovation networks. Notably, EU-CN collaboration declined far less severely (45%), suggesting the EU's intermediate position enables hedging between US alliance and Chinese market access. Section 6 examines these geopolitical dynamics through knowledge flow analysis.

    ### Strategic Implications: Collaboration as Competitive Advantage?

    Our findings challenge simplistic narratives equating collaboration with innovation leadership. The data reveal three distinct collaboration strategies:

    Korea's selective excellence: Minimal collaboration outside batteries (primarily EU-KR), reflecting self-sufficient capabilities in chosen domains. Collaboration rate remains below 2% overall, concentrated in battery partnerships. This supports strategic focus—Korea collaborates only when accessing complementary capabilities (EU thermal management), not broadly.

    China's decreasing openness: Despite rhetoric of "open innovation," China's collaboration rate declined from 2.5% (2016) to 1.8% (2023). The US-CN collapse dominates this trend, but EU-CN and CN-JP also declined. This suggests China's growing self-sufficiency: as battery and infotainment capabilities matured, dependence on external knowledge decreased. The consumer electronics business model emphasizes rapid internal iteration over collaborative development.

    EU's dependent openness: Highest absolute collaboration volumes (EU-US, EU-JP, EU-KR all in top 6 pairs), but this reflects fragmented capabilities requiring external partnerships. The EU collaborates in batteries (EU-KR), software (EU-US), and hybrid systems (EU-JP)—precisely the domains where it lags in independent patent share. This pattern illustrates the innovator's dilemma: established automotive players seek partnerships to access disruptive capabilities they failed to develop internally.

    US strategic ambivalence: Historically collaborative (EU-US, US-JP, US-CN all major pairs), but the China decoupling reveals willingness to sacrifice collaboration for geopolitical objectives. Post-2020 data suggest the US increasingly relies on domestic software capabilities (Silicon Valley ecosystem) while selectively partnering with allies (EU, Japan, Korea) for hardware/manufacturing.

    ### The Open Innovation Paradox: Why EVs Remain Closed

    The low collaboration rates (0.65-1.28%) documented in Figure 4A contradict expectations that complex technologies drive external knowledge sourcing. Three factors explain this paradox:

    1. Winner-take-all dynamics: EV technologies (batteries, software) exhibit increasing returns to scale. Firms compete for dominant platforms (Tesla's Supercharger network, China's CATL battery hegemony) rather than sharing knowledge. Collaboration risks creating competitors.

    2. Institutional barriers: National security reviews (CFIUS in US, EU merger control), export controls, and intellectual property disputes raise collaboration costs. The 18-month patent publication delay creates asymmetric information—partners may exploit knowledge before protection.

    3. Vertical integration strategies: Tesla's model of in-house batteries, software, and manufacturing directly contradicts open innovation. Chinese EV makers (BYD, NIO) similarly pursue vertical integration. This suggests EV business models favor control over collaboration.

    Open innovation may apply within regional clusters but not between competing national systems. Silicon Valley exhibits openness through talent mobility and startup collaboration, but US-China knowledge flows face state-imposed barriers.
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
    ## Citation-Based Quality Metrics

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
def _(alt, citation_by_region_year, region_colors, region_shapes):
    # Figure 5A: Average Forward Citations by Region (2014-2024)
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

    fig5a = (_cit_solid + _cit_dashed).properties(
        width=700,
        height=400,
        title=alt.Title(
            'Figure 5A: Average Forward Citations by Region (2014-2024)',
            subtitle='Patents require 5-7 years to accumulate citations. Declining trends after 2019 reflect citation lag, not quality decline. Dashed lines indicate incomplete 2024 data.',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    fig5a
    return


@app.cell(hide_code=True)
def _(alt, citation_data, region_colors, region_shapes):
    # Figure 5B: Citation Quality by Domain (2014-2018 only)
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
            'Figure 5B: Citation Quality by Technology Domain (2014-2018)',
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
    ### The US Quality Advantage: 2.4-3.6× Higher Citation Impact

    Figure 5A reveals a stark quality hierarchy. Using 2014-2018 data (patents with 6-10 years to accumulate citations), the US achieves 8.87 average citations per patent—2.4× to 3.6× higher than all other regions. Korea ranks second (3.77 citations), followed by Japan (3.45), China (3.31), and the EU last (2.50 citations).

    This finding contradicts volume-based rankings. The EU files the second-highest patent volume (288,520 patents in 2014-2018), yet generates the lowest per-patent impact. This volume-quality paradox suggests the EU pursues a defensive patenting strategy—filing many incremental patents to protect existing products—rather than investing in foundational research that others build upon. The US quality advantage persists consistently across the full time series where citation data is mature.

    ### Software-Hardware Quality Gap

    Figure 5B's domain analysis exposes the software-hardware quality divide. Software-centric domains generate far higher citations than hardware domains (software knowledge is more reusable across applications):

    High-citation software domains (2014-2018 averages):
    - Autonomous Driving & ADAS: US 14.50, CN 5.91, KR 5.21, JP 4.81, EU 3.73
    - Infotainment & Connectivity: US 12.09, KR 5.34, JP 4.34, EU 3.48, CN 2.86
    - Vehicle Safety Systems: US 8.95, JP 4.11, KR 3.81, CN 2.97, EU 2.39

    Lower-citation hardware domains:
    - Thermal Management: US 5.21, JP 2.89, KR 2.78, CN 2.08, EU 1.63
    - Hybrid Powertrains: US 5.23, CN 2.43, KR 2.16, JP 1.81, EU 1.42
    - Battery Technology: US 7.69, KR 3.63, CN 3.48, JP 3.24, EU 2.55

    This pattern holds strategic significance: the highest-quality innovation occurs in software domains where the EU is weakest. Autonomous driving patents receive 2-3× more citations than thermal management patents, yet the EU holds only 31% of autonomous patents versus 44% of thermal patents (from Section 3 data). The EU invests R&D in lower-impact domains while lagging in high-impact areas.

    ### EU's Quality Crisis: Weak Even in Traditional Strengths

    Figure 5B reveals the EU's most troubling pattern: ranking last in 6 of 7 technology domains, including traditional automotive strengths:

    - Safety Systems: EU 2.39 citations (5th of 5 regions, despite 47% patent share from Section 3)
    - Thermal Management: EU 1.63 citations (5th of 5, despite 44% share)
    - Hybrid Powertrains: EU 1.42 citations (5th of 5, despite 50% share)

    This finding challenges the "European engineering excellence" narrative. While EU companies maintain volume leadership in traditional domains, their patents generate minimal follow-on research. Possible explanations include:

    1. Incremental innovation focus: EU patents improve existing technologies (better thermal systems, optimized hybrids) rather than enabling new capabilities
    2. Product-specific IP: Patents tied to specific vehicle models, not reusable platforms others can build on
    3. Declining relevance: Traditional domains (hybrids, thermal) become less central to EV value creation, attracting less researcher attention

    The US dominates quality across ALL domains, even hardware areas where EU holds volume advantages. In thermal management, US patents (5.21 citations) generate 3.2× more impact than EU patents (1.63) despite the EU filing 44% of thermal patents versus US 17% (Section 3 data). This inversion—EU volume leadership producing minimal citation impact—epitomizes the quality crisis.

    ### Korea's Battery Paradox: High Volume, Moderate Quality

    Korea's battery patents present an interesting anomaly: highest volume (31% share) but moderate citation quality (3.63 citations, 2nd of 5), with US battery patents (7.69) generating 2.1× more impact. For detailed analysis of this patent-market gap, see Box 1, Section 3.

    ### Theoretical Implications

    The US innovation system emphasizes university-industry collaboration (Stanford-Silicon Valley, MIT-Route 128), producing foundational research published and cited widely. EU systems emphasize industry-led applied research, generating proprietary knowledge with narrower applicability. China's system prioritizes rapid commercialization over academic citation networks.

    Software innovations are more citation-intensive because knowledge is less tacit than hardware engineering. Autonomous driving algorithms can be described, published, and adapted across contexts (high citations). Battery chemistry knowledge involves undocumented manufacturing expertise (lower citations despite importance).

    EU patents may receive fewer citations because they improve sustaining technologies (better combustion engines → hybrids) while US/China patents target disruptive shifts (BEV architecture, software-defined vehicles). Sustaining innovations serve existing customers; disruptive innovations create new markets and research trajectories—hence higher citations.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Methodological Note: Citations as One Quality Dimension

    Forward citations measure one dimension of innovation quality: the extent to which a patent generates follow-on research by other inventors. This metric favors foundational, platform-enabling technologies over incremental improvements or product-specific innovations. Citations do not capture all forms of knowledge transfer.

    As documented in Section 4, the EU maintains the highest cross-border collaboration rates (2.59% of portfolio vs. 1.90% US, 2.16% JP, 3.20% CN, 0.66% KR). This suggests knowledge also flows through direct partnerships, joint ventures, and complementary capability exchanges. However, collaboration intensity does not fully offset citation gaps—the EU ranks highest in collaboration yet lowest in citations.

    Our interpretation: High-quality innovation requires both breakthrough research (citations) and collaborative capability exchange (partnerships). The US excels at both; the EU emphasizes collaboration but lags in foundational research generation. China prioritizes volume and rapid deployment over either citations or partnerships.

    Citations should thus be interpreted alongside collaboration patterns (Section 4), patent volume (Section 3), and generality/originality indices (Section 5.2) to provide a complete picture of innovation strategies. The next section examines patent quality through the lens of knowledge breadth and diversity.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Generality & Originality Indices: Knowledge Breadth and Diversity

    Forward citations (Section 5.1) measure how frequently other inventors reference a patent. Generality and originality indices provide complementary quality dimensions:

    - Generality Index: Measures the breadth of a patent's technological impact—does it influence only its own narrow field, or does it enable innovation across diverse technology domains? (0-1 scale, higher = broader cross-domain influence)

    - Originality Index: Measures the diversity of knowledge sources a patent draws upon—does it build on narrow prior art, or synthesize insights from multiple technology areas? (0-1 scale, higher = more diverse knowledge integration)

    These Hall-Jaffe-Trajtenberg indices (Hall et al., 2001) distinguish foundational innovations (high generality/originality) from incremental improvements (low scores). A patent scoring 0.80+ on both metrics typically represents architectural breakthroughs enabling broad follow-on research; patents below 0.55 suggest domain-specific optimization.
    """
    )
    return


@app.cell(hide_code=True)
def _(pd):
    # Data loading: Generality & Originality Indices (5 regions × 7 domains = 35 rows)
    generality_data = pd.read_csv('data/06_generality_originality_indices.csv')
    return (generality_data,)


@app.cell(hide_code=True)
def _(alt, generality_data, region_colors, region_shapes):
    # Figure 5C: Small multiples scatter plots (7 domains)
    # Each panel shows generality vs. originality for 5 regions within one domain
    # Size encodes patent volume

    _scatter_data = generality_data.copy()

    # Create scatter plot with size encoding for patent volume
    _scatter_chart = alt.Chart(_scatter_data).mark_point(
        filled=True,
        opacity=0.8
    ).encode(
        x=alt.X('avg_generality:Q',
                title='Generality Index',
                scale=alt.Scale(domain=[0.45, 0.85]),
                axis=alt.Axis(labelFontSize=9, grid=True, gridOpacity=0.2)),
        y=alt.Y('avg_originality:Q',
                title='Originality Index',
                scale=alt.Scale(domain=[0.50, 0.90]),
                axis=alt.Axis(labelFontSize=9, grid=True, gridOpacity=0.2)),
        color=alt.Color('region:N',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_colors[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=alt.Legend(orient='bottom', titleFontSize=11, labelFontSize=10, columns=5, title='Region')),
        shape=alt.Shape('region:N',
                       scale=alt.Scale(
                           domain=['US', 'EU', 'CN', 'JP', 'KR'],
                           range=[region_shapes[r] for r in ['US', 'EU', 'CN', 'JP', 'KR']]
                       ),
                       legend=None),
        size=alt.Size('patent_count:Q',
                     scale=alt.Scale(range=[80, 400]),
                     legend=None),
        tooltip=[
            alt.Tooltip('region:N', title='Region'),
            alt.Tooltip('application_area:N', title='Domain'),
            alt.Tooltip('avg_generality:Q', title='Generality', format='.3f'),
            alt.Tooltip('avg_originality:Q', title='Originality', format='.3f'),
            alt.Tooltip('patent_count:Q', title='Patents', format=','),
            alt.Tooltip('avg_citing_classes:Q', title='Citing Classes', format='.1f'),
            alt.Tooltip('avg_cited_classes:Q', title='Cited Classes', format='.1f')
        ]
    ).properties(
        width=210,
        height=160
    ).facet(
        facet=alt.Facet('application_area:N', title=None,
                       header=alt.Header(labelFontSize=11, labelLimit=200)),
        columns=3
    ).properties(
        title=alt.Title(
            'Figure 5C: Patent Quality - Generality vs. Originality by Technology Domain',
            subtitle='Each panel shows one technology domain with 5 regions. Point size indicates patent volume. US consistently upper-right (foundational); Korea batteries lower-left (incremental).',
            fontSize=14,
            anchor='start'
        )
    ).configure_view(strokeWidth=0)

    _scatter_chart
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Interpreting Generality and Originality Through Theoretical Lenses

    Before examining regional patterns, we must clarify what these Hall-Jaffe-Trajtenberg indices actually measure. Generality and originality capture cross-domain knowledge integration, not absolute technical quality. A patent scoring 0.80 in generality draws prior art from diverse technology classes and enables follow-on innovation across multiple domains—emerging from knowledge-based (rather than manufacturing-based) competitive advantages. Conversely, patents scoring 0.50 remain confined to narrow technical domains, often reflecting *sustaining innovations*: incremental improvements within established trajectories rather than architectural breakthroughs creating new innovation paths.

    This distinction matters because low-generality patents can generate enormous commercial value through manufacturing excellence and process optimization—Korea's battery dominance demonstrates this. The metrics reveal *how* regions innovate (cross-domain integration vs. domain-specific optimization), not whether their innovations succeed commercially. University-industry collaboration ecosystems produce high-generality research crossing disciplinary boundaries, while industry-led applied research systems generate domain-confined knowledge serving specific product markets.

    We verified these patterns reflect real phenomena rather than measurement artifacts. US patents average 8.4-11.0 citing classes across technology domains—1.6-2.1× higher than EU's 4.5-6.0 range. We tested whether this gap stems from CPC classification bias (US patent examiners assigning more technology codes per patent). BigQuery analysis reveals US patents average 2.63 CPC codes versus EU's 2.41 (9% difference)—far too small to explain the 60-110% gap in citing classes. The cross-domain integration advantage is real.

    ### Domain-Specific Specialization Patterns

    Figure 5C's domain-by-domain analysis reveals regional specialization rather than simple hierarchy. Technology domains exhibit two distinct patterns. Convergent technologies—those where all regions achieve comparable scores—suggest globally-shared knowledge accumulated over decades. Hybrid powertrains exemplify this: regional scores cluster tightly (0.663-0.790 generality), with Korea (0.790), Japan (0.780), and China (0.770) matching or exceeding the US (0.763). This convergence reflects 20+ years of global hybrid development since the 1997 Toyota Prius, creating widely-diffused knowledge that becomes hard to sustain as competitive advantage. Notably, the EU ranks last (0.663) even in this mature domain, suggesting systematic difficulties translating engineering capabilities into cross-domain patent quality.

    Vehicle safety systems show similar convergence, with Korea leading (0.757 generality) followed closely by the US (0.752). This pattern aligns with Korea's broader competitive positioning: while battery patents score lowest (0.488 generality), safety system patents demonstrate how sensor-based innovations can achieve cross-domain impact. Korea's electronics heritage (Samsung, LG) provides complementary assets for integrating sensors, displays, and control systems—domains where manufacturing capabilities enhance rather than constrain knowledge breadth.

    Japan's leadership in infotainment (0.725 generality, highest among five regions) similarly reflects historical specialization. Despite US dominance in software, Japan ranks first by integrating consumer electronics heritage (Sony, Panasonic) with automotive systems. The US ranks third (0.677), suggesting Japan's decades of hardware-software-UX integration create patents drawing from diverse prior art classes. This finding challenges narratives positioning software expertise as universally superior—domain-specific knowledge accumulated over time can outperform cross-domain approaches when properly integrated.

    Divergent technologies exhibit wider quality gaps, with the US maintaining substantial leads. Autonomous driving produces the dataset's highest scores: US patents achieve 0.801 generality and 0.855 originality, drawing from 18.7 diverse prior art classes. The gap to second-place Japan (0.757) is significant. University-industry collaboration explains this: autonomous driving requires integrating computer vision, sensor fusion, machine learning, and control systems—precisely the interdisciplinary synthesis enabled by Stanford-Silicon Valley and MIT-Route 128 ecosystems. No other region possesses comparable institutional arrangements bridging multiple technical domains.

    Thermal management presents a surprising pattern. The US leads decisively (0.717 generality) with 9.3 citing classes—more than double the EU's 4.5, despite Europe's century of automotive engineering excellence. This finding suggests US thermal innovations integrate sensors, software controls, and system-level optimization approaches that generate cross-domain patents, while EU innovations remain confined to traditional mechanical engineering domains. US firms treat thermal management as a *systems integration* challenge requiring software capabilities, whereas EU firms approach it as a *component optimization* problem addressed through established engineering practices.

    ### Regional Innovation Strategy Patterns

    These domain-level patterns reveal distinct regional innovation strategies. The US demonstrates consistent cross-domain integration across all seven technology domains (weighted averages: 0.707 generality, 0.751 originality). The US leads in four domains and ranks top-three in all others, maintaining 8.4-11.0 citing classes regardless of technical area. This consistency suggests systematic institutional advantages rather than domain-specific expertise. National Innovation Systems theory attributes this to university-industry collaboration mechanisms: Stanford-Silicon Valley, MIT-Route 128, and similar ecosystems produce foundational research published in academic venues and cited across disciplinary boundaries. US autonomous driving patents (0.801/0.855) exemplify this, synthesizing computer vision, sensor fusion, machine learning, and control systems into innovations enabling applications far beyond vehicles.

    Japan and Korea pursue domain-specific excellence strategies (JP: 0.674/0.689; KR: 0.624/0.654 weighted averages). Rather than competing across all domains, both regions leverage historical specializations. Japan leads infotainment (0.725) and ranks second in hybrid powertrains (0.780), directly building on consumer electronics capabilities developed over 40+ years (Sony, Panasonic, Sharp) and automotive expertise (Toyota, Honda, Nissan). Korea leads vehicle safety systems (0.757) and ranks second in hybrids (0.790), extending sensor and display manufacturing strengths into automotive applications. Resource-Based View explains this: both regions convert tangible manufacturing assets into knowledge advantages within specific domains, demonstrating that specialized excellence can outperform generalist approaches when properly focused.

    However, Korea's battery paradox (see Box 1, Section 3) persists in generality metrics: 0.488/0.544 scores represent the dataset's absolute lowest despite Korea holding 31% global patent share, confirming incremental optimization focus rather than architectural innovation. Disruptive Innovation theory explains this: Korea's manufacturing-focused innovations serve existing markets through sustaining improvements, while foundational breakthroughs emerge from US research labs.

    China's pattern reveals strategic variance (0.571/0.602 overall). While ranking last in weighted averages, China shows deliberate focus: autonomous driving patents (0.705) approach EU levels, suggesting heavy investment in software domains where rapid learning is possible. Infotainment patents (0.506) score among the lowest, indicating acceptance of weaker performance where long knowledge accumulation is required. Disruptive Innovation theory predicts this pattern succeeds commercially: low-generality patents optimized for specific applications (affordable mass-market EVs) can disrupt established markets without matching incumbents' cross-domain capabilities. China prioritizes speed-to-market and manufacturing scale over foundational research breadth.

    The EU faces what we term "the generalist dilemma" (0.640/0.682). Figure 5C shows EU patents ranking 2nd-4th across all seven technology domains—solid performance everywhere, leadership nowhere. This middle-tier positioning (ahead of China/Korea, behind US/Japan) suggests a strategic challenge: the EU competes across all domains without choosing battles, spreading R&D resources thin. Contrast this with Japan's clear focus (consumer electronics-automotive fusion) or Korea's sensor/safety leadership. National Innovation Systems theory explains this through institutional fragmentation: the EU's 27 member states maintain separate research priorities and industrial policies, preventing the concentration of resources needed to achieve domain leadership. The EU demonstrates broad automotive engineering competence but lacks the focused specialization or cross-domain integration that creates competitive advantages in electric vehicle innovation.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Knowledge Flow Networks: Citation Patterns and Regional Openness

    Patent citations reveal how knowledge diffuses across regional boundaries. When a patent from region X cites a patent from region Y, it signals knowledge transfer: inventors in X built upon Y's prior art. Forward citations—the frequency with which subsequent patents reference a given patent—not only measure quality (Section 5.1) but also map knowledge flows between regions.

    This section analyzes citation flows using the knowledge flow networks dataset (1,921 rows covering 2014-2024, 5 regions, 7 technology domains). We examine three critical questions: Which regions remain insular versus open to external knowledge? Where do major knowledge flows concentrate? And how have geopolitical tensions disrupted knowledge exchange?
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
    ### China's Surprising Openness: Lowest Self-Citation Rate

    Figure 6A reveals a counterintuitive pattern: China exhibits the lowest self-citation rate among all five regions. Averaging across 2014-2024, Chinese EV patents cite their own region's prior art only 21.2% of the time—less than half the rates observed in the European Union (43.7%), South Korea (50.1%), United States (50.7%), and Japan (51.5%). Japan emerges as the most insular innovator, with over half of all citations remaining within Japanese patents.

    This finding contradicts narratives of Chinese technological isolation. State-directed innovation systems typically exhibit high self-citation emphasizing indigenous technology development. Yet China's patent citation patterns reveal extensive engagement with external knowledge, explained by capability gaps: Chinese firms cite US software patents and Japanese electronics research to compensate for weaker foundational R&D, actively absorbing global knowledge rather than relying solely on domestic sources.

    Temporal dynamics add nuance. China's openness increased dramatically from 2014 (32.0% self-citation) to 2018 (19.2%), then reversed partially by 2024 (30.7%). This U-shaped trajectory suggests initial rapid learning from global leaders (2014-2018), followed by gradual strengthening of domestic knowledge bases (2019+) as Chinese firms accumulated their own patent portfolios. Meanwhile, the US demonstrates steady opening: self-citation declined from 63.6% (2014) to 44.7% (2022), indicating American inventors increasingly cite foreign innovations—particularly in battery technology where Asian leadership is undeniable (Section 5.1).

    Korea's trajectory moves opposite: self-citation rose from 39.5% (2014) to 59.8% (2023), suggesting Korean battery and electronics firms increasingly reference their own extensive patent portfolios rather than external sources. This pattern aligns with Korea's dominance in battery patents (31% global share) documented in Section 3.

    ### The EU-US Knowledge Axis: Dominant Bilateral Flow

    Figure 6B maps the ten largest cross-regional knowledge flows in 2023. The EU-US bilateral relationship dominates global knowledge exchange: European patents cite US innovations 7,043 times, while US patents cite European research 6,096 times—totaling 13,139 citations. This bidirectional flow dwarfs all other pairs and reflects complementary strengths: US software/autonomous driving capabilities (60% patent share in infotainment, 55% in autonomous systems) combined with EU mechanical engineering and safety system expertise (Section 3 documentation).

    The next-largest flows involve the US as knowledge source: US→Japan (4,958 citations), US→Korea (4,014), and US→China (2,903). This centrality validates US patents' high forward citation counts documented in Section 5.1: when US patents generate 8.87 average citations versus EU's 2.50, those citations originate disproportionately from Asian innovators building on American foundational research. The US functions as a knowledge exporter across multiple domains—particularly autonomous driving, infotainment, and software-heavy applications where US patents lead in both volume and quality (generality/originality indices 0.801/0.855).

    The EU maintains significant ties to Japan (3,869 citations) and Korea (2,664 citations), supporting its role as "collaboration hub" identified in Section 4. However, EU-China knowledge flows remain modest: EU→CN totals 1,543 citations and CN→EU totals 1,502 citations in 2023, far below the EU's ties to Japan or Korea. This mirrors the 45% decline in EU-CN collaborative patents documented in Section 4. Knowledge flows typically follow collaboration patterns: regions with joint R&D projects cite each other more frequently. The weak EU-CN knowledge linkage, despite China's massive patent output (25% global share), suggests limited genuine technical exchange—possibly reflecting IP protection concerns or divergent technological standards.

    ### The US-China Knowledge Flow Collapse: Geopolitics Overriding Complementarity

    Figure 6C documents a dramatic reversal in US-China knowledge exchange that mirrors the collaboration collapse analyzed in Section 4. US patents citing Chinese innovations grew steadily from 629 (2014) to a peak of 8,068 (2021)—a 1,183% increase. Simultaneously, Chinese patents citing US innovations rose from 517 (2014) to 7,914 (2021). This bilateral flow constituted the fastest-growing knowledge linkage globally.

    Then came the collapse. By 2023, US→China citations fell 64% to 2,903, while China→US citations plummeted 70% to 2,409. Partial-year 2024 data shows further decline to ~600 citations in each direction. This coincides precisely with US-China trade tensions (2018 tariffs), Trump administration technology restrictions, Biden administration semiconductor export controls (2022), and escalating concerns over technology transfer. The timing provides quasi-experimental evidence that state-level geopolitical strategy can fragment knowledge networks independent of technical complementarity.

    This pattern is puzzling. Complementary capabilities should sustain knowledge flows: China's battery manufacturing scale and cost engineering should drive US citations, while US software and system integration expertise should attract Chinese citations. The technological logic supporting collaboration remains intact—yet knowledge flows collapsed. Geopolitical institutions can override innovation-system complementarity. Export controls, entity lists, and technology restrictions create barriers even when economic incentives favor exchange.

    The strategic implications are profound. If the 2014-2021 knowledge flow growth had continued, US-China citations might have reached 12,000+ annually by 2024. Instead, they contracted to 2021 levels equivalent to 2017. This represents approximately 5 years of lost knowledge diffusion—a "missing generation" of cross-border learning. For the EU, this fragmentation creates both risk and opportunity: risk if forced to choose sides in a bifurcated technology ecosystem, opportunity if EU patents can serve as neutral knowledge bridges acceptable to both US and Chinese innovators.

    ### Citation Lags and Knowledge Absorption Speed

    An important methodological note: citation lags (time between cited and citing patent filing dates) increase naturally over time due to data structure. Recent patents (2020+) lack sufficient time to accumulate citations, creating the appearance of longer lags. Focusing on mature data (2014-2020), all regions exhibit similar absorption speeds: Japan 1.45 years, China 1.54 years, EU 1.56 years, Korea 1.63 years, US 1.66 years. The differences are modest (0.2 years), suggesting comparable knowledge diffusion timelines across regions. This contrasts with early expectations that state-directed Chinese innovation might exhibit faster or slower absorption—in practice, citation lags reflect universal R&D cycle times (~18 months) rather than institutional differences.

    ---
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Case Study: China's Cross-Industry Innovation Strategy

    The remarkable transformation of China's EV sector represents a fundamental departure from traditional automotive paradigms. Chinese manufacturers have systematically transferred consumer electronics business logic into automotive manufacturing—a strategic reconfiguration that challenges century-old industry assumptions. Rather than competing within established automotive rules emphasizing mechanical engineering excellence and long development cycles, Chinese firms have imported the consumer electronics playbook: rapid iteration, software-centric differentiation, aggressive cost reduction, and ecosystem lock-in. This cross-industry knowledge transfer enables disruptive innovation by redefining competition along dimensions where incumbents possess limited advantages. Our patent analysis reveals how this business model innovation manifests across hardware, software, and organizational strategies.

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

    Chinese EV manufacturers operationalize consumer electronics principles through organizational practices diverging from traditional automotive norms. Agile development methodologies—emphasizing rapid iteration, shorter time-to-market, and continuous improvement—have been adapted from software engineering into hardware manufacturing (Womack, 2018). Tesla pioneered this automotive application; Chinese firms scaled it systematically.

    Model Proliferation Strategy (2017-2023):
    - BYD: 19 new models (3.2 models/year average)
    - NIO: 9 new models (1.5 models/year)
    - XPeng: 6 new models (1.0 model/year)
    - Tesla: 5 models (0.8 models/year, for comparison)

    This launch cadence mirrors smartphone industry cycles (annual flagship releases) rather than traditional automotive development timelines (5-7 year platforms). BYD's 19-model portfolio across 6 years required platform modularity strategies enabling rapid variant generation—automotive equivalents of Samsung's Galaxy series spanning multiple price points annually (Salvador et al., 2002).

    Chinese EVs embed consumer electronics design language: dual or triple touchscreen displays (11-17 inches), augmented reality headset integration (NIO's $350 AR glasses), seamless smartphone-vehicle ecosystems (XPeng's phone-as-key and settings synchronization), in-vehicle karaoke systems, and over-the-air software updates enabling continuous feature addition post-purchase. These elements prioritize digital experience and entertainment over traditional automotive concerns like tactile controls or mechanical refinement—a values inversion reflecting consumer electronics DNA.

    XPeng's SEPA 2.0 platform exemplifies platform-based mass customization strategies (Salvador et al., 2002): achieving 70% cost reduction in ADAS components and 85% in infotainment systems through modular architectures. This approach—familiar in consumer electronics where standardized components enable rapid configuration and cost scaling—challenges automotive conventions emphasizing bespoke engineering.

    ### Modular Design: Patent Evidence for Physical Customization

    Beyond software and digital experiences, China's consumer electronics strategy extends to physical vehicle customization—a defining characteristic of modern consumer products. Exploratory patent analysis of modular design domains (CPC codes B60N seats/interiors, B60J windows/doors, B62D29 chassis/body structure) reveals countercyclical investment patterns supporting this thesis.

    China's Strategic Growth in Modular Design Patents:

    Among five major regions (US, China, EU, Japan, South Korea), China's modular design patent share evolved dramatically:
    - 2014: 1.8% (214 patents) - negligible presence
    - 2018: 4.4% (433 patents) - emerging focus
    - 2022: 5.1% (480 patents) - sustained growth
    - 2023: 8.3% (476 patents) - quadrupled from 2014

    China is the only major region showing growth in this domain. Competitors experienced decline or stagnation:
    - EU: 43.3% → 34.3% (-9pp decline, from 5,222 to 1,960 patents)
    - US: 24.4% → 27.9% (modest gain, but absolute decline from 2,946 to 1,591 patents)
    - Japan: 18.2% → 13.9% (-4.3pp decline, collapsed from 2,193 to 795 patents)
    - Korea: 12.3% → 15.5% (share gain, but absolute stagnation around 1,500-1,960 patents)

    Interpretation: This pattern mirrors China's smartphone-industry playbook. Just as Xiaomi, Oppo, and Huawei offer extensive color options, material choices, and accessory ecosystems, Chinese EV makers (NIO, BYD, XPeng) emphasize configurability. NIO's modular interior systems, BYD's 19 model variants in 6 years, and industry-wide emphasis on build-to-order customization all reflect consumer electronics DNA.

    China's 122% absolute growth (214 → 476 patents) while incumbents decline signals strategic intent: treating EVs as mass-customizable products rather than standardized industrial goods. This contrasts sharply with traditional automotive approaches emphasizing platform standardization and limited variation (the "Ford Model T" paradigm).

    Important Caveat: The overall category declined 53% across all regions (12,055 patents in 2014 → 5,708 in 2023), suggesting either technological maturation or—more likely—that key manufacturing innovations are protected as trade secrets rather than patents. China's modular design patents remain modest in absolute terms (476) compared to core technologies like batteries (2,567 in 2024). The CPC codes capture broad vehicle design elements (seats, windows, chassis) extending beyond EV-specific customization.

    Nonetheless, China's countercyclical growth—patenting more while others patent less—provides tangible evidence for the "EVs as consumer electronics" thesis. Where traditional automakers reduce investment in physical modularity (viewing it as mature technology), Chinese firms increase patenting activity, treating configurability as strategic differentiation. This pattern, combined with battery dominance and infotainment focus, reveals a comprehensive consumer electronics approach spanning hardware, software, and manufacturing flexibility.

    ## Innovation Quality and Knowledge Flows: Incremental Optimization Strategy

    Sections 5 and 6 provide critical context for interpreting China's volume-focused patent strategy. While Chinese firms demonstrate impressive quantitative growth, qualitative metrics reveal systematic differences in innovation characteristics—patterns consistent with consumer electronics industry norms emphasizing incremental refinement over foundational breakthroughs.

    ### Patent Quality: Lower Generality and Originality Indices

    Hall-Jaffe-Trajtenberg quality metrics (Section 5.2) quantify cross-domain knowledge integration. China's weighted-average scores lag substantially:

    - Generality Index (diversity of citing patent classes): US 0.707, EU 0.640, China 0.571
    - Originality Index (diversity of cited patent classes): US 0.751, EU 0.682, China 0.602

    These indices measure whether patents draw upon and influence diverse technological domains (high scores indicate foundational, cross-cutting innovations) or remain confined within narrow specializations (low scores suggest incremental refinements). China's approximately 20% lower scores compared to US patents indicate domain-specific incremental innovation—improving existing battery chemistries, infotainment interfaces, and manufacturing processes rather than pioneering new scientific principles (Boeing & Mueller, 2019; Li, 2012).

    This pattern mirrors consumer electronics innovation: smartphone manufacturers continuously refine displays, processors, and cameras (incremental) while foundational technologies (ARM architectures, OLED panels, CMOS sensors) originate from specialized suppliers like ARM Holdings, Samsung Display, and Sony. China's EV strategy follows this logic—optimizing integrated systems rather than inventing underlying components. BYD's Blade Battery, for example, reconfigures existing LFP chemistry into novel cell-to-pack architectures (incremental), contrasting with Korea's solid-state R&D targeting next-generation chemistries (radical).

    Forward citation analysis (Section 5.1) reinforces this interpretation. Chinese EV patents average 2.80 citations (2014-2020 cohort), compared to US 7.16 and EU 2.08. Lower citation counts indicate narrower technological influence—patents solving specific application problems rather than generating broad follow-on research. This volume-over-impact approach characterizes consumer electronics: rapid iteration generates numerous patents with modest individual significance, cumulating to market dominance through manufacturing scale rather than licensing revenue.

    ### Knowledge Openness: Contradicting the "Insular Innovation" Narrative

    Section 6's knowledge flow analysis reveals a counterintuitive finding challenging conventional wisdom about Chinese innovation insularity. China exhibits the lowest self-citation rate among major regions: 19.2% (2018 citation-weighted), compared to EU 42.5%, Japan 47.4%, US 48.9%, and Korea 51.6%.

    Self-citation rates measure knowledge insularity—high rates indicate firms primarily building upon their own prior work (closed innovation), while low rates suggest extensive absorption of external knowledge (open innovation). China's markedly low self-citation contradicts narratives portraying Chinese innovation as insular or domestically-focused. Instead, Chinese EV manufacturers demonstrate aggressive external knowledge absorption, scanning global patent landscapes and rapidly incorporating foreign technological advances—a practice common in consumer electronics where Chinese firms historically excelled at "fast-follower" strategies (ITIF, 2024).

    Citation lag analysis (Section 6) supports rapid-iteration strategies: Chinese patents cite prior art with 1.54-year average lag, comparable to US (1.66 years) and EU (1.56 years), enabling swift integration of cutting-edge technologies into mass-market vehicles.

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

    Differentiation Through Durability and Sustainability: Position EVs as durable premium goods rather than fast-moving consumer products. European strengths in thermal management (44% patent share, Section 3) and safety systems (47% share) enable longer vehicle lifespans, battery durability, and circular economy integration—values inconsistent with 3-year upgrade cycles but appealing to environmentally-conscious premium segments globally (Section 8 elaborates strategic scenarios).

    Privacy-First Digital Architectures: European data protection regulations (GDPR) and consumer privacy preferences create differentiation opportunities. Rather than competing on screen quantity or feature abundance, EU manufacturers can emphasize user-controlled data sovereignty, minimal data collection, and transparent connectivity—digital experiences aligned with European values rather than Chinese surveillance capitalism norms.

    Selective Software Investment: Prioritize safety-critical domains (autonomous driving, ADAS) where the EU retains competitiveness (31% autonomous driving patent share) while avoiding head-to-head infotainment competition against US software dominance (60% share). The EU's engineering culture advantages safety system integration over entertainment features.

    Ecosystem Compatibility Over Ecosystem Lock-In: Chinese and US strategies pursue proprietary ecosystems (Apple CarPlay exclusivity, Chinese vehicle-phone integration). The EU can differentiate through open interoperability standards, enabling consumer choice and avoiding anti-competitive concerns—positioning aligned with European regulatory philosophies.

    The fundamental strategic insight: China has redefined EV competition along consumer electronics dimensions. The EU cannot win this redefined game with traditional automotive tools, but neither should it play by Chinese rules. Instead, the EU must offer a compelling third path—premium sustainable mobility combining engineering excellence with selective digitalization, durability with privacy, and quality with environmental responsibility. Whether European manufacturers can execute this differentiated strategy rapidly enough to stem market share erosion (Section 3's 42% → 28% decline) remains the critical open question.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ---

    # 8. EU Strategic Imperatives: Pathways Forward

    The empirical evidence presented in Sections 3-7 paints a sobering portrait of European competitive erosion in EV innovation. From 2014 to 2024, the EU's patent share declined from 42% to 28%—a 14-percentage-point contraction affecting six of seven core technology domains (Section 3). Yet within this trajectory of decline lie insights for strategic renewal. This section translates empirical findings into actionable strategic imperatives, examining both immediate priorities and alternative futures the EU might navigate through 2030.

    ## 8.1 Strategic Imperative: Leveraging Asymmetric Advantages

    The EU confronts a fundamental strategic asymmetry: it cannot compete with China's consumer electronics model (rapid iteration, software dominance, massive scale) nor match US foundational research advantages (2.4-3.6× citation quality advantage, 0.801/0.855 generality/originality indices; Sections 5.1-5.2). However, asymmetry need not imply disadvantage. European strengths lie precisely where competitors possess structural vulnerabilities—durability, sustainability, privacy, and engineering depth.

    ### Priority Action 1: Anchor in Defensible Technology Domains

    European patent leadership persists in thermal management (44% share) and safety systems (47% share)—domains where engineering complexity, regulatory standards, and durability requirements create barriers to rapid commoditization (Section 3). These technologies directly address the consumer electronics model's Achilles' heel: longevity and reliability. Chinese manufacturers designing for 3-5 year replacement cycles systematically underinvest in thermal optimization and long-term battery health—precisely the domains where 10-15 year vehicle lifespans require sophisticated engineering.

    The EU should amplify R&D investment in these domains not as defensive retreats but as foundations for differentiation. Advanced thermal architectures enabling faster charging without degradation, predictive safety systems integrating decades of crash engineering data, and modular designs facilitating circular economy integration—these capabilities transform apparent weaknesses (slower iteration) into premium market positioning (lifecycle value).

    ### Priority Action 2: Forge Strategic Knowledge Alliances

    European collaboration rates (1.28% in 2023) exceed all competitors, with the EU-US knowledge axis generating 13,139 citations—the dominant bilateral flow globally (Sections 4 and 6). Yet China's self-citation rate (21.2%, lowest among five regions) reveals unexpected openness to external knowledge, while US-China flows collapsed 70% since 2021 due to geopolitical tensions (Section 6). This creates strategic opportunities: the EU can position itself as the indispensable intermediary in fragmenting global innovation networks.

    Concrete actions include deepening EU-Korea battery collaboration (already the second-largest cross-border partnership at 5,410 patents; Section 4), leveraging Japan's hybrid expertise as bridging technology during the BEV transition, and selectively engaging Chinese research institutions on pre-competitive fundamental research (where China's openness enables knowledge flows). Simultaneously, the EU must protect critical IP through stronger enforcement and technology transfer controls—openness paired with strategic guardrails.

    ### Priority Action 3: Differentiate on Privacy and Sustainability

    The China case study (Section 7) reveals that consumer electronics business models depend on data-intensive ecosystems for monetization—connected services, usage analytics, ecosystem lock-in. European GDPR regulations, initially viewed as innovation constraints, now offer differentiation foundations. Privacy-first vehicle architectures emphasizing user data sovereignty, minimal collection, and interoperability align with European consumer preferences increasingly wary of surveillance capitalism.

    Similarly, sustainability certifications for battery lifecycle management, mandatory repairability standards, and circular economy integration impose costs on volume-oriented competitors while rewarding European engineering depth. The EU's strength in thermal management (critical for battery longevity and second-life applications) becomes strategic when regulation mandates lifecycle optimization over initial cost minimization.

    ### Priority Action 4: Accept Strategic Triage

    European resources cannot match China's state subsidies ($230.9 billion; ITIF, 2024) or US venture capital deployment. Strategic triage becomes essential: selectively abandon domains where competitive gaps widen beyond closure horizons.

    Infotainment and connectivity illustrate necessary retreats. China's share grew from 14% to 23% (2014-2023) while US software dominance remains unassailable (60% infotainment patent share; Sections 3, 5.1). Rather than matching screen quantity or entertainment features, the EU should standardize open interfaces (Apple CarPlay, Android Auto integration) and focus software investment exclusively on safety-critical systems (ADAS, autonomous driving) where engineering culture advantages persist (31% autonomous driving patent share; Section 3).

    This is not defeatism but strategic concentration—channeling limited resources toward defensible positions rather than dispersing efforts across unwinnable battles. The smartphone industry's consolidation around 3-5 global brands (Apple, Samsung, Chinese manufacturers) presages similar EV market dynamics; European manufacturers must identify niches where premium positioning enables survival without requiring mass-market scale.

    ## 8.2 Alternative Futures: Three Scenarios for 2030

    Strategic planning under uncertainty requires exploring alternative futures. We construct three scenarios for 2030, each grounded in current trajectory analyses (Sections 3-7) but diverging based on critical uncertainties: EU policy effectiveness, technology disruption timing, and geopolitical stability. Following van der Heijden (2005), we identify robust strategies valid across multiple scenarios rather than optimizing for single predicted outcomes.

    ### Scenario A: "European Renaissance" (Optimistic)

    Narrative: Coordinated EU industrial policy successfully mobilizes €100+ billion in targeted R&D subsidies (2025-2030), focusing on thermal management, battery durability, and safety-autonomous driving integration. Breakthrough innovations in solid-state batteries (commercialized 2027-2028) and AI-optimized thermal systems enable 20-30% range improvements and 15-year battery warranties, repositioning European EVs as premium sustainable mobility solutions. Simultaneously, stringent EU lifecycle regulations (mandatory 70% battery recyclability, 2028; repairability scores, 2029) impose costs on Chinese competitors optimized for rapid obsolescence. Geopolitical stabilization enables renewed EU-US-Japan R&D partnerships while China's domestic market saturation and overcapacity trigger industry consolidation, weakening competitive intensity.

    Patent Share Projections (2030): EU stabilizes at 30-32% (modest recovery from 28%), China 28-30% (plateau from 25%), US 24-26%, Korea 12-14%, Japan 6-8%.

    Key Indicators:
    - EU forward citations improve to 3.5-4.0 average (from 2.50; Section 5.1)
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

    4. Selective Globalization: Collaboration with Japan (hybrids) and Korea (batteries) remains valuable across scenarios, hedging against US-China decoupling while accessing complementary expertise. EU-US knowledge flows (13,139 citations; Section 6) should be protected as strategic assets.

    5. Innovation Concentration: Dispersed R&D across all seven technology domains spreads resources insufficiently to achieve leadership anywhere (the "generalist dilemma"; Section 5.2). Concentrating efforts on 2-3 defensible domains (thermal, safety, autonomous-ADAS integration) maximizes impact regardless of future trajectories.

    The scenarios clarify strategic stakes: the EU stands at a crossroads between managed premium repositioning (Scenarios A-B) and structural irrelevance (Scenario C). Current patent trajectories point toward Scenario B absent policy intervention, but Scenario C remains plausible if Chinese scale economics materialize faster than European differentiation strategies. Scenario A requires aggressive, coordinated action beginning immediately—not incremental adjustments but transformative industrial policy matching the scale of China's state-directed mobilization. The window for strategic choice narrows with each passing year; by 2030, trajectories may become irreversible.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # 9. Conclusion: The Innovation Imperative

    This analysis reveals a European paradox: sustained patent output masking structural erosion in competitive position. The EU produces the second-highest patent volumes globally yet ranks last in citation quality (2.50 average forward citations vs. US 8.87; Section 5.1), holds leadership in only two of seven core domains despite ranking second-to-fourth in all others (the "generalist dilemma"; Section 5.2), and experiences share declines in six technology domains over the past decade (Section 3). These patterns signal not temporary cyclical weakness but fundamental strategic misalignment between European innovation systems and emergent competitive realities in EV markets.

    The global EV innovation landscape has bifurcated along two incompatible value propositions. China's consumer electronics model—rapid iteration, software primacy, affordability through scale—redefines competition along dimensions foreign to traditional automotive logic. The United States leverages software dominance and foundational research depth to maintain quality leadership even as volume share stagnates. The European Union, anchored in engineering excellence and incremental refinement, finds its competitive logic obsoleted by rivals playing entirely different games.

    Yet obsolescence need not imply extinction. Our analysis identifies asymmetric advantages—thermal management (44% patent share), safety systems (47%), durability engineering, sustainability leadership, and privacy protection—where European strengths exploit competitor vulnerabilities. Chinese consumer electronics business models systematically underinvest in longevity; US software giants underestimate regulatory and sustainability constraints. These gaps create strategic opportunities for differentiated "Premium Sustainable Mobility" positioning: vehicles designed for 15-year lifespans, privacy-first digital architectures, and circular economy integration.

    The scenarios presented in Section 8.2 clarify strategic stakes. Scenario A ("European Renaissance") remains achievable through coordinated industrial policy mobilizing €100+ billion in targeted R&D, regulatory leverage imposing lifecycle standards, and deepened EU-Korea-Japan partnerships. Scenario B ("Managed Transition") describes the current trajectory—gradual erosion toward 25-27% patent share and <10% global volume but sustainable premium niche positioning. Scenario C ("Structural Crisis") looms if policy fragmentation and delayed action enable Chinese scale economics and US software dominance to render European competencies irrelevant, collapsing market share below 20% and patent leadership to two declining domains.

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

    Data was queried from Google BigQuery's `patents-public-data.patents.publications` table using SQL, joining with CPC classification definitions to categorize patents. Complete SQL queries and analytical methods are available from the authors upon request.
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
    - Collaborative patents: Separate analysis identifies patents with multiple assignees from different regions (Section 4)
    - Global filing capture: Counts patents filed anywhere in world by companies from these regions, not just domestic filings
    - No "Others" category: Patents not matching specific categories excluded entirely to maintain focus on core EV technologies

    ## Quality Metrics Methodology

    Beyond patent counts, we assess innovation quality through three complementary metrics:

    Forward Citations (Section 5.1)
    - Definition: Number of times a patent is cited by subsequent patents as prior art
    - Interpretation: Higher citations indicate foundational, influential innovations that shape subsequent research
    - Time window: Analysis focuses on 2014-2018 patents (6-10 years citation accumulation) to avoid recency bias
    - Calculation: Average citations per patent by region and technology domain
    - Source: Google BigQuery `patents-public-data.patents.publications` citations table

    Generality Index (Section 5.2)
    - Definition: Herfindahl-based diversity measure of citing patents' technology classes
    - Formula: `1 - Σ(share_of_citations_in_class_i)²` across all CPC classes citing the patent
    - Interpretation: High generality (approaching 1.0) indicates patents influencing diverse technology fields; low generality (approaching 0) indicates narrow specialist impact
    - Theoretical basis: Hall, Jaffe, & Trajtenberg (2001) - measures breadth of technological influence
    - Calculation: Computed at region-domain level (5 regions × 7 domains = 35 observations)

    Originality Index (Section 5.2)
    - Definition: Herfindahl-based diversity measure of cited patents' technology classes (backward citations)
    - Formula: `1 - Σ(share_of_citations_to_class_i)²` across all CPC classes cited by the patent
    - Interpretation: High originality (approaching 1.0) indicates patents synthesizing knowledge from diverse sources; low originality (approaching 0) indicates incremental innovation within single domain
    - Theoretical basis: Hall, Jaffe, & Trajtenberg (2001) - measures cross-domain knowledge integration
    - Calculation: Computed at region-domain level (5 regions × 7 domains = 35 observations)

    ## Cross-Border Collaboration Analysis (Section 4)

    Collaborative Patent Definition: Patents with multiple assignees from different regions among the five analyzed (US, China, EU, Korea, Japan)

    Methodology:
    - Query identifies patents where `assignee_harmonized.country_code` includes multiple regions
    - Collaboration rate = (collaborative patents / total patents) × 100%
    - Bilateral pairs counted (e.g., EU-US, US-CN) to map collaboration networks
    - Important scope note: Only cross-REGIONAL collaboration counted; within-region (e.g., Germany-France) and outside-region (e.g., US-India) collaborations excluded

    Findings: Collaboration rates extremely low (0.65-1.28% across 2014-2024), contradicting open innovation predictions

    ## Knowledge Flow Network Analysis (Section 6)

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

    This analysis is fully reproducible using Google BigQuery's public patent dataset (`patents-public-data.patents.publications`). The complete SQL queries, data processing code, and analytical methods are available from the authors upon request. Primary data was extracted October 2024; citation and collaboration data extracted January 2025, reflecting patent publications available as of those dates.

    ---
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Appendix B: Technical Glossary

    ## Innovation Quality Metrics

    Forward Citations: The number of times a patent is cited by subsequent patents as prior art. Higher citation counts indicate foundational, influential innovations that shape follow-on research. Used as proxy for technological impact and quality.

    Generality Index: A Herfindahl-based diversity measure ranging from 0 to 1, calculated as `1 - Σ(share_of_citations_in_class_i)²`. High values (approaching 1.0) indicate patents influencing diverse technology fields; low values indicate narrow specialist impact. Based on Hall, Jaffe, & Trajtenberg (2001).

    Originality Index: A Herfindahl-based diversity measure ranging from 0 to 1, calculated as `1 - Σ(share_of_citations_to_class_i)²`. High values indicate patents synthesizing knowledge from diverse sources; low values indicate incremental innovation within single domains. Measures cross-domain knowledge integration.

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
