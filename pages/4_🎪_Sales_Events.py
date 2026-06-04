import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("🎪 Sales Events & Markdown Performance Analysis")
df = load_and_prep_data()

if not df.empty:
    event_perf = df.groupby('sales_event').agg({'revenue':'sum', 'units_sold':'mean'}).reset_index()
    fig = px.bar(event_perf, x='sales_event', y='revenue', color='units_sold', title="Event Gross Revenue Capture vs Mean Order Units", color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** Aggregated Composite Bar Chart overlaid with Volume Color Scale.
        - **Variables:** `sales_event` vs total `revenue`.
        - **Core Metric Displayed:** Campaign Promotional Lift Ratio.
        - **Business Insight:** Differentiates high-margin promotional holiday events from standard baseline business operations.
        """)