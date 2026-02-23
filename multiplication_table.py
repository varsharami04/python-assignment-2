# multiplication_table.py

def main():
    print("=== MULTIPLICATION TABLE GENERATOR ===")

    try:
        number = int(input("Enter number: "))
        end_range = int(input("Enter range (end): "))

        if end_range <= 0:
            print("Range must be greater than 0.")
            return

        print(f"\nMultiplication Table of {number}")

        for i in range(1, end_range + 1):
            print(f"{number} x {i} = {number * i}")

    except ValueError:
        print("Invalid input! Please enter whole numbers only.")


if __name__ == "__main__":
    main()