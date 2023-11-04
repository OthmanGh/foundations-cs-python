
# ? Excersice 1 : 
#! fist Approach : 
#number = int(input("Enter a number : "))
def count_digits(num):
    num_ = num
    cnt = 0
    while num_ >= 1:
        num_ = num / 10
        cnt+= 1
    return f"{num} has {cnt} digits."

#print(count_digits(number))
print(count_digits(3725))
print(count_digits(454891516519816514988))


# number = int(input("Enter a number : "))

#!  Second Approach : 
def get_digits(number):
    if number == 0: # Base Case
        return 1
    return 1 + get_digits(number//10) # Recursive Case 

print(get_digits(288487))
print(get_digits(454891516519816514988))

# ?  Excersice 2 : 
stars_num = int(input("Enter a star number : "))

for i in range(1, stars_num + 1):
    star = '*'
    print((star*i))


# ?  Excersice 3 : 
# 3. Write a program that takes two integers from the user and outputs the range of values from this list list1=[54,76,2,4,98,100]. Make sure the values of the integers are valid. In case they are not, ask again.
# Ex: int1=20, int2=80. The program would print:
# 54
# 76

int1 = int(input("Enter first Integer : "))
int2 = int(input("Enter second Integer "))
list1=[54,76,2,4,98,100]

def swap(n1, n2): 
    n1, n2 = n2, n1
    return [n1, n2]

def numbers_in_range(num1, num2):
    if num1 > num2:
        [num1, num2] = swap(num1, num2)
    
    does_not_exist = True

    for number in list1:
        if num1 <= number <= num2:
            does_not_exist = False
            print(number)
    
    if does_not_exist:
        print(f"No number exists in the range of [{num1}, {num2}]")

numbers_in_range(int1, int2)


# In Python, you can use the * operator to capture multiple elements into a single variable, often called the "splat" or "extended unpacking" operator. This allows you to collect the remaining elements into a list or tuple. It's similar to the concept of a "rest parameter" in some other programming languages.


# ? Excersice 4 : 
#  find method() : 
# Syntax: string.find(substring, start, end)
# Returns the index of the first occurrence of 'substring' in 'string' between 'start' and 'end'.

stop_runing = False
names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while not stop_runing:
    char = input("Enter a character ? ")
    for name in names:
        index = name.find(char)
        if index != -1:
            print(name)

    should_continue = input("Do u want to try different character ? Type y for 'yes', n for 'no' : ")
    if should_continue.lower() == 'n':
        stop_runing = True
