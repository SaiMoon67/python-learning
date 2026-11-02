months = ("January", "February", "March")
try:
    print(months[0], months[-1])
    months[0] = "April"
except TypeError:
    print("Ошибка: кортежи неизменяемы, нельзя изменять их элементы.")