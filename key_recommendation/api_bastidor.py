import requests
import json
import vars

def api_parts_catalog():
    url = "https://api.parts-catalogs.com/v1"
    params = {
        "vin": vars.vin
    }
    headers = {
        "X-Api-Key": vars.api_key
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error: bad request")
# W0LSD9EG9B4207973
def api_ninja():
    url = "https://api.api-ninjas.com/v1/vinlookup"

    params = {
        "vin": vars.vin
    }
    headers = {
        "X-Api-Key": vars.api_key
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error: bad request")
    # Ingition lock
    # Transmitter sub-assy -> mando
    # Key,cut -> Espadin
    
api_ninja()