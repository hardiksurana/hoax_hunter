from bs4 import BeautifulSoup
import lxml
from google import search
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import feedparser
from newspaper import Article
from fuzzywuzzy import fuzz
import getTrusted
from flask import Flask, render_template
import flask

'''
app = Flask(__name__)
@app.route('/')

def templateRender():
  return render_template('flaskHTML2.html')

'''
app = Flask(__name__)
@app.route('/')

def templateRender():
  return render_template('flaskHTML2.html')


def url_check(trusted, hoax, url):
    for i in range (0,len(trusted)):
        if trusted[i] in url:
            # print("authentic")
            authenticity_flag = 0
    for i in range(0,len(hoax)):
        hoax[i]=hoax[i].lower()
        if hoax[i] in url:
            # print("unauthentic")
            authenticity_flag = 1
        if(".com.co" or ".lo" in url):
            authenticity_flag = 1
    return authenticity_flag

def sentiment_check(url, sid):
    article = Article(url)
    article.download()
    article.parse()
    text = article.text
    text = text.split('\u201c')
    no_quotes = []
    for i in range(0,len(text)):
        if '\u201d' in text[i]:
            no_quotes.append(text[i].split('\u201d')[1])
        else:
            no_quotes.append(text[i])
    no_quotes = " ".join(no_quotes)
    ss = sid.polarity_scores(no_quotes)
    # print("negative score is",ss['neg'])
    if ss['neg'] > 0.5:
        return 1
    else:
        return 0

sid = SentimentIntensityAnalyzer()

# gets authentic website links
soup = BeautifulSoup(open('list.html'),'lxml')
authentic_sites = soup.find(id="lol")
trusted = list()
temp = authentic_sites.find_all('a')
for x in temp:
    x = x.get('href').split("/")
    if(x[2] not in trusted):
        trusted.append(x[2])

# gets hoax website links
soup1 = BeautifulSoup(open('list_hoax.html'),'lxml')
hoax_sites = soup1.find_all('li')
hoax = list()
for x in hoax_sites:
    hoax.append(x.text)

authenticity_flag = 2

# generated a score based on 2 tests
def calculate_hoax_score(url, query, searched_content):
    stop_count = 0
    hoax_score = 0

    if(stop_count > 10):
        hoax_score += 0
    stop_count += 1

    # search for similar content from RSS feed sites
    for url_rss in getTrusted.get_hoax_links():
        rss_limit = 0
        d = feedparser.parse(url_rss)
        for news in d['entries']:
            # TODO: replace with gensim or other method
            rss_limit += 1
            if(rss_limit > 10):
                break
            if(fuzz.token_set_ratio(query, news['title_detail']['value']) >80):
                link = news['link']
                paper = Article(link, language='en')
                paper.download()
                paper.parse()
                text = ' '.join(paper.text[:].split('\n'))
                # TODO: replace with gensim or other method for efficient comparison
                if(fuzz.token_set_ratio(text, searched_content) > 80):
                    hoax_score += 0
                else:
                    hoax_score += 1
            else:
                pass
    hoax_score += url_check(trusted, hoax, url)
    hoax_score += sentiment_check(url, sid)
    return hoax_score

# query = formPost()
bigList=[]
query = "Donald Trump is the new president elect"
for url in search(query, stop=1):
    # TODO: render template with other article content and set the flag appropriately
    content = Article(url, language='en')
    content.download()
    content.parse()
    text_content = ' '.join(content.text[0:70].split('\n'))
    hoax_score = calculate_hoax_score(url, query, text_content)
    # print(text_content)
    # print(hoax_score)
    # print(url)
    bigList.append([text_content, url, hoax_score])
    print("*"*100)

print(bigList)
