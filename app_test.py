from flask.json import jsonify
import requests
import json
import sqlite3 as sl
import databse_helper as dbh

def database():
    url = "http://localhost"
    with sl.connect('penguin-protocol-test.db') as db:
        #dbh.drop_all_db(db)
        dbh.create_db(db)
        
        # r = dbh.select_db(db, "*", "REVIEW")
        # print(r)

        # db.row_factory = sl.Row
        # r = dbh.print_db(db)
        # r = json.dumps([dict(ix) for ix in r], indent=4)
        # print(r)

        # #dbh.fill_table_test(db)

        # r = dbh.select_db(db, "*", "REVIEW", "stars = 5")
        # r = json.dumps([dict(ix) for ix in r], indent=4)
        # print(r)

        # print("*" * 20)

        # r = requests.get(url + "/basic-query", data=json.dumps({"sel": "*", "table": "REVIEW", "where": "stars >= 4"}), headers={'Content-type': 'application/json'})
        # print(r.text)

        # data = {"name": "bbq", "address": "848 Main", "city": "Paris", "country": "France"}
        # print("add_location() data:", data)
        # entry = (data["name"], data["address"], data["city"], data["country"])
        # print("add_location() entry:", entry)
        # dbh.add_instance(db, "LOCATION (name, address, city, country)", entry)

        # data = """{"name": "bagels", "address": "999 Second", "city": "Toronto", "country": "Canada"}"""
        # r = requests.post(url + "/add-location", data=data, headers={'Content-type': 'application/json'})
        # print(r)
        
        # rows = dbh.select_db(db, "*", "PROGRAM")
        # # print(json.dumps({"rows": rows}, indent=4))
        # # print(rows_json)
        # for row in rows["rows"]:
        #     print(row)
        # #print(json.dumps({"rows": rows}, indent=4))
        r = requests.get(url + "/basic-query", data=json.dumps({"sel": "*", "table": "PROGRAM", "where": ""}), headers={'Content-type': 'application/json'})
        print(json.dumps(json.loads(r.text), indent=2))  


def main():
    #r = requests.get("http://localhost/test")
    # r = requests.post(url="http://localhost/post", data=json.dumps({"input": 1234}), headers={'Content-type': 'application/json'})
    # print(r.text)
    database()

if __name__ == "__main__":
    main()