import pymongo
import VARIABLES
from dNLP import NLP
from pymongo import MongoClient
from dConnecter import reader,rediser
import json


class writer:
    """ the idea of this class is to write to the outcome of content based to a
    new collection of mongodb given its name"""

    def __init__(self):
        """gets the MongoDB collection name in which to write the documents
        from source sourcedb and _mongocollection
        from target targetdb and targetcollection"""

        self._r = reader()
        self.sourcedb = self._r.connectToMongoRecipeDB()
        self._mongocollection = pymongo.collection.Collection(self.sourcedb,VARIABLES.colname)

        self.targetdb = self._r.connectToRcmnddDB()
        self.targetdb.drop_collection(VARIABLES.rcmndd_recipes)
        self.targetcollection = pymongo.collection.Collection(self.targetdb,VARIABLES.rcmndd_recipes)


    def insertRecipes(self,recipes):
        """ inserts the content based results to mongodb, expects a python dict
        like { recipe_id: ['recommended_recipe1','recom_2','recom3'] ... """
        #self._mongocollection.insert_many(recipes)

        for r in recipes.keys():
            #print r
            self.targetcollection.insert_one({"title":r,"recommended":recipes.get(r)})
            self._mongocollection.update({"title":r},{ "$set": { "recommended": recipes.get(r) }})

            #self.targetcollection.insert_one(x)
            #db.users.update({ status: "A" } ,


        '''
        for r in recipes:
            tmp = {"title":r,"recommended":recipes.get(r)}
            self._mongocollection.insert_one(tmp)
        '''
