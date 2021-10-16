import requests
import json
import sqlite3 as sl
import databse_helper as dbh

def database():
    db = sl.connect('penguin-protocol-test.db')
    #dbh.drop_all_db(db)
    dbh.create_db(db)
    
    r = dbh.select_db(db, "*", "REVIEW")
    print(r)

    db.row_factory = sl.Row
    r = dbh.print_db(db)
    r = json.dumps([dict(ix) for ix in r])
    print(r)

    r = dbh.select_db(db, "*", "REVIEW", "stars = 5")
    r = json.dumps([dict(ix) for ix in r])
    print(r)

def main():
    #r = requests.get("http://localhost/test")
    # r = requests.post(url="http://localhost/post", data=json.dumps({"input": 1234}), headers={'Content-type': 'application/json'})
    # print(r.text)
    database()

if __name__ == "__main__":
    main()