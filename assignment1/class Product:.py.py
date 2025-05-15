class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Transaction:
    def __init__(self, inventory):
        self.inventory = inventory
        self.cart = []

    def find_product(self, name):
        for product in self.inventory:
            if product.name.lower() == name.lower():
                return product
        return None

    def display_items(self):
        print("Item Name\tPrice")
        for product in self.inventory:
            print(f"{product.name}\t${product.price}")

class Purchase(Transaction):
    def process(self):
        while True:
            self.display_items()
            item_name = input("Which items would you like to buy? ")
            product = self.find_product(item_name)
            if product:
                self.cart.append(product)
            else:
                print("Item not found!")
            more = input("Anything else? (Y/N): ").lower()
            if more != 'y':
                break
        total = sum(item.price for item in self.cart)
        report.append(total)
        print(f"Your Total is ${total:.2f}.")
        print("Thank you for shopping at Target!")
        self.cart.clear()

class Return(Transaction):
    def process(self):
        while True:
            self.display_items()
            item_name = input("Which items would you like to return? ")
            product = self.find_product(item_name)
            if product:
                self.cart.append(product)
            else:
                print("Item not found!")
            more = input("Anything else? (Y/N): ").lower()
            if more != 'y':
                break
        total = sum(item.price for item in self.cart)
        print(f"Your Refund total is ${total:.2f}.")
        print("Thank you for shopping at Target!")
        self.cart.clear()


def manage_inventory():
    while True:
        print("\nManage Inventory")
        print("Item Name\tPrice")
        for product in inventory:
            print(f"{product.name}\t${product.price}")
        print("1) Add New Item")
        print("2) Remove Item")
        print("3) Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Item Name: ")
            price = float(input("Item Price: "))
            inventory.append(Product(name, price))
            print("Added Successfully!!")
        elif choice == '2':
            name = input("Item Name to remove: ")
            product = next((p for p in inventory if p.name.lower() == name.lower()), None)
            if product:
                inventory.remove(product)
                print("Item Removed Successfully")
            else:
                print("Item Not Found! Please Try Again!")
        elif choice == '3':
            break


def view_report():
    print("\nReports:")
    print(f"Total Customers: {len(report)}")
    print(f"Total Profit: ${sum(report):.2f}")
    input("Click any key to go back to the main menu.")


# Initial Data
inventory = [
    Product("Lego Star Wars", 25.00),
    Product("Cookie", 5.00)
]

report = []

# Main Loop
while True:
    print("\nWelcome to Target! Choose the following options:")
    print("1) Make a Purchase")
    print("2) Make a Return")
    print("3) Manage Inventory")
    print("4) View Report")
    print("5) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        Purchase(inventory).process()
    elif choice == '2':
        Return(inventory).process()
    elif choice == '3':
        manage_inventory()
    elif choice == '4':
        view_report()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
