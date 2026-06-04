import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.title("🔮 Predictive Margin Strategy Optimizer")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_dir, "models", "demand_predictor.joblib")

if not os.path.exists(model_path):
    st.error(f"Machine Learning Pipeline file missing at: {model_path}. Run train_model.py first.")
else:
    pipeline = joblib.load(model_path)
    
    with st.form("ml_predict_form"):
        c1, c2 = st.columns(2)
        with c1:
            cat = st.selectbox("Category", ['Fashion', 'Sports & Fitness', 'Grocery Essentials', 'Footwear', 'Electronics', 'Home & Living', 'Premium Lifestyle'])
            brand = st.selectbox("Brand Tier", ['Mass', 'Premium'])
            price = st.slider("Base Price (INR)", 100.0, 15000.0, 1500.0)
        with c2:
            disc = st.slider("Applied Discount (%)", 0.0, 90.0, 15.0)
            age = st.number_input("Customer Age Context", min_value=18, max_value=80, value=30)
            comp = st.radio("Competition Density", ['Low', 'Medium', 'High'])
            press = st.radio("Inventory Stock Pressure", ['Low', 'Medium', 'High'])
            
        submit = st.form_submit_button("Execute Machine Learning Demand Forecasting")
        
    if submit:
        payload = pd.DataFrame([{'base_price': price, 'discount_percent': disc, 'customer_age': age, 'category': cat, 'brand_type': brand, 'competition_intensity': comp, 'inventory_pressure': press}])
        pred = pipeline.predict(payload)[0]
        st.success(f"### Predicted Demand Target Vector: **{int(np.round(pred))} product units sold**")

with st.expander("🔍 Information Panel: About This Predictor Engine"):
    st.markdown("""
    ### Dashboard Technical Breakdown
    - **Architecture:** Pre-compiled Scikit-Learn Random Forest Regressor Pipeline.
    - **Core Metric Generated:** Prescriptive Volume Projection.
    - **Business Insight:** Simulates pricing and markdown changes before moving adjustments live in production environments.
    """)