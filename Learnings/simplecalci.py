def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2

print("Please select operation:\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

select = int(input("Select operations from 1, 2, 3, 4: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print("Result:", add(num1, num2))
elif select == 2:
    print("Result:", subtract(num1, num2))
elif select == 3:
    print("Result:", multiply(num1, num2))
elif select == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
