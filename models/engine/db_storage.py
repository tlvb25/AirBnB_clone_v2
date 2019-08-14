#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize an instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query all objects from the current db session, based on class name
        """
        if cls is None:
            query = self.__session.query(User,
                                         State,
                                         City,
                                         Place,
                                         Review).all()
        else:
            query = self.__session.query(cls)
        query_results = {}
        for classes in query:
            key = '{}.{}'.format(type(classes).__name__, classes.id)
            query_results[key] = classes
        return query_results

    def new(self, obj):
        """add the object to the current databse session
        """
        self.__session.add(obj)

    def save(self):
        """commits changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
