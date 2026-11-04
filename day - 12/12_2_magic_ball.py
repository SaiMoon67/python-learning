import random

answer = ["Да", "Нет", "Скорее всего да", "Спроси позже", "Не думаю"]
while True:
    question = input("Задайте вопрос (или stop для выхода): ")
    if question == "stop":
        break
    choice = random.choice(answer)
    print(choice)