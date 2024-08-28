# Create a date.py script that is a date simulator and does the following:

# User inputs who is on the date with them
# User inputs their budget for the date
# Print the restaurant menu (your group created this!) 
# User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
# Script tells the user how much money they have left after each order.
# At the end of the date user must agree to pay the bill and then their final budget is shown to them.
# Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision. 

# Welcome user to restaurant
def welcome_message():
    print("\nHello and welcome to Grand Haven!\nWe're pleased to have you dine with us tonight.\n"
          "I see you have a partner with you tonight.\nI hope you both enjoy your evening with us.\n"
          "Before we get started, I'll have to ask for some information.\n")

# User input who is on the date with them
def get_date_info():
    dates_name = input("What is your date's name?\n")
    while True:
        try:
            date_budget = input("What is your budget for tonight's date?\n")
            date_budget = float(date_budget)
            break # Exit if conversion successful
        except ValueError:
            print("Invalid input. Please enter a numerical value for the budget.")
    return dates_name, date_budget

# I need to print out the menu so that the user can select what they want for their food.
def display_menu(menu):
    print(f"\nHere's the menu for tonight. Please take a look and decide what you'd like to order.\n")
    displayed_menu = ""
    for category, dishes in menu.items():
        displayed_menu += f"{category}\n" + "-" * 28 + "\n"
        for dish, details in dishes.items():
            displayed_menu += f"{dish:<28}{details['Price']}\n"
        displayed_menu += "\n"
    return displayed_menu

# I need to get user input for the food/drink choices on the menu they would like to order and store that somewhere. 
def get_order(menu, budget):
    # Prompt user for order and validate input
    orders = []
    food_tab = 0
    while True:
        print(f"\nYour current budget is: ${budget:.2f}\n")
        food_order = input("What would you like to order? (Type 'done' to finish): ")
        
        # Check if user wants to exit
        if food_order.lower() == 'done':
            break
        
        # Check if order is in the menu
        found = False
        for category, dishes in menu.items():
            for dish_name in dishes:
                if food_order.lower() == dish_name.lower():
                    price = dishes[dish_name]['Price']
                    if price == "Free":
                        price = 0.0
                    if price <= budget:
                        orders.append(dish_name)
                        food_tab += price
                        budget -= price
                        print(f"Added '{dish_name}' to your order for ${price:.2f}.")
                        found = True
                        break
                    else:
                        print(f"Insufficient budget for '{dish_name}'.")
                        found = True
                        break
        # If variable found is still false, then that means order was not found in the menu then this if not statement runs because if not false == if true.
        if not found:
            print(f"'{food_order}' is not on the menu. Please select a valid menu item.")
    return orders, food_tab, budget

def close_out(orders, check, budget, dates_name):
    print(f"\nPerfect, thank you for your order. We'll get your dishes right out to you.\n")
    closeout_tab = input(f"\nI hope you and {dates_name} had a wonderful meal with us today. Would you like the check?\n").lower()

    # List of acceptable responses
    yes_responses = ['y', 'yes', 'yep', 'yeah', 'sure', 'of course']

    if closeout_tab in yes_responses:
        print("Great, I'll go get your check for you.")
    else:
        print(f"Apologies, your time with us is coming to an end and I must implore that you close our your bill.\n"
               "We have other customers to serve, now that you are finished, I ask that you pay your bill and leave.\n"
               "Apologies for pushing you out but I ask for your understanding. Thank you.\n")

    print(f"Here is your check. This is what you've ordered: {orders}")
    print(f"You owe ${check:.2f} and your remaining budget is ${budget:.2f}.")

def second_date(orders, check, date_budget):
    


if __name__ == "__main__":
    welcome_message()
    dates_name, date_budget = get_date_info()
    
    # Restaurant Menu
    menu = {
        "Appetizers": {
            "Nachos": {"Price": 3.0, "Ingredients": ["Chips", "Cheese", "Beans"], "Dietary Info": "Vegetarian"},
            "Queso": {"Price": 4.0, "Ingredients": ["Cheddar", "Swiss", "Pepper Jack"], "Dietary Info": "Lactose Free"}, 
            "Calamari": {"Price": 5.0, "Ingredients": ["Squid", "Panko", "Marinara"], "Dietary Info": "Gluten Free"}
        },
        "Entree": {
            "Chicken": {"Price": 6.0, "Ingredients": ["Chicken", "Mushrooms", "Pasta"], "Dietary Info": "GF"},
            "Beef": {"Price": 7.0, "Ingredients": ["Beef", "Onions"], "Dietary Info": "Keto Friendly"},
            "Shrimp": {"Price": 8.0, "Ingredients": ["Shrimp", "Lemon Pepper", "Cocktail Sauce"], "Dietary Info": "Keto Friendly"},
        },
        "Dessert": {
            "Cake": {"Price": 5.0, "Ingredients": ["Strawberry", "Cream Cheese", "Graham Crackers"], "Dietary Info": "Dairy, Eggs"},
            "Pie": {"Price": 5.0, "Ingredients": ["Cherry", "Whipped Cream", "Walnuts"], "Dietary Info": "Dairy, Nuts"},
            "Ice Cream": {"Price": 3.0, "Ingredients": ["Heavy Cream", "Vanilla", "Chocolate Syrup"], "Dietary Info": "Dairy"}
        },
        "Beverages": {
            "Milkshake": {"Price": 6.0, "Ingredients": ["Strawberry", "Vanilla", "Chocolate", "Oreos", "Milk"], "Dietary Info": "Dairy"}, 
            "Coke": {"Price": 1.0, "Ingredients": ["Sugar", "Artificial Flavors"], "Dietary Info": "N/A"}, 
            "Water": {"Price": "Free", "Ingredients": ["Water"], "Dietary Info": "High Quality H20"}
        }
    }

    print(f"\n\nAmazing, thank you so much for that information.\nLet me take you to your seats and give you our menu.")
    print(display_menu(menu))

    orders, check, budget = get_order(menu, date_budget)
    close_out(orders, check, budget, dates_name)
