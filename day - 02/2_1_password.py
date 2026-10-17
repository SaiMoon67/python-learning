password = "python"
attempts = 0
max_attempts = 3
   
while True:
    answer = input("Введите пароль: ")
    attempts += 1
    if answer == password:
        print(f"доступ разрешен (кол-во попыток {attempts})")
        break
    elif attempts >= max_attempts:
        print("Доступ заблокирован")
        break
    else:
        print(f"Неверно (попыток осталось {max_attempts - attempts})")
   

    