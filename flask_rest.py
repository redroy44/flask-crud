#!/usr/bin/env python

import sys
import os
from flask import Flask, request
from flask_restful import abort, Api, Resource
import sqlobject as sq

app = Flask(__name__)
api = Api(app)

# Host and port
SERVER_HOST = 'localhost'
SERVER_PORT = 8001


class CarDef(sq.SQLObject):
    pass

class OwnerDef(sq.SQLObject):
    pass

def open_db(db_filename):
    create = False
    if not os.path.exists(db_filename):
        create = True
    conn = sq.sqlite.builder()(db_filename)
    sq.sqlhub.processConnection = conn
    if create:
        CarDef.createTable()
        OwnerDef.createTable()

class CarList(Resource):
    def __init__(self, *args, **kwargs):
        super(CarList, self).__init__(*args, **kwargs)

    def get(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

api.add_resource(
    CarList,
    # Get a list of cars/owners.
    '/get/<object_name>',
    # Get one car/owner by id.
    '/get/<object_name>/<object_id>',
    # Add car/owner.  Form data: object_name, fields.
    '/add/<object_name>',
    # Update car/owner.  Form data: object_name, fields.
    '/update/<object_name>',
    # Delete one car/owner.`
    '/delete/<object_name>',
)


def main():
    args = sys.argv[1:]
    db_filename = args[0]
    open_db(db_filename)
    app.run(host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
