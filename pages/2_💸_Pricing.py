import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("💸 Pricing Distribution & Discount Optimization Matrix")
df = load_and_prep_data()

if not df.empty:
    fig = px.scatter(df.sample(2000, random_state=42), x='base_price', y='discount_percent', color='category', size='revenue', title="Price Elasticity & Discount Slicing Analysis")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** Dynamic Multivariable Scatter Plot Matrix.
        - **Variables:** `base_price` (X-Axis), `discount_percent` (Y-Axis), sizing scaled by `revenue`.
        - **Core Metric Displayed:** Discount Elasticity Index — tracks markdown behaviors across product verticals.
        - **Business Insight:** Identifies clear markdown clusters, helping flag over-discounted, margin-eroding stock clearance tactics.
        """)