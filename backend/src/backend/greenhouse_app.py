
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import json

# Page config
st.set_page_config(
    page_title="Greenhouse Gas Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Cache the data loading
@st.cache_data
def load_sample_data():
    # Sample data generation (replace with real data in production)
    food_data = pd.DataFrame({
        'Category': ['Beef', 'Pork', 'Chicken', 'Fish', 'Vegetables'],
        'Emissions': [50, 20, 10, 8, 5],
        'Year': [2022] * 5
    })
    
    energy_data = pd.DataFrame({
        'Year': range(2015, 2023),
        'Coal': np.random.randint(100, 150, 8),
        'Oil': np.random.randint(80, 120, 8),
        'Gas': np.random.randint(60, 90, 8)
    })
    
    geo_data = pd.DataFrame({
        'Country': ['USA', 'China', 'India', 'Russia', 'Japan'],
        'Emissions': [15, 30, 7, 5, 3]
    })
    
    renewable_data = pd.DataFrame({
        'Source': ['Solar', 'Wind', 'Hydro', 'Biomass'],
        'Percentage': [15, 25, 40, 20]
    })
    
    return food_data, energy_data, geo_data, renewable_data

def create_food_charts(food_data):
    # Stacked bar chart
    fig_bar = px.bar(
        food_data,
        x='Category',
        y='Emissions',
        title='Food Emissions by Category'
    )
    
    # Treemap
    fig_treemap = px.treemap(
        food_data,
        path=['Category'],
        values='Emissions',
        title='Food Emissions Distribution'
    )
    
    return fig_bar, fig_treemap

def create_energy_charts(energy_data):
    # Multi-line chart
    fig_line = px.line(
        energy_data,
        x='Year',
        y=['Coal', 'Oil', 'Gas'],
        title='Energy Emissions Over Time'
    )
    
    # Area chart
    fig_area = px.area(
        energy_data,
        x='Year',
        y=['Coal', 'Oil', 'Gas'],
        title='Cumulative Energy Emissions'
    )
    
    return fig_line, fig_area

def create_geo_chart(geo_data):
    fig_geo = px.choropleth(
        geo_data,
        locations='Country',
        locationmode='country names',
        color='Emissions',
        title='Global Emissions Distribution'
    )
    return fig_geo

def create_renewable_charts(renewable_data):
    fig_gauge = go.Figure()
    
    for idx, row in renewable_data.iterrows():
        fig_gauge.add_trace(go.Indicator(
            mode="gauge+number",
            value=row['Percentage'],
            title={'text': row['Source']},
            domain={'row': idx, 'column': 0}
        ))
    
    fig_gauge.update_layout(
        grid={'rows': len(renewable_data), 'columns': 1},
        height=150 * len(renewable_data)
    )
    
    return fig_gauge

# Main app
def main():
    st.title("🌍 Greenhouse Gas Dashboard")
    st.write("Interactive dashboard for analyzing greenhouse gas emissions across different sectors")
    
    # Load data
    food_data, energy_data, geo_data, renewable_data = load_sample_data()
    
    # Sidebar filters
    st.sidebar.title("Filters")
    years = st.sidebar.slider(
        "Select Year Range",
        min_value=2015,
        max_value=2022,
        value=(2015, 2022)
    )
    
    # Main content with tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🍔 Food",
        "⚡ Energy",
        "🗺️ Geographic",
        "♻️ Renewable"
    ])
    
    with tab1:
        st.header("Food Emissions")
        col1, col2 = st.columns(2)
        fig_bar, fig_treemap = create_food_charts(food_data)
        col1.plotly_chart(fig_bar, use_container_width=True)
        col2.plotly_chart(fig_treemap, use_container_width=True)
    
    with tab2:
        st.header("Energy Emissions")
        col1, col2 = st.columns(2)
        fig_line, fig_area = create_energy_charts(energy_data)
        col1.plotly_chart(fig_line, use_container_width=True)
        col2.plotly_chart(fig_area, use_container_width=True)
    
    with tab3:
        st.header("Geographic Distribution")
        fig_geo = create_geo_chart(geo_data)
        st.plotly_chart(fig_geo, use_container_width=True)
    
    with tab4:
        st.header("Renewable Energy Progress")
        fig_gauge = create_renewable_charts(renewable_data)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    # Download options
    st.sidebar.header("Download Data")
    if st.sidebar.button("Download Food Data"):
        csv = food_data.to_csv(index=False)
        st.sidebar.download_button(
            label="Download CSV",
            data=csv,
            file_name="food_emissions.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
