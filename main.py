text = "the cat sat on the mat the cat"
def word_frequency(text):
    words = text.lower().split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


sample_text = "The quick brown fox jumps over the lazy dog. The fox is quick."

result = word_frequency(sample_text)

print(result)
