from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def isCommon(ngram):
    commonWords = [
'THE', 'BE', 'AND', 'OF', 'A', 'IN', 'TO', 'HAVE', 'IT', 'I',
'THAT', 'FOR', 'YOU', 'HE', 'WITH', 'ON', 'DO', 'SAY', 'THIS', 'THEY',
'IS', 'AN', 'AT', 'BUT', 'WE', 'HIS', 'FROM', 'THAT', 'NOT', 'BY',
'SHE', 'OR', 'AS', 'WHAT', 'GO', 'THEIR', 'CAN', 'WHO', 'GET', 'IF',
'WOULD', 'HER', 'ALL', 'MY', 'MAKE', 'ABOUT', 'KNOW', 'WILL', 'AS',
'UP', 'ONE', 'TIME', 'HAS', 'BEEN', 'THERE', 'YEAR', 'SO', 'THINK',
'WHEN', 'WHICH', 'THEM', 'SOME', 'ME', 'PEOPLE', 'TAKE', 'OUT', 'INTO',
'JUST', 'SEE', 'HIM', 'YOUR', 'COME', 'COULD', 'NOW', 'THAN', 'LIKE',
'OTHER', 'HOW', 'THEN', 'ITS', 'OUR', 'TWO', 'MORE', 'THESE', 'WANT',
'WAY', 'LOOK', 'FIRST', 'ALSO', 'NEW', 'BECAUSE', 'DAY', 'MORE', 'USE',
'NO', 'MAN', 'FIND', 'HERE', 'THING', 'GIVE', 'MANY', 'WELL']
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1
                or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):
    content = content.upper()
    content = re.sub('\n', ' ', content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        nWords = content[i:i+n]
        if isCommon(nWords) is False:
            #output.append(content[i:i+n])
            output.append(nWords)
    return output

def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [ ' '.join(ngram) for ngram in
                getNgramsFromSentence(sentence, 2)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return (ngrams)

def getFirstSentenceContaining(ngram, content):
    # print(ngram)
    sentences = content.upper().split(". ")
    for sentence in sentences:
        if ngram in sentence:
            return sentence+'\n'
    return ""
if __name__ == "__main__":
    content = str(
        urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt')
        .read(), 'utf-8')
    ngrams = getNgrams(content, 2)
    print(ngrams)
    print(getFirstSentenceContaining('EXCLUSIVE METALLIC CURRENCY', content))
    print(getFirstSentenceContaining('EXECUTIVE DEPARTMENT', content))
    print(getFirstSentenceContaining('GENERAL GOVERNMENT', content))
    print(getFirstSentenceContaining('CALLED UPON', content))
    print(getFirstSentenceContaining('CHIEF MAGISTRATE', content))



