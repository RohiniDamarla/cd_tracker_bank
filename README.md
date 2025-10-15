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

⚙️ Setup Instructions
Follow these steps to get the CD Tracker Bank app running locally:

🧬 1. Clone the Repository
git clone https://github.com/RohiniDamarla/cd_tracker_bank.git
cd cd_tracker_bank

🧪 2. Create a Virtual Environment
python -m venv venv

Activate it:
- - Windows
venv\Scripts\activate
- Mac/Linux
source venv/bin/activate

📦 3. Install Dependencies
pip install -r requirements.txt

🚀 4. Run the App
You can start the app with:
python app.py runserver

The app will be available at:
🌐 http://127.0.0.1:5000




---







