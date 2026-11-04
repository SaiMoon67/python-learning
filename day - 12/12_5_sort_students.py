numbers = [5, 2, 9, 1, 7]
sort_num = sorted(numbers)
print(f"Отсортированный список: {sort_num}")
reverse_sort_num = sorted(numbers, reverse=True)
print(f"Список в обратном порядке: {reverse_sort_num}")
print(f"Список: {numbers}")

students = [
    {"name": "Анна", "grade": 4},
    {"name": "Иван", "grade": 5},
    {"name": "Мария", "grade": 3},
    {"name": "Петр", "grade": 2}
]

def get_grades(student):
    return student["grade"]

sorted_students = sorted(students, key=get_grades, reverse=True)
for student in sorted_students:
    print(f"Имя: {student['name']}, Оценка: {student['grade']}")