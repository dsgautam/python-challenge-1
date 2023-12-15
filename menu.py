# This is a program to display men items to customers to place an order.
# This ncludes storing the customer's order and printing the receipt with the total price of all items ordered.
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
menu_selected = {}
j=1
total_price = 0
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
        #debug code
        #print(f"menu item is : {menu_items}" )
    # Get the customer's input
    menu_category = input("Type menu number: ")
        
    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            # debug code
            #print(menu_items)
            menu_selection = input("Select menu sub item number: ")
        
            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Check if the customer's input is a valid option
                # Convert the menu selection to an integer
                
                if int(menu_selection) in menu_items.keys():
                # 4. Check if the menu selection is in the menu items
                    # Store the item name as a variable
                #   menu_selection_item = 
                    menu_selected_item = menu_items[int(menu_selection)]["Item name"]
                    menu_selected_price = menu_items[int(menu_selection)]["Price"]
                    print (f"you selected: {menu_selected_item}, with price ${menu_selected_price}")
                    # Ask the customer for the quantity of the menu item
                    quantity = input("Type menu sub item Quanity, if error, default Quantity is 1: ")
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                        print(f"you selected {menu_selected_item}, quantity: {quantity}")
                    else:
                        print("E5: Invalid entry, quantity defaulted to 1")
                        quantiy=1
                    
                    # Add the item name, price, and quantity to the order list
                    menu_selected[j] = {
                        "Item name": menu_selected_item,
                        "Price": menu_selected_price,
                        "quantity" : quantity
                    }
                    j += 1
                    #print (f"Items selected : {menu_selected}")
                else:
                    # Tell the customer they didn't select a menu option
                    # Tell the customer that their input isn't valid
                    print(f"E4: {menu_selection} : was not a valid menu option.")
                   
            else:
                # Tell the customer they didn't select a number
                # Tell the customer they didn't select a menu option
                print(f" E3: {menu_selection} : You didn't select a valid menu item number.")         

        else:
            # Tell the customer they didn't select a menu option
            print(f"E2: {menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("E1: You didn't select a number.")
    line_separater= '*'*40
    print (f"{line_separater}")
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering.lower() == "y":
            print("continue")
            break
        elif keep_ordering.lower() == "n":
            print("Thank you for your order")
            place_order = False
            break
        else:
            print("please enter a valid input")
                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again
# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)
print (f"Items selected : {menu_selected}")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables
    # 8. Calculate the number of spaces for formatted printing
    # 9. Create space strings
    # 10. Print the item name, price, and quantity
i=1
for key, value in menu_selected.items():
    #print (key, value)
    if type(value) is dict:
        num_item_spaces = 25 - len(value["Item name"])
        item_spaces = " " * num_item_spaces
        item_spaces_2 = " " * 2                
        print(f"{value['Item name']}{item_spaces} | ${value['Price']}{item_spaces_2}| {value['quantity']}") 
        total_price = total_price + (value["Price"] * value["quantity"])
    else:
        num_item_spaces = 25 - len(value)
        item_spaces = " " * num_item_spaces
        item_spaces_2 = " " * 2                
        print(f"{value}{item_spaces} - Error | '*******' | '*' "  ) 
    i += 1
# 11. Calculate the cost of the order using list comprehension
print(f"Your Total order is: ${total_price: ,.2f}")

# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
