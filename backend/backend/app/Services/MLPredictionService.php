<?php

namespace App\Services;

use App\Contracts\MLPredictionServiceInterface;
use App\Enums\DiseaseType;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Http\Client\ConnectionException;

class MLPredictionService implements MLPredictionServiceInterface
{
    protected string $baseUrl;
    protected int $timeout;

    public function __construct()
    {
        $this->baseUrl = config('services.ml_service.url');
        $this->timeout = config('services.ml_service.timeout', 10);
    }

    /**
     * @inheritDoc
     */
    public function getPrediction(DiseaseType|string $disease, array $data): array
    {
        $diseaseSlug = $disease instanceof DiseaseType ? $disease->value : $disease;

        try {
            $response = Http::timeout($this->timeout)
                ->post("{$this->baseUrl}/predict/{$diseaseSlug}", $data);

            if ($response->successful()) {
                return [
                    'success' => true,
                    'data' => $response->json(),
                ];
            }

            Log::error("ML Service Error response", [
                'disease' => $diseaseSlug,
                'status' => $response->status(),
                'body' => $response->body()
            ]);

            return [
                'success' => false,
                'error' => 'The ML service returned an error.',
                'status_code' => $response->status()
            ];

        } catch (ConnectionException $e) {
            Log::error("ML Service Connection Failed", [
                'disease' => $diseaseSlug,
                'message' => $e->getMessage()
            ]);

            return [
                'success' => false,
                'error' => 'Could not connect to the ML service.'
            ];
        } catch (\Exception $e) {
            Log::critical("Unexpected error in ML Service Client", [
                'disease' => $diseaseSlug,
                'message' => $e->getMessage(),
                'trace' => $e->getTraceAsString()
            ]);

            return [
                'success' => false,
                'error' => 'An unexpected error occurred.'
            ];
        }
    }
}
