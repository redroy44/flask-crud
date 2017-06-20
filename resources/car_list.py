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


post_parser = reqparse.RequestParser()
post_parser.add_argument('brand', dest='brand',
                         location='form', required=True,
                         help='Car\'s brand')
post_parser.add_argument('model', dest='model',
                         location='form', required=True,
                         help='Car\'s model')
post_parser.add_argument('number', dest='number',
                         location='form', required=True,
                         help='Car\'s number')
post_parser.add_argument('owner', dest='owner',
                         type=owner, location='form', 
                         required=True, help='Car\'s owner')

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
        args = post_parser.parse_args()
        o = Owners.get(args['owner'])
        Cars(brand=args['brand'],model=args['model'],number=args['number'],ownersID=o)

        return args, 201
