from flask_restful import Resource, reqparse
import sqlobject as sq

from models.model import *

def pesel(pesel):
    # validate pesel
    if len(pesel) == 14:
        return pesel
    else:
        raise ValueError({'should be of length 14'}.format(pesel))

post_parser = reqparse.RequestParser()
post_parser.add_argument('first_name', dest='first_name',
                         location='form', required=True,
                         help='Owner\'s fitsr name')
post_parser.add_argument('last_name', dest='last_name',
                         location='form', required=True,
                         help='Owner\'s last name')
post_parser.add_argument('pesel', dest='pesel',
                         type=pesel, location='form', 
                         required=True, help='Owner\'s pesel (length 14)')


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
        args = post_parser.parse_args()
        Owners(first_name=args['first_name'],last_name=args['last_name'],pesel=args['pesel'])
        return args, 201
