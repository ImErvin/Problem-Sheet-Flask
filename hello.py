from flask import Flask 
from flask import request
from flask_cors import CORS, cross_origin

import flask as myFlask

app = myFlask.Flask(__name__)
CORS(app)

@app.route("/") 
def root():     
	return app.send_static_file('index.html')
	
@app.route('/name', methods=['GET','POST'])
def name():
	name = myFlask.request.values["userinput"]
	return 'Your name is ' + name
	
if __name__ == "__main__":     
	app.run()