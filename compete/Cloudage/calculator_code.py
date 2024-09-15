# simple calculator
# 1. accept two numbers (integer) 2. accept operation (string) 3. print the result


val_1 = input('Enter first number')
val_2 = input('Enter second number')
operator = input(
    'Enter one of the operations [ADD as addition, SUB as substraction, MUL as multiply, DIV as divide]: ')

# *Raise Exception for type checking


def get_result(val_1: int, val_2: int, op: str):
    match op:
        case 'ADD':
            return f'Addition: {(val_1 + val_2)}'
        case 'SUB':
            return f'Substraction: {(val_1 - val_2)}'
        case 'MUL':
            return f'Multiplication: {(val_1 * val_2)}'
        case 'DIV':
            if val_2 == 0:
                return 'Can not perform division as val_2 is 0'
            return f'Division: {(val_1 / val_2)}'


print(get_result(int(val_1), int(val_2), operator))
