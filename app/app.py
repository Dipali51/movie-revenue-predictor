
import streamlit as st
from src.predict import predict_revenue

st.title("🎬 Movie Revenue Predictor")

budget = st.number_input("Budget ($)", min_value=1000000)
popularity = st.slider("Popularity Score", 0.0, 100.0, 50.0)
runtime = st.slider("Runtime (minutes)", 60, 240, 120)
vote_average = st.slider("Average Rating", 0.0, 10.0, 7.0)
vote_count = st.slider("Vote Count", 0, 50000, 5000)

if st.button("Predict Revenue"):
    data = {
        "budget": budget,
        "popularity": popularity,
        "runtime": runtime,
        "vote_average": vote_average,
        "vote_count": vote_count
    }
    revenue = predict_revenue(data)
    st.success(f"Predicted Revenue: ${revenue:,}")
