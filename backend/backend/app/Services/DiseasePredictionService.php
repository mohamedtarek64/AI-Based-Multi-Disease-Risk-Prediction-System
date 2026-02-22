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
                'message' => 'ML Service Unavailable',
                'code' => 503
            ];
        }

        $prediction = $this->repository->create([
            'disease_type' => $disease,
            'input_data' => $validatedData,
            'risk_score' => $result['risk_score'],
            'risk_level' => $result['risk_level'],
            'prediction_result' => $result
        ]);

        return [
            'status' => 'success',
            'data' => $prediction
        ];
    }
}
