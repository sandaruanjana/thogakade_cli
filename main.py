import sys
from app.item import Item, item_init
from app.customer import Customer, customer_init
from app.order import Order, order_init
from pprint import pprint

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"


def customer_create(name, address, phone):
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.phone = phone
    customer.save()


def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)


def customer_view(id):
    customer = Customer()
    customer.find(id)
    print(customer.id, customer.name, customer.address, customer.phone)


def customer_search(key, value):
    customer = Customer()
    results = customer.search(key, value)
    pprint(results)


def item_create(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()


def item_all():
    item = Item()
    items = item.all()
    pprint(items)


def item_view(id):
    item = Item()
    item.find(id)
    print(item.id, item.name, item.price, item.selling_price)


def item_search(key, value):
    item = Item()
    results = item.search(key, value)
    pprint(results)


def login(username):
    f = open(__session_file__, "w")
    f.write(username)
    f.close()


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view_user():
    username = __get_logged_user()
    print(username)


def order_create(customer_id, item_id, item_price, quantity):
    order = Order()
    order.customerId = customer_id
    order.itemId = item_id
    order.itemPrice = item_price
    order.itemQty = quantity
    order.itemTotal = int(item_price) * int(quantity)
    order.save()


def order_all():
    order = Order()
    orders = order.all()
    pprint(orders)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    item_init(arguments)
    customer_init(arguments)
    order_init(arguments)

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
        if command == "login":
            login(*params)
        elif command == "view":
            view_user()
    elif section == "customer":
        if command == "save":
            customer_create(*params)
        elif command == "all":
            customer_all()
        elif command == "view":
            customer_view(*params)
        elif command == "search":
            customer_search(*params)
    elif section == "item":
        if command == "save":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
        elif command == "search":
            item_search(*params)
    elif section == "order":
        if command == "save":
            order_create(*params)
        elif command == "all":
            order_all()
