#!/usr/bin/env python3
"""
define a _hash_password method
"""

import bcrypt


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
