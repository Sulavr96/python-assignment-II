import operator


def calculate(num1, num2, num_operator):

    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul,
                 "/": operator.truediv}

    num_list = get_number(num1, num2)

    if num_operator == "+":
        return operators[num_operator](num_list[0], num_list[1])
    elif num_operator == "-":
        return operators[num_operator](num_list[0], num_list[1])
    elif num_operator == "*":
        return operators[num_operator](num_list[0], num_list[1])
    elif num_operator == "/":
        try:
            return operators[num_operator](num_list[0], num_list[1])
        except ZeroDivisionError:
            print("The denominator cannot be zero")


def get_number(num1, num2):
    num_list = []
    if num1.find(".") != -1:
        converted_num1 = float(num1)
    else:
        converted_num1 = int(num1)

    if num2.find(".") != -1:
        converted_num2 = float(num2)
    else:
        converted_num2 = int(num2)

    num_list.append(converted_num1)
    num_list.append(converted_num2)

    return num_list


first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
operation = input("Enter an operator(+ or - or * or /): ")
try:
    print(calculate(first_number, second_number, operation))
except ValueError:
    print('Please enter a number')
