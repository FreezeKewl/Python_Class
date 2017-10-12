from sys import argv
from collections import Counter

script, filename = argv

txt = open(filename)

passage = Counter(txt.read().upper().split())

print("The 15 most common words are:")
print(passage.most_common(15))


"""
word_document = txt.read()
words = word_document.split()
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)

print(word_counts)

********************

import re
from collections import Counter


with open('text.txt') as txt:
    passage = Counter(txt.read().upper().split())

print(passage.most_common(15))
"""
