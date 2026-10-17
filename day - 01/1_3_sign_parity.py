def describe_number(num):
    if num == 0:
        return "Ноль"
    if num % 2 != 0:
        if num > 0:
            return "Нечет, положительное"
        return "Нечет, отрицательное"
    if num > 0:
        return "Чет, положительное"
    return "Чет, отрицательное"

num1 = int(input("Введите целое число: "))
x = f"Результат: {describe_number(num1)}"
print(x)
    
