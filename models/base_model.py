#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import uuid
from datetime import datetime
import json


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """Initialize variables"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print a str"""
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """ Update the attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Return a dictionary """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
