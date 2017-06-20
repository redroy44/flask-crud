from flask_restful import Resource, reqparse
import sqlobject as sq

from models.model import *


def owner(owner_id):
    # validate owner_id
    try:
        Owners.get(owner_id)
    except sq.main.SQLObjectNotFound:
        raise ValueError({"Owner id:{} doesn't exist"}.format(owner_id))
    return owner_id


put_parser = reqparse.RequestParser()
put_parser.add_argument('brand', dest='brand',
                         location='form',
                         help='Car\'s brand')
put_parser.add_argument('model', dest='model',
                         location='form',
                         help='Car\'s model')
put_parser.add_argument('number', dest='number',
                         location='form',
                         help='Car\'s number')
put_parser.add_argument('owner', dest='ownersID',
                         type=owner, location='form', 
                         help='Car\'s owner')


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

    def put(self, car_id):
        #update a car
        args = put_parser.parse_args()
        try:
            car = Cars.get(car_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        for k,v in args.items():
            if v is not None:
                setattr(car, k, v)

        return car.sqlmeta.asDict(), 201
