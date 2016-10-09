from flask import Flask 
app = Flask(__name__)  

@app.route("/") 
def hello():     
	return "Hello!" 
	
@app.route('/name/<string:name>', methods=['GET'])
def name(name):
    return 'Your name is %s' %name
	
if __name__ == "__main__":     
	app.run()