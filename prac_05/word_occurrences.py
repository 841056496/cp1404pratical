"""
Word Occurrences
Estimate: 20 minutes
Actual:   42 minutes
"""

text = input("Text: ")
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

max_length = max(len(word) for word in word_count.keys())

for word, count in sorted(word_count.items()):
    print(f"{word:{max_length}} : {count}")
