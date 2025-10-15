# app_core/app_config.py

import os
from flask import Flask
from flask_mail import Mail
from models import db

# 📁 Ensure instance folder exists
if not os.path.exists('instance'):
    os.makedirs('instance')

# 🚀 Initialize Flask app
#app = Flask(__name__)
app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))



app.secret_key = 'Riansh@819'  # Replace with something unpredictable in production!

# 🔧 Core configuration
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 📧 Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rohinivelagapudi@gmail.com'
app.config['MAIL_PASSWORD'] = 'zjcw dlee ajgu fcvv'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@cdtracker.com'

# 📬 Initialize extensions
mail = Mail(app)
db.init_app(app)

# ✅ Export for use in app.py
__all__ = ['app', 'mail', 'db']