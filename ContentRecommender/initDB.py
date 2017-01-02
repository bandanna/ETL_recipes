from dConnecter import reader
import pymongo
import os



r = reader()
db = r.getMongoDB()
db.drop_collection('allrecipes')
os.system("mongorestore --db testdb /Users/Ward/Projects/Demeter/allrecipes.bson")
col = pymongo.collection.Collection(db,'allrecipes')
col.create_index([('title', pymongo.ASCENDING)], unique=True)
