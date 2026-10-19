def collect_numbers():
    nums = []
    while True:
        answer = input("Введите число (или stop для завершения): ")
        if answer == "stop":
            break
        else:
            answer = int(answer)
            nums.append(answer)
    return nums


def get_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_biggest(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def get_len_average(numbers: list[int]):
    x = len(numbers)
    if x == 0:
        return "Ошибка деление на 0"
    y = get_total(numbers) / x
    return y

numbers = collect_numbers()  
x = len(numbers) 

if x == 0:
    print("Вы не ввели ни одного числа")
else:
    print(f"Кол-во чисел: {x}, сумма чисел: {get_total(numbers)}, максимум: {get_biggest(numbers)}, Среднее: {get_len_average(numbers)} ")



    