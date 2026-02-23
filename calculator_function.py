# calculator_functions.py

# 1. Addition
def add(a, b):
    return a + b


# 2. Subtraction
def subtract(a, b):
    return a - b


# 3. Multiplication
def multiply(a, b):
    return a * b


# 4. Division (handle division by zero)
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# 5. Modulus
def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b


# 6. Power
def power(a, b):
    return a ** b


# 7. Main Calculator Function
def calculator():
    while True:
        print("\n=== FUNCTION CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Exiting calculator... Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = modulus(a, b)
            elif choice == "6":
                result = power(a, b)

            print("Result:", result)

        else:
            print("Invalid choice! Please select between 1 and 7.")


# Run the calculator
if __name__ == "__main__":
    calculator()