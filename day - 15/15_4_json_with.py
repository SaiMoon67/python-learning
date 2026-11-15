import json

book = {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967}

with open("data_day15.json", "w", encoding="utf-8") as f:
    json.dump(book, f, ensure_ascii=False)

with open("data_day15.json", "r", encoding="utf-8") as f1:
    book_data = json.load(f1)
    print(book_data)
    author = book_data.get("author")
    print(author)


