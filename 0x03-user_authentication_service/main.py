#!/usr/bin/env python3
"""A simple ene to end integration test for `app.py`
"""

import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """
    Register a new user.

    Args:
        email (str): Email of the user.
        password (str): Password of the user.

    Returns:
        None
    """
    response = requests.post(
        f"{BASE_URL}/users", data={"email": email, "password": password})
    assert response.status_code == 200
    print("User registered successfully")


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Attempt to log in with the wrong password.

    Args:
        email (str): Email of the user.
        password (str): Wrong password.

    Returns:
        None
    """
    response = requests.post(f"{BASE_URL}/sessions",
                             data={"email": email, "password": password})
    assert response.status_code == 401
    print("Logged in with wrong password")


def log_in(email: str, password: str) -> str:
    """
    Log in a user.

    Args:
        email (str): Email of the user.
        password (str): Password of the user.

    Returns:
        str: Session ID
    """
    response = requests.post(f"{BASE_URL}/sessions",
                             data={"email": email, "password": password})
    assert response.status_code == 200
    session_id = response.cookies.get("session_id")
    print("Logged in successfully")
    return session_id


def profile_unlogged() -> None:
    """
    Check profile while unlogged.

    Returns:
        None
    """
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403
    print("Profile accessed while unlogged")


def profile_logged(session_id: str) -> None:
    """
    Check profile while logged in.

    Args:
        session_id (str): Session ID of the user.

    Returns:
        None
    """
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200
    print("Profile accessed while logged in")


def log_out(session_id: str) -> None:
    """
    Log out the user.

    Args:
        session_id (str): Session ID of the user.

    Returns:
        None
    """
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert response.status_code == 302
    print("Logged out successfully")


def reset_password_token(email: str) -> str:
    """
    Get reset password token.

    Args:
        email (str): Email of the user.

    Returns:
        str: Reset password token
    """
    response = requests.post(
        f"{BASE_URL}/reset_password", data={"email": email})
    assert response.status_code == 200
    reset_token = response.json()["reset_token"]
    print("Reset password token obtained")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update password using reset token.

    Args:
        email (str): Email of the user.
        reset_token (str): Reset password token.
        new_password (str): New password.

    Returns:
        None
    """
    response = requests.put(
        f"{BASE_URL}/reset_password",
        data={"email": email, "reset_token": reset_token,
              "new_password": new_password}
    )
    assert response.status_code == 200
    print("Password updated successfully")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
