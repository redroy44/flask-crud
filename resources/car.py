from flask_restful import Resource
import sqlobject as sq

from models.model import *

class Car(Resource):
    def get(self, car_id):
        try:
            car = Cars.get(car_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        return car.sqlmeta.asDict()

    def delete(self, car_id):
        # delete a car
        try:
            Cars.delete(car_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        return "<p>Deleted car: {}</p>".format(car_id), 204

    def post(self):
        # add a car
        pass

    def put(self):
        #update a car
        pass
