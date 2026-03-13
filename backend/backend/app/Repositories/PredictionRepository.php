<?php

namespace App\Repositories;

use App\Models\Prediction;
use Illuminate\Support\Facades\Auth;

class PredictionRepository
{
    public function create(array $data)
    {
        // Try to get authenticated user, then any user, or finally null
        $userId = Auth::id() ?: (\App\Models\User::first()?->id);

        return Prediction::create([
            'user_id' => $userId,
            'disease_type' => $data['disease_type'],
            'input_data' => $data['input_data'],
            'risk_score' => $data['risk_score'],
            'risk_level' => $data['risk_level'],
            'prediction_result' => $data['prediction_result']
        ]);
    }

    public function getHistoryByUserId($userId)
    {
        return Prediction::where('user_id', $userId)->latest()->get();
    }

    public function findByIdAndUserId($id, $userId)
    {
        return Prediction::where('user_id', $userId)->findOrFail($id);
    }
}
