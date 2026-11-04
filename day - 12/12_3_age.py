from datetime import datetime

answer = int(input("Введите ваш год рождения: "))
age = datetime.now().year - answer
print(f"Ваш возраст: {age}")
now_time = datetime.now().strftime("%d.%m.%Y")
print(f"Текущая дата: {now_time}")