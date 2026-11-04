import random

random_number = random.randint(1, 20)
attempts = 0

while True:
    answer = int(input("Угадайте число от 1 до 20: "))
    attempts += 1
    if answer < random_number:
        print("Больше!")
    elif answer > random_number:
        print("Меньше!")
    else:
        print(f"Поздравляю! Вы угадали число! (Число попыток: {attempts})")
        break

