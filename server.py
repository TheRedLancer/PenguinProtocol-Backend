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
    with sl.connect('penguin-protocol.db') as db:
        data = request.json
        print("add_location() data:", data)
        entry = (data["name"], data["address"], data["city"], data["country"])
        print("add_location() entry:", entry)
        dbh.add_instance(db, "LOCATION (name, address, city, country)", entry)
    return jsonify({"success": True}), 201

@api.route("/add-user", methods=["POST"])
def add_user():
    with sl.connect('penguin-protocol.db') as db:
        data = request.json
        print("add_user() data:", data)
        entry = (data["name"], data["sem_attend"], data["program"])
        print("add_user() entry:", entry)
        dbh.add_instance(db, "USER (name, sem_attend, program)", entry)
    return jsonify({"success": True}), 201

@api.route("/add-review", methods=["POST"])
def add_review():
    with sl.connect('penguin-protocol.db') as db:
        data = request.json
        print("add_review() data:", data)
        entry = (data["user"], data["date"], data["location"], data["text"], data["stars"], data["price"])
        print("add_review() entry:", entry)
        dbh.add_instance(db, "REVIEW (user, date, location, text, stars, price)", entry)
    return jsonify({"success": True}), 201

@api.route("/add-program", methods=["POST"])
def add_program():
    with sl.connect('penguin-protocol.db') as db:
        data = request.json
        print("add_program() data:", data)
        entry = (data["name"], data["school"], data["city"], data["country"])
        print("add_program() entry:", entry)
        dbh.add_instance(db, "PROGRAM (name, school, city, country)", entry)
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)