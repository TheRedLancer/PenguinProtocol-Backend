from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin

# this data would NOT be in app memory, but rather saved to disk
# this could be in a database, a file, or some other process
id = 0
noteList = []

api = Flask(__name__)
cors = CORS(api)

@api.route("/test", methods=["GET"])
def get_test():
    return jsonify({"test": 1234}), 200


@api.route("/post", methods=["POST"])
def post_test():
    data = request.json["input"]

    return jsonify({"success": True, "input": data}), 201


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=80, debug=True)