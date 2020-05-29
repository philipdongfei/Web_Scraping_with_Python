from nltk import word_tokenize
from nltk import Text
from nltk.book import *
from nltk import FreqDist
from nltk import bigrams
from nltk import ngrams
from nltk import pos_tag

tokens = word_tokenize('Here is some not very interesting text')
text = Text(tokens)
print(text)
print(len(text6)/len(set(text6)))

fdist = FreqDist(text6)
print(fdist.most_common(10))
print(fdist["Grail"])

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[('Sir', 'Robin')])

fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist[('father','smelt', 'of','elderberries')])

fourgrams = ngrams(text6, 4)
for fourgram in fourgrams:
    if fourgram[0] == 'coconut':
        print(fourgram)

text = word_tokenize('Strange women lying in ponds distributing swords'\
                     'is no basic for a system of government.')
print(pos_tag(text))
text = word_tokenize('The dust was thick so he had to dust')
print(pos_tag(text))



