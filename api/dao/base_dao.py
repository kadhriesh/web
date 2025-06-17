
from api.utils.mongo_connection import MongoDBConnection


class BaseDao:
    """
    Base Data Access Object (DAO) class.
    This class serves as a base for all DAO classes, providing common functionality.
    """
    __mongo_instance = None
    def __new__(cls):
        __mongo_instance = MongoDBConnection().get_database()

    @property
    def getmongo_client(self):
        return self.__mongo_instance

    def __init__(self):
       pass

    def commit(self):
        """Commit the current transaction."""
        self.db_session.commit()

    def rollback(self):
        """Rollback the current transaction."""
        self.db_session.rollback()