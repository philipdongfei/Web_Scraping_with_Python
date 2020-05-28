from urllib.request import urlopen
from bs4 import BeautifulSoup
from re

def getNgrams(content, n):
    ## using regular expressions to remove escape characters and filtering to remove any Unicode characters
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    content = content.split(' ')
    content = [word for word in content if word != '']
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

if __name__ == '__main__':
    html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
    bs = BeautifulSoup(html, 'html.parser')
    content = bs.find('div', {'id':'mw-content-text'}).get_text()
    ngrams = getNgrams(content, 2)
    print(ngrams)
    print('2-grams count is: ' + str(len(ngrams)))

