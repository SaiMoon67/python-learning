def get_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_biggest(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

numbers1 = [1, 3, 2, 11, 9]
numbers2 = [-5, -2, -9]

print(f"Сумма: {get_total(numbers1)}, максимум: {get_biggest(numbers1)}")
print(f"Сумма: {get_total(numbers2)}, максимум: {get_biggest(numbers2)}")