students = [
    {"name": "Сергей", "mark": 4},
    {"name": "Дмитрий", "mark": 3},
    {"name": "Кирилл", "mark": 5},
    {"name": "Антон", "mark": 4}
]

for student in students:
    x = f"Имя: {student["name"]}, оценка: {student["mark"]}"
    print(x)

def average(students):
    total = 0
    for student in students:
        total += student["mark"]
    l = len(students)
    try:
        average = total / l
    except ZeroDivisionError:
        print("Деление на ноль запрещено!")
        return None
    return average

result = average(students)
print("Среднее: ", result)


       
