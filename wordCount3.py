import re
from collections import Counter
"""
frequency = {}
with open('text.txt') as txt:
    passage = txt.read().upper()

words = re.findall(r'\w+', passage)
word_counts = Counter(words)

for word_num in words:
    count = frequency.get(word_num,0)
    frequency[word_num] = count + 1

frequency_list = frequency.keys()

for words_num in frequency_list:
    print(words_num, frequency[words_num])
"""

with open('text.txt') as txt:
    passage = Counter(txt.read().upper().split())


#cap_words = [word.upper() for word in words]

print(passage.most_common(15))
