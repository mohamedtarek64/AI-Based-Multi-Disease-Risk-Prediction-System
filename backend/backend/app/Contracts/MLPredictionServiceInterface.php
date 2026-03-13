<?php

namespace App\Contracts;

use App\Enums\DiseaseType;

interface MLPredictionServiceInterface
{
    /**
     * Get prediction from the ML service.
     *
     * @param DiseaseType|string $disease
     * @param array $data
     * @return array
     */
    public function getPrediction(DiseaseType|string $disease, array $data): array;
}
