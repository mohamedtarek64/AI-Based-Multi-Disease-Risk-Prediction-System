import joblib
import os
import numpy as np
import pandas as pd
from typing import Dict, Any

class PredictorService:
    def __init__(self):
        self.models_path = os.path.join(os.path.dirname(__file__), "..", "models")
        self.models = {}
        self.scalers = {}
        self._load_models()

    def _load_models(self):
        diseases = ['diabetes', 'heart', 'hypertension', 'kidney', 'cancer', 'digestive', 'respiratory']
        for disease in diseases:
            model_file = os.path.join(self.models_path, f"{disease}_model.pkl")
            scaler_file = os.path.join(self.models_path, f"{disease}_scaler.pkl")
            
            if os.path.exists(model_file) and os.path.exists(scaler_file):
                try:
                    self.models[disease] = joblib.load(model_file)
                    self.scalers[disease] = joblib.load(scaler_file)
                    print(f"✅ Loaded {disease} model")
                except Exception as e:
                    print(f"❌ Error loading {disease} model: {e}")
            else:
                print(f"⚠️ {disease} model or scaler files not found")

        print("🧠 Model loading sequence complete.")

    def predict(self, disease: str, input_data: Dict[str, Any]):
        if disease not in self.models:
            raise ValueError(f"Model for {disease} not found")

        df = pd.DataFrame([input_data])
        X_scaled = self.scalers[disease].transform(df)
        
        prob = self.models[disease].predict_proba(X_scaled)[0][1] 
        score = float(prob * 100)
        
        risk_level = "low"
        if score > 80: risk_level = "critical"
        elif score > 60: risk_level = "high"
        elif score > 35: risk_level = "medium"
        
        return score, risk_level, df, X_scaled

predictor_service = PredictorService()
