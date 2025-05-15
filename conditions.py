fhir_conditions = [
      {
        "resourceType": "Condition",
        "id": "cond-001",
        "subject": {"reference": "Patient/patient-001"},
        "code": {"text": "Ventilação Pulmonar Simétrica"},
        "clinicalStatus": {"text": "active"},
        "verificationStatus": {"text": "confirmed"},
        "note": [{"text": "∆Z de expiração inferior a 0.5, o que indica simetria ventilatória."}],
        "onsetDateTime": "2025-05-14T00:00:00"
    },
      {
        "resourceType": "Condition",
        "id": "cond-002",
        "subject": {"reference": "Patient/patient-002"},
        "code": {"text": "Ventilação Pulmonar Simétrica"},
        "clinicalStatus": {"text": "active"},
        "verificationStatus": {"text": "confirmed"},
        "note": [{"text": "∆Z de inspiração inferior a 0.5, o que indica simetria ventilatória."}],
        "onsetDateTime": "2025-05-14T00:00:00"
    },
     {
        "resourceType": "Condition",
        "id": "cond-003",
        "subject": {"reference": "Patient/patient-003"},
        "code": {"text": "Ventilação Pulmonar Simétrica"},
        "clinicalStatus": {"text": "active"},
        "verificationStatus": {"text": "confirmed"},
        "note": [{"text": "∆Z de expiração inferior a 0.5, o que indica simetria ventilatória."}],
        "onsetDateTime": "2025-05-14T00:00:00"
    },
    {
        "resourceType": "Condition",
        "id": "cond-004",
        "subject": {"reference": "Patient/patient-004"},
        "code": {"text": "Ventilação Pulmonar Assimétrica"},
        "clinicalStatus": {"text": "active"},
        "verificationStatus": {"text": "confirmed"},
        "note": [{"text": "∆Z de inspiração superior a 0.5, o que indica assimetria ventilatória."}],
        "onsetDateTime": "2025-05-14T00:00:00"
    },
    {
        "resourceType": "Condition",
        "id": "cond-005",
        "subject": {"reference": "Patient/patient-005"},
        "code": {"text": "Ventilação Pulmonar Assimétrica"},
        "clinicalStatus": {"text": "active"},
        "verificationStatus": {"text": "confirmed"},
        "note": [{"text": "∆Z de inspiração superior a 0.5, o que indica assimetria ventilatória."}],
        "onsetDateTime": "2025-05-14T00:00:00"
    }
]
