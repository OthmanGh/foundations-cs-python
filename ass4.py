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


def isCityNameValid(city):

    if len(city) < 3 or len(city) > 20:
        return False
    
    for char in city: # Time Complexity O(N)
        if char.isdigit():
            return False
        
    if len(city.split()) != 1:
        return False
    
    if not city.isalnum(): # city must not include any symbol
        return False
    
    return True


def isCityNameValidForList(cities, city):
    
    if not isCityNameValid(city):
        return False
    
    for cityLi in cities: # Time Complexity O(N)
        if cityLi.lower() == city :
            return "exists"
        
    return True


def isDriverNameValid(driver):

    if len(driver) < 6 or len(driver) > 25:
        return False

    for char in driver: # numbers aren't allowed in driver name
        if char.isdigit():
            return False
        
    if len(driver.split()) != 2: # drive must have first && last name
        return False

    # driver first or last name may include special characters so we have to check that too
    [firstName, lastName] = driver.split()
    if not firstName.isalnum() or not lastName.isalnum(): #! spaces doesn't considered as alnum characters, this will prevent having speical character in driver name
        return False
    
    return True


def isDriverOnDict(dict, driver):
    isOnDict = False    

    for name in dict:
        if name == driver:
            isOnDict = True

    return isOnDict


def isCityNameOnDict(dict, driver, userCity):
    isOnList = False

    for city in dict[driver]:
        if userCity == city:
            isOnList = True
    return isOnList


def removeCity(dict, driver, cityToDelet):
    print("Deleting.....")
    routeList = dict[driver]
    routeList.remove(cityToDelet)

    if len(routeList) == 0:  # remove driver from dict
        print(f"removing {driver} from dict....")
        del dict[driver]


def driverValidation(): # almost every function do same work at first so this function will do it for us and prevent repitive code

    driver= input("Enter Driver Full Name : ").strip()

    # check if user entered driver name is valid
    isValid = isDriverNameValid(driver)

    if isValid:
        formattedDriverName = formatDriverName(driver)
        return formattedDriverName

    else:
        print("invalid driver name !!!")
        return -1


def validationAddRemoveData(dict, num = 0): # this function will check for inputs validation for both addCityToDriverRoute/removeCityFromDriverRoute functions, purpose is to decrease the amount of repetitive code

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
                return (-1, -1)
        else:
            print(f"{driver} is not on the list")
            return (-1,-1)
        

def getDriversDeliverability(dict, city):
    drivers = [] # list will store all the drivers that deliver to city
    for driver in dict: 
        if isCityNameOnDict(dict, driver, city):
            drivers.append(driver)

    if len(drivers) == 0:
        return None
    
    return drivers


def addCity(cities):
    city = input("\nEnter name of city you wanna add : ").strip() # used strip to get rid of any spaces at the beginning/end of inputed string

    addToCities = isCityNameValidForList(cities, city.lower()) # check if city name is valid
    
    formattedCityName = formatCityName(city) # format city name to match other cities on the list

    if addToCities == True:
        cities.append(formattedCityName)
    elif addToCities == "exists":
        print(f"\n{formattedCityName} already exists on the list")
    else:
        print("invalid city name")

    print("Cities List : ", cities)


def addDriver(dict):
    driver = driverValidation()
    
    if driver != -1:
        if not isDriverOnDict(dict, driver):  # Check if Driver already exist on our list: 

            driverRoutes = []             
            nbOfCitiesWillRoute = input("How many cities will driver route ? ").strip()

            if nbOfCitiesWillRoute.isdigit() and int(nbOfCitiesWillRoute) >= 1:
                
                    for i in range(0, int(nbOfCitiesWillRoute)):
                        
                        city= input(f"City {i + 1} name : ").strip()

                        if isCityNameValid(city):
                            driverRoutes.append(formatCityName(city))
                        else:
                            print("invalid city name") # only valid city names will be  added to the list
            else:
                    print("only natural number must be entered {0} - execlusive")

            if int(nbOfCitiesWillRoute) >= 1: # if not an empty list will be added within the driver name
                dict[driver] = driverRoutes
            print(dict)
        else:
            print(f"{driver} already exist on the list")


def addCityToDriverRoute(dict):
    (driver, city) = validationAddRemoveData(dict, 1)

    if driver != -1 and city != -1:

        # check if city already exist on driver route:
        if isCityNameOnDict(dict, driver, city):
            print(f"{city} already exists on {driver} route")

        else:
            driverRoutesList = dict[driver] # copy by reference driver route list
            print(f"{driver} takes this route {driverRoutesList}")

            # give user options to decide at which index city will be add to the list
            renderInsertOptionsInterFace()
            chosenOption = input("\nchoose one of the aboved options ? ").strip()

            if chosenOption.isdigit() or chosenOption.startswith("-") and chosenOption[1:].isdigit():
               index = int(chosenOption)

               if  index == 0:
                    print("Adding to the beginning....")
                    driverRoutesList.insert(0, city)
                    print(dict[driver])

               elif index == -1:
                    print("Adding to the end....")
                    driverRoutesList.append(city)
                    print(dict[driver])

               else:
                    print("invalid input")

            elif chosenOption == "#":
               index = input("Enter position where you wanna add city ? ").strip()

               if index.isdigit():
                    num = int(index)

                    if  1 <= num <= len(driverRoutesList) + 1:
                        driverRoutesList.insert(num - 1, city)
                        print(dict[driver])

                    else:
                        print(f"{num} out of range !!!")
               else:
                    print("a valid number must be entered !")
            else:
                print("invalid input")


def removeCityFromDriverRoute(dict):
    driver, cityToDelete = validationAddRemoveData(dict)

    if driver != -1 and cityToDelete != -1:
        # check if city do not exist on driver route:
        if not isCityNameOnDict(dict, driver, cityToDelete):
            print(f"{cityToDelete} is not on driver route")

        else: 
            removeCity(dict, driver, cityToDelete)
            print(dict)


def deliverability(dict):    
    city = input("name of city you would like to deliver package to? ").strip()

    if isCityNameValid(city): # check if city name is valid
        city = formatCityName(city)
        drivers = getDriversDeliverability(dict, city) 

    else:
        drivers = -1 # other wise error will generated since drivers won't be initialized
        print("Invalid city name !!!")

    if drivers == None : 
        print(f"Unfortunatly for now no driver is delivering packages to {city}")

    else:
        if drivers != -1 :
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
                addDriver(driver_route_dict)
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