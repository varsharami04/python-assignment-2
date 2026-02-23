# factorial_calculator.py

def main():
    print("=== FACTORIAL CALCULATOR ===")

    try:
        number = int(input("Enter a number: "))

        # Handle negative numbers
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        # Handle 0 separately
        if number == 0:
            print("0! = 1")
            return

        factorial = 1
        steps = ""

        for i in range(number, 0, -1):
            factorial *= i
            steps += str(i)
            if i != 1:
                steps += " × "

        print(f"\n{number}! = {steps} = {factorial}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")


if __name__ == "__main__":
    main()