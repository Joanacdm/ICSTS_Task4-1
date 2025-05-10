import requests
import json
import sys
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

base_url = "https://hapi.fhir.org/baseR4/"

headers = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/fhir+json"
}

# Get all patients
url = base_url + "Patient?_count=5" 

response = requests.get(url, headers=headers)

if response.status_code == 200:
    all_patients = response.json()
    
    # Salva todos os pacientes em um arquivo
    with open("all_patients.txt", 'w', encoding='utf-8') as file:
        json.dump(all_patients, file, indent=4)

    print("Lista de pacientes salva em all_patients.txt")
else:
    print("Erro ao buscar pacientes.")
    print("Status:", response.status_code)
    print("Resposta:", response.text)