import os
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Base:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    PORT = 5000
    SECRET_KEY = "My secret key =)"
    RESTFUL_JSON = {
        'ensure_ascii': False,
    }


class DevConfig(Base):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'main.db'}"


class TestConfig(Base):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Config(TestConfig):
    """
    ===============================================
     Для запуска тестов наследуемся от TestConfig
     Для запуска app.py наследуемся от DevConfig
    ===============================================
    """
    pass
