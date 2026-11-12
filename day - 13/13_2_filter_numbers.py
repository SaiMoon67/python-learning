numbers = [3, 8, 15, 22, 7, 10, 41, 6]
even_nums = [number for number in numbers if number % 2 == 0]
odd_nums = [number for number in numbers if number % 2 != 0]
big_nums = [number for number in numbers if number > 9]
print(f"Четные числа списка {numbers} равны {even_nums}")
print(f"Нечетные числа списка {numbers} равны {odd_nums}")
print(f"Числа больше 9 списка {numbers} равны {big_nums}")