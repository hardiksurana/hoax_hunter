from bs4 import BeautifulSoup

def get_links():
    soup = BeautifulSoup(open('list.html'), 'lxml')
    y = soup.find(id="lol");
    trusted = list()
    all_links = y.find_all('a')
    for x in all_links:
        x = x.get('href')
        if(x not in trusted):
            trusted.append(x)
    return trusted

def get_hoax_links():
    # soup = BeautifulSoup(open('list_hoax.html'),'lxml')
    # y=soup.find_all('li')
    # hoax=[]
    # for x in y:
    #     hoax.append(x.text)
    hoax = ['http://www.thespoof.com/rss/feeds/frontpage/rss.xml', 'http://www.thespoof.com/rss/feeds/us/rss.xml', 'http://www.thespoof.com/rss/feeds/uk/rss.xml', 'http://www.thespoof.com/rss/feeds/world/rss.xml', 'http://www.thespoof.com/rss/feeds/entertainment/rss.xml', 'http://www.thespoof.com/rss/feeds/science/rss.xml', 'http://www.thespoof.com/rss/feeds/sport/rss.xml', 'http://www.thespoof.com/rss/feeds/business/rss.xml']
    return hoax
