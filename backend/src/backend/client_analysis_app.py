
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load dummy data (in real app, this would be from a database)
@st.cache_data
def load_data():
    np.random.seed(42)
    sectors = ['Logistics', 'Maritime', 'Trade', 'Retail', 'Technology']
    client_names = [f'Client {i+1}' for i in range(20)]
    revenues = np.random.randint(100000, 1000000, 20)
    employees = np.random.randint(10, 500, 20)
    years_active = np.random.randint(1, 20, 20)
    client_sectors = np.random.choice(sectors, 20)
    
    return pd.DataFrame({
        'client_name': client_names,
        'sector': client_sectors,
        'revenue': revenues,
        'employees': employees,
        'years_active': years_active
    })

def main():
    st.set_page_config(page_title="Client Analysis Dashboard", layout="wide")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Client Overview", "Sector Analysis", "Data Management"])
    
    # Load data
    df = load_data()
    
    if page == "Client Overview":
        client_overview_page(df)
    elif page == "Sector Analysis":
        sector_analysis_page(df)
    else:
        data_management_page(df)

def client_overview_page(df):
    st.title("Client Overview")
    
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart for sector distribution
        fig_pie = px.pie(df, names='sector', title='Client Distribution by Sector')
        st.plotly_chart(fig_pie)
    
    with col2:
        # Bar chart for client count per sector
        sector_counts = df['sector'].value_counts()
        fig_bar = px.bar(
            x=sector_counts.index, 
            y=sector_counts.values,
            title='Number of Clients per Sector'
        )
        st.plotly_chart(fig_bar)
    
    # Sortable client list table
    st.subheader("Client List")
    st.dataframe(df)

def sector_analysis_page(df):
    st.title("Sector Analysis")
    
    # Treemap visualization
    fig_treemap = px.treemap(
        df,
        path=['sector'],
        values='revenue',
        title='Revenue Distribution by Sector'
    )
    st.plotly_chart(fig_treemap)
    
    # Sector metrics cards
    st.subheader("Sector Metrics")
    metrics_cols = st.columns(len(df['sector'].unique()))
    
    for idx, sector in enumerate(df['sector'].unique()):
        sector_data = df[df['sector'] == sector]
        with metrics_cols[idx]:
            st.metric(
                label=sector,
                value=f"${sector_data['revenue'].mean():,.0f}",
                delta=f"{len(sector_data)} clients"
            )
    
    # Sector distribution analysis
    st.subheader("Sector Distribution Analysis")
    fig_box = px.box(
        df,
        x='sector',
        y='revenue',
        title='Revenue Distribution by Sector'
    )
    st.plotly_chart(fig_box)

def data_management_page(df):
    st.title("Data Management")
    
    # Form for data entry
    st.subheader("Add New Client")
    with st.form("new_client_form"):
        client_name = st.text_input("Client Name")
        sector = st.selectbox("Sector", ['Logistics', 'Maritime', 'Trade', 'Retail', 'Technology'])
        revenue = st.number_input("Revenue", min_value=0)
        employees = st.number_input("Number of Employees", min_value=1)
        years_active = st.number_input("Years Active", min_value=0)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Data submitted successfully!")
    
    # Data overview statistics
    st.subheader("Data Overview Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Clients", len(df))
        
    with col2:
        st.metric("Average Revenue", f"${df['revenue'].mean():,.0f}")
        
    with col3:
        st.metric("Total Sectors", len(df['sector'].unique()))
    
    # Show summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

if __name__ == "__main__":
    main()
