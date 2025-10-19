import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI",
        "mysql+pymysql://root:admin@127.0.0.1:3306/horus_faeruz_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-string")
