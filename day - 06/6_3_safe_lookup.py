grades = {"Анна": 4, "Петя": 3, "Семён": 5}
while True:
    answer = input("Как вас зовут? (stop для выхода): ")
    if answer == "stop":
        break
    try:
        print(f"Ваша оценка: {grades[answer]}")
    except KeyError:
        print("Такого ученика нет")