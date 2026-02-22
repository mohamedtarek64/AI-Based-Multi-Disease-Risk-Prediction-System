from fastapi import APIRouter, HTTPException
from ..schemas.prediction import DiabetesInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/diabetes", response_model=PredictionResponse)
async def predict_diabetes(data: DiabetesInput):
    try:
        # Robust mapping for large-scale model
        input_dict = {
            'age': data.age,
            'gender': 1 if data.gender.lower() == 'female' else 0,
            'bmi': data.bmi,
            'glucose': data.glucose,
            'blood_pressure': data.blood_pressure,
            'insulin': data.insulin,
            'family_history': 1 if data.family_history else 0,
            'physical_activity': 2 if data.physical_activity.lower() == 'high' else (1 if data.physical_activity.lower() == 'medium' else 0),
            'smoking': 2 if data.smoking.lower() == 'current' else (1 if data.smoking.lower() == 'former' else 0)
        }

        score, risk_level, df, X_scaled = predictor_service.predict('diabetes', input_dict)
        importance = explainer_service.get_feature_importance('diabetes', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Diabetes Type 2",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.95,
            top_contributing_factors=importance,
            interpretation=f"The risk score is {round(score, 2)}%. This is considered a {risk_level} risk.",
            model_version="1.0.0-xgb-large"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
