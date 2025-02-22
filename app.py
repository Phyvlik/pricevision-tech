import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Title and description
st.title("Dynamic Pricing Dashboard")
st.write("Predicting mobile device prices over the next 6 months with actionable insights.")

# Sidebar for user inputs
st.sidebar.header("User Input")
device = st.sidebar.selectbox("Choose Device", ["iPhone 11 Plus", "iPhone 12 Mini"])
months = st.sidebar.slider("Months to Predict", 1, 6)
inflation_rate = st.sidebar.number_input("Inflation Rate (%)", value=2.5)
gdp_growth = st.sidebar.number_input("GDP Growth (%)", value=3.0)

# Display user input
st.write(f"Device: {device}")
st.write(f"Prediction Horizon: {months} months")
st.write(f"Macroeconomic Factors: Inflation Rate = {inflation_rate}%, GDP Growth = {gdp_growth}%")

# Function to simulate predictions (replace with your AI model logic)
def predict_prices(device, months, inflation_rate, gdp_growth):
    base_price = 700 if device == "iPhone 11 Plus" else 600
    price_decrease_factor = (1 + inflation_rate / 100) * (1 - gdp_growth / 100)
    return [max(base_price - i * 50 * price_decrease_factor, 0) for i in range(months)]

# Generate predictions on button click
if st.button("Generate Predictions"):
    predictions = predict_prices(device, months, inflation_rate, gdp_growth)
    data = {
        "Month": ["March", "April", "May", "June", "July", "August"][:months],
        "Price (USD)": predictions,
    }
    st.success(f"Predicted prices for {device}: {predictions}")

    # Create a line chart using Plotly
    fig = px.line(data, x="Month", y="Price (USD)", title="Price Prediction Over Time")
    st.plotly_chart(fig)

    # Provide recommendations based on predictions
    def recommend_strategy(predictions):
        if predictions[-1] < predictions[0] * 0.8:
            return "Consider reducing prices aggressively to clear inventory."
        else:
            return "Maintain current pricing strategy."

    strategy = recommend_strategy(predictions)
    st.info(f"Recommended Strategy: {strategy}")

# Historical data table (example data)
st.subheader("Historical Data")
historical_data = pd.DataFrame({
    "Month": ["January", "February", "March"],
    "Price (USD)": [750, 725, 700]
})
st.dataframe(historical_data)

# Download historical data as CSV
csv = historical_data.to_csv(index=False).encode('utf-8')
st.download_button(label="Download Historical Data", data=csv, file_name="historical_data.csv", mime="text/csv")

# Anomaly detection example (replace with actual logic)
st.subheader("Anomaly Detection")
historical_prices = [750, 725, 700, 500, 660]
z_scores = np.abs((historical_prices - np.mean(historical_prices)) / np.std(historical_prices))
anomalies = [price for price, z in zip(historical_prices, z_scores) if z > 1.5]
if anomalies:
    st.warning(f"Anomalies Detected in Historical Prices: {anomalies}")
else:
    st.success("No anomalies detected in historical prices.")

# Explanation of predictions (replace with LLM integration)
def explain_prediction(device, months):
    explanation = f"The price of {device} is predicted to decrease over the next {months} months due to depreciation and macroeconomic factors such as inflation and GDP growth."
    return explanation

if st.button("Explain Prediction"):
    explanation = explain_prediction(device, months)
    st.write(explanation)
