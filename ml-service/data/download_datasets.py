import pandas as pd
import numpy as np
import os

def generate_diabetes_data(n=100000):
    np.random.seed(42)
    data = {
        'age': np.random.randint(21, 85, n),
        'gender': np.random.choice([0, 1], n),
        'bmi': np.random.normal(30, 8, n).clip(15, 60),
        'glucose': np.random.normal(115, 35, n).clip(50, 350),
        'blood_pressure': np.random.normal(75, 12, n).clip(40, 140),
        'insulin': np.random.normal(90, 45, n).clip(0, 400),
        'family_history': np.random.choice([0, 1], n, p=[0.75, 0.25]),
        'physical_activity': np.random.choice([0, 1, 2], n),
        'smoking': np.random.choice([0, 1, 2], n)
    }
    df = pd.DataFrame(data)
    logit = 0.05 * df['glucose'] + 0.1 * df['bmi'] + 0.03 * df['age'] + 0.7 * df['family_history'] - 13
    df['target'] = (1 / (1 + np.exp(-logit)) > (np.random.rand(n) * 0.3 + 0.35)).astype(int)
    return df

def generate_heart_data(n=100000):
    np.random.seed(43)
    data = {
        'age': np.random.randint(30, 85, n),
        'gender': np.random.choice([0, 1], n),
        'chest_pain_type': np.random.randint(0, 4, n),
        'resting_bp': np.random.normal(135, 22, n).clip(80, 220),
        'cholesterol': np.random.normal(235, 55, n).clip(100, 500),
        'fasting_bs': np.random.choice([0, 1], n, p=[0.8, 0.2]),
        'resting_ecg': np.random.randint(0, 3, n),
        'max_heart_rate': np.random.normal(145, 28, n).clip(60, 220),
        'exercise_angina': np.random.choice([0, 1], n),
        'st_depression': np.random.uniform(0, 6, n),
        'st_slope': np.random.randint(0, 3, n),
        'major_vessels': np.random.randint(0, 5, n),
        'thalassemia': np.random.randint(1, 4, n)
    }
    df = pd.DataFrame(data)
    logit = 0.04 * df['age'] + 0.6 * df['exercise_angina'] + 0.5 * df['major_vessels'] + 0.4 * df['st_depression'] - 6
    df['target'] = (1 / (1 + np.exp(-logit)) > (np.random.rand(n) * 0.25 + 0.35)).astype(int)
    return df

def generate_cancer_data(n=100000):
    # Based on general oncological risk factors
    np.random.seed(46)
    data = {
        'age': np.random.randint(18, 90, n),
        'gender': np.random.choice([0, 1], n),
        'smoking_years': np.random.randint(0, 50, n),
        'alcohol_consumption': np.random.randint(0, 3, n), # 0: None, 1: Low, 2: High
        'family_history': np.random.choice([0, 1], n, p=[0.85, 0.15]),
        'environmental_exposure': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'bmi': np.random.normal(26, 6, n).clip(15, 50),
        'radiation_exposure': np.random.choice([0, 1], n, p=[0.95, 0.05]),
        'genetic_markers': np.random.choice([0, 1], n, p=[0.98, 0.02])
    }
    df = pd.DataFrame(data)
    logit = 0.06 * df['age'] + 0.1 * df['smoking_years'] + 1.5 * df['family_history'] + 2.0 * df['genetic_markers'] + 1.2 * df['environmental_exposure'] - 9
    df['target'] = (1 / (1 + np.exp(-logit)) > (np.random.rand(n) * 0.3 + 0.4)).astype(int)
    return df

def generate_digestive_data(n=100000):
    # Gastrointestinal Risk Factors
    np.random.seed(47)
    data = {
        'age': np.random.randint(18, 85, n),
        'diet_quality': np.random.randint(0, 3, n), # 0: Healthy, 1: Med, 2: Junk
        'processed_meat_intake': np.random.randint(0, 3, n),
        'abdominal_pain_freq': np.random.randint(0, 4, n),
        'heartburn_freq': np.random.randint(0, 4, n),
        'bowel_habit_changes': np.random.choice([0, 1], n),
        'family_history': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'bmi': np.random.normal(27, 6, n).clip(16, 48),
        'unexplained_weight_loss': np.random.choice([0, 1], n, p=[0.95, 0.05])
    }
    df = pd.DataFrame(data)
    logit = 0.03 * df['age'] + 0.8 * df['diet_quality'] + 1.2 * df['processed_meat_intake'] + 2.0 * df['unexplained_weight_loss'] + 1.5 * df['bowel_habit_changes'] - 6
    df['target'] = (1 / (1 + np.exp(-logit)) > (np.random.rand(n) * 0.3 + 0.3)).astype(int)
    return df

def generate_respiratory_data(n=100000):
    # Active/Respiratory diseases like Chronic Bronchitis or Risk Factors
    np.random.seed(48)
    data = {
        'age': np.random.randint(1, 90, n),
        'smoking_status': np.random.randint(0, 3, n), # 0: Non, 1: Former, 2: Current
        'air_pollution_exposure': np.random.randint(0, 3, n),
        'cough_freq': np.random.randint(0, 4, n),
        'shortness_of_breath': np.random.randint(0, 4, n),
        'fatigue_level': np.random.randint(0, 4, n),
        'chest_tightness': np.random.choice([0, 1], n),
        'fever_episodes': np.random.randint(0, 5, n),
        'occupational_dust': np.random.choice([0, 1], n)
    }
    df = pd.DataFrame(data)
    logit = 0.04 * df['age'] + 1.5 * df['smoking_status'] + 1.2 * df['air_pollution_exposure'] + 2.0 * df['shortness_of_breath'] - 7
    df['target'] = (1 / (1 + np.exp(-logit)) > (np.random.rand(n) * 0.2 + 0.4)).astype(int)
    return df

def save_datasets():
    base_path = "data/raw"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    print("🚀 Generating MEGA-SCALE clinical datasets (100k samples each)...")
    
    sample_size = 100000
    
    datasets = {
        "diabetes_raw.csv": generate_diabetes_data(sample_size),
        "heart_raw.csv": generate_heart_data(sample_size),
        "cancer_raw.csv": generate_cancer_data(sample_size),
        "digestive_raw.csv": generate_digestive_data(sample_size),
        "respiratory_raw.csv": generate_respiratory_data(sample_size)
    }
    
    for filename, df in datasets.items():
        df.to_csv(os.path.join(base_path, filename), index=False)
        print(f"✅ Saved {filename} ({len(df)} samples)")

if __name__ == "__main__":
    save_datasets()
