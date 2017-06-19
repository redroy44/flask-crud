#!/usr/bin/env python

import sys
import os
import json
from flask import Flask, request
from flask_restful import abort, Api, Resource
import sqlobject as sq

from model import *

app = Flask(__name__)
api = Api(app)

# Host and port
SERVER_HOST = 'localhost'
SERVER_PORT = 8001


class Car(Resource):
    def get(self, car_id):
        car = Cars.get(car_id)
        return car.sqlmeta.asDict()

    def delete(self):
        # delete a car
        pass

    def post(self):
        # add a car
        pass

    def put(self):
        #update a car
        pass


class CarList(Resource):
    def get(self):
        # list cars
        cars = []
        results = Cars.select()
        for car in results:
            cars.append(car.sqlmeta.asDict())
        return cars

    def post(self):
        #add car
        pass


class Owner(Resource):
    def get(self, owner_id):
        owner = Owners.get(owner_id)
        return owner.sqlmeta.asDict()

    def delete(self):
        # delete a owner
        pass

    def post(self):
        # add a owner
        pass

    def put(self):
        #update a owner
        pass


class OwnerList(Resource):
    def get(self):
        # list owners
        owners = []
        results = Owners.select()
        for owner in results:
            owners.append(owner.sqlmeta.asDict())
        return owners

    def post(self):
        #add owner
        pass


class CarOwnerList(Resource):
    def get(self):
        # list owners
        owners = []
        results = Owners.select()
        for owner in results:
            owners.append(owner.sqlmeta.asDict())
        return owners


api.add_resource(CarOwnerList, '/')
api.add_resource(CarList, '/cars')
api.add_resource(Car, '/cars/<int:car_id>')
api.add_resource(OwnerList, '/owners')
api.add_resource(Owner, '/owners/<int:owner_id>')


def main():
    args = sys.argv[1:]
    db_filename = args[0]
    open_db(db_filename)
    app.run(host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
