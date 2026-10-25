import json
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
        contacts = []

while True:
    answer_name = input("Введите ваше имя (или stop для выхода): ")
    if answer_name == "stop":
        break
    else:
        answer_phone = input("Введите ваш номер телефона: ")
        contact = {"name": answer_name, "phone": answer_phone}
        contacts.append(contact)

with open("contacts.json", "w") as f1:
     json.dump(contacts, f1)
     for contact in contacts:
          print(f"Имя: {contact['name']}, телефон: {contact['phone']}")
     


        




