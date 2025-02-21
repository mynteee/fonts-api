from flask import Flask, jsonify, request
import database  # Import data from separate file

app = Flask(__name__)

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(database.data), 200

# Get a single item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((i for i in database.data if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Get items by tag
@app.route("/items/tag/<string:tag>", methods=["GET"])
def get_items_by_tag(tag):
    filtered_items = [item for item in database.data if tag.lower() in [t.lower() for t in item["tags"]]]
    if filtered_items:
        return jsonify(filtered_items), 200
    return jsonify({"error": "No items found with this tag"}), 404

# Get items that are active
@app.route("/items/active", methods=["GET"])
def get_active_items():
    active_items = [item for item in database.data if item["active"]]
    if active_items:
        return jsonify(active_items), 200
    return jsonify({"error": "No active items found"}), 404

# Get items that are inactive (active = False)
@app.route("/items/inactive", methods=["GET"])
def get_inactive_items():
    inactive_items = [item for item in database.data if not item["active"]]  # Check for False
    if inactive_items:
        return jsonify(inactive_items), 200
    return jsonify({"error": "No inactive items found"}), 404