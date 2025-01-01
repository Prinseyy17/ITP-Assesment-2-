# Welcome message
print("Welcome to the International Vending Machine!")
print("We offer a selection of popular beverages from the UAE, the Philippines, Japan, and Korea!")

# Beverage options with prices in AED
beverages = {
    "UAE": [("Karak Tea", 3), ("Arabic Coffee", 5), ("Laban (Buttermilk)", 4), ("Mountain Dew", 2)],
    "Philippines": [("Buko Juice", 6), ("Sago't Gulaman", 5), ("Royal Tru-Orange", 3), ("Cobra Energy Drink", 4)],
    "Japan": [("Matcha Green Tea", 10), ("Calpis", 8), ("Pocari Sweat", 7), ("Ramune Soda", 9)],
    "Korea": [("Banana Milk", 7), ("Sikhye (Sweet Rice Drink)", 6), ("Milkis", 5), ("Iced Coffee", 8)]
}

# Display beverage menu
print("\nMenu:")
index = 1
for country, drinks in beverages.items():
    print(f"\n{country}:")
    for drink, price in drinks:
        print(f"{index}. {drink} - {price} AED")
        index += 1

# User selection
try:
    choice = int(input("\nSelect a beverage by entering the number (1-16): "))
    if 1 <= choice <= 16:
        selected_drink = None
        selected_price = 0
        index = 1
        for drinks in beverages.values():
            for drink, price in drinks:
                if index == choice:
                    selected_drink = drink
                    selected_price = price
                index += 1
        print(f"You selected: {selected_drink} - {selected_price} AED")
    else:
        print("Invalid choice! Please select a number between 1 and 16.")
except ValueError:
    print("Please enter a valid number.")

# Checkout
if selected_drink:
    print(f"The total cost is: {selected_price} AED")
    user_name = input("What's your name? ")
    print(f"Thank you, {user_name}! Enjoy your {selected_drink}!")
