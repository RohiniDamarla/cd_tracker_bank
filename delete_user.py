from app import app
from models import db, User, CD

def delete_user_by_name(name):
    with app.app_context():
        user = User.query.filter_by(username=name).first()
        if not user:
            print(f"⚠️ User '{name}' not found.")
            return

        # Delete all CDs linked to this user
        cds = CD.query.filter_by(user_id=user.id).all()
        for cd in cds:
            db.session.delete(cd)

        # Now delete the user
        db.session.delete(user)
        db.session.commit()
        print(f"✅ Deleted user '{name}' and {len(cds)} linked CDs.")

if __name__ == '__main__':
    delete_user_by_name('Mahendra')