"""
Flask app for A4: Version Control Git.
Routes: /, /api (reads JSON), /todo (To-Do page), /submittodoitem (POST, MongoDB).
"""
import os
import json
from pathlib import Path

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Path to JSON file used by /api route
DATA_DIR = Path(__file__).resolve().parent / "data"
API_JSON_PATH = DATA_DIR / "api_data.json"


def load_api_data():
    with open(API_JSON_PATH, "r") as f:
        return json.load(f)


def save_api_data(data):
    with open(API_JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api")
def api():
    data = load_api_data()
    return jsonify(data)


@app.route("/todo")
def todo_page():
    return render_template("todo.html")


@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    item_name = request.values.get("itemName")
    item_description = request.values.get("itemDescription")
    item_id = request.values.get("itemId")
    item_uuid = request.values.get("itemUuid")
    item_hash = request.values.get("itemHash")

    if not item_name and not item_description:
        return jsonify({"success": False, "error": "itemName and itemDescription required"}), 400

    doc = {
        "itemName": item_name,
        "itemDescription": item_description,
    }
    if item_id is not None:
        doc["itemId"] = item_id
    if item_uuid is not None:
        doc["itemUuid"] = item_uuid
    if item_hash is not None:
        doc["itemHash"] = item_hash

    mongo_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
    try:
        from pymongo import MongoClient
        client = MongoClient(mongo_uri)
        db = client.get_database("todo_db")
        coll = db["todo_items"]
        coll.insert_one(doc)
        return jsonify({"success": True, "message": "Todo item stored in MongoDB"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
