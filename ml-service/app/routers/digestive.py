from fastapi import APIRouter, HTTPException
from ..schemas.prediction import DigestiveInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/digestive", response_model=PredictionResponse)
async def predict_digestive(data: DigestiveInput):
    try:
        input_dict = {
            'age': data.age,
            'diet_quality': 2 if data.diet_quality.lower() == 'junk' else (1 if data.diet_quality.lower() == 'medium' else 0),
            'processed_meat_intake': 2 if data.processed_meat_intake.lower() == 'high' else (1 if data.processed_meat_intake.lower() == 'medium' else 0),
            'abdominal_pain_freq': data.abdominal_pain_freq,
            'heartburn_freq': data.heartburn_freq,
            'bowel_habit_changes': 1 if data.bowel_habit_changes else 0,
            'family_history': 1 if data.family_history else 0,
            'bmi': data.bmi,
            'unexplained_weight_loss': 1 if data.unexplained_weight_loss else 0
        }

        score, risk_level, df, X_scaled = predictor_service.predict('digestive', input_dict)
        importance = explainer_service.get_feature_importance('digestive', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Gastrointestinal (Digestive) Risk",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.89,
            top_contributing_factors=importance,
            interpretation=f"Digestive health assessment indicates a {risk_level} risk level.",
            model_version="1.0.0-mega-xgb"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
