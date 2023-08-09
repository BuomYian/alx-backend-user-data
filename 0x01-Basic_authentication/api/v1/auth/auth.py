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
        return False

    def authorization_header(self, request=None) -> str:
        """ retrieving authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieving current user
        """
        return None