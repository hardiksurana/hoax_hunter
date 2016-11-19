from bs4 import BeautifulSoup
from google import search
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import feedparser
from newspaper import Article
from fuzzywuzzy import fuzz
import getTrusted

# checks for general patterns in the url of the news article's source
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

# checks for biased opinions in an article by running semantic analysis on it
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

authenticity_flag = -1

# generated a score based on 2 tests
def calculate_hoax_score(url, query, searched_content):
    stop_count = 0
    hoax_score = 0
    if(stop_count > 10):
        return 0
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
            # checks if the title of search query and the title of RSS feed news are similar
            if(fuzz.token_set_ratio(query, news['title_detail']['value']) >80):
                link = news['link']
                paper = Article(link, language='en')
                paper.download()
                paper.parse()
                text = ' '.join(paper.text[:].split('\n'))
                # checks if the content in the 2 articles match - signifies similar content
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

query = "narendra modi is the prime minister of india"
for url in search(query, stop=1):
    # TODO: render template with other article content and set the flag appropriately
    content = Article(url, language='en')
    content.download()
    content.parse()
    text_content = ' '.join(content.text[:].split('\n'))
    print(url)
    hoax_score = calculate_hoax_score(url, query, text_content)
    print(hoax_score)
    print("*"*100)
