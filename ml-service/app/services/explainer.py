import shap
import numpy as np
import pandas as pd
from typing import Dict, Any
from .predictor import predictor_service

class ExplainerService:
    def __init__(self):
        self.explainers = {}

    def get_feature_importance(self, disease: str, X_scaled: np.ndarray, feature_names: list):
        model = predictor_service.models.get(disease)
        if not model:
            return {}

        # Create TreeExplainer for XGBoost
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_scaled)

        # For binary classification, shap_values might be a list (one per class)
        if isinstance(shap_values, list):
            instance_shap = shap_values[1][0] # Positive class
        else:
            instance_shap = shap_values[0]

        # Map feature names to importance
        importance = {name: float(val) for name, val in zip(feature_names, instance_shap)}
        
        # Sort and return top contributing factors
        return dict(sorted(importance.items(), key=lambda item: abs(item[1]), reverse=True))

explainer_service = ExplainerService()
