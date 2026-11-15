text = "to be or not to be"
words = text.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
    

