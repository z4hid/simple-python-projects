def add(n1, n2):
    """Takes two numbers as inputs and perform addition."""
    result = n1 + n2
    return result 


def sub(n1, n2):
    """Takes two numbers as inputs and perform substraction."""
    result = n1 - n2
    return result


def mul(n1, n2):
    """Takes two numbers as inputs and perform multiplication."""
    result = n1 * n2
    return result


def div(n1, n2):
    """Takes two numbers as inputs and perform division."""
    result = n1 / n2
    return result


calculation_on = True

while calculation_on:

    def calculation():
        report = input("What calculation you want to perform? Type '+' for addition , '-' for substraction, '*' for multiplication or '/' for division. \n")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if report == '+':
            print(f"Result = {add(num1, num2)}")
        elif report == '-':
            print(sub(num1, num2))
        elif report == '*':
            print(mul(num1, num2))
        elif report == '/':
            print(div(num1, num2))


    calculation()

    keep_going = input("Do you want to continue? Type 'y' to continue or type 'n' to exit.").lower()
    if keep_going == 'n':
        calculation_on = False
    elif keep_going == 'y':
        continue
        
    




