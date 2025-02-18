# my-python-app/app.py
from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)

# Route 1: Hello World
@main_routes.route('/')
def hello_world():
    return jsonify(message="Hello, Kubernetes!")

# Route 2: Info about the app
@main_routes.route('/info')
def info():
    return jsonify(
        name="My Python App",
        version="1.0.0",
        description="A simple Python app deployed in Kubernetes"
    )

# Route 3: Return a list of items
@main_routes.route('/items')
def items():
    return jsonify(
        items=[
            {"id": 1, "name": "Item 1", "price": 25.50},
            {"id": 2, "name": "Item 2", "price": 35.75},
            {"id": 3, "name": "Item 3", "price": 12.40}
        ]
    )

# Route 4: Return a specific item based on ID
@main_routes.route('/item/<int:item_id>')
def get_item(item_id):
    items = [
        {"id": 1, "name": "Item 1", "price": 25.50},
        {"id": 2, "name": "Item 2", "price": 35.75},
        {"id": 3, "name": "Item 3", "price": 12.40}
    ]
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify(error="Item not found"), 404

# Route 5: Health check endpoint
@main_routes.route('/health')
def health():
    return jsonify(status="Healthy", uptime="45 days")
