import math

# Function for Addition
def Addition():
    num_count = int(input("How many numbers do you want to add? "))
    numbers = []
    total = 0

    for i in range(num_count):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)
        total += number

    print(f"The sum of {num_count} numbers is {total}")

# Function for Subtraction
def Subtraction():
    num_count = int(input("How many numbers do you want to subtract? "))
    numbers = []

    for i in range(num_count):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    if num_count >= 2:
        result = numbers[0]
        for i in range(1, num_count):
            result -= numbers[i]
        print(f"The result of subtraction is: {result}")
    else:
        print("ERROR: At least two numbers are needed for subtraction.")

# Function for Multiplication
def Multiplication():
    num_count = int(input("How many numbers do you want to multiply? "))
    numbers = 1

    for i in range(num_count):
        number = float(input(f"Enter number {i + 1}: "))
        numbers *= number

    print(f"The result of multiplication is: {numbers}")

# Function for Division
def Division():
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print(f"The result of division is: {result}")

# Function for Square
def Square():
    num = float(input("Enter a number: "))
    result = num ** 2
    print(f"The square of {num} is: {result}")

# Function for Square Root
def SquareRoot():
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print(f"The square root of {num} is: {result}")

# Function for Cube Root
def CubeRoot():
    num = float(input("Enter a number: "))
    result = num ** (1/3)
    print(f"The cube root of {num} is: {result}")

# Function for Modulus
def Modulus():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number (divisor): "))

    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 % num2
        print(f"The modulus result is: {result}")

# Main loop
while True:
    # Main menu
    print("\nWelcome to CodeClause Calculator (CCC)!!!")
    print("Choose from the following options:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square\n6. Square Roots\n7. Cube Roots\n8. Modulus")
    print("9. Exit")
    
    # Ask the user to choose an option
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        Addition()
    elif choice == '2':
        Subtraction()
    elif choice == '3':
        Multiplication()
    elif choice == '4':
        Division()
    elif choice == '5':
        Square()
    elif choice == '6':
        SquareRoot()
    elif choice == '7':
        CubeRoot()
    elif choice == '8':
        Modulus()
    elif choice == '9':
        print("Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid choice. Please select a valid option.")
        






