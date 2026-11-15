grades = {"Анна": 4, "Иван": 5, "Мария": 3, "Петр": 2}

for name, grade in grades.items():
    print(f"{name}: {grade}")

average = sum(grades.values()) / len(grades)
print(f"Средняя оценка {average}")