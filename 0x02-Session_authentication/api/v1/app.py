#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None  # Initializing auth a None

if os.getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif os.getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()
elif os.getenv("AUTH_TYPE") == "session_auth":
    auth = SessionAuth()


@app.before_request
def authenticate_user():
    """Authenticates a user before processing a request.
    """
    if auth:
        excluded_paths = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
            '/api/v1/auth_session/login/'
        ]
        if auth.require_auth(request.path, excluded_paths):
            auth_header = auth.authorization_header(request)
            session_cookie = auth.session_cookie(request)
            if auth_header is None and session_cookie is None:
                abort(401)
            user = auth.current_user(request)
            if user is None:
                abort(403)
            # Assign the authenticated user to the request context
            request.current_user = user


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error):
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = os.getenv("API_PORT", "5000")
    app.run(host=host, port=port)
