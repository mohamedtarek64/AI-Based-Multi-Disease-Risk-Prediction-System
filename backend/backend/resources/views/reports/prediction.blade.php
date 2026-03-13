<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Medical Prediction Report</title>
    <style>
        body { font-family: 'Helvetica', 'Arial', sans-serif; color: #333; line-height: 1.6; }
        .header { text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 20px; margin-bottom: 30px; }
        .logo { color: #2c3e50; font-size: 24px; font-weight: bold; }
        .section { margin-bottom: 25px; }
        .section-title { font-size: 18px; font-weight: bold; color: #2c3e50; border-left: 5px solid #2c3e50; padding-left: 10px; margin-bottom: 15px; }
        .info-grid { display: block; }
        .info-item { margin-bottom: 8px; font-size: 14px; }
        .label { font-weight: bold; color: #7f8c8d; }
        .risk-box { padding: 20px; border-radius: 8px; text-align: center; margin: 20px 0; }
        .risk-critical { background-color: #fce4e4; color: #c0392b; border: 1px solid #c0392b; }
        .risk-high { background-color: #fef5e7; color: #d35400; border: 1px solid #d35400; }
        .risk-medium { background-color: #ebf5fb; color: #2980b9; border: 1px solid #2980b9; }
        .risk-low { background-color: #eafaf1; color: #27ae60; border: 1px solid #27ae60; }
        .score { font-size: 36px; font-weight: bold; display: block; }
        .footer { position: fixed; bottom: 0; width: 100%; text-align: center; font-size: 10px; color: #95a5a6; border-top: 1px solid #eee; padding-top: 10px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 10px; border: 1px solid #eee; text-align: left; }
        th { background: #f8f9fa; color: #2c3e50; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">MEGA AI MEDICAL SYSTEMS</div>
        <p>Advanced Disease Risk Assessment Report</p>
    </div>

    <div class="section">
        <div class="section-title">Patient & Assessment Information</div>
        <div class="info-grid">
            <div class="info-item"><span class="label">Patient Name:</span> {{ $prediction->user->name ?? 'Guest' }}</div>
            <div class="info-item"><span class="label">Assessment Date:</span> {{ $prediction->created_at->format('M d, Y H:i') }}</div>
            <div class="info-item"><span class="label">Disease Analyzed:</span> {{ ucfirst($prediction->disease_type) }}</div>
            <div class="info-item"><span class="label">Report ID:</span> #{{ str_pad($prediction->id, 8, '0', STR_PAD_LEFT) }}</div>
        </div>
    </div>

    <div class="risk-box risk-{{ strtolower($prediction->risk_level) }}">
        <span class="score">{{ number_format($prediction->risk_score, 1) }}%</span>
        <strong>{{ strtoupper($prediction->risk_level) }} RISK</strong>
    </div>

    <div class="section">
        <div class="section-title">Clinical Interpretation</div>
        <p>{{ $prediction->prediction_result['interpretation'] }}</p>
    </div>

    <div class="section">
        <div class="section-title">Input Data Analysis</div>
        <table>
            <thead>
                <tr>
                    <th>Factor</th>
                    <th>Recorded Value</th>
                </tr>
            </thead>
            <tbody>
                @foreach($prediction->input_data as $key => $value)
                <tr>
                    <td>{{ str_replace('_', ' ', ucfirst($key)) }}</td>
                    <td>{{ is_bool($value) ? ($value ? 'Yes' : 'No') : $value }}</td>
                </tr>
                @endforeach
            </tbody>
        </table>
    </div>

    <div class="section" style="page-break-before: auto;">
        <div class="section-title">AI Decision Support (Contributing Factors)</div>
        <p style="font-size: 12px; color: #666; margin-bottom: 10px;">The following factors were identified by the AI as the top contributors to your risk score:</p>
        <table>
            <thead>
                <tr>
                    <th>Factor</th>
                    <th>Impact Weight</th>
                    <th>Influence</th>
                </tr>
            </thead>
            <tbody>
                @foreach(array_slice($prediction->prediction_result['top_contributing_factors'], 0, 5) as $factor => $weight)
                <tr>
                    <td>{{ str_replace('_', ' ', ucfirst($factor)) }}</td>
                    <td>{{ number_format(abs($weight) * 100, 2) }}%</td>
                    <td style="color: {{ $weight > 0 ? '#c0392b' : '#27ae60' }}">
                        {{ $weight > 0 ? 'Increases Risk' : 'Decreases Risk' }}
                    </td>
                </tr>
                @endforeach
            </tbody>
        </table>
    </div>

    <div class="footer">
        Disclaimer: This AI-generated report is for information purposes only and is not a clinical diagnosis. 
        Please consult with a qualified medical professional for clinical guidance.
    </div>
</body>
</html>
