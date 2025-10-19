from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt, cors
from .routes.users import users_bp

def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    app.register_blueprint(users_bp, url_prefix="/users")

    @app.route("/")
    def index():
        return {"message": "API running"}

    return app
