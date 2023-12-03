
#* 1 : 
# Stacks and Queues
# 1.	Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.
# A palindrom is a sequence of characters that reads the same thing in both directions:
# Example of palindromes: “mom” “Neveroddoreven” 
# 2.	Use a stack or a queue (or both!) to determine if a given expression is balanced.
# The expression will contain a combination of these types of parenthesis: (), {},  or []
# You have to make sure that for every opening parenthesis, there is a valid closing one.
# Ex:
# Input: (1+2)-3*[41+6] output: True
# Input: (1+2)-3*[41+6} output: False
# Input: (1+2)-3*[41+6 output: False
# Input: (1+2)-3*]41+6[ output: False
# Input: (1+[2-3]*4{41+6})  output: True



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
            print("Length of list : ", self.length)

myList = LinkedList()
myList.push_front(12)
myList.push_back(11)
myList.insert(1, 56)
myList.insert(2, 76)
myList.printLL()

#myList.pop(0)
myList.pop(3) # node containing 11 deleted
myList.printLL()

# myList.push_front(30)
# myList.push_back(40)
# myList.push_front(20)
# myList.push_back(50)
# myList.push_front(10)

# myList.insert(3, 60)
# myList.insert(4, 70)

# myList.pop_front()
# myList.pop_back()
# myList.pop_back()
# myList.pop(2)
# myList.printLL()


#* 4 : 
# Graphs
# 1.	Given a graph where the nodes are cities and the edges are the routes connecting them. Write a function that takes as input two cities and returns true if there is a route connecting them, false otherwise.
# Write another function that takes as input one city and prints all the other cities directly reachable from it.
# 2.	Given a graph, write a function that checks if the graph contains a cycle (the graph is directed).
# 3.	Given a graph that represents the Instagram social media app. The nodes there represent users, and we connect user 1 to user 2 if user 1 follows user 2 (the graph is undirected).
# Write a function that takes as input a two users and prints the list of users they both follow.
# Write another function that prints the list of users none of them follow
