from sqlalchemy.orm import scoped_session, sessionmaker





class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
            

    def all(self, cls=None):
        if cls is None:
            query = self.__session.query(User, State, City, Amenity, Place, Review).all()
        query = self.__session.query(cls)
        query_results = dict()
        for row in query:
            key = '{}.{}'.format(type(row).__name__, row.id)
            query_results[key] = row
        return query_results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__session)
        self.__session = scoped_session(sessionmaker(
                                        bind=self.__engine,
                                        expire_on_commit=False))