students = [
    {"name": "Анна", "grade": 4},
    {"name": "Иван", "grade": 5},
    {"name": "Мария", "grade": 3},
    {"name": "Петр", "grade": 2}
]

names_students = [student["name"] for student in students]
good_students = [student['name'] for student in students if student['grade'] >= 4]
average_grade = sum(student['grade'] for student in students) / len(students)
print(f"Список имен студентов: {names_students}")
print(f"Список студентов с оценкой 4 и выше: {good_students}")
print(f"Средняя оценка студентов: {average_grade}")