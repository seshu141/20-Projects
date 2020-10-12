x = []
y = []

# This function addes two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    print()  # To have some space after enter your choice

    if choice == 5:
        print("Thank you. End of the program")
        break

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))
    if choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", subtract(num1, num2))
    if choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", multiply(num1, num2))
    if choice == 4:
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         print(num1, "/", num2, "=", divide(num1, num2))