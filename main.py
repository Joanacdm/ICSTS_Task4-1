import requests
import json
import sys
import os
from functions import *
from observations import *



def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

base_url = "https://hapi.fhir.org/baseR4/"

headers = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/fhir+json"
}

# Print Patient Info
#patient_info(5)

# Get Observation from patient
num_patient=1
patient_obs(num_patient)
