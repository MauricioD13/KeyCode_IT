import requests
from env_vars_Odoo import *

# Authenticate and get the UID
url = f"{odoo_url}/web/session/authenticate"
headers = {"Content-Type": "application/json"}
data = {
    "jsonrpc": "2.0",
    "params": {
        "db": db,
        "login": username,
        "password": password,
    },
}

response = requests.post(url, headers=headers, json=data)
response_data = response.json()

if "error" in response_data:
    print("Authentication failed:", response_data["error"]["data"]["message"])
else:
    uid = response_data["result"]["uid"]
    print(f"UID: {uid}")

    # Create a connection to the model
    url = f"{odoo_url}/web/dataset/call_kw/res.partner/check_access_rights"
    data = {
        "jsonrpc": "2.0",
        "params": {
            "model": "res.partner",
            "method": "check_access_rights",
            "args": ["read"],
            "kwargs": {"raise_exception": False},
        },
        "id": 1,
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    print(response_data)
