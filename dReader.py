import json
import pymongo
from pymongo import MongoClient
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import dVARIABLES


class reader:

    def __init__(self):
        self.eda_data=''
        self.edatitles=[]

        self.spo_data=''
        self.spotitles=[]

        with open(dVARIABLES.EDAMAM_RAW) as eda_json:
            self.eda_data = json.load(eda_json)
            #print len(self.eda_data)
        with open(dVARIABLES.SPOONACULAR_RAW) as spo_json:
            self.spo_data = json.load(spo_json)
            #print len(self.spo_data)

        self.db=self.connectToMongoRecipeDB()

    def getTitleAndIngredient(self, jsondata, filetitle):
        c=0
        col=[]
        for i in jsondata:
            #print ''
            doc={}
            if i['title']:
                c+=1
                #print i['title']
                ing=[]
                for j in i['ingredients']:
                    #print j['name']
                    ing.append(j['name'])
                #to remove exact duplicates within the same recipes
                ing=dict.fromkeys(ing).keys()
                doc= {'title' : i['title'] , 'ingredients': ing }
                #print doc
                col.append(doc)
        print filetitle ,"are %s" % c
        return col

    def getAllData(self,jsondata,filetitle):
        c=0
        col=[]
        for r in jsondata:
            #print "******* the length of keys is :%s" % len(r.keys())
            if r['title']:
                c+=1
                doc={}
                for key in r.keys():
                    ing_list=[]
                    #print "-----------"
                    #print "for key: %s" % key
                    if key=='title':
                        #print r[key]
                        title=r[key]
                        doc[key]=title

                    elif key=='ingredients':
                        doc[key]=r[key]
                        '''
                        for ing in r[key]:
                            #print ing['name']
                            ing_list.append(ing['name'])
                        ing_list=dict.fromkeys(ing_list).keys()
                        doc[key]=ing_list
                        '''
                    else:
                        #print r[key]
                        doc[key]=r[key]

                #print " ============================== "
                #print doc
                col.append(doc)
        print filetitle ,"are %s" % c
        return col

    # Connection to Mongo DB
    def connectToMongoRecipeDB(self):
        try:
            client = MongoClient()
            print "--------------------"
            print "Connected successfully: %s" % client
        except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e


        # create a DB if it doesn't exist
        db = client['recipes']
        print "--------------------"
        print "recipes DB created successfully: %s " % db
        print "--------------------"
        return db

    def insertDataToMongo(self):
        #eda_list= self.getTitleAndIngredient(self.eda_data, "edatitles")
        #spo_list=self.getTitleAndIngredient(self.spo_data, "spotitles")

        eda_list= self.getAllData(self.eda_data, "edatitles")
        spo_list=self.getAllData(self.spo_data, "spotitles")
        #db= self.connectToMongoRecipeDB()

        #drop if collections exist
        self.db.drop_collection('edamam')
        self.db.drop_collection('spoonacular')


        self.db.edamam.create_index([('title', pymongo.ASCENDING)], unique=True)

        c=0
        for d in eda_list:
            try:
                self.db.edamam.insert_one(d)
                c+=1
            except pymongo.errors.DuplicateKeyError, e:
                continue
        print "Edamam inserted %s" % c

        self.db.spoonacular.create_index([('title', pymongo.ASCENDING)], unique=True)
        c=0
        for d in spo_list:
            try:
                self.db.spoonacular.insert_one(d)
                c+=1
            except pymongo.errors.DuplicateKeyError, e:
                continue
        print "spoonacular inserted %s" % c


        #eda_collection = self.db.edamam.insert_many(eda_list)
        #spo_collection = self.db.spoonacular.insert_many(spo_list)



    def getMongoDB(self):
        return self.db

class grapher:
    def __init__(self):
        print "Here GraphDB will be implemented"
