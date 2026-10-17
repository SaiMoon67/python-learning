while True:
    answer = int(input("введите число от 1 до 9: "))
    if answer > 9 or answer < 1:
        print("Ошибка, нужно ввести число от 1 до 9!!!")
    else:
        for x in range(1, 11):
            print(f"{answer} * {x} = {answer * x}")
        break
