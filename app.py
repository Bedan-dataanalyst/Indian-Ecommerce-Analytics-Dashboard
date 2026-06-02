# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
import os

# Set production configuration parameters
st.set_page_config(
    page_title="Indian E-Commerce Revenue Intelligence",
    page_icon="📈",
    layout="wide"
)

# --- PERFORMANCE ENHANCED DATA LOADING ---
@st.cache_data
def load_and_preprocess_data():
    path = os.path.join("data", "indian_ecommerce_pricing_revenue_growth_36_months.csv")
    df = pd.read_csv(path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['Year-Month'] = df['order_date'].dt.to_period('M').astype(str)
    return df

df = load_and_preprocess_data()

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.image("https://img.icons8.com/fluent/96/000000/dashboard.png", width=80)
st.sidebar.title("Data Control Center")
st.sidebar.markdown("Use global parameters below to slice your analytical data views.")

# Dynamic Date Slicers
min_date, max_date = df['order_date'].min().to_pydatetime(), df['order_date'].max().to_pydatetime()
date_range = st.sidebar.date_input("Analysis Window", value=[min_date, max_date], min_value=min_date, max_value=max_date)

# Category and Regional Filter Controls
selected_zones = st.sidebar.multiselect("Regional Zones", options=list(df['zone'].unique()), default=list(df['zone'].unique()))
selected_categories = st.sidebar.multiselect("Product Verticals", options=list(df['category'].unique()), default=list(df['category'].unique()))

# Apply user filters to dataset globally
if len(date_range) == 2:
    start_dt, end_dt = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start_dt, end_dt = pd.to_datetime(min_date), pd.to_datetime(max_date)

filtered_df = df[
    (df['order_date'] >= start_dt) & 
    (df['order_date'] <= end_dt) & 
    (df['zone'].isin(selected_zones)) & 
    (df['category'].isin(selected_categories))
]

# --- MAIN APP INTERFACE ---
st.title("🇮🇳 Indian E-Commerce 36-Month Analytics & Revenue Intelligence Workspace")
st.markdown("This portfolio workspace provides interactive visibility metrics across commercial operations, localized performance, and demand optimization.")
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📊 Executive Revenue Performance", "🔍 Operational & Pricing Micro-Insights", "🔮 Prescriptive Machine Learning Forecast"])


# =====================================================================
# DASHBOARD TAB 1: EXECUTIVE REVENUE PERFORMANCE
# =====================================================================
with tab1:
    st.subheader("🚀 High-Level Core Performance Metrics")
    
    # Calculate Operational Totals
    total_revenue = filtered_df['revenue'].sum()
    total_volume = filtered_df['units_sold'].sum()
    avg_discount = filtered_df['discount_percent'].mean()
    avg_ticket = filtered_df['revenue'].mean()
    
    # KPI Display Grid
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Gross Revenue Realized", f"₹{total_revenue:,.2f}")
    kpi2.metric("Total Order Volume", f"{total_volume:,} units")
    kpi3.metric("Average Promotional Discount", f"{avg_discount:.2f}%")
    kpi4.metric("Average Revenue / Order (AOV)", f"₹{avg_ticket:,.2f}")
    
    st.markdown("---")
    
    # Layout 36-Month Trend Component
    st.subheader("📈 Macro-Revenue Trajectory & Sales Velocity")
    
    trend_data = filtered_df.groupby('Year-Month').agg({'revenue': 'sum', 'units_sold': 'sum'}).reset_index()
    
    fig_trend = px.line(
        trend_data, x='Year-Month', y='revenue', 
        title="36-Month Rolling Gross Revenue Performance Trajectory",
        markers=True, color_discrete_sequence=["#00D4B2"]
    )
    fig_trend.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_trend, use_container_width=True)
    
    # Contextual Dashboard Metadata Block
    st.info("""
    **💡 Visualization Insights & Business Context:**
    *   **Trend Chart Interpretation:** This chronological timeline demonstrates your organization's quarterly scaling trends and cyclical purchasing trends across the 36-month timeline.
    *   **Actionable Strategic Takeaway:** Spikes indicate successful performance during seasonal sale windows. If gross revenue falls while order volume climbs, it highlights over-discounting or margin erosion across your selected categories.
    """)


# =====================================================================
# DASHBOARD TAB 2: OPERATIONAL & PRICING MICRO-INSIGHTS
# =====================================================================
with tab2:
    st.subheader("🔍 Breakdown Matrix: Distribution and Elasticity Metrics")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("#### Geographic Market Share Strategy")
        zone_summary = filtered_df.groupby('zone')['revenue'].sum().reset_index()
        fig_pie = px.pie(zone_summary, values='revenue', names='zone', hole=0.4, color_discrete_sequence=px.colors.sequential.Mint)
        st.plotly_chart(fig_pie, use_container_width=True)
        
        st.caption("**Chart Guide:** Evaluates regional revenue contributions across India. Use this metric to identify underperforming logistics networks or target regions for regional distribution centers (RDCs).")
        
    with col_right:
        st.markdown("#### Product Category Matrix Evaluation")
        category_summary = filtered_df.groupby('category').agg({'revenue':'sum', 'units_sold':'sum'}).reset_index()
        fig_bar = px.bar(category_summary, x='category', y='revenue', color='units_sold', color_continuous_scale='Viridis', title="Revenue Matrix Overlaid with Unit Volume")
        st.plotly_chart(fig_bar, use_container_width=True)
        
        st.caption("**Chart Guide:** The height reveals total gross income, while the color depth indicates quantity velocity. High bars with dark coloring show low-margin, high-volume drivers (e.g., Grocery).")

    st.markdown("---")
    st.subheader("💸 Price Elasticity & Markdown Analysis vs Supply Pressures")
    
    # Sample down plotting payload size to ensure fast UI updates
    sampled_viz_df = filtered_df.sample(min(len(filtered_df), 2000), random_state=42)
    
    fig_scatter = px.scatter(
        sampled_viz_df, x='base_price', y='discount_percent', 
        color='inventory_pressure', size='units_sold',
        hover_data=['category', 'sales_event'],
        title="Pricing Distribution & Dynamic Discounting Behaviors Matrix",
        color_discrete_map={'High': '#FF4B4B', 'Medium': '#FFA500', 'Low': '#00D4B2'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.info("""
    **💡 Visualization Insights & Business Context:**
    *   **Scatter Plot Interpretation:** This distribution matrix evaluates the business's markdown actions. Each point represents an active catalog order, tracking how discount rates change based on inventory pressure.
    *   **Actionable Strategic Takeaway:** Clusters of large dots at high markdown rates under 'High Inventory Pressure' indicate reactive discounting to clear out excess stock. A healthier approach would use smaller, proactive markdowns earlier in the product lifecycle to protect margins.
    """)


# =====================================================================
# DASHBOARD TAB 3: MACHINE LEARNING DEMAND FORECAST
# =====================================================================
with tab3:
    st.subheader("🔮 Predictive Margin & Scenario Optimization Optimizer")
    st.markdown("Test pricing changes, discount limits, and inventory variables to see their impact on sales volume before changing production values.")
    
    model_path = os.path.join("models", "demand_predictor.joblib")
    
    if not os.path.exists(model_path):
        st.error(f"⚠️ Production model artifact asset could not be initialized at `{model_path}`. Run `train_model.py` first.")
    else:
        # Load serialized pipeline asset
        model_pipeline = joblib.load(model_path)
        
        # Scenario Parameter Form Input Interface
        with st.form("scenario_optimization_form"):
            form_col1, form_col2 = st.columns(2)
            
            with form_col1:
                ui_category = st.selectbox("Product Catalog Category Target", options=list(df['category'].unique()))
                ui_brand = st.selectbox("Brand Premium Classification", options=list(df['brand_type'].unique()))
                ui_base_price = st.slider("Product Base Retail Pricing (INR)", min_value=float(df['base_price'].min()), max_value=float(df['base_price'].max()), value=float(df['base_price'].median()))
                ui_discount = st.slider("Target Markdown Multiplier Selection (%)", min_value=0.0, max_value=90.0, value=15.0)
                
            with form_col2:
                ui_age = st.number_input("Target Core Customer Demography Age", min_value=18, max_value=90, value=28)
                ui_comp = st.radio("Localized Market Competition Density", options=['Low', 'Medium', 'High'], index=1)
                ui_pressure = st.radio("Logistics Center Inventory Stock Pressure", options=['Low', 'Medium', 'High'], index=0)
                
            # Form submission button
            submit_scenario = st.form_submit_button("Run Predictive Strategy Diagnostics")
            
        if submit_scenario:
            # Construct exact inference schema matching training framework
            inference_payload = pd.DataFrame([{
                'base_price': ui_base_price,
                'discount_percent': ui_discount,
                'customer_age': ui_age,
                'category': ui_category,
                'brand_type': ui_brand,
                'competition_intensity': ui_comp,
                'inventory_pressure': ui_pressure
            }])
            
            # Run model pipeline inference execution
            predicted_volume = model_pipeline.predict(inference_payload)[0]
            rounded_volume = int(np.round(predicted_volume))
            
            # Calculate financial parameters
            expected_unit_price = ui_base_price * (1 - (ui_discount / 100.0))
            projected_gross_yield = expected_unit_price * rounded_volume
            
            # Display Prediction Results
            res_col1, res_col2 = st.columns(2)
            res_col1.metric(label="🎯 Predicted Sales Velocity Target", value=f"{rounded_volume} Units")
            res_col2.metric(label="💰 Projected Gross Pipeline Revenue Yield", value=f"₹{projected_gross_yield:,.2f}")
            
            st.success("✨ Optimization Diagnostics Completed Successfully.")
            
    st.markdown("---")
    st.info("""
    **💡 Predictive Analytics Portfolio Context:**
    *   **Behind the Model:** This forecasting tool uses an integrated Scikit-Learn pipeline. Categorical inputs are processed via One-Hot Encoding before generating predictions through an ensemble Random Forest Regressor.
    *   **Business Impact Statement:** Instead of looking at past performance, this feature acts as an interactive tool for inventory planners. It helps teams test different promotional strategies and forecast sales volumes before launching campaigns.
    """)