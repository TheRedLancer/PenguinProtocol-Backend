from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin
import sqlite3 as sl
import databse_helper as dbh

db = sl.connect('penguin-protocol.db')



api = Flask(__name__)
cors = CORS(api)

@api.route("/get_all_reviews", methods=["GET"])
def get_all_reviews():
    pass

@api.route("/add_review", methods=["POST"])
def add_review():
    pass

@api.route("/test", methods=["GET"])
def get_test():
    return jsonify({"test": 1234}), 200


@api.route("/post", methods=["POST"])
def post_test():
    data = request.json
    print(data)

    return jsonify({"success": True, "input": data}), 201


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)