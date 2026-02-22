from fastapi import APIRouter, HTTPException
from ..schemas.prediction import HeartDiseaseInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/heart", response_model=PredictionResponse)
async def predict_heart(data: HeartDiseaseInput):
    try:
        input_dict = {
            'age': data.age,
            'gender': 1 if data.gender == 'female' else 0,
            'chest_pain_type': data.chest_pain_type,
            'resting_bp': data.resting_bp,
            'cholesterol': data.cholesterol,
            'fasting_bs': 1 if data.fasting_bs else 0,
            'resting_ecg': data.resting_ecg,
            'max_heart_rate': data.max_heart_rate,
            'exercise_angina': 1 if data.exercise_angina else 0,
            'st_depression': data.st_depression,
            'st_slope': data.st_slope,
            'major_vessels': data.major_vessels,
            'thalassemia': data.thalassemia
        }

        score, risk_level, df, X_scaled = predictor_service.predict('heart', input_dict)
        importance = explainer_service.get_feature_importance('heart', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Cardiovascular Disease",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.89,
            top_contributing_factors=importance,
            interpretation=f"Heart disease risk is {risk_level}.",
            model_version="1.0.0-xgb"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
