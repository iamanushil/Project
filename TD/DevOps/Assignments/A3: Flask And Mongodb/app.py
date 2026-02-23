"""
A3: Flask and MongoDB
- /api: Returns JSON list read from backend data file.
- Form: Submits data to MongoDB Atlas; redirects to success or shows error.
"""

import json
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# Path to the backend data file (same directory as this script)
DATA_FILE = Path(__file__).resolve().parent / "data.json"


def get_mongo_collection():
    """Connect to MongoDB Atlas and return the submissions collection."""
    uri = os.environ.get("MONGODB_URI")
    if not uri:
        raise ValueError("MONGODB_URI environment variable is not set")
    client = MongoClient(uri)
    db_name = os.environ.get("MONGODB_DB", "flask_a3")
    return client[db_name].submissions


@app.route("/api")
def api():
    """Read data from backend file and return as JSON list."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError as e:
        return jsonify({"error": f"Invalid JSON in data file: {e}"}), 500


@app.route("/")
def index():
    """Serve the form page."""
    return render_template("index.html", error=None)


@app.route("/success")
def success():
    """Page shown after successful form submission."""
    return render_template("success.html")


@app.route("/submit", methods=["POST"])
def submit():
    """Insert form data into MongoDB Atlas. Redirect on success; show error on same page on failure."""
    if request.method != "POST":
        return redirect(url_for("index"))

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email:
        return render_template("index.html", error="Name and email are required.")

    doc = {
        "name": name,
        "email": email,
        "message": message,
    }

    try:
        coll = get_mongo_collection()
        coll.insert_one(doc)
        return redirect(url_for("success"))
    except ValueError as e:
        return render_template("index.html", error=str(e))
    except PyMongoError as e:
        return render_template("index.html", error=f"Database error: {e}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
