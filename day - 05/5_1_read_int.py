def read_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            break
        except ValueError:
            print("Это не число, попробуйте еще раз")
    return n

x = read_int("Введите число: ")
print(x)

            