# Inventory dictionary to store item data
# Structure: { 'item_name': {'quantity': int, 'price': float} }
inventory = {}

# Function to display the main menu options
def display_menu():
    print('\n--- Inventory Management Menu ---')
    print('1. Add a new item')
    print('2. Update stock level')
    print('3. Delete out-of-stock items')
    print('4. Display inventory summary')
    print('5. Display total inventory value')
    print('6. Exit')

# Function to add a new item to the inventory
def add_item():
    item_name = input("Enter the item name: ").strip()

    # Check if the item already exists
    if item_name in inventory:
        print(f"{item_name} already exists in the inventory. Use the update option instead.")
        return

    try:
        # Get item quantity and price from user
        quantity = int(input(f"Enter the quantity for {item_name}: "))
        price = float(input(f"Enter the price for {item_name}: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input! Quantity must be an integer and price must be a number.")
        return

    # Add item to inventory
    inventory[item_name] = {'quantity': quantity, 'price': price}
    print(f"{item_name} added to inventory.")

# Function to update the quantity of an existing item
def update_stock():
    item_name = input("Enter the item name to update: ").strip()

    # Check if item exists in inventory
    if item_name not in inventory:
        print(f"{item_name} not found in inventory.")
        return

    try:
        # Get the new quantity from user
        new_quantity = int(input(f"Enter the new quantity for {item_name}: "))
    except ValueError:
        # Handle invalid input
        print("Invalid input! Quantity must be an integer.")
        return

    # Update the quantity
    inventory[item_name]['quantity'] = new_quantity
    print(f"{item_name} quantity updated to {new_quantity}.")

# Function to delete all items that are out of stock (quantity <= 0)
def delete_out_of_stock():
    # Identify all out-of-stock items
    out_of_stock_items = [item for item, data in inventory.items() if data['quantity'] <= 0]

    # Delete them from the inventory
    for item in out_of_stock_items:
        del inventory[item]
        print(f"{item} removed from inventory (out of stock).")

    # Inform if no out-of-stock items were found
    if not out_of_stock_items:
        print("No out-of-stock items to remove.")

# Function to display a formatted summary of all inventory items
def display_inventory_summary():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- Inventory Summary ---")
    print("{:<15} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    print("-" * 35)

    # Loop through inventory and print each item
    for item, data in inventory.items():
        print("{:<15} {:<10} ${:<10.2f}".format(item, data['quantity'], data['price']))

# Function to calculate and display total value of all items in inventory
def display_total_value():
    total_value = sum(data['quantity'] * data['price'] for data in inventory.values())
    print(f"\nTotal Inventory Value: ${total_value:.2f}")

# --- Main Program Loop ---
# Keeps running until the user chooses to exit
while True:
    display_menu()

    try:
        # Take user input for menu selection
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        # Handle invalid input
        print("Invalid choice! Please enter a number from 1 to 6.")
        continue

    # Call the appropriate function based on user's choice
    if choice == 1:
        add_item()
    elif choice == 2:
        update_stock()
    elif choice == 3:
        delete_out_of_stock()
    elif choice == 4:
        display_inventory_summary()
    elif choice == 5:
        display_total_value()
    elif choice == 6:
        # Exit the program
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice! Please choose a valid option.")
