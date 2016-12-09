from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from dReader import reader

class matcher:

    def __init__(self,db):
        self.db=db
        self.spotitles= self.getTitlesMongoList(db.spoonacular)
        self.edatitles= self.getTitlesMongoList(db.edamam)


    def getTitlesList(self,collection):
        """ returns regular python list of titles"""
        titles = collection.find({}, {"title": 1})
        tmp = []
        for d in titles:
            tmp.append(d['title'])
            print d
        return tmp

    def getTitlesMongoList(self,collection):
        """ returns mongodb object list of titles"""
        return collection.find({}, {"title": 1})

    def matchMongoTitles(self, titles1, titles2):
        """ expects 2 titles sets retrieved from MongoDB (with IDs)"""
        small= titles1
        if small.count() <= titles2.count():
            big = titles2
        else:
            big = small
            small = titles2

        tmp_small = []
        tmp_big = []
        for dsmall in small:
            tmp_small.append(dsmall['title'])
            #print d
        for dbig in big:
            tmp_big.append(dbig['title'])

        # these two lines to be deleted
        #tmp_small = tmp_small[:100]
        #tmp_big = tmp_big[:2000]
        toDelete =[]
        for ds in tmp_small:

            currentTitle= process.extract(ds, tmp_big, limit=3,scorer=fuzz.token_sort_ratio)
            print ("-------------")
            print "Matching recipe: %s" % ds
            for x in currentTitle:
                if x[1] > 87:
                    #print x
                    toDelete.append(x)
                    self.db.spoonacular.delete_one({'title': x[0]})

        print "to delete : %s" % len(toDelete)
        for dlt in toDelete:
            print dlt



        #big is spoonacular given priority for it








        #print len(titles2)

'''
testdb = reader().getMongoDB()
m = matcher(testdb)

spotitles = m.spotitles
edatitles = m.edatitles

m.matchMongoTitles(edatitles, spotitles)
'''
#print fuzz.ratio("this is a test", "this is a test!")
