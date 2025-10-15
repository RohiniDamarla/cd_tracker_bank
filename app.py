#import os
#from flask import Flask, render_template, request, redirect, url_for, flash, session
#from models import db, CD, User
#from flask_login import LoginManager, login_user, logout_user, login_required, #current_user
#from werkzeug.security import generate_password_hash, check_password_hash
#from datetime import datetime, date
#from flask_mail import Mail, Message
from app_core.imports import (
    os, Flask, render_template, request, redirect, url_for, flash, session,
    LoginManager, login_user, logout_user, login_required, current_user,
    generate_password_hash, check_password_hash,
    Mail, Message,
    datetime, date,
    db, CD, User
)
from app_core.app_config import app, mail, db
from routes.curdroutes import curd_bp



login_manager = LoginManager()
login_manager.login_view = 'curd_bp.login'
login_manager.init_app(app)

app.register_blueprint(curd_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from seed_users import seed_admin
print("\n🔍 Registered Flask Endpoints:")
for rule in app.url_map.iter_rules():
    print(f"  • {rule.endpoint} → {rule.rule}")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_admin()

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
