# app.py
import streamlit as st
from utils import load_and_prep_data

st.set_page_config(
    page_title="Indian E-Commerce Workspace Hub",
    page_icon="💼",
    layout="wide"
)

st.title("🇮🇳 Indian E-Commerce 36-Month Analytics & ML Workspace")
st.markdown("### Welcome to your Enterprise Intelligence Dashboard Portfolio")

st.info("""
👈 **Use the Sidebar Navigation Menu to explore the 8 custom analytical dashboards built for this project.**
Every page contains real-time visualization frameworks, specific asset metrics calculations, and business insights.
""")

df = load_and_prep_data()

st.subheader("📊 Dataset Overview Asset Check")
if not df.empty:
    st.dataframe(df.head(10), use_container_width=True)
    st.markdown(f"""
    - **Dataset Size:** {len(df):,} historical order transaction rows.
    - **Timeline Coverage:** 36 sequential operating months.
    - **Tech Stack Utilized:** Streamlit Multi-Page API, Plotly Express, Scikit-Learn Engine, Joblib Serialization.
    """)