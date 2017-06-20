from flask_restful import Resource
import sqlobject as sq

from models.model import *


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
