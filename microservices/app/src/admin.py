import requests
import json

# This is the url to which the query is made
url = "https://auth.normally12.hasura-app.io/v1/login"

# This is the json payload for the query
requestPayload = {
    "provider": "username",
    "data": {
        "username": "admin",
        "password": "femlixa-wziyoxc-esulmun-emhoba"
    }
}

# Setting headers
headers = {
    "Content-Type": "application/json"
}

# Make the query and store response in resp
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

# resp.content contains the json response.
print(resp.content)
