from dConnecter import reader
import pymongo
import VARIABLES


r = reader()
db = r.getMongoDB()
col = pymongo.collection.Collection(db,VARIABLES.colname)


titles = col.find()

l = []
for t in titles:
    for ing in t['ingredients']:
        l.append(ing)


print l.sort(key=unicode,reverse=False)
