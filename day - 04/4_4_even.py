def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def count_even(numbers):
    count = 0
    for x in numbers:
        if is_even(x) == True:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5, 6]))
print(count_even([1, 3, 5]))
print(count_even([]))
