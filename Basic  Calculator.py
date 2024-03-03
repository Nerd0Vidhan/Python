def calculator(a, b, c):
    if c == "+":
        print("Addition is ", a + b)
    elif c == "-":
        print("Subtraction is ", a - b)
    elif c == "*":
        print("Multiplication is ", a * b)
    elif c == "/":
        if b != 0:  # Add a check to avoid division by zero error
            print("Division is ", a / b)
        else:
            print("Cannot divide by zero!")
    elif c == "^":
        print("Power is ", a ** b)
    elif c == "%":
        print("Remainder is ", a % b)
    else:
        print("Not a valid operator")


e = "y"
while e.lower() == "y":
    a = int(input("Enter a value: "))
    b = int(input("Enter a value: "))
    c = input("Operator: ")
    calculator(a, b, c)
    e = input("Try again? (Y/N): ")
