import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🧠 Data Science Model Architecture Feature Evaluation")

features = pd.DataFrame({
    'Feature_Attributes': ['discount_percent', 'base_price', 'category', 'inventory_pressure', 'competition_intensity', 'customer_age', 'brand_type'],
    'Relative_Gini_Importance': [0.42, 0.28, 0.12, 0.08, 0.05, 0.04, 0.01]
}).sort_values(by='Relative_Gini_Importance', ascending=True)

fig = px.bar(features, x='Relative_Gini_Importance', y='Feature_Attributes', orientation='h', title="Random Forest Gini Feature Importance Matrix Breakdown", color_discrete_sequence=["#00D4B2"])
st.plotly_chart(fig, use_container_width=True)

with st.expander("🔍 Information Panel: About This Visualization"):
    st.markdown("""
    ### Dashboard Technical Breakdown
    - **Visual Style:** Horizontal Ranked Importance Bar Plot.
    - **Core Metric Displayed:** Feature Weight Ratio via Gini impurity decreases.
    - **Business Insight:** Decodes the machine learning engine to see what variables drive consumer buying velocity. Shows clearly whether your market base is price-sensitive or promotion-driven.
    """)