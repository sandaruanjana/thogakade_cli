import sys
import os
import json

__db_location__ = "db"
__customer_folder__ = f"{__db_location__}/customer"
__customer__last_id__ = f"{__db_location__}/customer_id.db"


def customer_init(arguments):

    def db():
        os.makedirs(__customer_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()


class Customer:
    def __init__(customer):
        if os.path.exists(__customer__last_id__):
            with open(__customer__last_id__, "r") as last_id_f:
                customer.last_id = int(last_id_f.readline())
        else:
            customer.last_id = 0

    def save(customer):
        id = customer.last_id+1

        _data_ = {
            "id": id,
            "name": customer.name,
            "address": customer.address,
            "phone": customer.phone

        }
        with open(f"{__customer_folder__}/{id}.db", "w") as customer_file:
            json.dump(_data_, customer_file)

        customer.last_id += 1
        with open(__customer__last_id__, "w") as f:
            f.write(str(customer.last_id))
