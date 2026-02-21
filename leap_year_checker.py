# leap_year_checker.py

def is_leap_year(year):
    # Rule:
    # A year is leap if divisible by 4 AND 
    # (NOT divisible by 100 OR divisible by 400)

    if year % 4 != 0:
        return False, "Not divisible by 4"

    elif year % 100 != 0:
        return True, "Divisible by 4 but not divisible by 100"

    elif year % 400 == 0:
        return True, "Divisible by 100 and also divisible by 400"

    else:
        return False, "Divisible by 100 but not divisible by 400"


def main():
    print("=== LEAP YEAR CHECKER ===")

    try:
        year = int(input("Enter a year: "))

        leap, reason = is_leap_year(year)

        print("\n=== RESULT ===")
        if leap:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")

        print(f"Reason: {reason}")

    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == "__main__":
    main()