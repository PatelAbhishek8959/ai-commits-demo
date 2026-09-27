def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
