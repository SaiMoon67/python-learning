nums = []
while True:
    answer = input("Введите число (или stop для завершения): ")
    if answer == "stop":
        break

    answer = int(answer)
    nums.append(answer)

total = 0
for x in nums:
    total += x

z = len(nums)
if z == 0:
    print("Вы не ввели ни одного числа")
else:
    average = total / z
    print(f"Количество чисел: {z}, сумма: {total}, среднее значение чисел: {average} ")

    