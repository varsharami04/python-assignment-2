# atm_simulator.py

def show_menu():
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def main():
    balance = 10000
    minimum_balance = 500

    while True:
        show_menu()
        choice = input("Enter choice: ")

        # Check Balance
        if choice == "1":
            print(f"Current balance: ₹{balance:.2f}")

        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Deposit amount must be greater than 0.")
                else:
                    balance += amount
                    print("Deposit successful!")
                    print(f"Updated balance: ₹{balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")

        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))

                if amount <= 0:
                    print("Withdrawal amount must be greater than 0.")

                elif amount > balance:
                    print("Insufficient balance!")

                elif balance - amount < minimum_balance:
                    print(f"Minimum balance of ₹{minimum_balance} must be maintained.")

                else:
                    balance -= amount
                    print("Withdrawal successful!")
                    print(f"New balance: ₹{balance:.2f}")

            except ValueError:
                print("Invalid amount entered.")

        # Exit
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()