from sys import argv
from collections import Counter

script, filename = argv

txt = open(filename)

word_document = txt.read()
words = word_document.split()
cap_words = [word.upper() for word in words]
word_counts = Counter(cap_words)

print(f"\nThe 15 most common words in {filename}:\n")
print(word_counts.most_common(15),"\n")


"""
import re
from collections import Counter

with open('text.txt') as txt:
    passage = Counter(txt.read().upper().split())

print(passage.most_common(15))
"""
