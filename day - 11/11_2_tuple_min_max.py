def find_min_max(list_of_numbers):
    n_min = list_of_numbers[0]
    n_max = list_of_numbers[0]
    for number in list_of_numbers:
        if number < n_min:
            n_min = number
        if number > n_max:
            n_max = number
    return (n_min, n_max)

smallest, biggest = find_min_max([1, 2, 3, 4, 5])
print(f"Минимальное число: {smallest}, Максимальное число: {biggest}")
