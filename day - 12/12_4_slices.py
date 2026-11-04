numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
word = "программирование"
slice1 = numbers[:3]
slice2 = numbers[-3:]
slice3 = numbers[1:-1]
slice4 = numbers[::-1]
print(f"Первые 3 элемента: {slice1}")
print(f"Последние 3 элемента: {slice2}")
print(f"Без первого и последнего: {slice3}")
print(f"В обратном порядке: {slice4}")
print(f"Первые 6 букв слова {word}: {word[:6]}")
print(f"Слово {word} в обратном порядке: {word[::-1]}")