import json

student = {"name": "Анна", "age": 18}
with open("student.json", "w") as f:
    json.dump(student, f)

with open("student.json", "r") as f1:
    data = json.load(f1)
    print(data["age"])
