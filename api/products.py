from flask import Flask, jsonify, request
from .models import pdts

def create_app():
    app = Flask(__name__)

    products = []


    @app.route("/api/v1/products", methods=['POST'])
    def post_a_product():
        data = request.get_json()
        product_id = len(products_lists) +1
        name = data["name"]
        price = data["price"]
        stock = data["stock"]
        products_list.append(pdts(product_id, name, price, stock))
        return jsonify({"message": "Added the product"}), 201

    return app