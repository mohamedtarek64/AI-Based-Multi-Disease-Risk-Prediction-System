from fastapi import APIRouter, HTTPException
from ..schemas.prediction import HypertensionInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/hypertension", response_model=PredictionResponse)
async def predict_hypertension(data: HypertensionInput):
    try:
        # Map categorical inputs to the numerical values used in large-scale training
        input_dict = {
            'age': data.age,
            'bmi': data.bmi,
            'stress_level': data.stress_level,
            'salt_intake': 1 if data.salt_intake.lower() in ['high', 'yes', 'true'] else 0,
            'alcohol_consumption': 2 if data.alcohol_consumption.lower() == 'high' else (1 if data.alcohol_consumption.lower() == 'medium' else 0),
            'physical_activity': 1 if data.physical_activity.lower() in ['high', 'yes', 'true'] else 0,
            'smoking': 1 if data.smoking.lower() in ['current', 'yes', 'true'] else 0,
            'sleep_hours': data.sleep_hours,
            'genetics': 1 if data.genetics else 0
        }

        score, risk_level, df, X_scaled = predictor_service.predict('hypertension', input_dict)
        importance = explainer_service.get_feature_importance('hypertension', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Hypertension",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.92,
            top_contributing_factors=importance,
            interpretation=f"Hypertension risk score: {round(score, 1)}%. {risk_level.capitalize()} monitoring suggested.",
            model_version="1.0.0-xgb-large"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
