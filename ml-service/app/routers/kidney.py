from fastapi import APIRouter, HTTPException
from ..schemas.prediction import KidneyDiseaseInput, PredictionResponse
from ..services.predictor import predictor_service
from ..services.explainer import explainer_service

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/kidney", response_model=PredictionResponse)
async def predict_kidney(data: KidneyDiseaseInput):
    try:
        input_dict = {
            'age': data.age,
            'blood_pressure': data.blood_pressure,
            'specific_gravity': data.specific_gravity,
            'albumin': data.albumin,
            'sugar': data.sugar,
            'red_blood_cells': 1 if data.red_blood_cells == 'abnormal' else 0,
            'pus_cell': 1 if data.pus_cell == 'abnormal' else 0,
            'bacteria': 1 if data.bacteria == 'present' else 0,
            'blood_glucose_random': data.blood_glucose_random
        }

        score, risk_level, df, X_scaled = predictor_service.predict('kidney', input_dict)
        importance = explainer_service.get_feature_importance('kidney', X_scaled, list(input_dict.keys()))

        return PredictionResponse(
            success=True,
            disease="Chronic Kidney Disease",
            risk_score=round(score, 2),
            risk_level=risk_level,
            confidence=0.88,
            top_contributing_factors=importance,
            interpretation=f"Kidney disease risk level: {risk_level}",
            model_version="1.0.0-xgb"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
