
#* You are writing a system for a transport company.
#* This company has a list of cities, and a list of drivers. Each driver has their specific route.
#* For example, if the route of the driver “Alex” is Beirut, Zahle, it means that he will go to Beirut and then Zahle.
#* Write a system that repeatedly prompts the user with the following options:
#* Enter:

#* 1.	To add a city
#* 2.	To add a driver
#* 3.	To add a city to the route of a driver
#* 4.	Remove a city from a driver’s route
#* 5.	To check the deliverability of a package
#* If the user inputs 1, they are asked the name of the city. This name (if valid) is added to the list of cities.
#* If the user input 2, they are asked the name of the driver and then the name of the cities they will visit (how you will ask for the route if up to you)
#* If the user inputs 3, they are prompted the name of the driver and then the name of the city to add. If all is well, the user is then given the following options:
#* Input:
#* 0.	To add to the beginning of the route
#* -1. To add to the end of the route
#* #. (any other number) to add that city to the given index
#* If the user inputs 4, they are prompted the name of the driver and then the name of the city to delete. If all is well, that city is removed from the route of the driver.
#* If the user inputs 5, they are asked for the name of the city they would like to deliver the package to if all is well, a list of all the drivers that deliver to this city is shown.

# Good luck and don’t cry too much 😭 :)

### Transportation Company :
# delivers to cities

cities = ["Sour", "Saida", "Beirut", "Zahle", "Baalbek"]

driver_route_dict = {
    "Ahmad Solyman": ["Sour", "Saida"],
    "Ali Hussein": ["Zahle"],
    "Hilal Jomaa": ["Beirut"],
    "Ali Ali": ["Beirut"],
}

# name of the city should be valid if: at least 4 chars, doesn't include any numbers, doesn't exist in the cities list
def isValidCityNameList(city):
    if len(city) < 3 or len(city) > 15:
        return False
    
    for cityNames in cities: # Time Complexity O(N)
        if city == cityNames.lower():
            return 0
    
    for char in city: # Time Complexity O(N)
        if char.isdigit():
            return False
    
    return True

def addCity():
    city = input("\nEnter name of city you wanna add : ")
    addToCities = isValidCityNameList(city.lower())

    formattedCityName = city[0].upper() + city[1:].lower() # first letter Capital, rest small letters

    if addToCities:
        cities.append(formattedCityName)
    elif addToCities == 0:
        print(f"{formattedCityName} already exist on the list")
    else:
        print("You've entered an invalid city name")


#* If the user input 2, they are asked the name of the driver and then the name of the cities they will visit (how you will ask for the route it up to you)

# name of the city valid if: max chars 26, min 7, doesn't include any numbers, doesn't exist as a key in the driver_route_dict dictionary

def formatDriverFullName(name):
    [firstName, lastName] = name.split()
    firstName = firstName[0].upper() + firstName[1:].lower()
    lastName = lastName[0].upper() + lastName[1:].lower()
    return  firstName + " " + lastName

def spaceCount(name):
# also should include only 2 words first and last name otherwise error will be generated
    space_cnt = 0
    for word in name:
        if ' ' in word:
            space_cnt+= 1

    return space_cnt


def isValidDriverName(fullName):
    if len(fullName) < 6 or len(fullName) > 25:
        return False

    for char in fullName:
        if char.isdigit():
            return False
        
    if spaceCount(fullName) != 1:
        return False
        
    for key in driver_route_dict: # key == fullName example : ("Ali Ali")
        if fullName == key.lower():
            return "exist" 
    
    return True

# ! be careful 0 is a falsey value so condition == 0 same as if condition (val of condition = False)

def addDriver():
    driverFullName= input("Enter Driver Full Name : ")
    isDriverFullNameValid = isValidDriverName(driverFullName.lower())
    formattedDriverFullName = formatDriverFullName(driverFullName)

    if isDriverFullNameValid == True:

        print(formattedDriverFullName)
        driverRoutes = []
        # Ask for the name of the cities they will visit (how you will ask for the route if up to you)
        nbOfCitiesWillVisit = input("How many cities will the driver visit ? ")

        if nbOfCitiesWillVisit.isdigit():
            for i in range(0, int(nbOfCitiesWillVisit)):
               # city name validation will be add later 😭
               city= input(f"City {i + 1} name : ")
               city= city[0].upper() + city[1:].lower()
               driverRoutes.append(city)
        else:
            print("Invalid Input")

        driver_route_dict[formattedDriverFullName] = driverRoutes
        print(driver_route_dict)

    else:
        if isDriverFullNameValid == "exist":
            print(f"{formattedDriverFullName} already exist on the list")
        else:
            print(isDriverFullNameValid)
            print("\nInvalid Driver Name")


def addCityToDriverRoute():
    print("\nAdding City To Driver Route")

def removeCityFromDriverRoute():
    print("\nRemoving City From Driver Route")


def checkDeliverability():
    print("\nChecking For Deliverability")

def Menu():
    close_system = False
    while not close_system:
        print("\n     1 - To add a city")
        print("     2 - To add a driver")
        print("     3 - To add a city to the route of a driver")
        print("     4 - To remove a city from a driver's route")
        print("     5 - To check the deliverability of a package")

        options = input("\nChoose one of these options : ")

        if options.isdigit() == True and 1 <= int(options) <= 5:
            options = int(options)
            if options == 1 :
                addCity()
            elif options == 2 :
                addDriver()
            elif options == 3 :
                addCityToDriverRoute()
            elif options == 4 :
                removeCityFromDriverRoute()
            elif options == 5 :
                checkDeliverability()
                close_system = True
        else:
            print("\nInvalid Input You've Should Choose a Number Only Between (1,5) - Try again")


Menu()



#* 1.	To add a city
#* 2.	To add a driver
#* 3.	To add a city to the route of a driver
#* 4.	Remove a city from a driver’s route
#* 5.	To check the deliverability of a package


# drivers = each drive has a route
# driver : 1 --> Tripli Akkar
# driver : 2 --> Beirut
# driver : 3 --> Saida

# user has option to add and delete
# list of cities each drivers do a tour

# Menu : 
# 1. Add a city -- double check using entering a new city
# 2. Add a driver: name, route
# 3. Add a city to the driver give user 3 options :
#       0. to add the city at the beginning of the tour
#       -1. to add the city at the end - be careful that is valid
#  4. To check availability --> print names of drivers that route in that city
# Remove a city from a driver's route

# check validation adding city, adding city to the driver that does not exist
