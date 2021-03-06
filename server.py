from flask import Flask, json, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS, cross_origin
import sqlite3 as sl
import databse_helper as dbh

with sl.connect('penguin-protocol.db') as db:
    dbh.drop_all_db(db)
    dbh.create_db(db)
    dbh.fill_table_test(db)

api = Flask(__name__)
cors = CORS(api)

@api.route("/basic-query", methods=["POST"])
def query_db():
    print(request.get_data())
    with sl.connect('penguin-protocol.db') as db:
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        print("query_db():", data)
        rows = dbh.select_db(db, data["sel"], data["table"], data["where"])
        return json.dumps(rows), 200
        

@api.route("/get-table-names", methods=["POST"])
def get_table_names():
    with sl.connect('penguin-protocol.db') as db:
        rows = dbh.print_db(db)
        return json.dumps({"table-names": [x[0] for x in rows]}), 200

@api.route("/", methods=["GET"])
def test():
    return "test", 200

@api.route("/add-location", methods=["POST"])
def add_location():
    with sl.connect('penguin-protocol.db') as db:
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        print("add_location() data:", data)

        entry = (data["name"], data["address"], data["city"], data["country"])

        print("add_location() entry:", entry)
        id = dbh.add_instance(db, "LOCATION (name, address, city, country)", entry)
    return jsonify({"id": id, "success": True}), 201

@api.route("/add-user", methods=["POST"])
def add_user():
    with sl.connect('penguin-protocol.db') as db:
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        print("add_user() data:", data)

        entry = (data["name"], data["sem_attend"], data["program"])

        print("add_user() entry:", entry)
        id = dbh.add_instance(db, "USER (name, sem_attend, program)", entry)
    return jsonify({"id": id, "success": True}), 201

@api.route("/add-review", methods=["POST"])
def add_review():
    with sl.connect('penguin-protocol.db') as db:
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        print("add_review() data:", data)

        entry = (data["user"], data["date"], data["location"], data["text"], data["stars"], data["price"])

        print("add_review() entry:", entry)
        id = dbh.add_instance(db, "REVIEW (user, date, location, text, stars, price)", entry)
    return jsonify({"id": id, "success": True}), 201

@api.route("/add-program", methods=["POST"])
def add_program():
    with sl.connect('penguin-protocol.db') as db:
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        print("add_program() data:", data)

        entry = (data["name"], data["school"], data["city"], data["country"])

        print("add_program() entry:", entry)
        id = dbh.add_instance(db, "PROGRAM (name, school, city, country)", entry)
    return jsonify({"id": id, "success": True}), 201

@api.route("/test_post", methods=["POST"])
def test_post():
    data = request.get_data().decode("utf-8")
    data = json.loads(data)
    print(data)
    return data, 202

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)