#!/usr/bin/env python

import sys
import os
import json
from flask import Flask, request
from flask_restful import abort, Api, Resource
import sqlobject as sq

from models.model import *

from resources.car import Car 
from resources.car_list import CarList
from resources.owner import Owner
from resources.owner_list import OwnerList
from resources.car_owner_list import CarOwnerList


app = Flask(__name__)
api = Api(app)

# Host and port
SERVER_HOST = 'localhost'
SERVER_PORT = 8001


api.add_resource(CarOwnerList, '/')
api.add_resource(CarList, '/cars')
api.add_resource(Car, '/cars/<int:car_id>')
api.add_resource(OwnerList, '/owners')
api.add_resource(Owner, '/owners/<int:owner_id>')


def main():
    args = sys.argv[1:]
    db_filename = args[0]
    open_db(db_filename)
    app.run(debug=True, host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
