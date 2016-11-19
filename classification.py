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
rss_url = 'http://www.business-standard.com/rss/beyond-business-104.rss'
d = feedparser.parse(rss_url)
if not os.path.exists(authentic_folder):
    os.makedirs(authentic_folder)
os.chdir(authentic_folder)
# create_files(d)

os.chdir('..')
rss_url = 'http://www.theonion.com/feeds/rss'
d = feedparser.parse(rss_url)
hoax_folder = r'Hoax'
if not os.path.exists(hoax_folder):
    os.makedirs(hoax_folder)
os.chdir(hoax_folder)
# create_files(d)

# does the classifications
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
bunch = load_files('/Topics')
X_train, X_test, y_train, y_test = train_test_split(bunch.data, bunch.target, test_size=.4)

print(X_test[:-2])
