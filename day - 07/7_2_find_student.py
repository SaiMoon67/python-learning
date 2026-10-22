students = [
    {"name": "Сергей", "mark": 4},
    {"name": "Дмитрий", "mark": 3},
    {"name": "Кирилл", "mark": 5},
    {"name": "Антон", "mark": 4}
]

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None

while True:
    answer = input("Введите ваше имя (или stop для завершения): ")
    if answer == "stop":
        break
    result = find_student(students, answer)    
    if result is None:
        print("Студент не найден")
    else:
        print(result["name"], result["mark"])




    
