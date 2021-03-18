"""
This module instantiates the models in the models.py file
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy import event
import sqlite3
import os

from content_scraper.db import models


class DBManager:
    Base = models.Base

    def __init__(
        self,
        database=os.getenv("DATABASE_NAME", default="content_scraper"),
        folder_path=os.getenv("DATABASE_FOLDER", default="./"),
        version=os.getenv("DATABASE_VERSION", default="0.1.0"),
    ):
        """Initalizes dbm object which can provide sessions

        :param str database: name of the database
        :param str folder_path: output folder
        :param str version: version string

        """
        self.database = database
        self.folder_path = folder_path
        self.version = version

        self.create_db()

    def create_db(self):
        """Initialize db with an engine"""
        if self.folder_path != "" and not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        self.sqlite_path = f"{os.path.join(self.folder_path,f'{self.database}_{self.version}')}.sqlite3"
        self.engine = self.create_engine()
        self.Base.metadata.create_all(self.engine)

    def create_engine(self):
        """Creates a new engine connecting to the db

        :return: sqlalchemy Engine object
        :rtype: Engine

        """
        return create_engine(
            f"sqlite:///{self.sqlite_path}",
            connect_args={"check_same_thread": False},
        )

    def get_session(self):
        """Returns a new session object the current engine

        :return: sqlalchemy Session
        :rtype: session

        """
        Session = sessionmaker(bind=self.engine)
        return Session()

    def drop_all(self):
        """Drop all tables in db

        :return: True if success
        :rtype: bool

        """
        self.Base.metadata.drop_all(self.engine)
        return True

    def delete_db(self):
        """Delete db construct (sqlite file)

        :return: True if success
        :rtype: bool

        """
        os.remove(self.sqlite_path)
        return True

    def wipe(self):
        """Drop all tables and delete file"""
        self.Base.metadata.drop_all(bind=self.engine)
        self.Base.metadata.create_all(bind=self.engine)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Ensures foreign key"""
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
