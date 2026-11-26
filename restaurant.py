menu = {
    "Pizza": 150,
    "Burger": 100,
    "Dosa": 60,
    "Sandwich": 80,
    "Coffee": 40
}

print("----- Restaurant Menu -----")
for item, price in menu.items():
    print(item, "- Rs.", price)

customer_name = input("\nEnter customer name: ")
food_item = input("Enter food item: ")
quantity = int(input("Enter quantity: "))

if food_item in menu:
    total = menu[food_item] * quantity

    print("\n----- Customer Bill -----")
    print("Customer Name:", customer_name)
    print("Food Item:", food_item)
    print("Quantity:", quantity)
    print("Price per item: Rs.", menu[food_item])
    print("Total Bill: Rs.", total)
else:
    print("Invalid food item")