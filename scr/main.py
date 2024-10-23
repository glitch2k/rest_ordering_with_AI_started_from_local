import random

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

def display_menu():
    print("\n---- Menu ----")
    for order in order_data['all_orders']:
        for key, value in order.items():
            print(f"{key}: {value['order_name']} - ${value['order_price']:.2f}")
    print("--------------\n")

def take_order():
    total_cost = 0
    orders_selected = []
    while True:
        try:
            order_number = int(input("Enter the order number (0 to finish): "))
            if order_number == 0:
                break
            found = False
            for order in order_data['all_orders']:
                if order_number in order:
                    orders_selected.append(order[order_number])
                    total_cost += order[order_number]['order_price']
                    found = True
                    print(f"Added {order[order_number]['order_name']} for ${order[order_number]['order_price']:.2f}")
            if not found:
                print("Invalid order number, please try again.")
        except ValueError:
            print("Please enter a valid number.")
    return orders_selected, total_cost

def handle_transaction(total_cost, orders_selected):
    while True:
        try:
            money_paid = float(input(f"Total cost is ${total_cost:.2f}. Enter the amount paid: "))
            if money_paid < total_cost:
                print("Not enough money, please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    change_due = money_paid - total_cost
    order_number = random.randint(1000, 9999)
    receipt_number = random.randint(100000, 999999)

    print("\n---- Receipt ----")
    for order in orders_selected:
        print(f"{order['order_name']} - ${order['order_price']:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Amount paid: ${money_paid:.2f}")
    print(f"Change due: ${change_due:.2f}")
    print(f"Order Number: {order_number}")
    print(f"Receipt Number: {receipt_number}")
    print("-----------------\n")

def main():
    print("Welcome to the restaurant!")
    while True:
        display_menu()
        orders_selected, total_cost = take_order()
        if orders_selected:
            handle_transaction(total_cost, orders_selected)
        else:
            print("No orders placed.")

        more_orders = input("Would you like to place another order? (yes/no): ").strip().lower()
        if more_orders != 'yes':
            print("Thank you for your visit!")
            break

if __name__ == "__main__":
    main()
