import re #regular expression module
from collections import Counter

with open('text.txt') as txt:
    passage = txt.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)
#all_words = word_counts
#while word_counts < [16]:
print(word_counts)


"""
while len(top_words) != 15:
    add_one = text_of_words.pop()
    print("Adding", add_one)
    top_words.append(add_one)
    print(f"There are {len(top_words)} now!")


for number in word_counts:
    num = number.split(",")
    print(num)


'TO': 5292, 'THE': 5265, 'AND': 4930, 'OF': 4337,
 'I': 3178, 'A': 3154, 'IT': 2545, 'HER': 2469,
 'WAS': 2398, 'SHE': 2340, 'IN': 2199, 'NOT': 2150,
 'YOU': 2034, 'BE': 1986, 'THAT': 1815,
"""
