# utils.py
import streamlit as st
import pandas as pd
import os

def inject_multicolored_theme():
    """Injects high-performance custom CSS layers for an advanced multicolored aesthetic."""
    st.markdown("""
        <style>
        /* 1. Flowing Top Spectrum Multi-Color Border */
        .main .block-container::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; height: 6px;
            background: linear-gradient(90deg, #FF007A 0%, #7928CA 25%, #00F2FE 50%, #00FF87 75%, #FF6F00 100%);
            z-index: 9999;
            border-radius: 3px;
        }
        
        /* 2. Custom Sidebar Styling Accent */
        [data-testid="stSidebar"] {
            border-right: 2px solid rgba(0, 242, 254, 0.15);
        }
        
        /* 3. Multi-Colored Title Gradient Effect for main headers */
        h1 {
            background: linear-gradient(45deg, #00F2FE, #4FACFE, #7928CA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
        }
        
        /* 4. Glowing Neon Teal for KPI Metrics values */
        div[data-testid="stMetricValue"] {
            color: #00F2FE !important;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            text-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
        }
        
        /* 5. Custom Background Accent For Forms and Interactive Panels */
        div[data-testid="stForm"] {
            border: 1px solid rgba(121, 40, 202, 0.3) !important;
            box-shadow: 0px 4px 20px rgba(121, 40, 202, 0.05);
            background-color: #131E35 !important;
        }
        </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_and_prep_data():
    # Automatically inject styling whenever data is pulled into a dashboard page
    inject_multicolored_theme()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "indian_ecommerce_pricing_revenue_growth_36_months.csv")
    
    if not os.path.exists(path):
        st.error(f"❌ Core dataset missing from root directory: {path}")
        return pd.DataFrame()
        
    df = pd.read_csv(path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['Year-Month'] = df['order_date'].dt.to_period('M').astype(str)
    return df
