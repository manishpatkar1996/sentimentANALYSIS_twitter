# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:54:17 2018

@author: patkarm
"""

import nltk
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import re
import string

#from sklearn.pipeline import Pipeline
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.model_selection import KFold, cross_val_score
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.model_selection import GridSearchCV
#from sklearn.externals import joblib
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
#from nltk.stem.wordnet import WordNetLemmatizerLoad

#load the data
data = pd.read_csv('twitter_data.csv', error_bad_lines= False,encoding = "ISO-8859-1")
#print(data.head())
data.columns =['label','id','time','query','source', 'text']
#print(data.head())
df= data.drop(['id','time','query','source'], axis=1 )
#print(df)

#mask = df.label == 4
#column_name = 'new_label'
#df.loc[mask, column_name]= 1

#df.new_label.fillna(0, inplace=True)
#df = df.drop(['label'], axis =1, inplace = True)
negative = df['label'][df.label == 0]
positive = df['label'][df.label == 4]
#semi_neg = df['label'][df.label == 1]
#semi_pos = df['label'][df.label == 3]

print("positives",len(positive), "negatives",len(negative))

#function that returns length of a sentence
def word_count(sentence):
    return len(sentence.split())

#creating a new column that gives wordcount
df['wordCount'] = df['text'].apply(word_count)
print(df.head(3))

#plotting

x = df['wordCount'][df.label == 4]
y = df['wordCount'][df.label == 0]
plt.figure(figsize = (12,6))
plt.xlim(0,45)
plt.xlabel('wordCount')
plt.ylabel('frequency')
g = plt.hist([x, y], color =['r','b'], alpha = 0.5, label=['positive','negative'])
plt.legend(loc= 'upper right')


#getting all th common words
all_words =[]
for line in list(data['text']):
    words = line.split()
    for word in words:
        all_words.append(word.lower())
            
print(Counter(all_words).most_common(10))

plt.figure(figsize=(12,5))
plt.title('25 common words')
plt.xticks(fontsize=13, rotation =90)
fd = nltk.FreqDist(all_words)
fd.plot(25, cumulative = False)

col_names = ['date', 'user_loc', 'followers', 'friends','message','bbox_coords','full_name','country','country_code','place_type']

df_paul = pd.read_csv('paul_ryan.csv', names=col_names)

print(df_paul.head())

def processTweet(tweet):
    #remove html special characters
    tweet = re.sub(r'\&\w*;', '',tweet)
    #convert @username
    tweet = re.sub('@[^\s]+','',tweet)
    #removing the tickers
    tweet = re.sub(r'\$\w*', '', tweet)
    #coverting to lower case
    tweet = tweet.lower()
    #remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
    #remove hastags
    tweet = re.sub(r'#\w*','', tweet)
    #removing puncutation and split 's ,'t with a space
    #tweet = re.sub(r'[' + string.punctuation.replace('@','') + ']+', ' ', tweet)
    #removing words with 2 or less letters
    tweet = re.sub(r'\b\w{1,2}\b', '',tweet)
    #removing whitespace
    tweet = re.sub(r'\s\s+', ' ', tweet)
    #remove single space remaining at the front 
    tweet = tweet.lstrip(' ')
    #remove characters beyond basic
    tweet = ''.join(c for c in tweet if c <= '\uFFFF')
    return tweet


df_paul['message'] = df_paul['message'].apply(processTweet)
print(df_paul['message'].head())
                  
    
# most common words in twitter dataset
all_words = []
for line in list(df_paul['message']):
    words = line.split()
    for word in words:
        all_words.append(word.lower())
# plot word frequency distribution of first few words
plt.figure(figsize=(12,5))
plt.xticks(fontsize=13, rotation=90)
fd = nltk.FreqDist(all_words)
fd.plot(25,cumulative=False)

#tokenizing the datasets

def text_process(raw_text):
    
        nonpunc = [char for char in list(raw_text) if char not in string.punctuation ]
        nonpunc = ''.join(nonpunc)
        
    
        return [word for word in nonpunc.lower().split() if word.lower() not in stopwords.words('english')]
        
            
            #print("exception found keyerror")
    #remove all the punctutation
    
    
    #stopwords =("i , me , my , myself , we , our , ours , ourselves , you , you're , you've , you'll , you'd , your , yours , yourself , yourselves , he , him , his , himself , she , her , hers , herself , it ")
    #removing stop words
    #return [word for word in nonpunc.lower().split if word.lower() not in stopwords.words('english')]


def remove_words(word_list):
    remove = ['paul', 'ryan', '...','"', '. . .', 'Paul']
    return [w for w in word_list if w not in remove]
    

df_paul = df_paul.copy()
df_paul['tokens'] = df_paul['message'].apply(text_process)
df_paul['no_pauls'] = df_paul['tokens'].apply(remove_words)

print(df_paul.head())





