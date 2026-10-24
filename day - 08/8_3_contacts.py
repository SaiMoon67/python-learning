def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name}: {phone}\n")

def show_contacts():
    try:
        with open("contacts.txt", "r") as f1:
            for line in f1:
                print(line, end="")
    except FileNotFoundError:
        print("Вы ничего не добавили, файла еще нет")

while True:
    answer = input("Введите ваше имя (или stop для выхода): ")
    if answer == "stop":
        break
    else:
        your_n = input("Введите ваш номер телефона: ")
        add_contact(answer, your_n)

show_contacts()
