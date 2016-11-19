from bs4 import BeautifulSoup

soup = BeautifulSoup(open('list.html'),'lxml')
y=soup.find(id="lol");
trusted=[]
all=y.find_all('a')
for  x in all:
    x=x.get('href')
    trusted.append(x[2])
