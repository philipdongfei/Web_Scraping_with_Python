from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1
                or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):
    content = re.sub(r'\n|[[\d+\]]', ' ', content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = []
    #ngrams = Counter()
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return (ngrams)


if __name__ == '__main__':
    '''

    html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
    bs = BeautifulSoup(html, 'html.parser')
    content = bs.find('div', {'id':'mw-content-text'}).get_text()
    '''
    html = urlopen('https://docs.python.org/3/library/re.html')
    bs = BeautifulSoup(html, 'html.parser')
    content = bs.find('div', {'id':'module-re'}).get_text()
    ngrams = getNgrams(content, 2)
    print(ngrams)
    print('2-grams count is: ' + str(len(ngrams)))

    # read txt


    content = urlopen('http://www.pythonscraping.com/'\
                   'pages/warandpeace/chapter1.txt').read().decode('utf-8')

    #print(type(content))
    ngrams = getNgrams(content, 2)
    print(ngrams)
    print('2-grams count is: ' + str(len(ngrams)))


