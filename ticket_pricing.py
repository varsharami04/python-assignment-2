# ticket_pricing_system.py

def determine_price_by_age(user_age):
    if user_age < 3:
        return 0, "Free Entry"
    if 3 <= user_age <= 12:
        return 150, "Child"
    if 13 <= user_age <= 59:
        return 300, "Adult"
    return 200, "Senior Citizen"


def calculate_discounted_total(base_cost, ticket_count, day_name):
    total_cost = base_cost * ticket_count
    weekend_days = {"friday", "saturday", "sunday"}

    if day_name.lower() in weekend_days:
        discount_value = total_cost * 0.20
        return total_cost, discount_value, total_cost - discount_value
    elif day_name.lower() in {"monday", "tuesday", "wednesday", "thursday"}:
        return total_cost, 0, total_cost
    else:
        return None, None, None


def main():
    print("🎬 Welcome to Cinema Ticket System 🎬")

    try:
        user_age = int(input("Enter your age: "))
        visit_day = input("Enter day of visit: ")
        ticket_count = int(input("How many tickets? "))

        if ticket_count <= 0:
            print("Ticket count must be at least 1.")
            return

        price_per_ticket, category = determine_price_by_age(user_age)

        subtotal, discount, final_total = calculate_discounted_total(
            price_per_ticket, ticket_count, visit_day
        )

        if subtotal is None:
            print("Invalid day entered. Please try again.")
            return

        print("\n------ PAYMENT SUMMARY ------")
        print(f"Ticket Category : {category}")
        print(f"Price per Ticket: ₹{price_per_ticket:.2f}")
        print(f"Tickets Booked  : {ticket_count}")
        print(f"Subtotal        : ₹{subtotal:.2f}")

        if discount > 0:
            print(f"Weekend Discount: -₹{discount:.2f}")
        else:
            print("Weekend Discount: ₹0.00")

        print(f"Amount Payable  : ₹{final_total:.2f}")
        print("------------------------------")

    except ValueError:
        print("Invalid input detected. Please enter correct values.")


if __name__ == "__main__":
    main()