from bs4 import BeautifulSoup

def get_links():
    soup = BeautifulSoup(open('list.html'), 'lxml')
    y = soup.find(id="lol");
    trusted = list()
    all_links = y.find_all('a')
    for  x in all_links:
        x = x.get('href')
        trusted.append(x[2])
    return trusted
