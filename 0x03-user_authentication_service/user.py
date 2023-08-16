#!/usr/bin/env python3
"""
This module defines the User model for the 'users' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    Represents a user in the database.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(length=250), nullable=False)
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250), nullable=True)
    reset_token = Column(String(length=250), nullable=True)
