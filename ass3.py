# POS for aamo el dekanje
# You want to write a POS system (point of service) to your neighbor’s dekene.
# In this system, you keep track of the items available. The items have a name and a price.
# When the system starts, it gives aamo el dekanje two options:
# 1.	To start a new order
# 2.	To close the program
# If they input 2, the program says “bye bye” and terminates.
# If they input 1, the program gives them the following options:
# 1.	To add a new item
# 2.	To check the total of the bill
# 3.	To add a coupon
# 4.	To checkout
# If the user inputs 1: the program asks them for the needed info to add an item to their order and then does so, then asks them what they would like to do again.
# If the user inputs 2: the program prints “the total of your bill is” and then the total, then asks them what they would like to do again.
# If the user inputs 3: the program asks for the value of the coupon and removes it from the total of the bill
# If the user inputs 4: the program prints all the items bought and their quantities
# It then prints the total of the order (without coupons)
# The total of the coupons
# And then the total they have to pay (total of order-total of coupons)
# once all of these are printed, aamo el dekanje is taken back to the original menu

# database of items -> list
# name, price
def printListItems(list):
    i = 1

    for item in list:
        print(f"{i} - {item[0]} for price : {item[1]}$")
        i += 1


def addItem(items) :

    add_more_items = True
    basket = []

    while add_more_items:

        print("\nWhich of these items would you like to add to your basket? ")
        printListItems(items)

    
        chosen_item_idx = int(input()) - 1

        if  chosen_item_idx >= 0 and chosen_item_idx < len(items):

            quantity = int(input(f"How many {items[chosen_item_idx][0]} would you like to have ? "))

            added_item = []
            added_item.extend(items[chosen_item_idx])
            added_item.append(quantity)
            
            basket.append(added_item)

            print(basket)

            print("Would you like to add another item ?")

            if input() == "no":
                add_more_items = False
        
        else:
            print("Invalid Input - Try again")

    return basket


def calc_total(basket):
    
    if len(basket) > 0:
        total = 0

        for item in basket:
            total += item[1] * item[2]
    
        return total
    else:
        return 0


def checkTotal(total):
    if total == 0:
        print("Please be sure to add items to your basket before checking for the total price")
    else:
        print(f"the total of your bill is {total}$")


def addCoupon() :
    coupon = int(input("What is the value of your coupon ? "))
    print(f"remove {coupon}$ from total price")
    return coupon
    

def checkOut(basket, total, coupon):
    print("You've bought these products : ")

    for item in basket:
        print(f"product name : {item[0]}, price : {item[1]}$, quantity : {item[2]}")

    print(f"The total of the order (wihtout coupons) : {total}$")
    print(f"The total of the coupons : {coupon}$")
    print(f"You've to pay {total - coupon}$")


def newOrder():
    items=[["tomato",1],["potato",2],["chocolate",3],["soap",0.5]]  # our item list will contain nested lists each list will contain [name_of_item, price, quantity], quantity will be taken from the user
    still_shopping = True
    user_basket = []
    coupon = 0
    total_price = 0

    while still_shopping:
        print("\n1 - Add new item : ")
        print("2 - Check the total of the bill")
        print("3 - To add a coupon")
        print("4 - To checkout")

        user_input = int(input())
    
        if user_input == 1:
            basket = addItem(items)
            user_basket.extend(basket)
        elif user_input == 2:
           total_price +=  calc_total(user_basket)
           checkTotal(total_price)
        elif user_input == 3:
            coupon += addCoupon()
        elif user_input == 4:
            checkOut(user_basket, total_price, coupon)
            still_shopping = False
        else:
            print("Invalid Input")

def mainMenu():
    still_shopping = True
    while still_shopping:
        print("1 - To start a new order ")
        print("2 - To close the program ")
        
        user_input = int(input())

        if user_input == 1:
            newOrder()
        else:
            still_shopping = False
            print("bye bye")

mainMenu()

# list --> name, count
# another list will be generated for price, count


# import re

# def is_valid_product(product_name):
#     if len(product_name) < 4: # product name must have at least 4 characters
#         return False

#     regex = "^[a-zA-Z\s]+$"# regular expression (only letters and spaces allowed for product name)

#     if not re.match(regex, product_name):
#         return False
#     return True


# def handle_products_count(item_list, product_name):
#     does_exist = False
    
#     for item in item_list:
#         if item[0] == product_name:
#             item[1] += 1
#             does_exist = True
#     return does_exist


# def add_item(user_items):
#     add_again = True
#     print("\nAdding items...")

#     while add_again:
#         product_name = input("Enter the info of the item you want to add: ")
#         quantity = 0
#         if is_valid_product(product_name): # will check if user entered a new product or product already exist on the list user_items
#             check_products = handle_products_count(user_items, product_name)

#             if not check_products:
#                 user_items.append([product_name, 1])
#             else:
#                 print("Item already exists")

#             print(user_items)

#             decision = input("\nWould you like to add another item? Type 'y' for yes, 'n' for no: ")

#             if decision == "n":
#                 add_again = False
#             elif decision == "y":
#                 print("\nAdding another item...")
#             else:
#                 print("Invalid Input - Try again")
#         else:
#             print("Invalid Input - Try again")


# import random

# def set_random_price():
#     return random.randint(1, 20)

# def calc_total_price(item_info):
#     total = 0
#     for entry in item_info:
#         total += entry[0] * entry[1]

#     return total
    
# def calc_total_bill(user_items):
#     total = 0

#     for item in user_items:
#         total += set_random_price() * item[1]
    
#     return total


# def add_coupon(totalBill):
#     coupon = int(input("Enter coupn value : "))
#     if coupon > 0:
#         totalBill -= coupon
#         print(f"Coupon applied : -{coupon}$")
#     else:
#         print("Invalid coupon value")

#     return coupon


# def check_out(user_items, totalBill, coupon):
#     print("User bought : ", end=" ")
#     for entry in user_items:
#         print(f"{entry[1]} {entry[0]}", end=" ")
#     print("\nChecking Out")
#     print(f"Total Bill without coupons : {totalBill}$")
#     print(f"You have to pay : {totalBill - coupon}")

# def new_order():
#     get_new_order = True
#     coupon_value  = 0
#     user_items = []
#     while get_new_order:
#         print("\n1. To add a new item")
#         print("2. Check the total of the bill")
#         print("3. To add a coupon")
#         print("4. To checkout")

#         choice = int(input())

#         if choice == 1:
#             add_item(user_items)
#         elif choice == 2:
#             totalBill = calc_total_bill(user_items)
#             print(f"The total of your bill is : {totalBill}$") # this will do check total bill functionality 
#         elif choice == 3:
#             coupon_value += add_coupon()
#             add_coupon(totalBill)
#         elif choice == 4:
#             check_out(user_items, totalBill)
#             get_new_order = False
#         else:
#             print("Invalid Input")

# def main_menu():

#     get_out = True
    
#     print("Welcome to the neighbor’s dekene")

#     while get_out:
#         print("Pick one of these options")
#         print("1. To start a new order")
#         print("2. To close the program")

#         choice = int(input())

#         if choice == 1:
#             print("Starting a new order...")
#             new_order()
#         elif choice == 2:
#             print("Bye bye")
#             get_out = False
#         else:
#             print("Invalid Input")
            
# main_menu()


