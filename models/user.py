#!/usr/bin/python3
"""This module defines a class User"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
