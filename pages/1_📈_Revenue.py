import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("📈 Executive Revenue Intelligence Dashboard")
df = load_and_prep_data()

if not df.empty:
    rev_trend = df.groupby('Year-Month').agg({'revenue': 'sum'}).reset_index()
    fig = px.line(rev_trend, x='Year-Month', y='revenue', title="36-Month Rolling Gross Revenue Performance Trajectory", markers=True, color_discrete_sequence=["#00D4B2"])
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** Line Chart Tracking with Trend Node Markers.
        - **Variables:** `Year-Month` vs `revenue` (Sum of Total Orders Cash Volume).
        - **Core Metric Displayed:** Gross Realized Income — tracks high-level corporate revenue scaling.
        - **Business Insight:** Highlights quarterly scaling trends and cyclical purchasing peaks over the 36-month operational window.
        """)