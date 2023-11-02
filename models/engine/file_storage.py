#!/usr/bin/python3
"""FileStorage Module"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """FileStorage class to serialize and deserialize instances"""
    __file_path = "file.json"
    __objects = {}
    CLASS_DICT = {"BaseModel": BaseModel,
                  "User": User,
                  "City": City,
                  "Place": Place,
                  "Review": Review,
                  "State": State,
                  "Amenity": Amenity}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    self.__objects[key] = self.CLASS_DICT[value["__class__"]](**value)
