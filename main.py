import sys
from app.item import Item, item_init
from app.customer import Customer, customer_init
from pprint import pprint


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


if __name__ == "__main__":
    arguments = sys.argv[1:]
    item_init(arguments)
    customer_init(arguments)
    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "customer":
        if command == "save":
            print(*params)
            customer_create(*params)
        elif command == "all":
            customer_all()
    elif section == "item":
        if command == "save":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
