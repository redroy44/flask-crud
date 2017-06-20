
from flask_restful import Resource
import sqlobject as sq

from models.model import *


class CarOwnerList(Resource):
    def get(self):
        # list owners
        owners = []
        results = Owners.select()
        for owner in results:
            cars = []
            for car in owner.cars:
                cars.append(car.sqlmeta.asDict())
            owner_dict = owner.sqlmeta.asDict()
            owner_dict["cars"] = cars
            owners.append(owner_dict)
        return owners
