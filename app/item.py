import sys
import os

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
