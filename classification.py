# working on classification using naive bayes classifier

# Steps:
#     get news dataset-authentic and hoax using RSS feeds
#     create csv file with the data
#     train the model
#     test the model

# get RSS feeds
import feedparser
from newspaper import Article
rss_url = 'http://www.business-standard.com/rss/beyond-business-104.rss'
d = feedparser.parse(rss_url)
# print(d['entries'])

for news in d['entries']:
    link = news['link']
    paper = Article(link, language='en')
    paper.download()
    paper.parse()
    # print(paper.title)
    print(paper.text[:])
    print('-'*100)
