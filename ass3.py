# system that records the orders of the customers
#* POS for aamo el dekanje
#* You want to write a POS system (point of service) to your neighbor’s dekene.
#* In this system, you keep track of the items available. The items have a name and a price.
#* When the system starts, it gives aamo el dekanje two options:
#* 1.	To start a new order
#* 2.	To close the program
#* If they input 2, the program says “bye bye” and terminates.
#* If they input 1, the program gives them the following options:
#* 1.	To add a new item
#* 2.	To check the total of the bill
#* 3.	To add a coupon
#* 4.	To checkout
#* If the user inputs 1: the program asks them for the needed info to add an item to their order and then does so, then asks them what they would like to do again.
#* If the user inputs 2: the program prints “the total of your bill is” and then the total, then asks them what they would like to do again.
#* If the user inputs 3: the program asks for the value of the coupon and removes it from the total of the bill
#* If the user inputs 4: the program prints all the items bought and their quantities
#* If then prints the total of the order (without coupons)
#* The total of the coupons
#* And then the total they have to pay (total of order-total of coupons)
#* once all of these are printed, aamo el dekanje is taken back to the original menu

#* database of items --> list
#* name, price

import re

user_items = []

def is_valid_product(product_name):
    if len(product_name) < 4: # product name must have at least 4 characters
        return False

    regex = "^[a-zA-Z\s]+$" # regular expression (only letters and spaces allowed for product name)

    if not re.match(regex, product_name):
        return False

    return True

def handle_products_count(item_list, product_name):
    does_exist = False
    
    for item in item_list:
        if item[0] == product_name:
            item[1] += 1
            does_exist = True

    return does_exist

def add_item():
    add_again = True
    print("\nAdding items...")

    while add_again:
        product_name = input("Enter the info of the item you want to add: ")

        if is_valid_product(product_name): # will check if user entered a new product or product already exist on the list user_items
            check_products = handle_products_count(user_items, product_name)

            if not check_products:
                user_items.append([product_name, 1])
            else:
                print("Item already exists")

            print(user_items)

            decision = input("\nWould you like to add another item? Type 'y' for yes, 'n' for no: ")

            if decision == "n":
                add_again = False
            elif decision == "y":
                print("\nAdding another item...")
            else:
                print("Invalid Input - Try again")
        else:
            print("Invalid Input - Try again")

def check_total_bill():
    print("Checking Total Bill")

def add_coupon():
    print("Adding a Coupon")

def check_out():
    print("Checking Out")

def new_order():
    get_new_order = True
    while get_new_order:
        print("\n1. To add a new item")
        print("2. Check the total of the bill")
        print("3. To add a coupon")
        print("4. To checkout")

        choice = int(input())

        if choice == 1:
            add_item()
        elif choice == 2:
            check_total_bill()
        elif choice == 3:
            add_coupon()
        elif choice == 4:
            get_new_order = False
        else:
            print("Invalid Input")

def main_menu():
    get_out = True

    while get_out:
        print("Welcome to the neighbor’s dekene")
        print("Pick one of these options")
        print("1. To start a new order")
        print("2. To close the program")

        choice = int(input())

        if choice == 1:
            print("Starting a new order...")
            new_order()
        elif choice == 2:
            print("Bye bye")
            get_out = False
        else:
            print("Invalid Input")

main_menu()


# regular expression (only letters and spaces allowed for product name)

    # In the regular expression:
    # ^ asserts the start of the string.
    # [a-zA-Z\s] matches any uppercase letter, lowercase letter, or space.
    # + ensures that one or more of these characters must be present.
    # $ asserts the end of the string.

