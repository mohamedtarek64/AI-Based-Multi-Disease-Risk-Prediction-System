# 🐍 AI Disease Prediction ML Service

This service provides real-time machine learning predictions using **XGBoost** and explainability using **SHAP**.

## 🚀 Getting Started

### 1. Setup Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Generate Development Models
If you don't have the real trained models yet, run the mock training script:
```bash
python notebooks/mock_training.py
```

### 3. Run the API
```bash
uvicorn app.main:app --reload --port 8001
```

## 🧪 API Endpoints

- `POST /predict/diabetes`: Predict diabetes risk.
- `POST /predict/heart`: Cardiovascular risk assessment.
- `POST /predict/cancer`: Oncology risk prediction.
- `POST /predict/digestive`: Gastrointestinal risk analysis.
- `POST /predict/respiratory`: Active/Respiratory disease metrics.
- `POST /predict/hypertension`: High blood pressure monitoring.
- `POST /predict/kidney`: Chronic kidney disease assessment.

## 🧠 Technology Stack
- **FastAPI**: High-performance web framework.
- **XGBoost**: Gradient boosting framework for the classification models.
- **SHAP**: Explainable AI to provide feature importance per prediction.
- **Joblib**: For efficient model serialization.
