# working on classification using naive bayes classifier

# Steps:
#     get news dataset-authentic and hoax using RSS feeds
#     create csv file with the data
#     train the model
#     test the model

# get RSS feeds
import feedparser
from newspaper import Article
import csv
import os
from getTrusted import *

def create_files(d):
    count = 1
    for news in d['entries']:
        filename = open(str(count) + '.txt', 'w')
        count += 1
        link = news['link']
        paper = Article(link, language='en')
        paper.download()
        paper.parse()
        filename.write(' '.join(paper.text[:].split('\n')))
        filename.write('\n')
        filename.write('\n')
        filename.close()

# creates the dataset from the RSS feeds
if not os.path.exists('Topics'):
    os.makedirs('Topics')
os.chdir('Topics')

authentic_folder = r'Authentic'
if not os.path.exists(authentic_folder):
    os.makedirs(authentic_folder)
os.chdir(authentic_folder)

# rss_url = 'http://www.business-standard.com/rss/beyond-business-104.rss'
urls = getTrusted.get_links()
for url in urls:
    d = feedparser.parse(url)
    create_files(d)

os.chdir('..')
rss_url = 'http://www.theonion.com/feeds/rss'
d = feedparser.parse(rss_url)
hoax_folder = r'Hoax'
if not os.path.exists(hoax_folder):
    os.makedirs(hoax_folder)
os.chdir(hoax_folder)
# create_files(d)

os.chdir('../..')

'''
# does the classifications
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics

bunch = load_files('Topics')
X_train, X_test, y_train, y_test = train_test_split(bunch.data, bunch.target, test_size=0.05)

count_vect = CountVectorizer()

X_train_counts = count_vect.transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)
clf = MultinomialNB().fit(X_train_tfidf, bunch.target)

docs_new = ['God is love', 'OpenGL on the GPU is fast', 'Donald trump died']
X_new_counts = count_vect.transform(X_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

# for doc, category in zip(X_test, predicted):
#     print('%r => %s' % (doc, bunch.target_names[category]))

print(metrics.classification_report(bunch.target, predicted,target_names=bunch.target_names))
'''
