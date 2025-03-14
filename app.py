import streamlit as st
import requests

st.title("🚕 Taxi Fare Prediction")

st.markdown("## Enter Ride Details Below")

# Input fields
date_time = st.text_input("Enter Date & Time (YYYY-MM-DD HH:MM:SS)", "2024-03-14 12:00:00")
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)

# Button to predict fare
if st.button("Predict Fare"):
    url = "https://taxifare.lewagon.ai/predict"  # Change this to your own API if available
    params = {
        "pickup_datetime": date_time,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        fare = response.json().get("fare", "Unknown")
        st.success(f"Estimated Fare: ${fare:.2f}")
    else:
        st.error("Failed to retrieve prediction. Check API connection.")
