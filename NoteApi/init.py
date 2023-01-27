from config import DevelopmentConfig, TestingConfig
from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__)
    if test_config is None:
        app.config.from_object(DevelopmentConfig)
    elif test_config == 'test':
        app.config.from_object(TestingConfig)

    return app
