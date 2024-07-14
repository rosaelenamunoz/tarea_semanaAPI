import requests
import json

#consumir el recurso
URL = "https://api.lambdatest.com/automation/api/v1/platforms"


# Realizar la solicitud GET a la API con autenticación 
respuesta = requests.get(URL)

# Verificar el estado de la solicitud
if respuesta.status_code == 200:
    print('La Solicitud fue exitosa')
    print('Datos Extraidos: ', respuesta.json())
else:
    print('Error al realizar la solicitud del recurso. Detalles: \n', respuesta.text)