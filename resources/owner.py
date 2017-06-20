from flask_restful import Resource
import sqlobject as sq

from models.model import *


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

    def put(self):
        #update a owner
        pass
