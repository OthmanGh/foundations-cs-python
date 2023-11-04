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

items = []

def handle_products_count(list, product_name):
    does_exist = False
    
    for item in list:
        if item[0] == product_name:
            item[1] += 1
            does_exist = True

    return does_exist

def addItem():
    add_again = True
    print("\nAdding Items...")

    while add_again:
        product_name = input("Enter the info of the item you wanna add : ")
        
        check_products = handle_products_count(items, product_name)

        if not check_products:
            items.append([product_name, 1])
        else:
            print("Already exist")

        print(items)

        descision = input("\nWould you like to add another item or same maybe? Type y for yes, n for no ")

        if descision == "n":
            add_again = False
        elif descision == "y":
            print("\nAdding another Item...")
        else:
            print("Invalid Input - Try again")
        

def checkTotalBill():
    print("checking Total Bill")

def addCoupon():
    print("Adding a Coupon")

def checkOut():
    print("Checking Out")

def newOrder():
    get_new_order = True
    while get_new_order:
        print("\n1. To add a new item")
        print("2. Check the total of bill")
        print("3. To add a coupon")
        print("4. To checkout")

        choice = int(input())

        if choice == 1:
            addItem()
        elif choice == 2:
            checkTotalBill()
        elif choice == 3:
            addCoupon()
        elif choice == 4:
            get_new_order = False
        else:
            print("Invalid Input")


def mainMenu():
    get_out = True

    while get_out:
        print("Welcome to neighbor’s dekene ")
        print("Pick one of these options ")
        print("1. To start a new order ")
        print("2. To close the program ")

        choice = int(input())

        if choice == 1:
            print("starting a new order...")
            newOrder()
        elif choice == 2:
            print("“bye bye”")
            get_out = False
        else:
            print("Invalid Input")


mainMenu()
