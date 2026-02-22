from fastapi import APIRouter, HTTPException
from ..schemas.prediction import CancerInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/cancer", response_model=PredictionResponse)
async def predict_cancer(data: CancerInput):
    try:
        input_dict = {
            'age': data.age,
            'gender': 1 if data.gender.lower() == 'female' else 0,
            'smoking_years': data.smoking_years,
            'alcohol_consumption': 2 if data.alcohol_consumption.lower() == 'high' else (1 if data.alcohol_consumption.lower() == 'medium' else 0),
            'family_history': 1 if data.family_history else 0,
            'environmental_exposure': 1 if data.environmental_exposure else 0,
            'bmi': data.bmi,
            'radiation_exposure': 1 if data.radiation_exposure else 0,
            'genetic_markers': 1 if data.genetic_markers else 0
        }

        score, risk_level, df, X_scaled = predictor_service.predict('cancer', input_dict)
        importance = explainer_service.get_feature_importance('cancer', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Oncology (Cancer) Risk",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.91,
            top_contributing_factors=importance,
            interpretation=f"Based on genetic and lifestyle markers, the risk level is {risk_level}.",
            model_version="1.0.0-mega-xgb"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
