from flask_restful import Resource
import sqlobject as sq

from models.model import *

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
