import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_dev_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
