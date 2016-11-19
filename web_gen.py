# web interface
# import feedparser
# from newspaper import Article
# import csv
import os
from flask import Flask, render_template
import dataset_gen
# import getTrusted

'''
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

os.chdir('..')
rss_url = 'http://www.theonion.com/feeds/rss'
d = feedparser.parse(rss_url)
hoax_folder = r'Hoax'
if not os.path.exists(hoax_folder):
    os.makedirs(hoax_folder)
'''


def get_news_data(d, flag):
    titleList = []
    print(os.listdir('./'))
    # for i in range(len(os.listdir('./'))):
    firIndex = []
    firIndex.append(d['entries'][0]['title'])
    firIndex.append(d['entries'][0]['summary_detail']['value'][10:60])
    firIndex.append(flag)
    titleList.append(firIndex)
    print(titleList)
    return titleList

# app = Flask(__name__)
# @app.route('/')

# def templateRender():
# 	return render_template('flaskHTML2.html',headline=titles)
