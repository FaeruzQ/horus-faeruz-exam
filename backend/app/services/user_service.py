from ..extensions import db
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, password, email, nama):
        hashed = generate_password_hash(password)
        user = User(username=username, password=hashed, email=email, nama=nama)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if not user:
            return None
        if check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    # @staticmethod
    # def update_user(user_id, username, email, nama):
    #     user = User.query.get(user_id)
    #     if not user:
    #         return None
    #     user.username = username
    #     user.email = email
    #     user.nama = nama
    #     db.session.commit()
    #     return user

    @staticmethod
    def update_user(user_id, username, email, nama):
        user = User.query.get(user_id)
        if not user:
            return None
            
        user.username = username
        user.email = email
        user.nama = nama
        
        try:
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True
