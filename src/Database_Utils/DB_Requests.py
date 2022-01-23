from src.Database_Utils.DB_connections import *
from src.Database_Utils.Schemas.DB_Schema import *
from sqlalchemy import insert, select, delete


class DatabaseORM(DatabaseConnection, Tables):
    def __init__(self):
        self.metadata = MetaData()
        Tables.__init__(self)
        DatabaseConnection.__init__(self)

    def create_tables(self):
        self.metadata.create_all(self.engine)

    def show_tables(self):
        req = select([self.table_1])
        info = self.db_connection.execute(req)

        req2 = select([self.table_2])
        info2 = self.db_connection.execute(req2)

        info_dict = list(zip(info.fetchall(), info2.fetchall()))

        return info_dict

    def insert_tables(self) -> None:
        ins = insert(self.table_1)
        self.db_connection.execute(ins,
                                   first_name="Ilya",
                                   last_name="Vtoroy")

        ins2 = insert(self.table_2)
        self.db_connection.execute(ins2,
                                   first_name="Vadim",
                                   last_name="Demon")

    def delete_tables(self):
        deletion = delete(self.table_1)
        self.db_connection.execute(deletion)
