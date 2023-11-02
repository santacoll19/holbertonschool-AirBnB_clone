#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel


class State(BaseModel):
    """ State Class """
    name = ""

    def __str__(self):
        """String representation of the State instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
