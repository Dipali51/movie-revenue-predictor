# src/predict.py
import joblib
import pandas as pd

model = joblib.load("model.pkl")

def predict_revenue(data_dict):
    df = pd.DataFrame([data_dict])
    prediction = model.predict(df)[0]
    return round(prediction, 2)
