<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PredictionController;
use App\Http\Controllers\AuthController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
*/

Route::prefix('v1')->group(function () {
    // Auth Routes
    Route::post('/register', [AuthController::class, 'register']);
    Route::post('/login', [AuthController::class, 'login']);

    // Prediction Routes
    Route::post('/predict/{disease}', [PredictionController::class, 'predict']);
    Route::get('/predictions/history', [PredictionController::class, 'getHistory']);
    Route::get('/predictions/{id}', [PredictionController::class, 'show']);
});
