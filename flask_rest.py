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


class Cars(sq.SQLObject):
    brand = sq.StringCol()
    model = sq.StringCol()
    number = sq.StringCol()
    owner = sq.ForeignKey('Owners')

class Owners(sq.SQLObject):
    first_name = sq.StringCol()
    last_name = sq.StringCol()
    pesel = sq.StringCol(length=14)
    cars = sq.MultipleJoin('Cars')

def open_db(db_filename):
    create = False
    if not os.path.exists(db_filename):
        create = True
    conn = sq.sqlite.builder()(db_filename)
    sq.sqlhub.processConnection = conn
    if create:
        Cars.createTable()
        Owners.createTable()

class Car(Resource):
    def get(self, car_id):
        # list cars
        print(car_id)
        if car_id is None:
            collection = {}
            results = Cars.select()
            for car in results:
                collection[car.id] = car.brand + " " + car.model
            return collection

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
        collection = {}
        results = Cars.select()
        for car in results:
            collection[car.id] = car.brand + " " + car.model
        return collection


class OwnerList(Resource):
    def get(self):
        # list owners
        pass

    def delete(self):
        # delete owner
        pass

    def post(self):
        #add owner
        pass

    def put(self):
        # update owner
        pass


api.add_resource(CarList, '/cars')
api.add_resource(Car, '/cars/<int:car_id>')
api.add_resource(OwnerList, '/owners')
# TODO
# add resource in root to display cars with their owners




def main():
    args = sys.argv[1:]
    db_filename = args[0]
    open_db(db_filename)
    app.run(host=SERVER_HOST, port=SERVER_PORT)


if __name__ == '__main__':
    main()
