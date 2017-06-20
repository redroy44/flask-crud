from flask_restful import Resource, reqparse
import sqlobject as sq

from models.model import *


def pesel(pesel):
    # validate pesel
    if len(pesel) == 14:
        return pesel
    else:
        raise ValueError({'should be of length 14'}.format(pesel))

put_parser = reqparse.RequestParser()
put_parser.add_argument('first_name', dest='first_name',
                         location='form',
                         help='Owner\'s fitsr name')
put_parser.add_argument('last_name', dest='last_name',
                         location='form',
                         help='Owner\'s last name')
put_parser.add_argument('pesel', dest='pesel',
                         type=pesel, location='form', 
                         help='Owner\'s pesel (length 14)')


class Owner(Resource):
    def get(self, owner_id):
        try:
            owner = Owners.get(owner_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        return owner.sqlmeta.asDict()

    def delete(self, owner_id):
        # delete a owner
        try:
            Owners.delete(owner_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        return "<p>Deleted owner: {}</p>".format(owner_id), 204

    def put(self, owner_id):
        #update a owner
        args = put_parser.parse_args()
        try:
            owner = Owners.get(owner_id)
        except sq.main.SQLObjectNotFound:
            return '404 Not Found', 404
        for k,v in args.items():
            if v is not None:
                setattr(owner, k, v)

        return owner.sqlmeta.asDict(), 201
        
