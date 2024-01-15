# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {"apple": 1,"banana": 2,"orange": 3}

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
    if item in inventory:
        i = inventory[item] + quantity
        inventory[item] = i
    else:
        inventory[item] = quantity

    pass

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    for key in inventory:
        print(f"{key}: {inventory[key]}")
    pass
# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    if item in inventory:
        inventory[item] = quantity
    else:
        print("NOT FOUND")

    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = int(input("Enter choice (1/2/3/4): "))
    
        if choice == 1:
           item = input("Please enter the item: ")
           quantity = int(input("Please enter the quantity: "))
           add_item(item, quantity)
           print ("The inventory is:")
           print(inventory)
    
        elif choice == 2:
            view_inventory()
    
        elif choice == 3:
            item = input("Please enter the item: ")
            quantity = int(input("Please enter the quantity: "))
            update_item(item, quantity)
            print ("The inventory is:")
            print(inventory)
    
        elif choice == 4:
            print("Thank You!")
            break
        else:
            print("please enter a valid choice")

        # Process the user's choice
        # Implementatin Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
manage_inventory()