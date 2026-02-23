# palindrome_checker.py

def main():
    print("=== PALINDROME CHECKER ===")

    user_input = input("Enter word/number: ")

    # Convert input to string (so numbers also work)
    original = user_input
    reversed_value = original[::-1]

    print("\n--- Verification Steps ---")
    print("Original :", original)
    print("Reversed :", reversed_value)

    # Case-insensitive comparison
    if original.lower() == reversed_value.lower():
        print("Result   : PALINDROME")
    else:
        print("Result   : NOT A PALINDROME")


if __name__ == "__main__":
    main()