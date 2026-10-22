students = [
    {"name": "Сергей", "mark": 4},
    {"name": "Дмитрий", "mark": 3},
    {"name": "Кирилл", "mark": 5},
    {"name": "Антон", "mark": 4}
]

with open("students.txt", "w") as f:
    for student in students:
        x = f"Имя: {student["name"]}, оценка: {student["mark"]}\n"
        f.write(x)

with open("students.txt", "r") as f2:
    for line in f2:
        print(line, end="")

with open("students.txt", "a") as f3:
    f3.write("Имя: Семён, оценка: 5\n")
    

