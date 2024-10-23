import random
import json
import os
from datetime import datetime

# Data Model for all order objects
order_data = {
    'all_orders': [
        {
            1: {
                'order_name': 'cheese burger meal',
                'order_desc': 'cheese burger - fries - medium drink',
                'order_price': 5.34
            }
        },
        {
            2: {
                'order_name': 'dark chicken meal',
                'order_desc': '1/4 dark chicken - fries - medium drink',
                'order_price': 11.49
            }
        },
        {
            3: {
                'order_name': 'white chicken meal',
                'order_desc': '1/4 white chicken - fries - medium drink',
                'order_price': 21.49
            }
        }
    ]
}

# File to store the transactions
TRANSACTION_FILE = "transactions.json"

# List to store today's transactions
daily_transactions = []


def load_transactions():
    """
    Loads the existing transactions from the file (if any).
    Returns the list of transactions loaded from the file.
    """
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "r") as file:
            return json.load(file)
    return []


def save_transactions(transactions):
    """
    Saves the transactions to a JSON file.
    Writes the list of transactions (including the ones for the current day) to the file.
    """
    with open(TRANSACTION_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


def display_menu():
    """
    Displays the menu of available orders to the user.
    Loops through the order_data and prints each order's name and price.
    """
    print("\n---- Menu ----")
    for order in order_data['all_orders']:
        for key, value in order.items():
            print(f"{key}: {value['order_name']} - ${value['order_price']:.2f}")
    print("--------------\n")


def take_order():
    """
    Handles the process of taking an order from the user.
    Prompts the user to input order numbers and adds the selected orders to a list.
    Also calculates the total cost of the selected orders.
    Returns:
        orders_selected: List of dictionaries containing the selected orders.
        total_cost: The total sum of all selected orders.
    """
    total_cost = 0
    orders_selected = []
    while True:
        try:
            order_number = input("Enter the order number (0 to finish): ")

            # Validate if the input is numeric
            if not order_number.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            order_number = int(order_number)
            
            if order_number == 0:
                break
            
            found = False
            for order in order_data['all_orders']:
                if order_number in order:
                    # Add the selected order to the list and update total cost
                    orders_selected.append(order[order_number])
                    total_cost += order[order_number]['order_price']
                    found = True
                    print(f"Added {order[order_number]['order_name']} for ${order[order_number]['order_price']:.2f}")
                    break

            if not found:
                print("Invalid order number, please try again.")
        except ValueError:
            print("Please enter a valid number.")
    return orders_selected, total_cost


def handle_transaction(total_cost, orders_selected):
    """
    Handles the payment transaction process.
    Prompts the user to input the amount of money paid, checks if it covers the total cost,
    and calculates the change due. Then generates a random order number and receipt number.
    Displays a receipt showing the orders, their prices, total cost, money paid, change due, order number, and receipt number.
    Logs the transaction to the list of daily transactions.
    
    Parameters:
        total_cost: The total cost of the selected orders.
        orders_selected: List of dictionaries containing the selected orders.
    """
    while True:
        try:
            money_paid = input(f"Total cost is ${total_cost:.2f}. Enter the amount paid: ")

            # Validate if input is a valid float
            try:
                money_paid = float(money_paid)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                continue

            if money_paid < total_cost:
                print("Not enough money, please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    change_due = money_paid - total_cost
    order_number = random.randint(1000, 9999)
    receipt_number = random.randint(100000, 999999)

    # Log the transaction
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "order_number": order_number,
        "receipt_number": receipt_number,
        "orders": orders_selected,
        "total_cost": total_cost,
        "money_paid": money_paid,
        "change_due": change_due
    }
    daily_transactions.append(transaction)

    # Display receipt with order details and payment information
    print("\n---- Receipt ----")
    for order in orders_selected:
        print(f"{order['order_name']} - ${order['order_price']:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Amount paid: ${money_paid:.2f}")
    print(f"Change due: ${change_due:.2f}")
    print(f"Order Number: {order_number}")
    print(f"Receipt Number: {receipt_number}")
    print("-----------------\n")


def view_todays_transactions():
    """
    Displays the list of all transactions made today.
    Shows each transaction's order details, total cost, money paid, change due, order number, and receipt number.
    """
    print("\n---- Today's Transactions ----")
    if not daily_transactions:
        print("No transactions have been made today.")
    else:
        for transaction in daily_transactions:
            print(f"Order Number: {transaction['order_number']}, Receipt Number: {transaction['receipt_number']}")
            for order in transaction['orders']:
                print(f"- {order['order_name']} - ${order['order_price']:.2f}")
            print(f"Total cost: ${transaction['total_cost']:.2f}")
            print(f"Amount paid: ${transaction['money_paid']:.2f}")
            print(f"Change due: ${transaction['change_due']:.2f}")
            print("-----------------\n")


def main():
    """
    Main function to run the program.
    Welcomes the user, displays the menu, handles taking an order, and manages the payment transaction.
    After completing an order, asks if the user wants to place another order.
    Adds an option to view the transactions made today.
    Saves the transactions of the day to a file when the user finishes.
    """
    print("Welcome to the restaurant!")

    # Load existing transactions from file
    transactions = load_transactions()

    while True:
        print("\nMain Menu:")
        print("1. Place an Order")
        print("2. View Today's Transactions")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            # Show menu and handle order placement
            display_menu()
            orders_selected, total_cost = take_order()

            # Proceed to payment only if there are selected orders
            if orders_selected:
                handle_transaction(total_cost, orders_selected)
            else:
                print("No orders placed.")

        elif choice == '2':
            # View today's transactions
            view_todays_transactions()

        elif choice == '3':
            print("Thank you for your visit!")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")

    # Save the day's transactions to the file
    transactions.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "transactions": daily_transactions
    })
    save_transactions(transactions)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
