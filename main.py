from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Stock Prediction API Running"}

@app.get("/predict")
def predict(days: int = 30):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(days)
    return result.to_dict()
