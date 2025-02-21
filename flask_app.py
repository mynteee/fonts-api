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

# Add a new item (not persistent)
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.json
    if "name" not in new_item:
        return jsonify({"error": "Missing 'name' field"}), 400
    new_item["id"] = max(i["id"] for i in database.data) + 1 if database.data else 1
    database.data.append(new_item)
    return jsonify(new_item), 201
