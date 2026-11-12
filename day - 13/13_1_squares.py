numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)
print(f"Квадраты чисел {numbers} равны {squares}")

squares_short = [number ** 2 for number in numbers]
print(f"Квадраты чисел {numbers} равны {squares_short}", squares_short == squares)


