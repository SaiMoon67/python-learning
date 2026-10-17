answer = input("Введите слово или фразу: ").lower().strip()
vowels = ("а", "е", "ё", "и", "у", "ы", "э", "ю", "я", "о")
count = 0
for x in answer:
    if x in vowels:
        count += 1
print(count)