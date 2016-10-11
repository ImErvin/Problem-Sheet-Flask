from flask import Flask 
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/") 
def hello():     
	return "Hello!" 

@app.route('/name')
def enterName():
	return "Please specify your name in the address bar e.g /name/ervin"
	
@app.route('/name/<string:name>')
def name(name):
    return 'Your name is %s' %name
	
if __name__ == "__main__":     
	app.run()