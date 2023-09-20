
from flask import Flask
from .models import ai_agent
from .services import email_service, zoom_service, networking_service, search_service

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Welcome to AI Networking Agent!'

    return app
