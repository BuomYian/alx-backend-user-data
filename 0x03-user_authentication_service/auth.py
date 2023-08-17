#!/usr/bin/env python3
"""
define a _hash_password method
"""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User

def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed and salted password.
    """
    salt = bcrypt.gensalt()
    encoded_pw = bcrypt.hashpw(password.encode("utf-8"), salt)
    return encoded_pw

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Adds a new user to the database.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User ${email} already exists")
