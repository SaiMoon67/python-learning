total = 0
i = 1

while True:
    num = int(input("Введите число: "))
    if num > 0:
        break
    else:
        print ("нужно положительное число.")

while i <= num:
    total += i
    i += 1

print(f"Сумма от 1 до {num} равна: {total}")


    