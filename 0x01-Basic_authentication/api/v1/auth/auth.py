#!/usr/bin/env python3
"""
Class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar

class Auth:
    """ Class to manage authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Implement for checking authentication
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_paths in excluded_paths:
            if excluded_paths.endswith('/') and path.startswith(excluded_paths):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieving authorization header
        """
        if request is None:
            return None
        auth_header = request.headers.get("Authorization")
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieving current user
        """
        return None