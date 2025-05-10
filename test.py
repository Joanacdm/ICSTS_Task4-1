import requests
import json
import sys
import os

"""
 - Define uma função chamada `cls()` que **limpa o terminal/console**.
  - Se estiver no Windows (`os.name == 'nt'`), executa o comando `cls`.
  - Se estiver em Linux/Mac, executa `clear`.

> ⚠️ Para funcionar, o módulo `os` precisa estar importado: `import os`.

"""

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------------------------ URL do servidor FHIR
url = "https://hapi.fhir.org/baseR4/"

"""
- Define os **headers HTTP** usados nas requisições:
  - `"Content-Type"`: indica que o corpo da requisição está em **formato FHIR codificado em JSON**.
  - `"Accept"`: indica que a resposta esperada também deve estar em **formato FHIR JSON**.

"""

#------------------- Headers que indicam que o pedido FHIR usa JSON
headers = {
    "Content-Type": "application/fhir+json",
    "Accept": "application/fhir+json"
}

"""
"resourceType": "Patient" → tipo de recurso FHIR
"name" → lista de nomes, com "family" (apelido) e "given" (prenomes)
"gender" → sexo do paciente ("male", "female", "other", "unknown")
"birthDate" → data de nascimento (formato ISO: AAAA-MM-DD)

"""

#-----------------------Exemplo de um recurso Patient no formato FHIR
fhir_patient = {
	"resourceType": "Patient",
	 "name": [
		{ "family": "Carapau", "given": [ "Anastacio", "Manuel" ] } 
	],
	"gender": "male",
	"birthDate": "1974-12-25"
}

"""
"resourceType": "Observation" → tipo do recurso
"status": "final" → status da observação (pode ser registered, preliminary, final, etc.)
"code" → descreve o tipo da observação, usando LOINC, um sistema padrão para exames clínicos
    "29463-7" é o código LOINC para peso corporal
"subject" → referência ao paciente (pelo id)
"effectiveDateTime" → data em que a observação foi realizada
"valueQuantity" → valor da observação:
    "value": 85
    "unit": "Kgs"
    "system": sistema padrão para unidades (aqui http://unitsofmeasure.org)
    "code": código da unidade (⚠️ está com [lb_av] que é libras — isso não combina com "Kgs")

"""
#------------------------------------- Observation
fhir_observation = {
	"resourceType": "Observation",
	"status": "final",
	"code": {
		"coding": [
			{
				"system": "http://loinc.org",
				"code": "29463-7",
				"display": "Body Weight"
			}
		]
	},
	"subject": {
		"reference": "Patient/47119777" #ID IMPORTANT
	},
	"effectiveDateTime": "2016-03-28",
	"valueQuantity": {
		"value": 85,
		"unit": "Kgs",
		"system": "http://unitsofmeasure.org",
		"code": "[lb_av]"
	}
}

#========================================================
# POST  
# ========================================================
#-------------------- Criar um patient - Enviando a requisição POST para o servidor FHIR

"""
Envia uma requisição POST para criar um novo paciente no servidor.
Os dados estão em fhir_patient (que definiste antes).
Usa Content-Type: application/fhir+json.
"""

url ="https://hapi.fhir.org/baseR4/Patient"
response = requests.post(url, data=json.dumps(fhir_patient), headers=headers)

# Verificando o status da resposta
if response.status_code == 201:
    data = response.json()
    resource_id = data.get("id")  # Supondo que o campo ID esteja no JSON
    #os.system('cls')
    print("-----------------------------------")
    print("Paciente criado com sucesso ID:",resource_id)
    print("-----------------------------------\n")
    print("Resposta do servidor:", data,"\n")
else:
    print("Erro ao criar o paciente.\n")
    print("Status:", response.status_code,"\n")
    print("Resposta:", response.text,"\n")

       
#========================================================
# GET ========================================================
#----------------- Aceder dados patient - Enviando a requisição POST para o servidor FHIR

url = "https://hapi.fhir.org/baseR4/Patient/47119777"
response = requests.get(url, data=json.dumps(fhir_patient), headers=headers)
print(response.json())

#--------------------------- save the result - file patient.txt 
with open("patient.txt", 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4)
resource_id = data.get("id")  # Supondo que o campo ID esteja no JSON

sys.exit()


#===========================================================
# OBSERVATION 
#-------------------------------------- Criar observação  resource

url = "https://hapi.fhir.org/baseR4/Observation/"
response = requests.post(url, data=json.dumps(fhir_observation), headers=headers)
print("OBSERVATION :", response.status_code)
data = response.json()
resource_id = data.get("id")  # Supondo que o campo ID esteja no JSON

#===========================================================
#---------- Aceder observação
# GET
url = "https://hapi.fhir.org/baseR4/Observation/"+str(resource_id)
response = requests.get(url, data=json.dumps(fhir_patient), headers=headers)
print(response.json())

#--------------------------- save the result - file observation.txt 
with open("observation.txt", 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4)

