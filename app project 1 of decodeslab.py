from flask import Flask, jsonify, request

app = Flask(__name__)

products_database = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "AirPods", "price": 150}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"status": "success", "data": products_database}), 200

@app.route('/products', methods=['POST'])
def add_product():
    new_data = request.get_json()
    if not new_data or "name" not in new_data or "price" not in new_data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400
    
    new_product = {
        "id": len(products_database) + 1,
        "name": new_data["name"],
        "price": new_data["price"]
    }
    products_database.append(new_product)
    return jsonify({"status": "created", "data": new_product}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)