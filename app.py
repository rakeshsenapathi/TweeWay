from flask import Flask

app = Flask(__name__)

#Decorator
@app.route('/')
def index():
	return "Index"

if(__name__ == "__main__"):
	app.run(debug = True)