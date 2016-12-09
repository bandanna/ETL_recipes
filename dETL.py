from dReader import reader
from dCleaner import matcher
import pymongo


r = reader()
r.insertDataToMongo()
db=r.db


m = matcher(db)

spotitles = m.spotitles
edatitles = m.edatitles

m.matchMongoTitles(edatitles, spotitles)


s1 = db.edamam.find()
s2 = db.spoonacular.find()

print "----Last Insertion----"
print "edamam %s" % len(s1)
print "spoonacular %s" % len(s2)

db.drop_collection('finalcollection')
db.finalcollection.create_index([('title', pymongo.ASCENDING)], unique=True)

c=0
for s in s1:
    try:
        db.finalcollection.insert_one(s)
        c+=1
    except pymongo.errors.DuplicateKeyError, e:
        continue

for s in s2:
    try:
        db.finalcollection.insert_one(s)
        c+=1
    except pymongo.errors.DuplicateKeyError, e:
        continue

print "After matching total recipes are %s" % c

#db.finalcollection.create_index([('title', pymongo.ASCENDING)], unique=True)
