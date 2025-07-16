# Redactr
A privacy-focused, web-based hiring tool that enables anonymous resume/CV screening to help reduce unconscious bias in recruitment.

## Features

- Applicants submit resumes with name, email, phone and optional photo.
- Automatically stores both the original and redacted versions.
- Recruiters see only anonymized resumes with unique IDs.
- Original details are only revealed upon shortlisting.
- Simple recruiter dashboard and applicant form.
- Built with Python, Flask and SQLite (PostgreSQL-ready)

## 🚀 Features

This project is ideal for small businesses, ethical startups, or any organization aiming to reduce hiring bias and improve fairness in early-stage candidate screening.

## 📦 Tech Stack

- Python + Flask
- SQLAlchemy

## 📁 Project Structure

Redactr/  
├── app.py  
├── templates/  
│ └── apply.html  
├── uploads/  
├── instance/  
│ └── config.py  
├── requirements.txt  

## 🛡 Security Considerations

- Resume/photo uploads use sanitized filenames
- Email/phone/name redaction logic (WIP in redactor module)
- Recruiter view is intentionally blind to prevent early bias
- Admin access can be protected with Flask-Login or basic auth

## 🛠 Roadmap

- ✅ Applicant resume submission
- ✅ Resume redaction module
- ⬜ Recruiter dashboard
- ⬜ Role-based login
- ⬜ Export to CSV
- ⬜ ATS API integration
