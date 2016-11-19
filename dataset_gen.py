# get the relevant modules
import feedparser
from newspaper import Article
from flask import Flask, render_template
import csv
import os
import getTrusted
import web_gen

count = 1
titles= list()
# creates a text file for every news article
def create_files(d):
    for news in d['entries']:
        global count
        filename = open(str(count) + '.txt', 'a+')
        title = news['title']
        try:
            paper = Article(title, language='en')
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
    titles.extend(web_gen.get_news_data(d, 0))
    # create_files(d)

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
    titles.extend(web_gen.get_news_data(d, 1))
    # create_files(d)

os.chdir('../..')
print(titles)
