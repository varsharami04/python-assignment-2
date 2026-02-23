# sum_average_calculator.py

def main():
    print("=== SUM AND AVERAGE CALCULATOR ===")

    try:
        count = int(input("How many numbers? "))

        if count <= 0:
            print("Please enter a number greater than 0.")
            return

        numbers = []

        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)

        print("\n=== RESULT ===")
        print(f"Sum: {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()