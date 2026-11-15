with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Заметка 1\n")
    f.write("Заметка 2\n")
    f.write("Заметка 3\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())