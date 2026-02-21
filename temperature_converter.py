# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def main():
    while True:
        print("\n=== TEMPERATURE CONVERTER ===")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting program. Thank you!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Please select between 1 and 7.")
            continue

        try:
            temp = float(input("Enter temperature value: "))

            if choice == "1":
                result = celsius_to_fahrenheit(temp)
                print(f"Result: {result:.2f} °F")

            elif choice == "2":
                result = fahrenheit_to_celsius(temp)
                print(f"Result: {result:.2f} °C")

            elif choice == "3":
                result = celsius_to_kelvin(temp)
                print(f"Result: {result:.2f} K")

            elif choice == "4":
                result = kelvin_to_celsius(temp)
                print(f"Result: {result:.2f} °C")

            elif choice == "5":
                result = fahrenheit_to_kelvin(temp)
                print(f"Result: {result:.2f} K")

            elif choice == "6":
                result = kelvin_to_fahrenheit(temp)
                print(f"Result: {result:.2f} °F")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()