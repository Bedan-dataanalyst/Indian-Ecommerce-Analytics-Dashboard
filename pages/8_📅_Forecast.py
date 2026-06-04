import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("📅 Time-Series Forward Operational Trend Line")
df = load_and_prep_data()

if not df.empty:
    time_series = df.groupby('Year-Month')['units_sold'].sum().reset_index()
    fig = px.area(time_series, x='Year-Month', y='units_sold', title="36-Month Rolling Historical Sales Volume Curve", color_discrete_sequence=["#00D4B2"])
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** Shaded Line Timeline Area Plot.
        - **Variables:** `Year-Month` vs total sum of `units_sold`.
        - **Core Metric Displayed:** Rolling Transaction Volume Trajectory.
        - **Business Insight:** Maps long-term order fulfillment demands, giving warehouse teams the information they need to schedule staffing and scaling over consecutive quarters.
        """)