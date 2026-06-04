# utils.py
import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_and_prep_data():
    # Dynamically find the root folder where this file lives
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "indian_ecommerce_pricing_revenue_growth_36_months.csv")
    
    if not os.path.exists(path):
        st.error(f"❌ Core dataset missing from root directory: {path}")
        return pd.DataFrame()
        
    df = pd.read_csv(path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['Year-Month'] = df['order_date'].dt.to_period('M').astype(str)
    return df