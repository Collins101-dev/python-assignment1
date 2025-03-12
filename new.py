num1 = input("Enter first number: ")
operation = input("Enter operation (+, -, *, /): ")
num2 = input("Enter second number: ")
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero.")
        exit()
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
    exit()

print("Result:", result)