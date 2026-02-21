# bill_splitter.py

def main():
    print("=== RESTAURANT BILL SPLITTER ===")

    try:
        # Inputs
        subtotal = float(input("Enter total bill: "))
        people = int(input("Number of people: "))
        tax_percent = float(input("Tax percentage: "))
        tip_percent = float(input("Tip percentage: "))

        if people <= 0:
            print("Number of people must be greater than 0.")
            return

        # Calculations
        tax_amount = subtotal * (tax_percent / 100)
        after_tax = subtotal + tax_amount

        tip_amount = after_tax * (tip_percent / 100)
        total_bill = after_tax + tip_amount

        per_person = total_bill / people

        # Output
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal:    ₹{subtotal:.2f}")
        print(f"Tax ({tax_percent:.0f}%):   ₹{tax_amount:.2f}")
        print(f"After tax:   ₹{after_tax:.2f}")
        print(f"Tip ({tip_percent:.0f}%):   ₹{tip_amount:.2f}")
        print(f"Total:       ₹{total_bill:.2f}")
        print(f"Per person:  ₹{per_person:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()