def print_formatted(number):
    # your code goes here
    max_len = bin(number)[2:]
    for i in range(1, number+1):
        print(str(i).rjust(len(max_len)), oct(i)[2:].rjust(len(max_len)), hex(
            i)[2:].upper().rjust(len(max_len)), bin(i)[2:].rjust(len(max_len)))


print_formatted(99)
