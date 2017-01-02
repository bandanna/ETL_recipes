import VARIABLES
from dConnecter import reader,rediser
from dNLP import NLP
import pymongo
from dWriter import writer
import sys
import dFun
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.stem.wordnet import WordNetLemmatizer



r = reader()
db = r.getMongoDB()
col = pymongo.collection.Collection(db,VARIABLES.colname)

titles_n_ingredients = r.getTitlesNLP(col)[:5]
title_only = r.getTitlesList(col)[:5]

print dFun.s
print ''
print "SHOWING TITLES ONLY:\n"
for t in title_only:
    print t

print "\n--------------------------------\n"
print "SHOWING TITLES and INGREDIENTS:\n"
for t in titles_n_ingredients:
    print t

print "\n--------------------------------\n"
print "SHOWING TOKENIZATION, LEMATIZATION and OMMITTING STOPWORDS:\n"
tf = TfidfVectorizer(analyzer='word', stop_words='english')
tfidf_matrix = tf.fit_transform(titles_n_ingredients)

lmtzr = WordNetLemmatizer()
#print lmtzr.lemmatize('words')
l=[]
for t in tf.get_feature_names():
    l.append(lmtzr.lemmatize(t))

l= set(l)

for k in l:
    print k
