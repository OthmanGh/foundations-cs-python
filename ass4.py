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


def wordCnt(fullName):
# also should include only 2 words first and last name otherwise error will be generated
    word_cnt = 1
    for word in fullName:
        if ' ' in word:
            word_cnt+= 1

    return word_cnt

def isCityNameValid(city):

    if len(city) < 3 or len(city) > 20:
        return False
    
    for char in city: # Time Complexity O(N)
        if char.isdigit():
            return False
        
    if wordCnt(city) != 1:
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
        
    if wordCnt(driver) != 2: # drive must have first && last name
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


def removeDriver(dict, driver):
    print(f"removing {driver} from dict....")
    del dict[driver]


def removeCity(dict, formattedDriverName, cityToDelet):
    print("Deleting.....")
    routeList = dict[formattedDriverName]
    routeList.remove(cityToDelet)

    if len(routeList) == 0:  # remove  driver from dict
        removeDriver(dict, formattedDriverName)


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
    
    driver= input("Enter Driver Full Name : ")

    driverValidation = isDriverNameValid(driver) # Check if driver name is valid

    if driverValidation == True:

        formattedDriverName = formatDriverName(driver)

        if not isDriverOnDict(dict, formattedDriverName):  # Check if Driver already exist on our list: 

            driverRoutes = []             
            nbOfCitiesWillRoute = input("How many cities will driver route ? ")

            if nbOfCitiesWillRoute.isdigit() and int(nbOfCitiesWillRoute) >= 1:
                
                    for i in range(0, int(nbOfCitiesWillRoute)):
                        
                        city= input(f"City {i + 1} name : ")

                        if isCityNameValid(city):
                            driverRoutes.append(formatCityName(city))
                        else:
                            print("invalid city name") # only valid city names will be  added to the list
            else:
                    print("only natural number must be entered {0} - execlusive")

            if int(nbOfCitiesWillRoute) >= 1: # if not an empty list will be added within the driver name
                dict[formattedDriverName] = driverRoutes

            print(dict)
        else:
            print(f"{formattedDriverName} already exist on the list")
    else:
        print("invalid driver name !!!")


def addCityToDriverRoute(dict):
    driver = input("Enter Driver Full Name ? ")

    # check if user entered driver name is valid
    driverValidation = isDriverNameValid(driver)

    if driverValidation:
        formattedDriverName = formatDriverName(driver)

        # check if driver name exists on dict:
        if isDriverOnDict(dict, formattedDriverName):

            print(f"{formattedDriverName} is on the list")       
                 
            cityToAdd =  input("Enter name of the city you wanna add to the driver route ? ")            

            # check if user entered city name is valid:
            if isCityNameValid(cityToAdd):

                city = formatCityName(cityToAdd)

                # check if city already exist on driver route:
                if isCityNameOnDict(dict, formattedDriverName, city):
                    print(f"{city} already exists on {formattedDriverName} route")

                else:
                    
                    driverRoutesList = dict[formattedDriverName] # copy by reference driver route list
                    print(f"{formattedDriverName} take this route {driverRoutesList}")

                    # give user option to decide at which index city will be add on the list
                    renderInsertOptionsInterFace()
                    chosenOption = input("\nchoose one of the aboved options ? ")

                    if  chosenOption.isdigit() or chosenOption.startswith("-") and chosenOption[1:].isdigit():
                        index = int(chosenOption)

                        if  index == 0:
                            print("Adding to the beginning....")
                            driverRoutesList.insert(0, city) # ! note lists are refrenced data structure types so inserting an elment to the list will affect the actual list of the driver inside the dictionary
                        elif index == -1:
                            print("Adding to the end....")
                            driverRoutesList.append(city)
                        else:
                            print("invalid input")

                    elif chosenOption == "#":
                        index = input("Enter position where you wanna add city ? ")

                        if index.isdigit():
                            num = int(index)
                            if  1 <= num <= len(driverRoutesList) + 1: # developers only start counting from zero 😆
                                driverRoutesList.insert(num - 1, city)
                            else:
                                print(f"{num} out of range !!!")
                        else:
                            print("a valid number must be entered !")
                    else:
                        print("invalid input")

                    print(dict[formattedDriverName]) # output driver route list
            else:
                print("invalid city name !!")
        else:
            print(f"{formattedDriverName} is not on the list")
    else:
        print("invalid driver name")

def removeCityFromDriverRoute(dict):
    driver = input("Enter Driver Full Name ? ")
    
    # check if user entered driver name is valid
    driverValidation = isDriverNameValid(driver)

    if driverValidation:
        formattedDriverName = formatDriverName(driver)

        # check if driver name exists on dict:
        if isDriverOnDict(dict, formattedDriverName):

            print(f"{formattedDriverName} is on the list")       
                 
            cityToDelete =  input("Enter name of the city you wanna delete from the driver route ? ")            

            # check if user entered city name is valid:
            if isCityNameValid(cityToDelete):

                city = formatCityName(cityToDelete)

                # check if city do not exist on driver route:
                if not isCityNameOnDict(dict, formattedDriverName, city):
                    print(f"{city} is not on driver route")

                else: 
                    removeCity(dict, formattedDriverName, city)
                    print(dict)
            else:
                print("invalid city name !!")
        else:
            print(f"{formattedDriverName} is not on the list")
    else:
        print("invalid driver name")


def checkDeliverability():
    print("\nChecking For Deliverability")

def Menu():
    cities = ["Sour", "Saida", "Beirut", "Zahle", "Baalbek"]

    driver_route_dict = {
    "Ahmad Solyman": ["Sour", "Saida", "Zahle"],
    "Ali Hussein": ["Zahle"],
    "Hilal Jomaa": ["Beirut"],
    "Ali Ali": ["Beirut", "Akkar", "Saida"]
}

    close_system = False
    while not close_system:

        renderUserInterFace()

        options = input("\nChoose one of these options : ")

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
                checkDeliverability()
                close_system = True
        else:
            print("\nInvalid Input You've Should Choose a Number Only Between (1,5) - Try again")

Menu()

# The insert() method in Python generally inserts the element at any position in the list and also performs the necessary shifts required internally and hence can also be used to perform this very task. source : https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
