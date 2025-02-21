from flask import Flask, request, jsonify
import json

app = Flask(__name__)

DATA_FILE = "data.json"

# Helper functions
def read_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
        
#real stuff

#default page
@app.route('/')
def hello_world():
    return 'welcome to my crude attempt at a web api'

# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(read_data()), 200

# Get single item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    data = read_data()
    item = next((i for i in data if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404