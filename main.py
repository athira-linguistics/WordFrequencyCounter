 text = "the cat sat on the mat the cat"

words = text.lower().split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
