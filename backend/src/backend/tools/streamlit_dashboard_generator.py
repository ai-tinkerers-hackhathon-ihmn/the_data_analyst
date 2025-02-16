"""Streamlit dashboard generator module."""

from typing import Optional
import streamlit as st
from smolagents import tool, Tool

#class SetupDefaultDashboard(Tool):



@tool
def setup_default_dashboard(
    page_title: str,
    page_icon: Optional[str] = "📊",
    layout: str = "wide",
    initial_sidebar_state: str = "expanded",
) -> None:
    """
    Sets up a default Streamlit dashboard layout with common configurations.
    
    Args:
        page_title: The title of the dashboard page
        page_icon: Icon to display in the browser tab. Defaults to "📊"
        layout: Page layout - either "wide" or "centered". Defaults to "wide"
        initial_sidebar_state: Initial state of sidebar - "expanded" or "collapsed"
                                             Defaults to "expanded"
    """
    # Configure the page settings
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state,
    )

    # Add custom CSS to improve the default styling
    st.markdown("""
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
        .element-container {
            margin-bottom: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Set up the main title
    st.title(page_title)

    # Add a sidebar header
    with st.sidebar:
        st.header("Dashboard Controls")

@tool
def create_dashboard_section(
    section_title: str,
    section_description: Optional[str] = None,
) -> None:
    """
    Creates a new section in the dashboard with a title and optional description.
    
    Args:
        section_title: The title of the section
        section_description: Description text for the section
    """
    st.markdown("---")  # Add a horizontal line for separation
    st.header(section_title)
    if section_description:
        st.markdown(section_description)
