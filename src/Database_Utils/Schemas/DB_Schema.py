from sqlalchemy import MetaData, Table, Integer, Column, Text

metadata = MetaData()


class Tables:
    table_1 = Table('table1', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('first_name', Text(), nullable=False),
                    Column('last_name', Text(), nullable=False))

    table_2 = Table('table2', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('first_name', Text(), nullable=False),
                    Column('last_name', Text(), nullable=False))
