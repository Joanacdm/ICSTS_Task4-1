fhir_observations = [
    # diferença de expiração participante 1
       {
        "resourceType": "Observation",
        "id": "obs-001",
        "status": "final",
        "code": {"text": "Impedância Pulmonar (Expiração)"},
        "valueQuantity": {"value": 0.170369, "unit": "∆Z"},
        "subject": {"reference": "Patient/patient-001"},
    },
    # diferença de inspiração participante 2
    {
        "resourceType": "Observation",
        "id": "obs-002",
        "status": "final",
        "code": {"text": "Impedância Pulmonar (Inspiração)"},
        "valueQuantity": {"value": 0.309032, "unit": "∆Z"},
        "subject": {"reference": "Patient/patient-002"}
    },
    # diferença de expiração participante 3
    {
        "resourceType": "Observation",
        "id": "obs-003",
        "status": "final",
        "code": {"text": "Impedância Pulmonar (Expiração)"},
        "valueQuantity": {"value": 0.098384, "unit": "∆Z"},
        "subject": {"reference": "Patient/patient-003"}
    },
    # diferença de inspiração participante 4
    {
        "resourceType": "Observation",
        "id": "obs-004",
        "status": "final",
        "code": {"text": "Impedância Pulmonar (Inspiração)"},
        "valueQuantity": {"value": 0.947524, "unit": "∆Z"},
        "subject": {"reference": "Patient/patient-004"}
    },
    # diferença de inspiração participante 5
    {
        "resourceType": "Observation",
        "id": "obs-005",
        "status": "final",
        "code": {"text": "Impedância Pulmonar (Inspiração)"},
        "valueQuantity": {"value": 0.668257, "unit": "∆Z"},
        "subject": {"reference": "Patient/patient-005"}
    }
]
