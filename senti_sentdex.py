# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:49:36 2018

@author: MANISH PATKAR
"""

import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB , GaussianNB , BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC , NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import  word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            return mode(votes)
        
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            
            result = mode(votes)
            n = votes.count(result)
            
            return (n/len(votes))*100

short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()

Documents = []
all_words = []

allowed_word_types = ["J"]

for r in short_pos.split('\n'):
    Documents.append((r , "pos"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
    
for r in short_neg.split('\n'):
    Documents.append((r , "neg"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

#all_words = []
#save_documents = open("pickled_algos/documents.pickle","wb")
#pickle.dump(Documents, save_documents)
#save_documents.close()
#short_pos_words = word_tokenize(short_pos)
#short_neg_words = word_tokenize(short_neg)


#for w in short_pos_words:
 #   all_words.append(w.lower())
    
#for w in short_neg_words:
#   all_words.append(w.lower())


all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))

word_featureset = list(all_words.keys())[:5000]

#save_word_features = open("pickled_algos/word_features5k.pickle","wb")
#pickle.dump(word_featureset, save_word_features)
#save_word_features.close()

def find_feature(document):
    words = word_tokenize(document)
    features ={}
    for w in word_featureset:
        features[w] = (w in words)
        
    return features

#print(find_feature(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_feature(rev),category) for (rev , category) in Documents]

random.shuffle(featuresets)

training_set = featuresets[:10000]
test_set =featuresets[10000:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive bayes algo accuracy is :",(nltk.classify.accuracy(classifier, test_set))*100)

classifier.show_most_informative_features(15)

#save_classifier = open("naivebayes.pickle","wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()



MNB_Classifier = SklearnClassifier(MultinomialNB())
#MNB_Classifier.train(training_set)
print("Naive bayes multinomial algo accuracy is :",(nltk.classify.accuracy(MNB_Classifier, test_set))*100)

#save_MNBclassifier = open("MNBclassifier.pickle","wb")
#pickle.dump(MNB_Classifier, save_MNBclassifier)
#save_MNBclassifier.close()

save_MNBclassifier1 = open("MNBclassifier.pickle","wb")
pickle.load(save_MNBclassifier1)
save_MNBclassifier1.close()

#MNGaussian_Classifier = SklearnClassifier(GaussianNB())
#MNGaussian_Classifier.train(training_set)
#print("Naive bayes MNGaussian_Classifier algo accuracy is :",(nltk.classify.accuracy(MNGaussian_Classifier, test_set))*100)        
            
                                                       
        
MNBernouli_Classifier = SklearnClassifier(BernoulliNB())
#MNBernouli_Classifier.train(training_set)
print("bernouli  algo accuracy is :",(nltk.classify.accuracy(MNBernouli_Classifier, test_set))*100)       

#save_MNBernouliclassifier = open("MNBernouliclassifier.pickle","wb")
#pickle.dump(MNBernouli_Classifier, save_MNBernouliclassifier)
#save_MNBernouliclassifier.close()

save_MNBernouliclassifier1 = open("MNBernouliclassifier.pickle","wb")
pickle.load(save_MNBernouliclassifier1)
save_MNBernouliclassifier1.close()

# LogisticRegression, SGDClassifier
# sklearn.svm import SVC, LinearSVC , NuSVC

LogisticRegression_Classifier = SklearnClassifier(LogisticRegression())
#LogisticRegression_Classifier.train(training_set)
print(" LogisticRegression_Classifier algo accuracy is :",(nltk.classify.accuracy(LogisticRegression_Classifier, test_set))*100)

#save_MNBernouliclassifier = open("MNBernouliclassifier.pickle","wb")
#pickle.dump(MNBernouli_Classifier, save_MNBernouliclassifier)
#save_MNBernouliclassifier.close()

save_MNBernouliclassifier1 = open("MNBernouliclassifier.pickle","wb")
pickle.load(save_MNBernouliclassifier1)
save_MNBernouliclassifier1.close()

SGDClassifier = SklearnClassifier(SGDClassifier())
#SGDClassifier.train(training_set)
print("SGDClassifier algo accuracy is :",(nltk.classify.accuracy(SGDClassifier, test_set))*100)

#save_SGDclassifier = open("save_SGDclassifier.pickle","wb")
#pickle.dump(SGDClassifier, save_SGDclassifier)
#save_SGDclassifier.close()

save_SGDclassifier1 = open("save_SGDclassifier.pickle","wb")
pickle.load( save_SGDclassifier1)
save_SGDclassifier1.close()

SVC_Classifier = SklearnClassifier(SVC())
#SVC_Classifier.train(training_set)
print("SVC_Classifier algo accuracy is :",(nltk.classify.accuracy(SVC_Classifier, test_set))*100)

#save_SVCclassifier = open("save_SVCclassifier.pickle","wb")
#pickle.dump(SVC_Classifier, save_SVCclassifier)
#save_SVCclassifier.close()


save_SVCclassifier1 = open("save_SVCclassifier.pickle","wb")
pickle.load( save_SVCclassifier1)
save_SVCclassifier1.close()


LinearSVC_Classifier = SklearnClassifier(LinearSVC())
#LinearSVC_Classifier.train(training_set)
print("LinearSVC_Classifier algo accuracy is :",(nltk.classify.accuracy(LinearSVC_Classifier, test_set))*100)

#save_LinearSVCclassifier = open("save_LinearSVCclassifier.pickle","wb")
#pickle.dump(LinearSVC_Classifier, save_LinearSVCclassifier)
#save_LinearSVCclassifier.close()

save_LinearSVCclassifier1 = open("save_LinearSVCclassifier.pickle","wb")
pickle.load( save_LinearSVCclassifier1)
save_LinearSVCclassifier1.close()

NuSVC_Classifier = SklearnClassifier(NuSVC())
#NuSVC_Classifier.train(training_set)
print("NuSVC_Classifier algo accuracy is :",(nltk.classify.accuracy(NuSVC_Classifier, test_set))*100)

#save_NuSVCclassifier = open("save_NuSVCclassifier.pickle","wb")
#pickle.dump(NuSVC_Classifier, save_NuSVCclassifier)
#save_NuSVCclassifier.close()

save_NuSVCclassifier1 = open("save_NuSVCclassifier.pickle","wb")
pickle.load(save_NuSVCclassifier1)
save_NuSVCclassifier1.close()

vote_classifier = VoteClassifier(classifier ,
                                 NuSVC_Classifier,
                                 LinearSVC_Classifier, 
                                 SGDClassifier ,
                                 LogisticRegression_Classifier,
                                 MNBernouli_Classifier)

print("voted classifier confidence percentage:", (nltk.classify.accuracy(vote_classifier , test_set))*100)

#print("classification :", vote_classifier.classify(test_set[0][0]), "confidence ",vote_classifier.confidence(test_set[0][0]))
#print("classification :", vote_classifier.classify(test_set[1][0]), "confidence ",vote_classifier.confidence(test_set[1][0]))
#print("classification :", vote_classifier.classify(test_set[2][0]), "confidence ",vote_classifier.confidence(test_set[2][0]))
#print("classification :", vote_classifier.classify(test_set[3][0]), "confidence ",vote_classifier.confidence(test_set[3][0]))
#print("classification :", vote_classifier.classify(test_set[4][0]), "confidence ",vote_classifier.confidence(test_set[4][0]))
#print("classification :", vote_classifier.classify(test_set[5][0]), "confidence ",vote_classifier.confidence(test_set[5][0]))


def sentiment(text):
    f = find_feature(text)
    
    return vote_classifier.classify(f)
















