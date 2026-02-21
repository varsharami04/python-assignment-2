# age_calculator.py

from datetime import datetime, date

def main():
    print("=== AGE CALCULATOR ===")

    choice = input("Do you want precise calculation using full birth date? (yes/no): ").lower()

    today = date.today()

    if choice == "yes":
        # BONUS: Exact birth date calculation
        try:
            day = int(input("Enter birth day (1-31): "))
            month = int(input("Enter birth month (1-12): "))
            year = int(input("Enter birth year (e.g., 2000): "))

            birth_date = date(year, month, day)

            # Calculate exact age in days
            total_days = (today - birth_date).days

            age_years = total_days // 365
            age_months = age_years * 12
            age_hours = total_days * 24
            age_minutes = age_hours * 60

        except ValueError:
            print("Invalid date entered. Please try again.")
            return

    else:
        # Basic calculation using birth year only
        try:
            year = int(input("Enter your birth year: "))
            age_years = today.year - year
            total_days = age_years * 365
            age_months = age_years * 12
            age_hours = total_days * 24
            age_minutes = age_hours * 60

        except ValueError:
            print("Invalid year entered. Please enter numbers only.")
            return

    # Years until 100
    years_to_100 = 100 - age_years

    print("\n=== AGE DETAILS ===")
    print(f"Current Age: {age_years} years")
    print(f"Age in Months: {age_months} months")
    print(f"Age in Days (approx): {total_days} days")
    print(f"Age in Hours: {age_hours} hours")
    print(f"Age in Minutes: {age_minutes} minutes")
    print(f"Years until 100: {years_to_100} years")

if __name__ == "__main__":
    main()