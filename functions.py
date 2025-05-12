
from patients import *
from observations import *


def patient_info(num_patients):
    for patient in range(num_patients):

        patient = fhir_patients[patient]

        print("--------------------------------------------------------------------------------")
        print("Full name:", " ".join(patient["name"][0]["given"]), patient["name"][0]["family"])
        print("Gender:", patient["gender"])
        print("Birth Date:", patient["birthDate"])
        print("--------------------------------------------------------------------------------")


def patient_obs(num_patient):
    patient_id = "patient-00"+str(num_patient)
    patient_obs = [obs for obs in fhir_observations if obs["subject"]["reference"] == f"Patient/{patient_id}"]

    for obs in patient_obs:
        print(f"{obs['code']['text']}: {obs['valueQuantity']['value']} {obs['valueQuantity']['unit']}")