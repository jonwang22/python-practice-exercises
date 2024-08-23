# Nested Restaurnat Menu Dictionary
# Course: Appetizers, Entree, Dessert, Beverages
# Subcategories: Price, Ingredients (Dietary Restrictions (GF = Gluten Free V = Vegan)
# Appetizers = Nachos, Queso, Calamari
# Entree = Chicken, Beef, Shrimp
# Dessert = Cake, Pie, Ice Cream
# Beverages = Milkshakes, Coke, Water 



menu = {
    "Appetizers": {
        "Nachos": {"Price": 3.0, "Ingredients": ["Chips", "Cheese", "Beans"], "Dietary Restrictions": "GF"},
        "Queso": {"Price": 4.0, "Ingredients": ["Cheddar", "Swiss", "Pepper Jack"], "Dietary Restrictions": "V"}, 
        "Calamari": {"Price": 5.0, "Ingredients": ["Squid", "Panko", "Marinara"], "Dietary Restrictions": "GF/V"}
    },
    "Entree": {
        "Chicken": {"Price": 6.0, "Ingredients": ["Chicken", "Mushrooms", "Pasta"], "Dietary Restrictions": "GF"},
        "Beef": {"Price": 7.0, "Ingredients": ["Beef", "Onions"], "Dietary Restrictions": "GF"},
        "Shrimp": {"Price": 8.0, "Ingredients": ["Squid", "Panko", "Marinara"]},
    },
    "Dessert": {"Cake", "Pie", "Ice Cream"},
    "Beverages": {"Milkshakes", "Coke", "Water"}
}

print(menu["Appetizers"]["Calamari"]["Ingredients"][0])