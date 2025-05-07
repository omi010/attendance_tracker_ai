import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

def train():
    df = pd.read_csv("training_data.csv")
    for col in ["day_of_week", "weather"]:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
    X = df.drop("expected_absent", axis=1)
    y = df["expected_absent"]
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, "model.pkl")

if __name__ == "__main__":
    train()
