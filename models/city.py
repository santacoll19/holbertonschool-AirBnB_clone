#!/usr/bin/python3
""" Modules for City class """

from models.base_model import BaseModel


class City(BaseModel):
    """ Class of city """
    state_id = ""
    name = ""

    def __str__(self):
        """Returns a string representation of the City instance."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
