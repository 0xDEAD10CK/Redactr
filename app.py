from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

# --- Models ---
class Applicant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(120))
	email = db.Column(db.String(120))
	phone = db.Column(db.string(20))
	resume_filename = db.Column(db.String(200))
	photo_filename = db.Column(db.String(200))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)


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
