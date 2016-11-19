from bs4 import BeautifulSoup
from google import search
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from newspaper import Article

def url_check(trusted, hoax):
    for i in range (0,len(trusted)):
        if trusted[i] in url:
            print("authentic")
            authenticity_flag = 1
    for i in range(0,len(hoax)):
        hoax[i]=hoax[i].lower()
        if hoax[i] in url:
            print("unauthentic")
            authenticity_flag = 0
        if(".com.co" or ".lo" in url):
            authenticity_flag = 0
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
    print("negative score is",ss['neg'])
    if ss['neg']>0.5:
        return 0
    else:
        return 1
    # for k in sorted(ss):
    #     print('{0}: {1} \n'.format(k, ss[k]), end='')

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

x = input("\nPlease enter the text query: ")
authenticity_flag = 2
stop_count = 0
score = 0

# generated a score based on 2 tests
for url in search(x, stop=1):
    print(url)
    if(stop_count > 10):
        break
    stop_count += 1
    score += url_check(trusted, hoax)
    score += sentiment_check(url, sid)
    print("Score is ",score)
    score = 0
