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
    r = json.dumps([dict(ix) for ix in r], indent=4)
    print(r)

    #dbh.fill_table_test(db)

    r = dbh.select_db(db, "*", "REVIEW", "stars = 5")
    r = json.dumps([dict(ix) for ix in r], indent=4)
    print(r)

    print("*" * 20)

    r = requests.get("http://localhost/basic-query", data=json.dumps({"sel": "*", "table": "REVIEW", "where": "stars > 4"}), headers={'Content-type': 'application/json'})
    r = json.dumps([dict(ix) for ix in r], indent=4)
    print(r.text)

def main():
    #r = requests.get("http://localhost/test")
    # r = requests.post(url="http://localhost/post", data=json.dumps({"input": 1234}), headers={'Content-type': 'application/json'})
    # print(r.text)
    database()

if __name__ == "__main__":
    main()