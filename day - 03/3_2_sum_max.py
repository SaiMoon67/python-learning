numbers = [1, 3, 2, 11, 9]
total = 0
biggest = numbers[0]
for n in numbers:
    total += n
    if n > biggest:
        biggest = n
print(f"Сумма: {total}, максимум: {biggest}")