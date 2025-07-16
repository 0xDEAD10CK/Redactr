from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

# --- Models ---
class Applicant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(120))
	email = db.Column(db.String(120))
	phone = db.Column(db.String(20))
	resume_filename = db.Column(db.String(200))
	photo_filename = db.Column(db.String(200))
	created_at = db.Column(db.DateTime, default=datetime.now())


@app.route('/')
def home():
	return "Welcome to homepage!"

@app.route('/about')
def about():
	return "Welcome to About!"

@app.route("/apply", methods=["GET", "POST"])
def apply():
	if request.method == "POST":
		name = request.form["full_name"]
		email = request.form["email"]
		phone = request.form["phone"]

		resume = request.files.get("resume")
		photo = request.files.get("photo")

		print("Received files:", resume, photo)
		print("Received form data:", name, email, phone)

		if resume is None or resume.filename == "":
			flash("Resume is required.")
			return redirect(request.url)

		print("Received application from:", name, email, phone)

		# Save files
		resume_filename = secure_filename(resume.filename)
		resume_path = os.path.join(app.config["RESUME_FOLDER"], resume_filename)
		resume.save(resume_path)

		photo_filename = None
		if photo and photo.filename != "":
			photo_filename = secure_filename(photo.filename)
			photo_path = os.path.join(app.config["PHOTO_FOLDER"], photo_filename)
			photo.save(photo_path)

        # Save to DB
		applicant = Applicant(
			full_name=name,
			email=email,
			phone=phone,
			resume_filename=resume_filename,
			photo_filename=photo_filename,
		)
		db.session.add(applicant)
		db.session.commit()

		return redirect(url_for("thank_you"))

	return render_template("apply.html")

@app.route("/thanks")
def thank_you():
    return "<h2>Thanks for applying! We'll be in touch.</h2>"

# --- Init ---
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
