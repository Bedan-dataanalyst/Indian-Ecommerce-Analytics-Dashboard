# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_and_prep_data

# 1. Page Configuration Framework
st.set_page_config(
    page_title="Indian E-Commerce Workspace Hub",
    page_icon="💼",
    layout="wide"
)

st.title("🇮🇳 Indian E-Commerce 36-Month Executive Summary Hub")
st.markdown("### Strategic Performance Overview & Multi-Departmental Intelligence Ledger")

st.info("""
👈 **Navigation Index:** Use the sidebar menu on the left to leave the summary hub and enter dedicated, full-screen deep dives for each analytics vertical or machine learning simulator.
""")

# Load global safe preprocessed data asset
df = load_and_prep_data()

if df.empty:
    st.error("❌ The primary dataset asset cannot be initialized. Please check repository file health mappings.")
else:
    # =========================================================================
    # MILESTONE 1: ENTERPRISE KEY PERFORMANCE INDICATORS (KPIs)
    # =========================================================================
    total_rev = df['revenue'].sum()
    total_units = df['units_sold'].sum()
    avg_disc = df['discount_percent'].mean()
    
    # Programmatically calculate top revenue vertical
    cat_summary = df.groupby('category')['revenue'].sum().reset_index()
    top_cat = cat_summary.sort_values(by='revenue', ascending=False).iloc[0]['category']
    
    kpicol1, kpicol2, kpicol3, kpicol4 = st.columns(4)
    kpicol1.metric("Gross Merchandise Value (GMV)", f"₹{total_rev:,.2f}")
    kpicol2.metric("Aggregate Units Dispatched", f"{total_units:,} units")
    kpicol3.metric("Primary Growth Engine", top_cat)
    kpicol4.metric("Mean Markdown Depth", f"{avg_disc:.2f}%")
    
    st.markdown("---")
    
    # =========================================================================
    # MILESTONE 2: COMMERCIAL VERTICAL PROFILE (Summarizes Pages 2 & 4)
    # =========================================================================
    st.subheader("📊 Part 1: Commercial Mix & Cross-Category Revenue Density")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        cat_rev_df = df.groupby('category').agg({'revenue': 'sum', 'units_sold': 'sum'}).reset_index().sort_values(by='revenue', ascending=True)
        fig_cat = px.bar(
            cat_rev_df,
            x='revenue',
            y='category',
            orientation='h',
            title="Gross Revenue Generation Across Product Verticals",
            color='units_sold',
            color_continuous_scale='Viridis',
            labels={'revenue': 'Total Realized Revenue (INR)', 'category': 'Product Category', 'units_sold': 'Units Sold'}
        )
        fig_cat.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_cat, use_container_width=True)
    
    with c2:
        st.markdown(f"""
        #### 🔍 Corporate Briefing & Formulation
        The high-level category allocation tracks absolute market penetration across consumer item sectors. Gross revenue performance is calculated via the formulation:
        $$\\text{{GMV}} = \\sum_{{i=1}}^{{n}} (Q_i \\times P_i)$$
        where $Q_i$ matches the variable `units_sold` and $P_i$ denotes the net `final_price` for order transaction index $i$.
        
        #### 💡 Operational Data Interpretation
        * **Volume Optimization Matrix:** Shading shifts toward brighter yellow vectors reveal sectors driving intensive physical inventory turnover. Darker bars match categories generating heavy currency margins with lower shipping weight overheads.
        * **Portfolio Focus:** Core capital and display allocation assets should prioritize the **{top_cat}** vector, which currently dominates baseline fiscal generation.
        """)
        
    st.markdown("---")
    
    # =========================================================================
    # MILESTONE 3: TIMELINE TIMING & MOMENTUM PROFILE (Summarizes Pages 1 & 8)
    # =========================================================================
    st.subheader("📅 Part 2: Macro Timeline Scaling & Trend Velocity")
    
    c3, c4 = st.columns([1, 2])
    with c3:
        st.markdown("""
        #### 🔍 Timeline Diagnostics & Vector Shifts
        This component isolates the sequential operational movement of commercial asset performance across the continuous 36-month tracking matrix.
        
        The baseline velocity parameter evaluates the system's month-over-month growth variance tracking vector:
        $$\\Delta R_t = \\frac{{R_t - R_{t-1}}}{{R_{t-1}}} \\times 100$$
        where $R_t$ specifies aggregate marketplace revenue inside a targeted operating monthly interval $t$.
        
        #### 💡 Operational Data Interpretation
        * **Peak Seasonality Allocations:** Recurring cyclical upward wave peaks reveal platform expansion constraints during major regional festival events, signaling logistics networks to pre-stage packaging assets.
        * **Baseline Stabilization Floor:** The rolling upward expansion floor indicates consistent multi-quarter user retention outside active discounting waves.
        """)
        
    with c4:
        monthly_trend = df.groupby('Year-Month').agg({'revenue': 'sum'}).reset_index()
        fig_time = px.area(
            monthly_trend,
            x='Year-Month',
            y='revenue',
            title="36-Month Rolling Enterprise Cash Capture Waveform",
            color_discrete_sequence=["#00D4B2"],
            labels={'revenue': 'Monthly Cumulative Revenue (INR)', 'Year-Month': 'Operational Timeline'}
        )
        fig_time.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_time, use_container_width=True)

    st.markdown("---")

    # =========================================================================
    # MILESTONE 4: GEOGRAPHIC EXPANSION FIELD MAP (Summarizes Pages 3 & 6)
    # =========================================================================
    st.subheader("🗺️ Part 3: Regional Distribution & Demographic Profiles")
    
    c5, c6 = st.columns([2, 1])
    with c5:
        zone_df = df.groupby('zone').agg({'revenue': 'sum', 'customer_age': 'mean'}).reset_index()
        fig_zone = px.pie(
            zone_df,
            values='revenue',
            names='zone',
            title="Territorial Contribution Weights (Fulfillment Zone Ratios)",
            color_discrete_sequence=px.colors.sequential.Mint_r
        )
        fig_zone.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_zone, use_container_width=True)
        
    with c6:
        st.markdown("""
        #### 🔍 Spatial Demographics Overview
        This multi-variable metric tracks regional revenue density proportions intersected against target purchasing group characteristics.
        
        The centralized cohort indicator evaluating localized customer age concentrations corresponds to the average value:
        $$\\mu_{\\text{{age}}} = \\frac{{1}}{{N}} \\sum_{{j=1}}^{{N}} A_j$$
        where $A_j$ matches the historical consumer age recorded for a validated order $j$, and $N$ represents total system transaction volume.
        
        #### 💡 Operational Data Interpretation
        * **Regional Infrastructure Focus:** Supply chain assets and regional marketing deployment profiles should focus directly on dominating the primary geographic pie slices.
        * **Targeted Inventory Sourcing:** Adapt fulfillment centers to prioritize item assortments tailored to the buying habits of consumer age segments prominent within those high-performance hubs.
        """)

    st.markdown("---")
    
    # =========================================================================
    # MILESTONE 5: PREDICTIVE PIPELINE ENSEMBLE SYSTEM ABSTRACT (Summarizes Pages 5 & 7)
    # =========================================================================
    st.subheader("🔮 Part 4: Predictive Machine Learning Integration Abstract")
    st.markdown("""
    The core architecture integrates an enterprise **Random Forest Regressor Pipeline Ensemble** to map non-linear elasticities across variable pricing matrix nodes. 
    This diagnostic model is split into deep-dive operational dashboards accessible via the navigation sidebar.
    """)
    
    mlcol1, mlcol2 = st.columns(2)
    with mlcol1:
        st.info("""
        **🔮 Machine Learning Demand Forecast Simulation (Page 5)**
        - **Objective:** Simulates the market response to a proposed base price variation ($\Delta \\text{Base Price}$) alongside markdown depth modifications ($\Delta \\text{Discount Percent}$) in real time before pushing pricing updates live.
        - **Business Utility:** Returns a predictive buying volume forecast based on regional competition parameters and fulfillment center stock pressures.
        """)
    with mlcol2:
        st.success("""
        **🧠 Model Architecture Gini Importance Weights (Page 7)**
        - **Objective:** Provides full algorithmic transparency by charting model parameters.
        - **Business Utility:** Ranks data features based on absolute Gini index impurity drops. This clearly identifies whether consumer buying volume is driven by pricing tiers, markdown structures, or target demographic characteristics.
        """)
