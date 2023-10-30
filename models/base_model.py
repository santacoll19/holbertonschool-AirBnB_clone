#!/usr/bin/python3
"""Unittest for BaseModel class"""

import uuid
from datetime import datetime


class BaseModel:
    """This is the BaseModel class"""

    def __init__(self):
        """Initialization of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the class"""
        return F"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary"""
        class_dict = dict(self.__dict__)
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
