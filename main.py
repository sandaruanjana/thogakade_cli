import sys
from app.item import item_init
from app.customer import Customer, customer_init


def customer_create(name, address, phone):
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.phone = phone
    customer.save()


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