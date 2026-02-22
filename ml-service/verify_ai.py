import requests
import json

BASE_URL = "http://localhost:8001"

def test_health():
    print("🔍 Testing Health Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}, Body: {response.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_diabetes():
    print("\n🩺 Testing Diabetes Prediction...")
    payload = {
        "age": 45,
        "gender": "male",
        "bmi": 28.5,
        "glucose": 150,
        "blood_pressure": 85,
        "insulin": 100,
        "family_history": True,
        "physical_activity": "medium",
        "smoking": "never"
    }
    try:
        response = requests.post(f"{BASE_URL}/predict/diabetes", json=payload)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Risk Score: {result['risk_score']}%")
            print(f"Risk Level: {result['risk_level']}")
            print(f"Top Factors: {list(result['top_contributing_factors'].keys())[:3]}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 ML Service Verification Utility")
    test_health()
    test_diabetes()
