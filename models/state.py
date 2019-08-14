#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City
​
​
class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    # DBStorage class attribute
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
​
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    # FileStorage getter attribute
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            return [city for city in models.storage.all(City)
                    if city.state_id == self.id]
