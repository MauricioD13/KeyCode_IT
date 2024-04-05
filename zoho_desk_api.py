import requests
import json
from env_vars_Zoho import *

def auth_token(grant_token, client_secret, client_id):
    URL = "https://accounts.zoho.eu/oauth/v2/token"
    code_token = grant_token

    headers = {
        "grant_type": "authorization_code",
        "client_id": f"{client_id}",
        "client_secret": f"{client_secret}",
        "code": f"{code_token}",
    }
    # print(headers)
    req = requests.post(url=URL, data=headers)
    print(req)
    try:
        data = req.json()
        print(data)
    except:
        print("Error JSON")
    return data["access_token"]


def article_list(access_token):
    URL = "https://desk.zoho.eu/api/v1/articles"
    headers = {"Authorization": f"Zoho-Oauthtoken {access_token}"}
    req = requests.get(url=URL, headers=headers)

    data = req.json()

    print(json.dumps(data, indent=2))


def article_create(access_token, client_secret):
    URL = "https://desk.zoho.eu/api/v1/articles"
    headers = {
        "orgId": orgID,
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }
    params = (
        ("orgId", orgID),
        ("authtoken", client_secret),
    )
    data = '{ "seoDescription" : "Knowledge Base for your product", "permission" : "ALL", "title" : "Importance of a Knowledge Base", "authorId" : 22372000000094004, "seoTitle" : "Knowledge Base", "seoKeywords" : "Helpcenter, Knowledge Base", "tags" : [ "knowledge base", "helpcenter" ], "expiryDate" : "2018-05-21T05:55:00.000Z", "isSEOEnabled" : true, "answer" : "The knowledge base is a key component of a good help center. This is where you can share the basics of using your products or services to your customers. Help articles and FAQs are great assets when it comes to answering the most fundamental questions your customers might have regarding your offerings. Help articles also ease the burden of your customer support agents by enabling self-service.", "permalink" : "knowledgebase", "categoryId" : 22372000000094160, "status" : "Draft" }'

    response = requests.post(
        f"https://desk.zoho.eu/api/v1/articles",
        headers=headers,
        params=params,
        data=data,
    )

    # req = requests.post(url=URL, headers=headers, data=str(data))
    print(response)


def get_viewId(access_token):
    URL = "https://desk.zoho.eu/api/v1/views"
    headers = {
        "orgId": orgID,
        "Authorization": f"Zoho-oauthtoken {access_token}",
    }
    params = {("module", "tickets"), ("departmentId", "161824000000007061")}
    response = requests.get(url=URL, headers=headers, params=params)
    print(response.json())


# access_token = auth_token(grant_token,client_secret,client_id)
print("TOKEN DE ACCESO: ", access_token)


# article_list(access_token)
# article_create(access_token, client_secret)
get_viewId(access_token)
