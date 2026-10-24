while True:
    answer = input("Введите название товара (или stop для выхода): ")
    if answer == "stop":
        break
    with open("shopping.txt", "a") as f:
        f.write(answer + "\n")
try:
    with open("shopping.txt", "r") as f1:
        for line in f1:
            print(line, end="")
except FileNotFoundError:
    print("Вы ничего не добавили, файла еще нет")

