import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("💡 Strategic Operational Business Insights Matrix")
df = load_and_prep_data()

if not df.empty:
    matrix = df.groupby(['zone', 'inventory_pressure']).agg({'revenue':'sum'}).reset_index()
    fig = px.density_heatmap(matrix, x='zone', y='inventory_pressure', z='revenue', title="Regional Revenue Density vs Supply Inventory Constraints", color_continuous_scale='Mint')
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** 2D Bivariate Density Heatmap Grid.
        - **Variables:** Regional `zone` grids intersected with category inventory stock levels.
        - **Core Metric Displayed:** Supply Node Exposure Density.
        - **Business Insight:** Pinpoints systemic inventory logjams and delivery bottlenecks where product shortages clash with high-revenue zones.
        """)