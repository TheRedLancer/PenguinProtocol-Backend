import sqlite3 as sq
from sqlite3.dbapi2 import Connection

def create_db(database: Connection) -> None:
    sql_file = open("create_db.sql", "r")
    data = sql_file.read()
    sql_file.close()
    with database:
        database.execute("""
            CREATE TABLE IF NOT EXISTS LOCATION (
            lid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        )""")

        database.execute("""
            CREATE TABLE IF NOT EXISTS REVIEW (
            rid INTEGER PRIMARY KEY,
            uid INTEGER NOT NULL,
            date INTEGER NOT NULL,
            location TEXT NOT NULL,
            text TEXT NOT NULL,
            stars INTEGER NOT NULL CHECK (stars >= 1 AND stars <= 5),
            price INTEGER NOT NULL CHECK (price >= 1 AND price <= 3)
        )""")

        database.execute("""
            CREATE TABLE IF NOT EXISTS PROGRAM (
            pid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            school TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        )""")

        database.execute("""
            CREATE TABLE IF NOT EXISTS USER (
            uid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            sem_attend TEXT NOT NULL,
            program INTEGER,
            FOREIGN KEY (program) REFERENCES PROGRAM(pid)
        )""")


def print_db(database: Connection) -> None:
    with database:
        cursor = database.cursor()
        data = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        print(cursor.fetchall())

def print_db_table(database: Connection, table_name: str):
    pass
