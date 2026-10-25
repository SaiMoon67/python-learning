import json

students = [
    {"name": "Анна", "age": 19},
    {"name": "Семён", "age": 21},
    {"name": "Дмитрий", "age": 29}
]

with open("students.json", "w") as f:
    json.dump(students, f)

with open("students.json", "r") as f1:
    data = json.load(f1)
    for student in data:
        print(f"Имя: {student['name']}, возраст: {student['age']}")
