import json

try:
    with open("books.json", "r") as f:
        books = json.load(f)
except FileNotFoundError:
    books = []

while True:
    answer_name_book = input("Введите название книги (или stop для выхода): ")
    if answer_name_book == "stop":
        break
    answer_name_author = input("Введите имя автора: ")
    book = {"name": answer_name_book, "name_author": answer_name_author}
    books.append(book)

with open("books.json", "w") as f1:
    json.dump(books, f1)
for book in books:
    print(f"Название книги: {book['name']}, имя автора: {book['name_author']}")
    
answer = input("Введите слово: ")
found = False
for book_name in books:
    if answer.lower() in book_name['name'].lower():
        print(f"Название книги: {book_name['name']}")
        found = True
if not found:
    print("Такой книги не нашлось")

