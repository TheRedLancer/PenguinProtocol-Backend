from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sl
import databse_helper as dbh


with sl.connect('penguin-protocol.db') as db:
    dbh.drop_all_db(db)
    dbh.create_db(db)
    dbh.fill_tables_test(db)

api = Flask(__name__)
cors = CORS(api)

@api.route("/get-all-reviews", methods=["GET"])
def get_all_reviews():
    pass

@api.route("/add-review", methods=["POST"])
def add_review():
    pass

@api.route("/get-table-names", methods=["GET"])
def get_table_names():
    with sl.connect('penguin-protocol.db') as db:
        db.row_factory = sl.Row
        rows = dbh.print_db(db)
        return json.dumps([dict(x) for x in rows])


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)