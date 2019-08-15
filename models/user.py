#!/usr/bin/python3
"""This is the user class"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
    """
    # DBStorage class attribute
    __tablename__ = 'users'
    # DBStorage class attributes
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
