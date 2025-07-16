from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return "Welcome to homepage!"

@app.route('/about')
def about():
	return "Welcome to About!"

@app.route('/apply')
def apply():
	return render_template("apply.html")

if __name__ == '__main__':
	app.run(debug=True)
