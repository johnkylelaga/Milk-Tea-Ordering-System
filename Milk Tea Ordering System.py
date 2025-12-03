def display_menu():
    print("\n--- MENU ---")
    print("1. Classic")
    print("2. Red Velvet")
    print("3. Matcha")
    print("4. Cookies and Cream")
    print("5. Caramel Macchiato")

def display_sizes():
    print("\n--- SIZES ---")
    print("1. Extra Large")
    print("2. Large")
    print("3. Medium")
    print("4. Small")

def display_sugar_levels():
    print("\n--- SUGAR LEVELS ---")
    print("1. 100%")
    print("2. 75%")
    print("3. 50%")
    print("4. 25%")
    print("5. No Sugar")

def display_add_ons():
    print("\n--- ADD-ONS ---")
    print("1. Black Pearls (Classic)")
    print("2. Mini Pearl")
    print("3. Coffee Jelly")
    print("4. Chocolate Pudding")
    print("5. Crushed Oreos")

flavor_prices = {
    "Classic": 120,
    "Red Velvet": 130,
    "Matcha": 140,
    "Cookies and Cream": 150,
    "Caramel Macchiato": 160
}

size_multiplier = {
    "Extra Large": 1.5,
    "Large": 1.25,
    "Medium": 1.0,
    "Small": 0.75
}

add_on_prices = {
    "Black Pearls (Classic)": 20,
    "Mini Pearl": 15,
    "Coffee Jelly": 20,
    "Chocolate Pudding": 25,
    "Crushed Oreos": 25
}

def get_choice(options):
    while True:
        choice = input("Enter your choice: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice)-1]
        else:
            print("Invalid choice. Try again.")

def yes_no(prompt):
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")

def main():

    while True:  
        print("\nWelcome to the Milk Tea Ordering System!")

        while True:
            display_menu()
            flavor_options = ["Classic", "Red Velvet", "Matcha", "Cookies and Cream", "Caramel Macchiato"]
            flavor = get_choice(flavor_options)
            if yes_no(f"Confirm flavor: {flavor}?"):
                break

        while True:
            display_sizes()
            size_options = ["Extra Large", "Large", "Medium", "Small"]
            size = get_choice(size_options)
            if yes_no(f"Confirm size: {size}?"):
                break
            else:
                print("Please select size again.\n")

        while True:
            display_sugar_levels()
            sugar_options = ["100%", "75%", "50%", "25%", "No Sugar"]
            sugar = get_choice(sugar_options)
            if yes_no(f"Confirm sugar level: {sugar}?"):
                break
            else:
                print("Please select sugar level again.\n")

        display_add_ons()
        add_on_options = ["Black Pearls (Classic)", "Mini Pearl", "Coffee Jelly", "Chocolate Pudding", "Crushed Oreos"]
        add_ons = []

        while True:
            add_on = get_choice(add_on_options)
            add_ons.append(add_on)
            if not yes_no("Add more add-ons?"):
                break

        print("\n--- REVIEW ORDER ---")
        print(f"Flavor: {flavor}")
        print(f"Size: {size}")
        print(f"Sugar Level: {sugar}")
        print(f"Add-ons: {', '.join(add_ons)}")

        if not yes_no("Confirm this drink?"):
            print("\nRestarting order...\n")
            continue

        base_price = flavor_prices[flavor] * size_multiplier[size]
        add_on_total = sum([add_on_prices[a] for a in add_ons])
        total_amount = base_price + add_on_total

        print(f"\nTotal amount: ₱{total_amount:.2f}")

        while True:
            payment = float(input(f"Enter payment: ₱"))
            if payment < total_amount:
                print("Insufficient payment. Please pay the full amount.")
            else:
                change = payment - total_amount
                print(f"Payment accepted. Your change is: ₱{change:.2f}")
                break

        print("\n--- ORDER DETAILS ---")
        print(f"Flavor: {flavor}")
        print(f"Size: {size}")
        print(f"Sugar Level: {sugar}")
        print(f"Add-Ons: {', '.join(add_ons)}")
        print(f"Total Amount Paid: ₱{payment:.2f}")
        print("Thank you for your order!")

        if not yes_no("\nDo you want to order again?"):
            print("Thank you! Come again!")
            break

if __name__ == "__main__":
    main()
