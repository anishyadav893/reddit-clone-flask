from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello people.'

if __name__ == '__main__':
	app.run(debug = True)