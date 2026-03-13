<?php

namespace App\Enums;

enum DiseaseType: string
{
    case DIABETES = 'diabetes';
    case HEART = 'heart';
    case HYPERTENSION = 'hypertension';
    case KIDNEY = 'kidney';
    case CANCER = 'cancer';
    case DIGESTIVE = 'digestive';
    case RESPIRATORY = 'respiratory';

    public function label(): string
    {
        return match($this) {
            self::DIABETES => 'Diabetes',
            self::HEART => 'Heart Disease',
            self::HYPERTENSION => 'Hypertension',
            self::KIDNEY => 'Kidney Disease',
            self::CANCER => 'Cancer',
            self::DIGESTIVE => 'Digestive Disease',
            self::RESPIRATORY => 'Respiratory Disease',
        };
    }
}
