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


# The insert() method in Python generally inserts the element at any position in the list and also performs the necessary shifts required internally and hence can also be used to perform this very task. source : https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/

# Python | Ways to remove a key from dictionary : https://www.geeksforgeeks.org/python-ways-to-remove-a-key-from-dictionary/

def renderUserInterFace():
        print("\n     1 - To add a city")
        print("     2 - To add a driver")
        print("     3 - To add a city to the route of a driver")
        print("     4 - To remove a city from a driver's route")
        print("     5 - To check the deliverability of a package")


def renderInsertOptionsInterFace():
    print("\n     1. Add to the beginning of the route enter 0")
    print("     2. Add to the end of the route enter -1")
    print("     3. Add that city to the given index enter #")


def formatCityName(city):
    return city[0].upper() + city[1:].lower() 


def formatDriverName(fullName):
    [firstName, lastName] = fullName.split()
    firstName = firstName[0].upper() + firstName[1:].lower()
    lastName = lastName[0].upper() + lastName[1:].lower()
    return  firstName + " " + lastName


# Function --> isCityNameValid : check if city name valid based on condition below
def isCityNameValid(city):
    if len(city) < 3 or len(city) > 20:
        return False
    
    for char in city:  # shouldn't include any numbers
        if char.isdigit():
            return False
        
    if len(city.split()) != 1: # city must be only one words
        return False
    
    if not city.isalnum(): # city must not include any symbol
        return False
    
    return True

# Function --> isCityOnList : check if city exist on cities list return true if yes otherwise false
def isCityOnList(cities, city):
    city = formatCityName(city)
    return city in cities


# Function --> isDriverNameValid : will check if driver name valid based on the terms below
def isDriverNameValid(driver):
    if len(driver) < 6 or len(driver) > 25:
        return False

    for char in driver: # Numbers aren't allowed in driver name
        if char.isdigit():
            return False
        
    if len(driver.split()) != 2: # Driver must have first && last name
        return False

    # Driver first or last name may contain special characters so we have to check that too
    [firstName, lastName] = driver.split()
    if not firstName.isalnum() or not lastName.isalnum(): #! Spaces doesn't considered as alnum characters, this will prevent having speical character in driver name alpha-numeric[0-9, a-z]
        return False
    
    return True

# Function --> isDriverOnDict : return true if driver on dictonary otherwise false
def isDriverOnDict(dict, driver):
    return driver in dict

# Function --> isCityNameOnDict : return true if driver on dictonary otherwise false
def isCityNameOnDict(dict, driver, userCity):
    return userCity in dict[driver]


# Function --> removeCity : this function will remove a city from driver route and if driver has no city left to route his data will be removed too
# param --> cityToDelete : city that will be delete
def removeCity(dict, driver, cityToDelet):
    print("Deleting.....")
    routeList = dict[driver]
    routeList.remove(cityToDelet)

    if len(routeList) == 0:  # remove driver from dict
        print(f"removing {driver} from dict....")
        del dict[driver]


# Function --> driverValidation :  almost every function do same work at first (2,3,4) so this function will do it for us and prevent repitive code
def driverValidation():
    driver= input("Enter Driver Full Name : ").strip()

    # check if user entered driver name is valid
    isValid = isDriverNameValid(driver) # will return true or false

    return formatDriverName(driver) if isValid else -1 # ternary operator


# function --> validationAddRemoveData : check inputs validation for both addCityToDriverRoute/removeCityFromDriverRoute functions
# param 2 --> num : num parameter will decide which output statment will be printed for 2 different functions, if no parameter passed 0 will be set as a default parameter
def validationAddRemoveData(dict, num = 0):
    driver = driverValidation()    

    if driver != -1:
        # check if driver name exists on dict:
        if isDriverOnDict(dict, driver):

            print(f"{driver} is on the list")   

            if num == 1:
                city = input("Enter name of the city you wanna add to the driver route ? ").strip()
            else:
                city = input("Enter name of the city you wanna delete from the driver route ? ").strip()

            if isCityNameValid(city):
                cityFormat = formatCityName(city)

                return driver, cityFormat # will return a tuple
            else:
                print("invalid city name")
                
        else:
            print(f"{driver} is not on the list")
    else:
        print("invalid driver name !!!")

    return (-1, -1)


# function --> getDriversDeliverability : checks for the deliverability of a certain city and returns a list of drivers that pass through that city. if no driver reach specified city None will be returned
def getDriversDeliverability(dict, city):
    drivers = [] # list will store all the drivers that deliver to city
    for driver in dict: 
        if isCityNameOnDict(dict, driver, city):
            drivers.append(driver)

    if len(drivers) == 0:
        return None
    
    return drivers


# function --> addCity will add city to cities main lists
# parameter --> cities : list of cities
def addCity(cities):

    # Input a city name from a user
    city = input("\nEnter name of city you wanna add : ").strip() # used strip to get rid of any spaces at the beginning/end of inputed string

    # Check if city exists on the list
    if isCityOnList(cities, city) :
        print(f"{formatCityName(city)} already exists on main list")
        
    else:
        # Check if city is valid
        addToCities = isCityNameValid(city)

        if addToCities:

            # Before adding city reformat it to match rest of cities
            formattedCityName = formatCityName(city)
            
            # Add city to cities main list
            cities.append(formattedCityName)
            print(cities)
        else:
            print("invalid city name")


# # Function to add a driver attached to a list of cities will route to dictionary
def addDriver(dict, cities):

    # Validate and get the driver name
    driver = driverValidation()
    
    # Check if driver is valid
    if driver != -1:

        # Check if driver don't exists on dictionary
        if not isDriverOnDict(dict, driver):

            driverRoutes = [] # Driver's route list
            nbOfCitiesWillRoute = input("How many cities will driver route ? ").strip() 
            addToDict = True

            # Check if number of cities not valid
            if not nbOfCitiesWillRoute.isdigit():
                    print("only natural number must be entered {0} - execlusive")
    
            else:
                # Check if number of cities greater or equal 1
                if int(nbOfCitiesWillRoute) >= 1:

                    # Loop starting from zero to number of cities execlusive
                    for i in range(0, int(nbOfCitiesWillRoute)):
                        
                        # Get city name from user
                        city= input(f"City {i + 1} name : ").strip()

                        # Check if city name is valid and in main cities list and not in driver's cities list 
                        if isCityNameValid(city) and isCityOnList(cities, city) and not isCityOnList(driverRoutes, city):
                            driverRoutes.append(formatCityName(city))

                        # Check if city name in driver's cities list
                        elif isCityOnList(driverRoutes, city):
                            print("invalid input - you can't add same city name twice")
                            addToDict = False
                            break
                        else:
                            print("make sure you've entered a valid city name and it's exists on our main list")
                            addToDict = False
                            break 
                
                # Check if user entered data must be added to dictionary, note in case user enters 0 as number of cities a driver attached to an empty list will be added to the dictionary to prevent that it has to be at least 1
                if int(nbOfCitiesWillRoute) >= 1 and addToDict: 
                    dict[driver] = driverRoutes
                    print(dict)
        else:
            print(f"{driver} already exist on the list")


# Function to add a city to the route of a driver in the given dictionary
def addCityToDriverRoute(dict):
    # Validate and get the driver and city inputs
    (driver, city) = validationAddRemoveData(dict, 1)

    # Check if both driver and city are valid
    if driver != -1 and city != -1:

        # Check if the city already exists on the driver's route
        if isCityNameOnDict(dict, driver, city):
            print(f"{city} already exists on {driver}'s route")

        else:
            # Get the driver's current route list
            driverRoutesList = dict[driver]

            # Display the current route of the driver
            print(f"{driver} takes this route {driverRoutesList}")

            # Display options for the user to choose where to add the city in the route
            renderInsertOptionsInterFace()
            chosenOption = input("\nChoose one of the above options? ").strip()

            # Check user input for the index to add the city
            if chosenOption.isdigit() or chosenOption.startswith("-") and chosenOption[1:].isdigit():
                index = int(chosenOption)

                # Add the city to the beginning of the route
                if index == 0:
                    print("Adding to the beginning....")
                    driverRoutesList.insert(0, city)
                    print(dict[driver])

                # Add the city to the end of the route
                elif index == -1:
                    print("Adding to the end....")
                    driverRoutesList.append(city)
                    print(dict[driver])

                else:
                    print("Invalid input")

            # Check if the user chose to enter a specific position for the city in the route
            elif chosenOption == "#":
                index = input("Enter the position where you want to add the city? ").strip()

                # Check if the entered position is a valid number
                if index.isdigit():
                    num = int(index)

                    # Add the city to the specified position in the route
                    if 1 <= num <= len(driverRoutesList) + 1:
                        driverRoutesList.insert(num - 1, city)
                        print(dict[driver])

                    else:
                        print(f"{num} out of range !!!")

                else:
                    print("A valid number must be entered!")

            else:
                print("Invalid input")


# Function to remove a city from a driver's route
def removeCityFromDriverRoute(dict):
    # Recieve a driver and city data
    driver, cityToDelete = validationAddRemoveData(dict)

    # Check if recieved data are valid
    if driver != -1 and cityToDelete != -1:

        # Check if city do not exist on driver's route:
        if not isCityNameOnDict(dict, driver, cityToDelete):
            print(f"{cityToDelete} is not in driver route")

        else:
            # Remove city from driver's route
            removeCity(dict, driver, cityToDelete)
            print(dict)


# Function to check for available deliverability for a certain city
def deliverability(dict):
    city = input("name of city you would like to deliver package to? ").strip()

    # Check if city is valid
    if isCityNameValid(city): 
        # Format city
        city = formatCityName(city)
        # Get list of drivers that route through city
        drivers = getDriversDeliverability(dict, city) 
    else:
        drivers = -1  # Otherwise an error will generated since drivers won't be accessible (not initialized)
        print("Invalid city name !!!")

    if drivers == None : 
        print(f"Unfortunatly no driver is delivering packages to {city}")
    elif drivers != -1 :
        print("Available Drivers : ", drivers)


def Menu():
    cities = ["Sour", "Saida", "Beirut", "Zahle", "Baalbek"]

    driver_route_dict = {
    "Ahmad Solyman": ["Sour", "Saida", "Zahle"],
    "Ali Hussein": ["Zahle", "Akkar"],
    "Hilal Jomaa": ["Beirut", "Zahle"],
    "Ali Ali": ["Beirut", "Akkar", "Zahle", "Saida"]
}
    
    close_system = False

    while not close_system:
        renderUserInterFace()

        options = input("\nChoose one of these options : ").strip()

        if options.isdigit() and 1 <= int(options) <= 5:
            options = int(options)
            if options == 1 :
                addCity(cities)
            elif options == 2 :
                addDriver(driver_route_dict, cities)
            elif options == 3 :
                addCityToDriverRoute(driver_route_dict)
            elif options == 4 :
                removeCityFromDriverRoute(driver_route_dict)
            elif options == 5 :
                deliverability(driver_route_dict)
                close_system = True
        else:
            print("\nInvalid Input You've Should Choose a Number Only Between (1,5) - Try again")


Menu()