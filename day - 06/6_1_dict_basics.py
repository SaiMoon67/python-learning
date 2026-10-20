grades = {"Анна": 4, "Петя": 3, "Семён": 5}
anna_mark = grades["Анна"]
grades["Марк"] = 2
grades["Петя"] = 4
count = len(grades)
for name, mark in grades.items():
    print(f"{name}: {mark}")

print("Оценка Анны: ",anna_mark)
print("Длина словаря: ",count)
