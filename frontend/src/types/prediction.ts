export interface PredictionResult {
    success: boolean;
    disease: string;
    risk_score: number;
    risk_level: 'low' | 'medium' | 'high' | 'critical';
    confidence: number;
    top_contributing_factors: Record<string, number>;
    interpretation: string;
    model_version: string;
}

export interface SavedPrediction {
    id: number;
    user_id: number;
    disease_type: string;
    input_data: any;
    risk_score: number;
    risk_level: string;
    prediction_result: PredictionResult;
    created_at: string;
}
