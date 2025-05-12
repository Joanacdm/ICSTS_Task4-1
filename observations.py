fhir_observations = [
    {
        "resourceType": "Observation",
        "id": "obs-001",
        "status": "final",
        "code": {"text": "Blood Pressure"},
        "valueQuantity": {"value": 120, "unit": "mmHg"},
        "subject": {"reference": "Patient/patient-001"}
    },
    {
        "resourceType": "Observation",
        "id": "obs-002",
        "status": "final",
        "code": {"text": "Heart Rate"},
        "valueQuantity": {"value": 75, "unit": "bpm"},
        "subject": {"reference": "Patient/patient-001"}
    },
    {
        "resourceType": "Observation",
        "id": "obs-003",
        "status": "final",
        "code": {"text": "Temperature"},
        "valueQuantity": {"value": 36.8, "unit": "°C"},
        "subject": {"reference": "Patient/patient-003"}
    },
    {
        "resourceType": "Observation",
        "id": "obs-004",
        "status": "final",
        "code": {"text": "Respiratory Rate"},
        "valueQuantity": {"value": 16, "unit": "breaths/min"},
        "subject": {"reference": "Patient/patient-004"}
    },
    {
        "resourceType": "Observation",
        "id": "obs-005",
        "status": "final",
        "code": {"text": "Oxygen Saturation"},
        "valueQuantity": {"value": 98, "unit": "%"},
        "subject": {"reference": "Patient/patient-005"}
    }
]
