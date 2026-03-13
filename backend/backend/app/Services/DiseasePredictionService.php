<?php

namespace App\Services;

use App\Repositories\PredictionRepository;

class DiseasePredictionService
{
    protected $mlClient;
    protected $repository;

    public function __construct(MLPredictionService $mlClient, PredictionRepository $repository)
    {
        $this->mlClient = $mlClient;
        $this->repository = $repository;
    }

    public function processPrediction(string $disease, array $validatedData)
    {
        $result = $this->mlClient->getPrediction($disease, $validatedData);

        if (!$result['success']) {
            return [
                'status' => 'error',
                'message' => $result['error'] ?? 'ML Service Unavailable',
                'code' => $result['status_code'] ?? 503
            ];
        }

        $predictionData = $result['data'];

        $prediction = $this->repository->create([
            'disease_type' => $disease,
            'input_data' => $validatedData,
            'risk_score' => $predictionData['risk_score'],
            'risk_level' => $predictionData['risk_level'],
            'prediction_result' => $predictionData
        ]);

        return [
            'status' => 'success',
            'data' => $prediction
        ];
    }
}
