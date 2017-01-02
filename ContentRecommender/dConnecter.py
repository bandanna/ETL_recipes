import json
import pymongo
from pymongo import MongoClient
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import VARIABLES
import redis


class reader:
    """ initiates connection to the main db used in this project: MongoDB"""

    def __init__(self):
        """ dbname is the mongodb name includes all data which had ETL on already"""

            #print len(self.spo_data)
        self.dbname= VARIABLES.dbname
        self.db=self.connectToMongoRecipeDB()

    # Connection to Mongo DB
    def connectToMongoRecipeDB(self):
        try:
            client = MongoClient()
            print "--------------------"
            print "Connected successfully: %s" % client
        except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e


        # create a DB if it doesn't exist
        db = client[self.dbname]
        print "--------------------"
        print "recipes DB created successfully: %s " % db
        print "--------------------"
        return db

        # Connection to Mongo DB
    def connectToRcmnddDB(self):
        try:
            client = MongoClient()
            print "--------------------"
            print "Connected successfully: %s" % client
        except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e


        # create a DB if it doesn't exist
        db = client[VARIABLES.db_target]
        print "--------------------"
        print "recipes DB created successfully: %s " % db
        print "--------------------"
        return db

    def getMongoDB(self):
        return self.db

    def getTitlesList(self,collection):
        """ returns regular python list of titles"""
        titles = collection.find({}, {"title": 1})

        tmp = []
        for d in titles:
            tmp.append(d['title'])
            # print d
        return tmp

    def getTitlesNLP(self,collection):
        """ returns titles with ingredients for NLP usage"""
        #titles = collection.find({}, {"title": 1})
        titles = collection.find()
        tmp = []
        for d in titles:
            st = ''
            for ing in d['ingredients']:
                st+= ' ' + ing['name']

            #print st
            tmp.append(d['title'] + st)
            # print d
        return tmp


class rediser:
    """ initiates conenction to Redis, see VARIABLES file for the configurations"""

    def __init__(self):
        self.redisdb = redis.StrictRedis(host=VARIABLES.redishost, port=VARIABLES.redisport, db=VARIABLES.dbvalue)

    def getRedisDB(self):
        return self.redisdb


class grapher:
    def __init__(self):
        print "Here GraphDB will be implemented"
