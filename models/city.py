#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    state_id = ""
    name = ""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))

    @property
    def cities(self):
        city_list = []
        for city in self.cities:
            if self.id == city.state_id:
                city_list.append(city)
        return city_list
