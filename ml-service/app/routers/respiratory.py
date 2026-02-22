from fastapi import APIRouter, HTTPException
from ..schemas.prediction import RespiratoryInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/respiratory", response_model=PredictionResponse)
async def predict_respiratory(data: RespiratoryInput):
    try:
        input_dict = {
            'age': data.age,
            'smoking_status': 2 if data.smoking_status.lower() == 'current' else (1 if data.smoking_status.lower() == 'former' else 0),
            'air_pollution_exposure': 2 if data.air_pollution_exposure.lower() == 'high' else (1 if data.air_pollution_exposure.lower() == 'medium' else 0),
            'cough_freq': data.cough_freq,
            'shortness_of_breath': data.shortness_of_breath,
            'fatigue_level': data.fatigue_level,
            'chest_tightness': 1 if data.chest_tightness else 0,
            'fever_episodes': data.fever_episodes,
            'occupational_dust': 1 if data.occupational_dust else 0
        }

        score, risk_level, df, X_scaled = predictor_service.predict('respiratory', input_dict)
        importance = explainer_service.get_feature_importance('respiratory', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Respiratory / Active Disease Risk",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.88,
            top_contributing_factors=importance,
            interpretation=f"Assessment for respiratory and active systemic conditions: {risk_level} risk.",
            model_version="1.0.0-mega-xgb"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
