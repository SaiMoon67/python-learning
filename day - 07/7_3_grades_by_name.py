grades = {"Анна": [4, 5, 2, 5, 4], "Петя": [3, 3, 4, 5, 4], "Семён": [5, 5, 5, 5, 4]}

for name, marks in grades.items():
    x = sum(marks) / len(marks)
    print(f"Имя: {name}, Среднее значение оценок: {x}")

