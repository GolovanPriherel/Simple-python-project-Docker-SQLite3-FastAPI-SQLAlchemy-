from sqlalchemy import create_engine
from src.Other_Utils.Directories_storage import *


class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.db_connection = self.engine.connect()
