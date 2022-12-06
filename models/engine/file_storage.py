#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
#from models.base_model import BaseModel\
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        objt = {}
        if cls:
            if cls.__name in self.classes:
                for i, val in self.__objects.items():
                    cls_name = i.split('.')
                    if cls_name[0] == cls.__name__:
                        objt[i] = val
        else:
            objt = self.__objects
        return objt

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            self.__objects.update({obj.to_dict()['__class__'] +
                                      '.' + obj.id: obj})

    def delete(self, obj=None):
        """Deletes object from __object parameter"""
        if obj:
            key = "{}.{}".format(obj.__name__, obj.id)
            del self.__objects[key]

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = self.classes[val
                                                         ['__class__']](**val)
        except FileNotFoundError:
            pass
