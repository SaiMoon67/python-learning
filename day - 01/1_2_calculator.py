def calculate(operation, num1, num2):
    if operation in ("/", "//", "%") and num2 == 0:
        return "Ошибка"
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    if operation == "//":
        return num1 // num2
    if operation == "%":
        return num1 % num2
    return "такой операции нет"

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
x = input("Выберите операцию (+), (-), (*), (/), (//), (%):  ")
result = calculate(x, num1, num2)
print("Результат: ", result)
    


