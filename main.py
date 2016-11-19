from bs4 import BeautifulSoup
from google import search
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()
soup = BeautifulSoup(open('list.html'),'lxml')
y=soup.find(id="lol");
trusted=[]
soup1 = BeautifulSoup(open('list_hoax.html'),'lxml')
y=soup1.find_all('li')
hoax=[]
for x in y:
    hoax.append(x.text)
return hoax
all=y.find_all('a')
for  x in all:
    x=x.get('href').split("/")
    if(x[2] not in trusted):
        trusted.append(x[2])
# print(trusted)
x=input("\n\nPlease enter the tezxt query: ")
authenticity_flag=0;
for url in search(x, stop=1):
    for i in range (0,len(trusted)):
        if url in trusted[i]:
            authenticity_flag=1
    for i in range(0,len(hoax)):
        if url in hoax[i]:
            authenticity_flag=0
        if(".com.co/" or ".lo/" in url):
            authenticity_flag=0
    article=Article(url)
    article.download()
    article.parse()
    # print(article.text)
    text=article.text
    text=text.split('\u201c')
    no_quotes=[]
    for i in range(0,len(text)):
        if '\u201d' in text[i]:
            no_quotes.append(text[i].split('\u201d')[1])
        else:
            no_quotes.append(text[i])
    no_quotes=" ".join(no_quotes)
    ss = sid.polarity_scores(no_quotes)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
