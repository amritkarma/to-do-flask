from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from app.config import DevelopmentConfig, ProductionConfig
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()

def create_app():
    env = os.getenv("FLASK_ENV", "development")

    if env == "development":
        app = Flask(__name__, instance_relative_config=True)
        os.makedirs(app.instance_path, exist_ok=True)
        app.config.from_object(DevelopmentConfig)
    else:
        app = Flask(__name__)
        app.config.from_object(ProductionConfig)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)

    return app
