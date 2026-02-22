<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
use App\Models\User;
use App\Services\MLPredictionService;
use Mockery\MockInterface;

class PredictionFeatureTest extends TestCase
{
    use RefreshDatabase;

    protected function setUp(): void
    {
        parent::setUp();
        // Create a user and authenticate
        $this->user = User::factory()->create();
        $this->actingAs($this->user);
    }

    public function test_can_get_diabetes_prediction()
    {
        // Mock the ML Service response
        $this->mock(MLPredictionService::class, function (MockInterface $mock) {
            $mock->shouldReceive('getPrediction')
                ->once()
                ->andReturn([
                    'success' => true,
                    'risk_score' => 15.5,
                    'risk_level' => 'low',
                    'prediction_result' => ['some' => 'meta data']
                ]);
        });

        $response = $this->postJson('/api/v1/predict/diabetes', [
            'age' => 45,
            'gender' => 'male',
            'bmi' => 28.5,
            'glucose' => 120,
            'blood_pressure' => 80,
            'insulin' => 15,
            'family_history' => true,
            'physical_activity' => 'moderate',
            'smoking' => 'never',
        ]);

        $response->assertStatus(200)
            ->assertJsonPath('status', 'success')
            ->assertJsonPath('data.disease_type', 'diabetes')
            ->assertJsonPath('data.risk_score', 15.5);

        $this->assertDatabaseHas('predictions', [
            'user_id' => $this->user->id,
            'disease_type' => 'diabetes'
        ]);
    }

    public function test_prediction_fails_if_ml_service_down()
    {
        $this->mock(MLPredictionService::class, function (MockInterface $mock) {
            $mock->shouldReceive('getPrediction')
                ->once()
                ->andReturn(['success' => false]);
        });

        $response = $this->postJson('/api/v1/predict/diabetes', [
            'age' => 45,
            'gender' => 'male',
            'bmi' => 28.5,
            'glucose' => 120,
            'blood_pressure' => 80,
            'insulin' => 15,
            'family_history' => true,
            'physical_activity' => 'moderate',
            'smoking' => 'never',
        ]);

        $response->assertStatus(503);
    }

    public function test_can_fetch_prediction_history()
    {
        // Create some dummy predictions
        \App\Models\Prediction::create([
            'user_id' => $this->user->id,
            'disease_type' => 'heart',
            'input_data' => [],
            'risk_score' => 10,
            'risk_level' => 'low',
            'prediction_result' => []
        ]);

        $response = $this->getJson('/api/v1/predictions/history');

        $response->assertStatus(200)
            ->assertJsonCount(1, 'data');
    }
}
