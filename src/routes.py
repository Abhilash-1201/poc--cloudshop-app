from flask import Blueprint, jsonify
import json
import os

product_routes = Blueprint("products", __name__)


@product_routes.route("/products")
def get_products():
    file_path = os.path.join(os.path.dirname(__file__), "products.json")

    with open(file_path) as f:
        data = json.load(f)

    return jsonify(data)
