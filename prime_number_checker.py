# prime_number_checker.py

import math

def is_prime(n):
    """Function to check if a number is prime"""
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    print("=== PRIME NUMBER CHECKER ===")

    # ------------------ PART 1 ------------------
    try:
        number = int(input("Enter a number: "))

        if is_prime(number):
            print(f"{number} is a PRIME number")
        else:
            print(f"{number} is NOT a prime number")

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    # ------------------ PART 2 ------------------
    try:
        start = int(input("\nEnter start range: "))
        end = int(input("Enter end range: "))

        if start > end:
            print("Start range cannot be greater than end range.")
            return

        primes = []

        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(str(num))

        if primes:
            print("Prime numbers:", ", ".join(primes))
        else:
            print("No prime numbers found in this range.")

    except ValueError:
        print("Invalid range input! Please enter whole numbers.")


if __name__ == "__main__":
    main()