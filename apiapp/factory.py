"""Factory module helps initialize the Application"""

from flask import Flask, jsonify
from flask_restful import Api
from .helloworld import HelloWorldResource

def create_app():
    """Create an instance of Flask application with all the routes"""
    app = Flask(__name__)
    app.add_url_rule("/health", "health", health_check)

    # Setup Flask-RESTful API extension
    api = Api(app)
    api.add_resource(HelloWorldResource, "/")
    return app


def health_check():
    """Health Check function should perform diagnostics"""
    return jsonify({"status": "ok"})
