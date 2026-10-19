def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
while True:
    try: 
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
    except ValueError:
        print("Ошибка. Введите корректное число")
        continue
    z = safe_divide(a, b)
    if z is None:
        print("Ошибка: деление на ноль запрещено! Попробуйте ещё раз.")
        continue
    else:
        print(z)
        break
