from flask import Flask,jsonify

app = Flask(__name__)

purchase_orders = [
    {"id":1,
     "Description": "PO-0001",
     "Item":[
                {"item":1,
                 "Descricao": "Caneta Bic",
                 "Price":10.15
            }]
    }]

# ENDPOINT 01 - GET retorna as Purchase Orders
# ENDPOINT 02 - GET Purchase orders by id
# ENDPOINT 03 - POST new Purchase order


@app.route("/purchase_orders") # endpoint 01
def get_purchase_orders():
    return jsonify(purchase_orders)

@app.route('/purchase_orders/<int:id>')
def get_purchase_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({"Message":"Id {} Nao Encontrado".format(id)})

@app.route("/")
def home():
    return "Hello, World Alterado!!"

app.run(port=5000)


