# 💰 CD Tracker Bank

A secure, modular Flask web app for tracking Certificates of Deposit (CDs) across multiple banks. Built for users who want clarity, automation, and control over their financial data.

---

## 🚀 Features

- 🔐 User authentication with password reset
- 🏦 Add, update, and delete CD entries
- 📊 Visual charts for CD maturity and interest trends
- 🧱 Modular architecture using Flask Blueprints
- 📁 Clean folder structure for maintainability
- 🛡️ Secure form handling and session management

---

## 🗂️ Folder Structure
cd_tracker_bank/ ├── app.py                  # Main entry point ├── app_core/               # Configs, imports, seed scripts ├── routes/                 # Modular route files (curdroutes, auth, etc.) ├── templates/              # HTML templates (Bootstrap 5 styled) ├── static/                 # CSS and JS files ├── instance/               # SQLite DB and .gitignore ├── models.py               # SQLAlchemy models ├── requirements.txt        # Python dependencies ├── Procfile                # For deployment (e.g. Heroku) └── .gitignore              # Excludes venv, DB, secrets

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/RohiniDamarla/cd_tracker_bank.git
cd cd_tracker_bank
2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

4. Run the app
#flask run
python app.py runserver
App will run locally at http://127.0.0.1:5000




