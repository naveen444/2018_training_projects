import bs4
import urllib.request

url = urllib.request.urlopen('https://www.imdb.com/list/ls021105452/')

soup = bs4.BeautifulSoup(url, 'lxml')

data = soup.find_all('h3', class_='lister-item-header')

for d in data:
    print(d.text)