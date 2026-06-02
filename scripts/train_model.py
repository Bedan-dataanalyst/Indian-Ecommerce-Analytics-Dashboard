# train_model.py
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def train_demand_model():
    data_path = os.path.join("data", "indian_ecommerce_pricing_revenue_growth_36_months.csv")
    if not os.path.exists(data_path):
        print(f"[ERROR] Missing dataset at {data_path}. Please place the file correctly.")
        return

    # Load finalized dataset
    df = pd.read_csv(data_path)

    # Engineering target variable and predictive features
    target = 'units_sold'
    num_features = ['base_price', 'discount_percent', 'customer_age']
    cat_features = ['category', 'brand_type', 'competition_intensity', 'inventory_pressure']

    X = df[num_features + cat_features]
    y = df[target]

    # Preprocessing Pipeline (Numeric attributes pass through, Categorical features get One-Hot Encoded)
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', num_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
        ])

    # Combine preprocessing with an ensemble machine learning model
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
    ])

    print("Executing Model Pipeline Training...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_pipeline.fit(X_train, y_train)

    # Evaluate performance accuracy
    r2_score = model_pipeline.score(X_test, y_test)
    print(f"Model Pipeline successfully constructed! Test R² Score: {r2_score:.4f}")

    # Export production artifact
    os.makedirs("models", exist_ok=True)
    joblib.dump(model_pipeline, os.path.join("models", "demand_predictor.joblib"))
    print("Model serialized and exported safely to 'models/demand_predictor.joblib'")

if __name__ == "__main__":
    train_demand_model()