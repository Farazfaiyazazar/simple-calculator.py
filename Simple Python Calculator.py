# Simple calculator in python
# define function for operations


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def devide(x, y):
    if y == 0:
        return "Eror! Division by zero."


# and this is the Display option for users
print("select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
4

# in this part we are going to take the user choice for operation
choice = input("Enter choice(1/2/3/4): ")

# Take user input for numbers
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

# Perform calculation based on user choice
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("INVALID INPUT")
