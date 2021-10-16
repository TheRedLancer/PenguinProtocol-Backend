from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sl
import databse_helper as dbh


with sl.connect('penguin-protocol.db') as db:
    dbh.drop_all_db(db)
    dbh.create_db(db)
    dbh.fill_table_test(db)

api = Flask(__name__)
cors = CORS(api)

@api.route("/basic-query", methods=["GET"])
def query_db():
    with sl.connect('penguin-protocol.db') as db:
        db.row_factory = sl.Row
        data = request.json
        print("query_db():", data)
        rows = dbh.select_db(db, data["sel"], data["table"], data["where"])
        return json.dumps([dict(x) for x in rows]), 200
        

@api.route("/get-table-names", methods=["GET"])
def get_table_names():
    with sl.connect('penguin-protocol.db') as db:
        db.row_factory = sl.Row
        rows = dbh.print_db(db)
        return json.dumps([dict(x) for x in rows]), 200

@api.route("/", methods=["GET"])
def test():
    return "test", 200

@api.route("/add-location", methods=["POST"])
def add_location():
    data = request.json
    entry = (data["name"], data["address"], data["city"], data["country"])
    dbh.add_instance(db, "LOCATION (name, address, city, country)", entry)


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)