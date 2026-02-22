from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class DiabetesInput(BaseModel):
    age: float
    gender: str
    bmi: float
    glucose: float
    blood_pressure: float
    insulin: float
    family_history: bool
    physical_activity: str
    smoking: str

class HeartDiseaseInput(BaseModel):
    age: float
    gender: str
    chest_pain_type: int
    resting_bp: float
    cholesterol: float
    fasting_bs: bool
    resting_ecg: int
    max_heart_rate: float
    exercise_angina: bool
    st_depression: float
    st_slope: int
    major_vessels: int
    thalassemia: int

class CancerInput(BaseModel):
    age: float
    gender: str
    smoking_years: int
    alcohol_consumption: str
    family_history: bool
    environmental_exposure: bool
    bmi: float
    radiation_exposure: bool
    genetic_markers: bool

class DigestiveInput(BaseModel):
    age: float
    diet_quality: str
    processed_meat_intake: str
    abdominal_pain_freq: int
    heartburn_freq: int
    bowel_habit_changes: bool
    family_history: bool
    bmi: float
    unexplained_weight_loss: bool

class RespiratoryInput(BaseModel):
    age: float
    smoking_status: str
    air_pollution_exposure: str
    cough_freq: int
    shortness_of_breath: int
    fatigue_level: int
    chest_tightness: bool
    fever_episodes: int
    occupational_dust: bool

class HypertensionInput(BaseModel):
    age: float
    bmi: float
    stress_level: int
    salt_intake: str
    alcohol_consumption: str
    physical_activity: str
    smoking: str
    sleep_hours: float
    genetics: bool

class KidneyDiseaseInput(BaseModel):
    age: float
    blood_pressure: float
    specific_gravity: float
    albumin: int
    sugar: int
    red_blood_cells: str
    pus_cell: str
    bacteria: str
    blood_glucose_random: float

class PredictionResponse(BaseModel):
    success: bool
    disease: str
    risk_score: float
    risk_level: str
    confidence: float
    top_contributing_factors: Dict[str, float]
    interpretation: str
    model_version: str
