import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score
import joblib
import os

def train_professional_models():
    print("🧠 Starting MEGA AI Training (500k Total Samples)...")
    
    raw_path = "data/raw"
    model_path = "app/models"
    
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    
    datasets = {
        'diabetes': 'diabetes_raw.csv',
        'heart': 'heart_raw.csv',
        'cancer': 'cancer_raw.csv',
        'digestive': 'digestive_raw.csv',
        'respiratory': 'respiratory_raw.csv'
    }

    report = []

    for disease, filename in datasets.items():
        print(f"\n[▶] Training Deep XGBoost for {disease.upper()}...")
        
        file_path = os.path.join(raw_path, filename)
        if not os.path.exists(file_path):
            continue
            
        df = pd.read_csv(file_path)
        X = df.drop("target", axis=1)
        y = df["target"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # "Train a lot" -> More estimators, deeper trees, slower learning rate
        model = XGBClassifier(
            n_estimators=500,
            learning_rate=0.02,
            max_depth=8,
            subsample=0.85,
            colsample_bytree=0.85,
            eval_metric='logloss',
            random_state=42
        )
        model.fit(X_train_scaled, y_train)

        probs = model.predict_proba(X_test_scaled)[:, 1]
        auc = roc_auc_score(y_test, probs)
        acc = accuracy_score(y_test, (probs > 0.5))
        
        print(f"    🌟 Result: Accuracy {acc:.4f} | AUC {auc:.4f}")

        joblib.dump(model, os.path.join(model_path, f"{disease}_model.pkl"))
        joblib.dump(scaler, os.path.join(model_path, f"{disease}_scaler.pkl"))
        
        report.append({
            'Disease': disease,
            'Accuracy': f"{acc*100:.2f}%",
            'AUC': f"{auc:.4f}"
        })

    print("\n" + "="*40)
    print("📊 MEGA TRAINING SUMMARY")
    print("="*40)
    print(pd.DataFrame(report).to_string(index=False))
    print("="*40)

if __name__ == "__main__":
    train_professional_models()
