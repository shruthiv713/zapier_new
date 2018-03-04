from src import app
from flask import Flask,jsonify,request,render_template,make_response,abort
import requests
import json

tname=""
app=Flask(__name__,template_folder='templates')
@app.route('/')
def get_names():
	url = "https://data.normally12.hasura-app.io/v1/query"

# This is the json payload for the query
	requestPayload = {
    	"type": "run_sql",
    	"args": {
        	"sql": "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND 	table_type='BASE TABLE'; "
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
	
	return render_template('get_table.html',names=arr)
@app.route("/result" , methods=['GET', 'POST'])
def test():
	select = str(request.form.get('table_name'))
	a='\''
	sel=a+select+a
	global tname
	tname=select
	arr=get_col(sel)	
	return render_template('cols.html',col=arr,tname=select) # just to see what select is

def get_col(table_name):
	

# This is the url to which the query is made
	url = "https://data.normally12.hasura-app.io/v1/query"
	sql_query="select column_name from information_schema.columns where table_name ="+table_name
# This is the json payload for the query
	requestPayload = {
	    "type": "run_sql",
	    "args": {
	        "sql": sql_query
 #put table_name selected 
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
	for a in res[1:]:
		r=str(a)
		s=r[3:len(r)-2]
		arr.append(s)
		print s
	return arr
@app.route("/insert",methods=['GET', 'POST'])
def get_articles():
	result = request.form
	print "Table name*******"
	global tname
	print tname
	diction={}
	print "key value"
	for key, value in result.iteritems():
		print key
		print value		
		diction[key]=value
	r = json.dumps(diction)
	loaded_r = json.loads(r)
# This is the url to which the query is made
	url = "https://data.normally12.hasura-app.io/v1/query"

# This is the json payload for the query
	requestPayload = {
    	"type": "insert",
    	"args": {
        "table": tname,
        "objects": [
            loaded_r
        ]
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

	url = 'https://hooks.zapier.com/hooks/catch/2982892/zxgukj/'
	requests.post(url, json={'table': tname})
	return render_template('notify.html',table=tname)
if __name__=='__main__':
    	app.run(debug=True)
