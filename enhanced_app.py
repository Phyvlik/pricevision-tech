import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import requests  # For backend API integration (if applicable)
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="PriceVision.Tech", layout="wide")

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 20px;
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header Section ---
st.markdown('<div class="header">Welcome to PriceVision.Tech</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Showcasing AI-Powered Insights and Team Achievements</div>', unsafe_allow_html=True)

# --- Tabs for Navigation ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏆 About Us", "💻 Our Project", "📈 Achievements", "📞 Contact", "📊 Predictions"]
)

# --- About Us Tab ---
with tab1:
    st.header("About Us")
    st.write("We are a team of passionate developers aiming to solve real-world problems with innovative solutions.")

# --- Our Project Tab ---
with tab2:
    st.header("Our Project")
    st.write("""
        Our project leverages cutting-edge AI technologies to transform education by providing personalized learning experiences.
        It uses machine learning models to analyze student performance data and recommend tailored learning paths.
    """)
    
    # Add a video demo (replace with your project demo video link)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# --- Achievements Tab ---
with tab3:
    st.header("Our Achievements")
    st.write("""
        - 🏆 Winner of Hacklytics 2025
        - 🥇 Best AI-Powered Application Award
        - 🎖️ Recognized for Innovation in Education Technology
    """)
    
    # Add charts or visuals for achievements
    chart_data = {"Category": ["Innovation", "Impact", "Technical Depth"], "Score": [95, 90, 88]}
    df = pd.DataFrame(chart_data)
    
    st.bar_chart(df.set_index("Category"))

# --- Contact Tab ---
with tab4:
    st.header("Contact Us")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📧 Email: team@pricevision.tech")
        st.write("🌐 Website: www.pricevision.tech")
    
    with col2:
        st.write("📍 Location: Georgia Tech, Atlanta")
        st.write("📞 Phone: +1 (123) 456-7890")

# --- Predictions Tab ---
with tab5:
    st.header("AI-Powered Predictions")
    
    # Inputs and functionality exclusive to the Predictions Tab
    device = st.selectbox(
        "Choose iPhone 12 Model",
        [
            "iPhone 12 Mini 64GB", "iPhone 12 Mini 128GB", "iPhone 12 Mini 256GB",
            "iPhone 12 64GB", "iPhone 12 128GB", "iPhone 12 256GB",
            "iPhone 12 Pro 128GB", "iPhone 12 Pro 256GB", "iPhone 12 Pro Max"
        ]
    )
    
    months = st.slider("📅 Months to Predict", min_value=1, max_value=6, value=3)
    inflation_rate = st.number_input("📈 Inflation Rate (%)", value=2.5)
    gdp_growth = st.number_input("🌍 GDP Growth (%)", value=3.0)

    # Display User Inputs in Columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f"**Device Selected:** {device}")
        
    with col2:
        st.metric(label="Months to Predict", value=f"{months} months")
        
    with col3:
        st.metric(label="Inflation Rate (%)", value=f"{inflation_rate}%")

    # Backend Integration Example
    def get_predictions_from_backend(device, months, inflation_rate, gdp_growth):
        """
        Simulates fetching predictions from a backend API.
        Replace this with your actual backend endpoint.
        """
        try:
            response = requests.post(
                "http://127.0.0.1:5000/predict",  # Replace with your backend URL
                json={
                    "device": device,
                    "months": months,
                    "inflation_rate": inflation_rate,
                    "gdp_growth": gdp_growth,
                }
            )
            if response.status_code == 200:
                return response.json()  # Assuming the backend returns JSON data
            else:
                return {"error": f"Failed to fetch predictions (Status Code {response.status_code})"}
        except Exception as e:
            return {"error": str(e)}

    if st.button("🚀 Generate Predictions"):
        start_time = datetime.now()
        
        with st.spinner("Generating predictions..."):
            predictions = get_predictions_from_backend(device, months, inflation_rate, gdp_growth)
            
            if "error" in predictions:
                st.error(f"Error fetching predictions: {predictions['error']}")
            else:
                data = {
                    "Month": ["March", "April", "May", "June", "July", "August"][:months],
                    "Price (USD)": predictions["prices"],  # Replace with actual key from backend response
                }
                end_time = datetime.now()
                elapsed_time = (end_time - start_time).microseconds / 1000
                
                st.success(f"✅ Predicted prices for {device}: {data['Price (USD)']}")
                st.write(f"⏱️ Prediction Time: {elapsed_time:.2f} ms")

                # Plotly Line Chart
                fig = px.line(
                    data,
                    x="Month",
                    y="Price (USD)",
                    title="📊 Price Prediction Over Time",
                    markers=True,
                    line_shape="spline",
                    color_discrete_sequence=["#FF5733"]
                )
                fig.update_layout(template="plotly_white")
                st.plotly_chart(fig)

# --- Footer Section ---
st.markdown('<div class="footer">Hacklytics 2025 | PriceVision.Tech</div>', unsafe_allow_html=True)




