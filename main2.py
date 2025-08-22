inventory = [
    {"name": "apple", "quantity": "5kg", "price": "599$"},
    {"name": "mango", "quantity": "3kg", "price": "299$"},
    {"name": "orange", "quantity": "8kg", "price": "999$"}
]

choice = int(input("Enter the choice(1 for adding fruit & 2 for exit) : "))

if choice == 1:
    option = True
else:
    option = False

while option:
    new_name = input("Enter fruit name:- ")
    new_quantity = input("Enter quantity:- ")
    new_price = input("Enter the price:- ")

    new_fruit = {
        "name": new_name,
        "quantity": new_quantity,
        "price": new_price
    }

    inventory.append(new_fruit)

    for data in inventory:
        name = data["name"]
        price = data["price"]
        quantity = data["quantity"]
        print(f"Name:- {name} :: Quantity:- {quantity} ::  Price:- {price}")
    
    user_input = input("Do you want to add another fruit? (yes/no): ").strip().lower()
    if user_input != "yes":
        option = False


