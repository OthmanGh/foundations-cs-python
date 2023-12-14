# Data Structures : 

# * Stack : 
# implement stack using dynamic array(list)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            print("Stack is empty....")
            return None
    
    def top(self):
        if not self.empty():
            print(self.items[-1])
        else:
            print("Stack is empty....")
        return None
        
    def empty(self):
        return len(self.items) == 0
    
#* Queue :
# insertion at rear, deletion at head
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value, None)
        if self.head == None:
            self.head =self.rear = new_node
        
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.head == None:
            print("Queue is empty....")
            return None
        else:
            d = self.head.data
            if self.head == self.rear:
                self.head = self.rear = None
            else:
                self.head = self.head.next
            return d

    def front(self):
        if self.head == None:
            print("Queue is empty....")
        else:
            print(self.head.data)
        
    def empty(self):
        return not self.head == None

#* 1 : 
# Stacks and Queues
# 1.	Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.
# A palindrom is a sequence of characters that reads the same thing in both directions:
# Example of palindromes: “mom” “Neveroddoreven” 

# 1 : 
#! Note : In our impelementation non-alpha-numeric characters will be ignored as if they don't exist !!!

# Helper Functions : 
def formatString(string):
    if len(string) == 0:
        return False
    
    s = ""
    for char in string:
        if char.isalnum():
            s += char.lower()
    return s

def result(string, r):
    if r :
        print(f"{string} : is palindrome")
    else:
        print(f"{string} : not a palindrome")

# Test Data : 
str1 = "Neveroddoreven"
str2 = "UFO tofu *****"
str3 = "Borrow or rob?"
str4 = "1122334332211"

#* 1st approach : Two Pointers
def isPalindromeTwoPtrs(string):
    s = formatString(string)

    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1

    return True

r1 = isPalindromeTwoPtrs(str1)
r2 = isPalindromeTwoPtrs(str2)
r3 = isPalindromeTwoPtrs(str3)
r4 = isPalindromeTwoPtrs(str4)

result(str1, r1)
result(str2, r2)
result(str3, r3)
result(str4, r4)
print("------------------------------------------")

#* 2nd approach : Using a Stack DS
def isPalindromeStack(string):
    s = formatString(string)
    data = Stack()

    for char in s:
        data.push(char)

    for i in range(len(s)):
        if data.pop() != s[i]:
            return False
    return True

r1 = isPalindromeStack(str1)
r2 = isPalindromeStack(str2)
r3 = isPalindromeStack(str3)
r4 = isPalindromeStack(str4)

result(str1, r1)
result(str2, r2)
result(str3, r3)
result(str4, r4)
print("------------------------------------------")


#* 3nd approach : a Queue DS
def isPalindromeQueue(string):
    s = formatString(string)

    queue = Queue()

    for char in s:
        queue.enqueue(char)

    for i in range(len(s)):
        if queue.dequeue() != s[i]:
            return False
        
    return True


r1 = isPalindromeQueue(str1)
r2 = isPalindromeQueue(str2)
r3 = isPalindromeQueue(str3)
r4 = isPalindromeQueue(str4)

result(str1, r1)
result(str2, r2)
result(str3, r3)
result(str4, r4)
print("------------------------------------------")

# 2 : 
# 2.	Use a stack or a queue (or both!) to determine if a given expression is balanced.
# The expression will contain a combination of these types of parenthesis: (), {},  or []
# You have to make sure that for every opening parenthesis, there is a valid closing one.
# Ex:
# Input: (1+2)-3*[41+6] output: True
# Input: (1+2)-3*[41+6} output: False
# Input: (1+2)-3*[41+6 output: False
# Input: (1+2)-3*]41+6[ output: False
# Input: (1+[2-3]*4{41+6})  output: True
def balanced_exp_stack(exp):
    opening_symbols = ['(', '[', '{']
    closing_symbols = [')', ']', '}']

    stack = Stack()

    for char in exp:
        if char in opening_symbols:
            stack.push(char)
        elif char in closing_symbols:
            if stack.empty():
                return False
            top = stack.pop() 
            if opening_symbols.index(top) != closing_symbols.index(char):
                return False
    
    return stack.empty()


print(balanced_exp_stack("(1+2)-3*[41+6]"))
print(balanced_exp_stack("(1+2)-3*[41+6}"))
print(balanced_exp_stack("(1+2)-3*[41+6"))
print(balanced_exp_stack("(1+2)-3*]41+6["))
print(balanced_exp_stack("(1+[2-3]*4{41+6})"))

print("------------------------------------------")
#* 2 : 
# Stack
# You work for the MIB (men in black) and would like to decode the messages that they send you.
# The message contains alphabetical characters, white spaces, and Asterix.
# To decode the message, you need a stack.
# You start looping through the message pushing each alphabetical character and white space to your stack. Once you reach an Asterix, you pop one character out of your stack. 
# Sometimes, you receive an incomplete message. Therefore, if you reach the end of the string and you still have characters in your stack, pop all of them out.

# An example of such decoding is:
# Input: SIVLE ****** DAED TNSI ***
# Output: ELVIS ISNT DEAD

def decode_str(encoded_message):
    stack = Stack()
    decoded_message = ""

    for char in encoded_message:
        if char.isalpha() or char.isspace():
            stack.push(char)
        elif char == '*':
            decoded_message += stack.pop()

    while not stack.empty():
        decoded_message += stack.pop()

    return decoded_message

print(decode_str("SIVLE ****** DAED TNSI ***"))

print("------------------------------------------")


#* 3 : 
# Linked Lists- removing a node at a given location
# Write deleteAtLocation function for a LL that takes as input an integer and deletes the node at that given location.
# Example:
# Given this LL: 12 -> 56 -> 76-> 11-> 0
# An input =0 would delete the head of the LL: 12
# An input =3 would delete the node containing 11

class Node :
    def __init__(self, value, next): # constructor
        self.data = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # *  Implementation of adding nodes at the beginning, ending && pos : 

    def push_front(self, value):
        n = Node(value, None)

        # If List is empty : 
        if self.head == None:
            self.head = self.tail = n
            self.length = 1

        else:
            n.next = self.head
            self.head = n
            self.length +=1 


    def push_back(self, value):
        n = Node(value, None)

        # If List is empty : 
        if self.head == None:
            self.head = self.tail = n
            self.length = 1

        else:
            self.tail.next = n 
            self.tail = n
            self.length += 1


    def insert(self, pos, value):
        if pos < 0 or pos > self.length: # If pos val out of range
            print("invalid index value")
            return

        if pos == 0: # add at the beginning 
            self.push_front(value)
        
        elif pos == self.length: # add at the end
            self.push_back(value)

        else: # otherwise : 
            temp = self.head # Get a copy of the head pointer
            n = Node(value, None) # Create a new node with the given value and a None next pointer
            counter = 0

            while(counter < pos - 1): # Traverse the list until reaching the node before targeted position
                temp = temp.next
                counter += 1            
            
            # Insert the new node in between the current node and the next node
            n.next = temp.next 
            temp.next = n
            
            self.length +=1   # update list length val


    # *  Implementation of deleting nodes at the beginning, ending && pos : 
    
    def pop_front(self): # This func takes Constant time O(1)
        if self.head == None:
            print("List is empty....")

        else:
            self.head = self.head.next
            self.length -= 1

    def pop_back(self): # This func takes Linear time O(n)
        if self.head == None:
            print("List is empty....")

        else:
            temp =self.head

            while temp.next.next != None: # Travers the list until reaching the node before targeted position
                temp = temp.next

            temp.next = None
            self.tail = temp
            self.length -= 1


    def pop(self, pos):
        if pos < 0 or pos >= self.length: # If pos val out of range
            print("invalid index value")
            return
        
        if pos == 0:
            self.pop_front()
        elif pos == self.length - 1:
            self.pop_back()
        
        else:
            temp = self.head
            counter = 0

            while(counter < pos - 1): # Traverse the list until reaching the node before specified node
                temp = temp.next
                counter +=1

            temp.next = temp.next.next
            self.length -= 1


    # * Printing Linked List Func : 

    def printLL(self):
        # Check if list is empty : 
        if self.head == None:
            print("List is empty....")
        
        else:
            temp = self.head
            while(temp != None):
                print(f"{temp.data}", end=" -> ")
                temp = temp.next
            print("None")

myList = LinkedList()
myList.push_front(12)
myList.push_back(11)
myList.insert(1, 56)
myList.insert(2, 76)
myList.printLL()

myList.pop(2) 
myList.printLL()

print("------------------------------------------")

#* 4 : 
# Graphs
# 1.	Given a graph where the nodes are cities and the edges are the routes connecting them. Write a function that takes as input two cities and returns true if there is a route connecting them, false otherwise.
# Write another function that takes as input one city and prints all the other cities directly reachable from it.
# 2.	Given a graph, write a function that checks if the graph contains a cycle (the graph is directed).
# 3.	Given a graph that represents the Instagram social media app. The nodes there represent users, and we connect user 1 to user 2 if user 1 follows user 2 (the graph is undirected).
# Write a function that takes as input a two users and prints the list of users they both follow.
# Write another function that prints the list of users none of them follow


# 1.	Given a graph where the nodes are cities and the edges are the routes connecting them. Write a function that takes as input two cities and returns true if there is a route connecting them, false otherwise.

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
            return True
        return False

    def add_edge(self, v1, v2, distance):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append({'city' : v2, 'distance' : distance})
            self.adj_list[v2].append({'city': v1, 'distance' : distance})
            return True
        return False
    

    def print_adj_list(self):
        for v in self.adj_list.keys():
            print(v, f": {self.adj_list[v]}")


    # 1.
    def is_there_route(self, c1, c2):
        if c1 in self.adj_list.keys() and c2 in self.adj_list.keys():
           for info in self.adj_list[c1]:
               if info['city'] == c2:
                return True
               
        return False

    
graph = Graph()


c1 = "Zahle"
c2 = "Beirut"
c3 = "Saida"
c4 = "Tripoli"
c5 = "Akkar"
graph.add_vertex(c1)
graph.add_vertex(c2)
graph.add_vertex(c3)
graph.add_vertex(c4)
graph.add_vertex(c5)

graph.add_edge(c1, c2, 47)
graph.add_edge(c1, c3, 86)
graph.add_edge(c3, c4, 75)
graph.add_edge(c4, c1, 92)
graph.add_edge(c2, c4, 68)
graph.add_edge(c2, c5, 109)
print(graph.is_there_route(c2, c1))
print(graph.is_there_route(c1, c5))








