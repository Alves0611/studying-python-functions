def my_sum(*numbers):
    print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total

print(my_sum(15, 17, 13, 16))