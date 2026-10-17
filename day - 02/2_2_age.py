def classify_age(age):
    if age < 0:
        return "Ошибка"
    elif age <= 12:
        return "ребенок"
    elif age <= 17:
        return "подросток"
    else:
        return "взрослый"

age = int(input("Введите ваш возраст: "))
result = f"Категория: {classify_age(age)}"

print(result)
    
