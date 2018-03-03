import requests
import json

# This is the url to which the query is made
url = "https://data.normally12.hasura-app.io/v1/query"

# This is the json payload for the query
requestPayload = {
    "type": "run_sql",
    "args": {
        "sql": "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'; "
    }
}

# Setting headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 54bf39e989178501287cc9fab40b9be406a4452d0189b979"
}

# Make the query and store response in resp
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

# resp.content contains the json response.
data=resp.content
d = json.loads(data)
res=d["result"]
arr=[] 
for a in res[2:]:
	r=str(a)
	s=r[3:len(r)-2]
	arr.append(s)
	print s
#arr contains all table names 
	
