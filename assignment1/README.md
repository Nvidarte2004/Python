# Target Store CLI App

A command-line shopping system that simulates a simple Target store interface using object-oriented programming principles such as inheritance and polymorphism. Built in Python for CMPS 372: Python Programming Spring 2025.

## Features

* **Purchase Items**: Select products from an inventory list and calculate the total.
* **Return Items**: Return purchased products and calculate refunds.
* **Manage Inventory**: Add or remove items from the store.
* **View Reports**: See the number of customers and total profit from purchases.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Lists for storage and manipulation of data

## How to Run

1. Clone the repository or download the Python file.
2. Run the script using a Python interpreter:

   ```bash
   python your_script_name.py
   ```
3. Follow the on-screen instructions to make purchases, returns, manage inventory, or view reports.

## Class Structure

* `Product`: Represents an item with a name and price.
* `Transaction` (Base class): Shared logic for purchases and returns.
* `Purchase` (Inherits from `Transaction`): Handles item selection and total cost.
* `Return` (Inherits from `Transaction`): Handles item returns and refund calculation.

## Example Output

```
Welcome to Target! Choose the following options:
1) Make a Purchase
2) Make a Return
3) Manage Inventory
4) View Report
5) Exit
Enter your choice: 1
Item Name       Price
Lego Star Wars  $25.0
Cookie  $5.0
Which items would you like to buy? Lego Star Wars 
Anything else? (Y/N): Y
Item Name       Price
Lego Star Wars  $25.0
Cookie  $5.0
Which items would you like to buy? Cookie
Anything else? (Y/N): n
Your Total is $30.00.
Thank you for shopping at Target!

Welcome to Target! Choose the following options:
1) Make a Purchase
2) Make a Return
3) Manage Inventory
4) View Report
5) Exit
Enter your choice: 2
Item Name       Price
Lego Star Wars  $25.0
Cookie  $5.0
Which items would you like to return? Cookie
Anything else? (Y/N): n
Your Refund total is $5.00.
Thank you for shopping at Target!

Welcome to Target! Choose the following options:
1) Make a Purchase
2) Make a Return
3) Manage Inventory
4) View Report
5) Exit
Enter your choice: 3

Manage Inventory
Item Name       Price
Lego Star Wars  $25.0
Cookie  $5.0
1) Add New Item
2) Remove Item
3) Main Menu
Choose an option: 1
Item Name: Candy
Item Price: 2
Added Successfully!!

Manage Inventory
Item Name       Price
Lego Star Wars  $25.0
Cookie  $5.0
Candy   $2.0
1) Add New Item
2) Remove Item
3) Main Menu
Choose an option: 3

Welcome to Target! Choose the following options:
1) Make a Purchase
2) Make a Return
3) Manage Inventory
4) View Report
5) Exit
Enter your choice: 4

Reports:
Total Customers: 1
Total Profit: $30.00
Click any key to go back to the main menu. 

Welcome to Target! Choose the following options:
1) Make a Purchase
2) Make a Return
3) Manage Inventory
4) View Report
5) Exit
Enter your choice: 5
Goodbye!
```

## Author

Natalie Vidarte CMPS 372 Student — Spring 2025


## screenshot
![Screenshot 2025-05-15 at 2 33 58 PM](https://github.com/user-attachments/assets/9145f403-1673-486e-bfd8-642a4cc17ec1)
