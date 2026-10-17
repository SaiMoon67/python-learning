while True:
    answer = input("Введите слово: ").lower().strip()
    if not answer:
        print("Вы ничего не ввели. Попробуйте ещё раз.")
    else:
        print ("Длина", len(answer), end = ", ")
        print ("первая буква", answer[0], end = ", ")
        print ("последняя буква", answer[-1], end = ", ")
        print ("слово наоборот", answer[:: -1], end = ", ")

        if answer [::-1] == answer:
            print ("палиндром")
        else:
            print("не палиндром")
        break
            

