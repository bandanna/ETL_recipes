import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import VARIABLES





class NLP:

    def __init__(self):
        print "NLP fun just began!"
        print " "
        self.ids_dict={}

    def train(self, ds):
        """ gets dataset and trains it, calculates cosine similarities etc, get titles
        and ingredients"""

        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), stop_words='english')
        tfidf_matrix = tf.fit_transform(ds)
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        idf = tf.idf_

        # print tfidf_matrix

        #print dict(zip(tf.get_feature_names(), idf))

        dims = cosine_similarities.shape
        print cosine_similarities
        #print cosine_similarities[0][3]

        #print dims[0]
        #ids_dict={}
        for i in range(dims[0]):
            srt = cosine_similarities[i].argsort()[::-1][:VARIABLES.num_recommended_recipes+1]

            print "\n For doc %s" % (i) ,": [%s]" % ds[i]

            z= srt[1:]
            self.ids_dict.update({i:list(z)})
            print z

            for j in srt[-(dims[0]-1):][1:]:
                print cosine_similarities[j][i]



            #x = [ (i[j]) for j in srt]



    def predict(self, ds):
        """ in this specific project it gets dataset with only titles here"""
        zipped_lists= zip(self.ids_dict.keys(),ds)
        tmp ={}
        for doc in self.ids_dict.keys():
            #print "For recipe -> [%s]" % ds[doc]," We recommend:"

            tmp_list=[]
            for rec in self.ids_dict.get(doc):
                #print ds[rec]
                tmp_list.append(ds[rec])
            tmp.update({ds[doc]:tmp_list})
            #print " --------- \n"
        return tmp
