import VARIABLES
from dConnecter import reader,rediser
from dNLP import NLP
import pymongo
import dFun
from dWriter import writer


r = reader()
db = r.getMongoDB()
col = pymongo.collection.Collection(db,VARIABLES.colname)



# colxn = [s1,s2,s3,s4]

#HIGHLY IMPORTANT CHANGE BOTH CONCAT NUMBERS SAME WAY
titles_n_ingredients = r.getTitlesNLP(col)[:5]
title_only = r.getTitlesList(col)[:5]
#print colxn

x= col.find_one({"title":"Apple Butter with Carolina B."})

#print x

nlp = NLP()

nlp.train(titles_n_ingredients)


print dFun.s

habibi = nlp.predict(title_only)


w = writer()
w.insertRecipes(habibi)
