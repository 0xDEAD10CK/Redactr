from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Welcome to homepage!"

@app.route('/about')
def about():
	return "Welcome to About!"

if __name__ == '__main__':
	app.run(debug=True)
