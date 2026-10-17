import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("угадай какое число я загадал: "))
    attempts += 1

    if guess < secret:
        print("загаданное число больше")
    elif guess > secret:
        print("загаданное число меньше")
    else:
        print(f"Угадал! (число попыток: {attempts})")
        break