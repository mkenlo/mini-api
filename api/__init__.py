
from flask import Flask
from flask_cors import CORS
from .app import api as api_bp


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)    
    app.register_blueprint(api_bp)
    CORS(app)
    return app
