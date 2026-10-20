def count_words(text):
    words = text.split(",")
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

x = count_words("a,b,a,c,a,b")
print(x)
        