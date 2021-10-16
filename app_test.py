import requests
import json
import sqlite3 as sl
import databse_helper as dbh

def database():
    db = sl.connect('penguin-protocol.db')
    dbh.create_db(db)
    dbh.print_db(db)

def main():
    #r = requests.get("http://localhost/test")
    # r = requests.post(url="http://localhost/post", data=json.dumps({"input": 1234}), headers={'Content-type': 'application/json'})
    # print(r.text)
    database()

if __name__ == "__main__":
    main()