import os
import sqlobject as sq

class Cars(sq.SQLObject):
    brand = sq.StringCol()
    model = sq.StringCol()
    number = sq.StringCol()
    owners = sq.ForeignKey('Owners',cascade=True)

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
