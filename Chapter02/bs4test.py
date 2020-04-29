from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')

bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())

print()

titles = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print([title for title in titles])
print()

allText = bs.find_all('span', {'class':{'green', 'red'}})
print([text for text in allText])

print()

nameList = bs.find_all(text='the prince')
print(len(nameList))

print()

titles = bs.find_all(id='title', class_='text')
print([title for title in titles])

print()

title = bs.find(id='title')
print(title)

print()

nameList = bs.findAll(class_='green')
for name in nameList:
    print(name.get_text())

'''
bs = BeautifulSoup(html.read(), 'lxml')
print(bs.h1)
'''
'''

bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.h1)
'''



