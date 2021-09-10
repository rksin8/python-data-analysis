# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num1 = expression.split(' ')
<<<<<<< HEAD
    num0, num1 = float(num0), float(num1)
=======
    num0, num1 = float(num0), float (num1)
    num0, num1 = float(num0), float(num1)

    num0, num1 = int(num0), float(num1)
>>>>>>> aec1332b26d1b3e66459f6b7f2f5867ebd82c189
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        return None
