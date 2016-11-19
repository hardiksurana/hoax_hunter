# working on classification using naive bayes classifier

# get the relevant modules
import feedparser
from newspaper import Article
import csv
import os
import getTrusted

count = 1

# creates a text file for every news article
def create_files(d):
    for news in d['entries']:
        global count
        filename = open(str(count) + '.txt', 'a+')
        link = news['link']
        try:
            paper = Article(link, language='en')
            paper.download()
            paper.parse()
            filename.write(' '.join(paper.text[:].split('\n')))
            filename.write('\n')
            filename.write('\n')
            print("File created for file {0}".format(count))
            count += 1
            filename.close()
        except NameError:
            pass

'''
# creates the dataset from the RSS feeds
if not os.path.exists('Topics'):
    os.makedirs('Topics')

authentic_urls = getTrusted.get_links()
print("Number of authentic links = {0}".format(len(authentic_urls)))

os.chdir('Topics')

authentic_folder = r'Authentic'
if not os.path.exists(authentic_folder):
    os.makedirs(authentic_folder)
os.chdir(authentic_folder)

url_count = 1

for url in authentic_urls:
    print("URL Count = {0}".format(url_count))
    url_count += 1
    if(url_count > 10):
        break
    d = feedparser.parse(url)
    create_files(d)

os.chdir('../..')

hoax_urls = getTrusted.get_hoax_links()
print("Number of hoax links = {0}".format(len(hoax_urls)))
hoax_folder = r'Hoax'
if not os.path.exists(hoax_folder):
    os.makedirs(hoax_folder)
os.chdir(hoax_folder)

url_count = 1
count = 1

for url in hoax_urls:
    print("URL Count = {0}".format(url_count))
    url_count += 1
    if(url_count > 10):
        break
    d = feedparser.parse(url)
    create_files(d)

os.chdir('../..')
'''

# does the classifications
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics

bunch = load_files('Topics')
X_train, X_test, y_train, y_test = train_test_split(bunch.data, bunch.target, test_size=0.05)
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)
vectorizer = TfidfVectorizer(sublinear_tf=True,max_df=0.5, stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
clf = MultinomialNB(alpha=0.01).fit(X_train_counts, y_train)

X_new_counts = vectorizer.transform(X_test)
l = clf.predict(X_new_counts)

print(accuracy_score(y_test, l))

# use custom input
custom = vectorizer.transform("narendra modi is PM of india")
l = clf.predict(custom)
print(l)
