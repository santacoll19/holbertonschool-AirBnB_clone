#!/usr/bin/python3
"""This module defines a class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines a amenity"""
    name = ""

    def __str__(self):
        """Returns a string representation of the Amenity instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
