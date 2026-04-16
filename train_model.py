from prophet import Prophet
import pandas as pd
import pickle

df = pd.read_csv("GOOG.csv")

df = df.rename(columns={"Date": "ds", "Close": "y"})

model = Prophet()
model.fit(df)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved")
