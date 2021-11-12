import json
import os


__db_location__ = "db"
__order_folder__ = f"{__db_location__}/order"
__order__last_id__ = f"{__db_location__}/order.db"


def order_init(arguments):

    def db():
        os.makedirs(__order_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()


class Order:
    def __init__(order):
        if os.path.exists(__order__last_id__):
            with open(__order__last_id__, "r") as last_id_f:
                order.last_id = int(last_id_f.readline())
        else:
            order.last_id = 0

    def save(order):
        id = order.last_id+1

        _data_ = {
            "id": id,
            "customerId": order.customerId,
            "itemId": order.itemId,
            "itemPrice": order.itemPrice,
            "itemQty": order.itemQty,
            "itemTotal": order.itemTotal

        }
        with open(f"{__order_folder__}/{id}.db", "w") as order_file:
            json.dump(_data_, order_file)

        order.last_id += 1
        with open(__order__last_id__, "w") as f:
            f.write(str(order.last_id))

    def __get_order_by_path(order, path):
        with open(path, "r") as order_file:
            _data_ = json.load(order_file)
            order.id = _data_["id"]
            order.customerId = _data_["customerId"]
            order.itemId = _data_["itemId"]
            order.itemQty = _data_["itemQty"]
            order.itemTotal = _data_["itemTotal"]

    def all(self):
        order_file_names = os.listdir(__order_folder__)
        orders = []
        for order_file_name in order_file_names:
            order = Order()
            Order.__get_order_by_path(
                order, f"{__order_folder__}/{order_file_name}")
            orders.append(order)
        return orders

    def find(self, id):
        Order.__get_order_by_path(self, f"{__order_folder__}/{id}.db")

    def search(self, key, value):
        orders = self.all()
        result_orders = []
        for order in orders:
            item_value = getattr(order, key)
            if item_value == value:
                result_orders.append(order)
        return result_orders

    def __repr__(self):
        return f"id:{self.id},customerId:{self.customerId},itemId:{self.itemId},itemQty:{self.itemQty},itemTotal:{self.itemTotal}"
