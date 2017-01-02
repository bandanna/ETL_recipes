import VARIABLES
from dConnecter import reader,rediser
from dNLP import NLP
import pymongo
from dWriter import writer
import sys
import dFun
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel



r = reader()
db = r.getMongoDB()
col = pymongo.collection.Collection(db,VARIABLES.colname)

titles_n_ingredients = r.getTitlesNLP(col)
title_only = r.getTitlesList(col)
# [:20]
nlp = NLP()
nlp.train(titles_n_ingredients)

print "---------------------------------------------"
print "\n<<<<< RETRIEVING ORIGINAL DATA .... >>>>>\n"
print "---------------------------------------------"

readyset = nlp.predict(title_only)

print "---------------------------------------------"
print "\n<<<<< WRITING RESULTS TO DB .... >>>>>\n"
print "---------------------------------------------"

w = writer()
w.insertRecipes(readyset)
