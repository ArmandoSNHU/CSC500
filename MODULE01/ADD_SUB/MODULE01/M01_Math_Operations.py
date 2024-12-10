# Combined Program: Addition, Subtraction, Multiplication, and Division

# Function for addition and subtraction of the numbers
def addition_and_subtraction():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform add and sub
    addition = num1 + num2
    subtraction = num1 - num2

    # Display the results
    print(f"The addition of {num1} and {num2} is {addition}")
    print(f"The subtraction of {num1} and {num2} is {subtraction}")

# Function for multi and div
def multiplication_and_division():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform multiplication task
    multiplication = num1 * num2

    # Handle division
    if num2 != 0:
        division = num1 / num2
        print(f"The division of {num1} by {num2} is {division}")
    else:
        print("Division by zero is undefined.")

    # Display multiplication results
    print(f"The multiplication of {num1} and {num2} is {multiplication}")

# Main program
def main():
    print("Choose an operation:")
    print("1. Addition and Subtraction")
    print("2. Multiplication and Division")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        addition_and_subtraction()
    elif choice == "2":
        multiplication_and_division()
    else:
        print("Invalid choice. Please run the program again.")

# Entry point of the prog
if __name__ == "__main__":
    main()
