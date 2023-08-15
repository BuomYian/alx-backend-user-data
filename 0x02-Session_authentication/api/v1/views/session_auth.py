#!/usr/bin/env python3
"""
SessionAuth view module
"""

from flask import Flask, request, jsonify
from models.user import User
from api.v1.app import auth


def create_session_auth_view():
    """
    create session auth view
    """
    app = Flask(__name__)

    @app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
    def auth_session_login():
        """
        Handles session authentication login
        """
        email = request.form.get('email')
        password = request.form.get('password')

        if not email:
            return jsonify({'error': 'email missing'}), 400
        if not password:
            return jsonify({'error': 'password missing'}), 400

        user = User.search({'email': email})
        if not user:
            return jsonify({'error': 'no user found for this email'}), 404
        if not user[0].is_valid_password(password):
            return jsonify({'error': 'wrong password'}), 401

        session_id = auth.create_session(user[0].id)
        user_json = user[0].to_json()
        response = jsonify(user_json)
        response.set_cookie(auth.SESSION_NAME, session_id)
        return response, 200

    return app
