import sys
import os
import json


__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__item_folder__ = f"{__db_location__}/item"
__item__last_id__ = f"{__db_location__}/item_id.db"


def item_init(arguments):

    def db():
        os.makedirs(__item_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        if command == "db":
            db()


class Item:
    def __init__(item):
        if os.path.exists(__item__last_id__):
            with open(__item__last_id__, "r") as last_id_f:
                item.last_id = int(last_id_f.readline())
        else:
            item.last_id = 0

    def save(item):
        id = item.last_id+1

        _data_ = {
            "id": id,
            "name": item.name,
            "price": item.price,
            "sellingPrice": item.selling_price
        }
        with open(f"{__item_folder__}/{id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        item.last_id += 1
        with open(__item__last_id__, "w") as f:
            f.write(str(item.last_id))
