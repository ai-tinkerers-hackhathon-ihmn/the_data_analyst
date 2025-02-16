
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Configure the page
st.set_page_config(
    page_title="Greenhouse Gas Emissions Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Cache the data loading
@st.cache_data
def load_sample_data():
    # Generate sample data for demonstration
    dates = pd.date_range(start='2010-01-01', end='2023-12-31', freq='M')
    
    # Energy emissions data
    energy_data = pd.DataFrame({
        'Date': dates,
        'Coal_Emissions': np.random.normal(100, 10, len(dates)),
        'Oil_Emissions': np.random.normal(80, 8, len(dates)),
        'Gas_Emissions': np.random.normal(60, 6, len(dates))
    })
    
    # Food emissions data
    food_products = ['Beef', 'Pork', 'Chicken', 'Rice', 'Wheat', 'Vegetables']
    food_data = pd.DataFrame({
        'Product': food_products,
        'Emissions': [36.4, 12.1, 6.9, 4.3, 1.6, 0.4],
        'Water_Usage': np.random.uniform(100, 1000, len(food_products))
    })
    
    return energy_data, food_data

# Load data
energy_data, food_data = load_sample_data()

# Sidebar
st.sidebar.title("Dashboard Controls")
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(energy_data['Date'].min(), energy_data['Date'].max())
)

emission_types = st.sidebar.multiselect(
    "Select Emission Types",
    ['Coal_Emissions', 'Oil_Emissions', 'Gas_Emissions'],
    default=['Coal_Emissions', 'Oil_Emissions', 'Gas_Emissions']
)

# Main dashboard
st.title("🌍 Greenhouse Gas Emissions Dashboard")

# Top metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Total Energy Emissions",
        f"{energy_data[emission_types].sum().sum():,.0f} Mt",
        "4.5%"
    )
with col2:
    st.metric(
        "Average Monthly Emissions",
        f"{energy_data[emission_types].mean().mean():,.0f} Mt",
        "-2.1%"
    )
with col3:
    st.metric(
        "Highest Food Emitter",
        f"{food_data.iloc[food_data['Emissions'].argmax()]['Product']}",
        f"{food_data['Emissions'].max():.1f} Mt"
    )

# Energy emissions time series
st.subheader("Energy-Related Emissions Over Time")
fig_energy = px.line(
    energy_data,
    x='Date',
    y=emission_types,
    title="Monthly Energy Emissions by Source"
)
st.plotly_chart(fig_energy, use_container_width=True)

# Food emissions
st.subheader("Food Product Emissions")
col1, col2 = st.columns(2)

with col1:
    fig_food = px.bar(
        food_data,
        x='Product',
        y='Emissions',
        title="Emissions by Food Product"
    )
    st.plotly_chart(fig_food, use_container_width=True)

with col2:
    fig_scatter = px.scatter(
        food_data,
        x='Emissions',
        y='Water_Usage',
        text='Product',
        title="Emissions vs Water Usage by Food Product"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Interactive data table
st.subheader("Detailed Data")
if st.checkbox("Show Raw Data"):
    tab1, tab2 = st.tabs(["Energy Data", "Food Data"])
    with tab1:
        st.dataframe(energy_data)
    with tab2:
        st.dataframe(food_data)

# Footer
st.markdown("---")
st.markdown("Dashboard created for greenhouse gas emissions analysis")
