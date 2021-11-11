import sys
from app.item import Item, item_init
from app.customer import Customer, customer_init
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


if __name__ == "__main__":
    arguments = sys.argv[1:]
    item_init(arguments)
    customer_init(arguments)
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
            print(*params)
            customer_create(*params)
        elif command == "all":
            customer_all()
        elif command == "view":
            customer_view(*params)
    elif section == "item":
        if command == "save":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
        elif command == "search":
            item_search(*params)
