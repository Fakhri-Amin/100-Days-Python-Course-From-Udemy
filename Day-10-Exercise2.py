
# Calculator

def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

answer = 0
stop = False
while not stop:
    num1 = int(input("Enter your number : "))
    for i in operations:
        print(i)
    operation_symbol = input("Pick an operation from the line above : ")
    num2 = int(input("Enter your number : "))
    calculation_function = operations[operation_symbol]
    answer += calculation_function(num1, num2)
    print(f"The answer = {answer}")

    uInput = input("Exit?(y)(n) :")
    if uInput.lower() == "y":
        stop = True
