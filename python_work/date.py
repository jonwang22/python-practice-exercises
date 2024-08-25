# Create a date.py script that is a date simulator and does the following:

# User inputs who is on the date with them
# User inputs their budget for the date
# Print the restaurant menu (your group created this!) 
# User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
# Script tells the user how much money they have left after each order.
# At the end of the date user must agree to pay the bill and then their final budget is shown to them.
# Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision. 

# Welcome user to restaurant
print(f"\nHello and welcome to Grand Haven!\nWe're pleased to have you dine with us tonight.\nI see you have a partner with you tonight.\nI hope you both enjoy your evening with us.\nBefore we get started, I'll have to ask for some information.")

# User input who is on the date with them
dates_name = input("What is your date's name?\n")

# User input budget for date
date_budget = input("What is your budget for tonight's date?\n")

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
        "Milkshakes": {"Price": 6.0, "Ingredients": ["Strawberry", "Vanilla", "Chocolate", "Oreos", "Milk"], "Dietary Info": "Dairy"}, 
        "Coke": {"Price": 1.0, "Ingredients": ["Sugar", "Artificial Flavors"], "Dietary Info": "N/A"}, 
        "Water": {"Price": "Free", "Ingredients": ["Water"], "Dietary Info": "High Quality H20"}
    }
}

# I need to print out the menu so that the user can select what they want for their food.
# pprint.pprint(menu)
def display_menu(menu):
    print(f"\nHere's the menu for tonight. Please take a look and decide what you'd like to order.\n")
    displayed_menu = ""
    for category, items in menu.items():
        displayed_menu += f"{category}\n" + "-" * 28 + "\n"
        for item, details in items.items():
            displayed_menu += f"{item:<28}{details['Price']}\n"
        displayed_menu += "\n"
    return displayed_menu


print(f"\n\nAmazing, thank you so much for that information.\nLet me take you to your seats and give you our menu.")

print(display_menu(menu))