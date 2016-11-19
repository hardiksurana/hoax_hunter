from bs4 import BeautifulSoup
soup = BeautifulSoup(open('list_hoax.html'),'lxml')
y=soup.find_all('li')
for x in y:
    print(x.text)
