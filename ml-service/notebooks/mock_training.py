import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_mock_models():
    print("🛠️ Training Mock Models for Development...")
    
    model_path = "../app/models"
    if not os.path.exists(model_path):
        os.makedirs(model_path)

    diseases = {
        'diabetes': ['age', 'gender', 'bmi', 'glucose', 'blood_pressure', 'insulin', 'family_history', 'physical_activity', 'smoking'],
        'heart': ['age', 'gender', 'chest_pain_type', 'resting_bp', 'cholesterol', 'fasting_bs', 'resting_ecg', 'max_heart_rate', 'exercise_angina', 'st_depression', 'st_slope', 'major_vessels', 'thalassemia'],
        'hypertension': ['age', 'bmi', 'stress_level', 'salt_intake', 'alcohol_consumption', 'physical_activity', 'smoking', 'sleep_hours', 'genetics'],
        'kidney': ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar', 'red_blood_cells', 'pus_cell', 'bacteria', 'blood_glucose_random']
    }

    for name, features in diseases.items():
        print(f"  [-] Training {name} model...")
        n_samples = 1000
        np.random.seed(42)
        X = pd.DataFrame(np.random.uniform(0, 100, size=(n_samples, len(features))), columns=features)
        y = (np.random.rand(n_samples) > 0.7).astype(int) # Mock labels
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = XGBClassifier()
        model.fit(X_scaled, y)
        
        joblib.dump(model, os.path.join(model_path, f"{name}_model.pkl"))
        joblib.dump(scaler, os.path.join(model_path, f"{name}_scaler.pkl"))
    
    print("✅ All mock models created successfully!")

if __name__ == "__main__":
    train_mock_models()
