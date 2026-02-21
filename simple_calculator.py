# simple_calculator.py

# Taking integer input to match sample output format
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Results:")

# Addition
print(f"{num1} + {num2} = {num1 + num2}")

# Subtraction
print(f"{num1} - {num2} = {num1 - num2}")

# Multiplication
print(f"{num1} * {num2} = {num1 * num2}")

# Division (formatted to 2 decimal places)
print(f"{num1} / {num2} = {num1 / num2:.2f}")

# Modulus
print(f"{num1} % {num2} = {num1 % num2}")

# Exponentiation
print(f"{num1} ^ {num2} = {num1 ** num2}")