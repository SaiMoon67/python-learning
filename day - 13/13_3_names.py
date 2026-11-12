names = ["anna", "ivan", "maria", "petr"]
names_up = [name.capitalize() for name in names]
names_l = [len(name) for name in names]
print(f"Список имен {names} с заглавной буквы {names_up}")
print(f"Список имен {names} с длиной имен {names_l}")
