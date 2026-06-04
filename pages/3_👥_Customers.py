import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.title("👥 Customer Demographics & Segmentation Ledger")
df = load_and_prep_data()

if not df.empty:
    fig = px.histogram(df, x='customer_age', color='customer_gender', barmode='group', title="Age Distribution & Cohort Gender Allocations", color_discrete_sequence=["#00D4B2", "#FF4B4B"])
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Information Panel: About This Visualization"):
        st.markdown("""
        ### Dashboard Technical Breakdown
        - **Visual Style:** Binned Frequency Bar Histogram.
        - **Variables:** `customer_age` (Age Cohorts) grouped by `customer_gender`.
        - **Core Metric Displayed:** Target Cohort Concentration Ratio.
        - **Business Insight:** Isolates your primary active customer demographics, enabling precise marketing spend optimization.
        """)