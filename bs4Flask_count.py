#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup
import string

url = 'http://flask.pocoo.org/'
with urllib.request.urlopen(url) as f:
    soup = BeautifulSoup(f, 'html5lib')

flask_count = soup.prettify()
flask_count = str(flask_count).lower()
with open('archives/extracted.txt', 'w') as arq:
    arq.write(flask_count)


for c in string.punctuation:
    flask_count = flask_count.replace(c, ' ')
flask_count = flask_count.split()

wordDict = {}
for l in flask_count:
    if l not in wordDict:
        wordDict[l] = 1
    else:
        wordDict[l] += 1
    with open('archives/dic.txt', 'w') as d:
        d.write('%s ' % wordDict)

print('Tamanho do dicionário %s ' % len(wordDict))
print('Quantidade de vezes que aparece a palavra Flask na página inicial %s' % url)
print('A palavra Flask aparece %s vezes.' % wordDict['flask'])


