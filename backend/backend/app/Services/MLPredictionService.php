<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class MLPredictionService
{
    protected $baseUrl;

    public function __construct()
    {
        $this->baseUrl = env('ML_SERVICE_URL', 'http://127.0.0.1:8001');
    }

    public function getPrediction($disease, $data)
    {
        try {
            $response = Http::post("{$this->baseUrl}/predict/{$disease}", $data);
            
            if ($response->successful()) {
                return $response->json();
            }

            Log::error("ML Service Error: " . $response->body());
            return ['success' => false, 'error' => 'Service error'];
        } catch (\Exception $e) {
            Log::error("ML Service Connection Failed: " . $e->getMessage());
            return ['success' => false, 'error' => 'Connection failed'];
        }
    }
}
