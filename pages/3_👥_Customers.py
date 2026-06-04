# pages/3_👥_Customers.py
import streamlit as st
import plotly.express as px
from utils import load_and_prep_data

st.set_page_config(layout="wide")
st.title("👥 Customer Demographics & Geographic Segmentation Hub")

df = load_and_prep_data()

if not df.empty:
    # 1. Geographic Coordinate Mapping Registry
    STATE_COORDINATES = {
        'Delhi NCR': {'lat': 28.6139, 'lon': 77.2090},
        'Haryana': {'lat': 29.0588, 'lon': 76.0856},
        'Punjab': {'lat': 31.1471, 'lon': 75.3412},
        'Uttar Pradesh': {'lat': 26.8467, 'lon': 80.9462},
        'Maharashtra': {'lat': 19.7515, 'lon': 75.7139},
        'Gujarat': {'lat': 22.2587, 'lon': 71.1924},
        'Rajasthan': {'lat': 27.0238, 'lon': 74.2179},
        'West Bengal': {'lat': 22.9868, 'lon': 87.8550},
        'Bihar': {'lat': 25.0961, 'lon': 85.3131},
        'Odisha': {'lat': 20.9517, 'lon': 85.0985},
        'Karnataka': {'lat': 15.3173, 'lon': 75.7139},
        'Tamil Nadu': {'lat': 11.1271, 'lon': 78.6569},
        'Telangana': {'lat': 18.1124, 'lon': 79.0193},
        'Kerala': {'lat': 10.8505, 'lon': 76.2711},
        'Madhya Pradesh': {'lat': 22.9734, 'lon': 78.6569},
        'Chhattisgarh': {'lat': 21.2787, 'lon': 81.8661}
    }

    # 2. Process Geospatial Aggregations
    geo_df = df.groupby(['state', 'zone']).agg({
        'revenue': 'sum',
        'units_sold': 'sum',
        'customer_age': 'mean'
    }).reset_index()

    # Safely inject coordinate markers with a baseline country fallback point
    geo_df['lat'] = geo_df['state'].map(lambda x: STATE_COORDINATES.get(x, {'lat': 20.5937, 'lon': 78.9629})['lat'])
    geo_df['lon'] = geo_df['state'].map(lambda x: STATE_COORDINATES.get(x, {'lat': 20.5937, 'lon': 78.9629})['lon'])

    # 3. Create Side-by-Side Analytics Canvas
    vis_col1, vis_col2 = st.columns(2)

    with vis_col1:
        # Visual A: Demographic Histogram
        fig_hist = px.histogram(
            df, 
            x='customer_age', 
            color='customer_gender', 
            barmode='group', 
            title="Age Distribution & Cohort Gender Allocations",
            color_discrete_sequence=["#00D4B2", "#FF4B4B"],
            labels={'customer_age': 'Customer Age', 'count': 'Transaction Volume'}
        )
        fig_hist.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_hist, use_container_width=True)

    with vis_col2:
        # Visual B: Geospatial Bubble Map
        fig_map = px.scatter_geo(
            geo_df,
            lat='lat',
            lon='lon',
            size='revenue',
            color='zone',
            hover_name='state',
            hover_data={
                'revenue': ':,.2f',
                'units_sold': ':,',
                'customer_age': ':.1f',
                'lat': False,
                'lon': False
            },
            title="Geographic Revenue Proportions & Regional Sales Densities",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        
        # Configure mapbox projection frame to lock focus explicitly onto India
        fig_map.update_geos(
            center=dict(lat=22.0, lon=78.0),
            projection_scale=4.2,
            showland=True, landcolor="#1E293B",
            showocean=True, oceancolor="#0F172A",
            showlakes=True, lakecolor="#0F172A",
            showcountries=True, countrycolor="#475569",
            visible=False
        )
        fig_map.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_map, use_container_width=True)

    # 4. Comprehensive Multi-Dimensional Insight Framework
    st.info("### 📘 Data Interpretation & Business Context Guide")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        #### 🔍 How to Read These Visualizations
        * **Demographic Histogram (Left):** Tracks absolute buying frequencies separated by age groups (X-axis) and gender categories (color blocks). Higher clusters indicate your primary demographic sweet spot.
        * **Geographic Bubble Map (Right):** Each node represents an operating Indian state. The **physical sizing of the bubble** scales linearly with total gross revenue generated, while the **color category** groups nodes into regional logistics fulfillment zones.
        """)
    with c2:
        st.markdown("""
        #### 💡 Strategic Business Translation
        * **Territorial Density Strategy:** Larger bubbles point directly to your highest-performing regional markets. If a specific state shows massive bubble sizes but an older average target group age, modify local digital ad copy to match that specific regional demographic's preferences rather than applying a blanket country-wide campaign style.
        * **Fulfillment Center Alignment:** Cross-reference bubble sizing with your logistics supply networks. High-density nodes require dedicated regional warehouse routing to lower shipping costs, minimize parcel delivery transit delays, and protect customer satisfaction scores.
        """)
