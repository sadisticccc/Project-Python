#initialising the constant value for a pizza.
PIZZA_PRICE = 12

#menu for different pizza options.
pizza_menu = {
    '1': 'Margherita',
    '2': 'Pepperoni',
    '3': 'Vegetarian',
    '4': 'Hawaiian',
    '5': 'Meat Lovers',
}

def display_menu():
    #display the pizza menu with prices.
    print("\nPizza Menu:")
    for key, value in pizza_menu.items():
        print(f"{key}. {value} - ${PIZZA_PRICE}")


def which_one():

    while True:
        try:
            orders = int(input("\nEnter which pizza you want to order. "))
            if orders <= 0:
                print("\nPlease enter a number between 1-5. ")
            elif orders >= 1  and orders<= 5:
                print(f"You ordered {pizza_menu[str(orders)]} pizza.")
                break
            else:
                print("\nPlease enter a number between 1-5. ")
        except ValueError:
            print("Enter a valid number!")
    

def take_input():
    # Get the number of pizzas from the user.
    while True:
        try:
            orders = int(input("\nEnter how many pizzas you want to order ? "))
            if orders <= 0:
                print("Please enter a valid number greater than 0.")
            else:
                print(f"You ordered {orders} pizza(s).")
                break
        except ValueError:
            print("Enter a valid number!")

    while True:
        # Get delivery preference from the user with error handling.
        delivery = input("\nIs delivery required? (yes/no) ").lower()
        if delivery in ['yes', 'no', 'y', 'n']:
            print(f"Delivery: {delivery}.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        # Check if it's Tuesday with error handling.
        tuesday = input("\nIs it Tuesday? (yes/no) ").lower()
        if tuesday in ['yes', 'no', 'y', 'n']:
            print(f"It is{' ' if (tuesday == 'yes' or tuesday == 'y') else 'not'} Tuesday. Get 50% off on Tuesdays!!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        # Check if the app was used with error handling.
        app = input("\nDid the customer use the app? (yes/no) ").lower()
        if app in ['yes', 'no', 'y', 'n']:
            print(f"App used: {app}.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    return orders, delivery, tuesday, app

def calculate_total_orders(orders):
    # Calculate the total cost of pizzas without any discounts.
    return orders * PIZZA_PRICE 

def calculate_delivery_cost(delivery, orders, total):
    # Add delivery cost if applicable.
    if int(orders) < 5 and (delivery == "yes" or delivery == 'y'):
        total += 2.5
        print("\nYour delivery cost is added(2.5). ")
    else:
        print("\nYour delivery cost is not added. ")
    return total

def apply_tuesday_discount(tuesday, total):
    # Apply Tuesday discount if applicable.
    if tuesday == "yes" or tuesday == 'y':
        total -= 0.5 * total  # 50% discount
    return total
    
def apply_app_discount(app, total):
    # Apply app discount if applicable.
    if app == "yes" or app == 'y':
        total -= 0.25 * total  # 25% discount
        print("You get 25% discount as you have used the app. ")
    else:
        print("You don't get 50% discount as you didnt use the app to order. ")
    return total

def print_receipt(final_price):
    # Display the final price after all discounts.
    print(f"\nYour total price after discounts is ${final_price:.2f}.")



# execute the pizza ordering process
#display the pizza menu
display_menu()

#allow the user to choose a pizza
selected_pizza = which_one()

#take user input for order details
orders, delivery, tuesday, app = take_input()

#calculate the total cost of pizzas without any discounts
total_price = calculate_total_orders(orders)

#add delivery cost if applicable
total_price_with_delivery = calculate_delivery_cost(delivery, orders, total_price)

#apply tuesday discount if applicable 
total_price_with_tuesday_discount= apply_tuesday_discount(tuesday, total_price_with_delivery)

#apply app discount if applicable 
final_price = apply_app_discount(app, total_price_with_tuesday_discount)

#print the final receipt
print_receipt(final_price)
