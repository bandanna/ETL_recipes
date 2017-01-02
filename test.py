from dReader import reader
from dCleaner import matcher
import pymongo


# read the json files fully and insert into different mongo collections
r = reader()
r.insertDataToMongo()
db=r.db


m = matcher(db)
