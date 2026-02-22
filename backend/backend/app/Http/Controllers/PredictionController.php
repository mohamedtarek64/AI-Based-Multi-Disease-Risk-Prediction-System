<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\MLPredictionService;
use App\Services\DiseasePredictionService;
use App\Models\Prediction;
use Illuminate\Support\Facades\Auth;
use App\Repositories\PredictionRepository;

class PredictionController extends Controller
{
    protected $predictionService;
    protected $repository;

    public function __construct(DiseasePredictionService $predictionService, PredictionRepository $repository)
    {
        $this->predictionService = $predictionService;
        $this->repository = $repository;
    }

    public function predict(Request $request, $disease)
    {
        $rules = $this->getValidationRules($disease);
        if (empty($rules)) {
            return response()->json(['error' => 'Unsupported disease type'], 400);
        }

        $validated = $request->validate($rules);
        
        $result = $this->predictionService->processPrediction($disease, $validated);

        if ($result['status'] === 'error') {
            return response()->json(['error' => $result['message']], $result['code']);
        }

        return response()->json(['status' => 'success', 'data' => $result['data']]);
    }

    protected function getValidationRules($disease)
    {
        return match ($disease) {
            'diabetes' => [
                'age' => 'required|numeric',
                'gender' => 'required|string',
                'bmi' => 'required|numeric',
                'glucose' => 'required|numeric',
                'blood_pressure' => 'required|numeric',
                'insulin' => 'required|numeric',
                'family_history' => 'required|boolean',
                'physical_activity' => 'required|string',
                'smoking' => 'required|string',
            ],
            'heart' => [
                'age' => 'required|numeric',
                'gender' => 'required|string',
                'chest_pain_type' => 'required|integer',
                'resting_bp' => 'required|numeric',
                'cholesterol' => 'required|numeric',
                'fasting_bs' => 'required|boolean',
                'resting_ecg' => 'required|integer',
                'max_heart_rate' => 'required|numeric',
                'exercise_angina' => 'required|boolean',
                'st_depression' => 'required|numeric',
                'st_slope' => 'required|integer',
                'major_vessels' => 'required|integer',
                'thalassemia' => 'required|integer',
            ],
            'cancer' => [
                'age' => 'required|numeric',
                'gender' => 'required|string',
                'smoking_years' => 'required|integer',
                'alcohol_consumption' => 'required|string',
                'family_history' => 'required|boolean',
                'environmental_exposure' => 'required|boolean',
                'bmi' => 'required|numeric',
                'radiation_exposure' => 'required|boolean',
                'genetic_markers' => 'required|boolean',
            ],
            'digestive' => [
                'age' => 'required|numeric',
                'diet_quality' => 'required|string',
                'processed_meat_intake' => 'required|string',
                'abdominal_pain_freq' => 'required|integer',
                'heartburn_freq' => 'required|integer',
                'bowel_habit_changes' => 'required|boolean',
                'family_history' => 'required|boolean',
                'bmi' => 'required|numeric',
                'unexplained_weight_loss' => 'required|boolean',
            ],
            'respiratory' => [
                'age' => 'required|numeric',
                'smoking_status' => 'required|string',
                'air_pollution_exposure' => 'required|string',
                'cough_freq' => 'required|integer',
                'shortness_of_breath' => 'required|integer',
                'fatigue_level' => 'required|integer',
                'chest_tightness' => 'required|boolean',
                'fever_episodes' => 'required|integer',
                'occupational_dust' => 'required|boolean',
            ],
            'hypertension' => [
                'age' => 'required|numeric',
                'bmi' => 'required|numeric',
                'stress_level' => 'required|integer',
                'salt_intake' => 'required|string',
                'alcohol_consumption' => 'required|string',
                'physical_activity' => 'required|string',
                'smoking' => 'required|string',
                'sleep_hours' => 'required|numeric',
                'genetics' => 'required|boolean',
            ],
            'kidney' => [
                'age' => 'required|numeric',
                'blood_pressure' => 'required|numeric',
                'specific_gravity' => 'required|numeric',
                'albumin' => 'required|integer',
                'sugar' => 'required|integer',
                'red_blood_cells' => 'required|string',
                'pus_cell' => 'required|string',
                'bacteria' => 'required|string',
                'blood_glucose_random' => 'required|numeric',
            ],
            default => [],
        };
    }

    public function getHistory()
    {
        return response()->json([
            'data' => $this->repository->getHistoryByUserId(Auth::id() ?? 1)
        ]);
    }

    public function show($id)
    {
        $prediction = $this->repository->findByIdAndUserId($id, Auth::id() ?? 1);
        return response()->json(['status' => 'success', 'data' => $prediction]);
    }
}
