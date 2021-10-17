import sqlite3 as sq
from sqlite3.dbapi2 import Connection

def create_db(database: Connection) -> None:
    sql_file = open("create_db.sql", "r")
    data = sql_file.read()
    sql_file.close()
    with database:
        database.executescript(data)
        # database.execute("""
        #     CREATE TABLE IF NOT EXISTS LOCATION (
        #     lid INTEGER PRIMARY KEY,
        #     name TEXT NOT NULL,
        #     address TEXT NOT NULL,
        #     city TEXT NOT NULL,
        #     country TEXT NOT NULL
        # )""")

        # database.execute("""
        #     CREATE TABLE IF NOT EXISTS REVIEW (
        #     rid INTEGER PRIMARY KEY,
        #     uid INTEGER NOT NULL,
        #     date INTEGER NOT NULL,
        #     location TEXT NOT NULL,
        #     text TEXT NOT NULL,
        #     stars INTEGER NOT NULL CHECK (stars >= 1 AND stars <= 5),
        #     price INTEGER NOT NULL CHECK (price >= 1 AND price <= 3)
        # )""")

        # database.execute("""
        #     CREATE TABLE IF NOT EXISTS PROGRAM (
        #     pid INTEGER PRIMARY KEY,
        #     name TEXT NOT NULL,
        #     school TEXT NOT NULL,
        #     city TEXT NOT NULL,
        #     country TEXT NOT NULL
        # )""")

        # database.execute("""
        #     CREATE TABLE IF NOT EXISTS USER (
        #     uid INTEGER PRIMARY KEY,
        #     name TEXT NOT NULL,
        #     sem_attend TEXT NOT NULL,
        #     program INTEGER,
        #     FOREIGN KEY (program) REFERENCES PROGRAM(pid)
        # )""")


def print_db(database: Connection) -> None:
    with database:
        cur = database.cursor()
        cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        return cur.fetchall()



def drop_all_db(database: Connection):
    cur = database.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS REVIEW;
        DROP TABLE IF EXISTS USER;
        DROP TABLE IF EXISTS PROGRAM;
        DROP TABLE IF EXISTS LOCATION;
    """)

def select_db(database: Connection, sel: str, table: str, where: str = ""):
    cur = database.cursor()
    query = "SELECT " + sel + " FROM " + table
    if where != "":
        query = query + " WHERE " + where
    print("QUERY:", query)
    rows = cur.execute(query).fetchall()
    rows_json = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in rows]
    return {"rows": rows_json}

def add_instance(database: Connection, table: str, entry):
    cur = database.cursor()
    q_marks = "?," * len(entry)
    cur.execute("INSERT INTO " + table + " VALUES (" + q_marks[0:-1] + ")", entry)
    return cur.lastrowid

def fill_table_test(database: Connection):
    sql_file = open("add-crap.sql", "r")
    data = sql_file.read()
    sql_file.close()
    with database:
        database.executescript(data)