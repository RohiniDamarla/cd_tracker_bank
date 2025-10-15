# seed_users.py
#from app import app
from app_core.app_config import app
from models import db, User
from werkzeug.security import generate_password_hash

def seed_admin():
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin_user = User(
                username='admin',
                email='admin@example.com',
                password=generate_password_hash('admin123'),
                is_locked=False
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Admin user seeded")