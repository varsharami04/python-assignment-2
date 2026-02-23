# number_pattern_printer.py

def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()


def pattern3(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def pattern4(n):
    for i in range(1, n + 1):
        # Increasing part
        for j in range(1, i + 1):
            print(j, end="")
        # Decreasing part
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


def show_menu():
    print("\n===== NUMBER PATTERN PRINTER =====")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose pattern (1-5): ")

        if choice == "5":
            print("Exiting program. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select 1-5.")
            continue

        try:
            height = int(input("Enter height: "))
            if height <= 0:
                print("Height must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        print("\n--- Pattern Output ---")

        if choice == "1":
            pattern1(height)
        elif choice == "2":
            pattern2(height)
        elif choice == "3":
            pattern3(height)
        elif choice == "4":
            pattern4(height)


if __name__ == "__main__":
    main()