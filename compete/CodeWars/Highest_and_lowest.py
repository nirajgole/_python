def high_and_low(numbers):
    number_list = [int(i) for i in numbers.split(' ')]
    return f'{max(number_list)} {min(number_list)}'


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
print(high_and_low("-1 -1 0 -9 -2 -2"))
print(high_and_low("4 1 0"))
