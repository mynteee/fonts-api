from flask import Flask, jsonify, request
import random
import database  # Import data from separate file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# assimilation
def normalize_string(s):
    return s.strip().lower().replace("-"," ")

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(database.data), 200

# Get a single item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in database.data if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Get items by project
@app.route("/items/project/<string:tag>", methods=["GET"])
def get_items_by_tag(tag):
    filtered_items = [item for item in database.data if tag.lower() in [t.lower() for t in item["projects"]]]
    if filtered_items:
        return jsonify(filtered_items), 200
    return jsonify({"error": "No items found with this project"}), 404

# Get items that are serif
@app.route("/items/serif", methods=["GET"])
def get_serif_items():
    serif_items = [item for item in database.data if item["serif"]]
    if serif_items:
        return jsonify(serif_items), 200
    return jsonify({"error": "No serif items found"}), 404

# Get items that are sans-serif
@app.route("/items/sans-serif", methods=["GET"])
def get_sans_serif_items():
    sans_serif_items = [item for item in database.data if not item["serif"]]
    if sans_serif_items:
        return jsonify(sans_serif_items), 200
    return jsonify({"error": "No sans-serif items found"}), 404

# Get items by name (case and spacing insensitive)
@app.route("/items/name/<string:name>", methods=["GET"])
def get_by_name(name):
    normalized_name = normalize_string(name)
    filtered_items = [item for item in database.data if normalize_string(item["name"]) == normalized_name]
    if filtered_items:
        return jsonify(filtered_items), 200
    return jsonify({"error": "Item with this name not found"}), 404

# Get items by family (case and spacing insensitive)
@app.route("/items/family/<string:family>", methods=["GET"])
def get_by_family(family):
    normalized_family = normalize_string(family)
    filtered_items = [item for item in database.data if normalize_string(item["family"]) == normalized_family]
    if filtered_items:
        return jsonify(filtered_items), 200
    return jsonify({"error": "Item with this family not found"}), 404

# Get a random item
@app.route("/items/random", methods=["GET"])
def get_random_item():
    random_item = random.choice(database.data)  # Randomly select an item from data
    return jsonify(random_item), 200

# Get the number of items in the database
@app.route("/items/count", methods=["GET"])
def get_item_count():
    item_count = len(database.data)-1  # Get the count of items in the data
    return jsonify({"count": item_count}), 200
