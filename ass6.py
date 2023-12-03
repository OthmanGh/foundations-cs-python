
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


    def push_front(self, value):
        # if List is empty : 
        if self.head == None:
            self.head = self.tail = None
            self.length = 1
            
        else:
            n = Node(value, None)
            n.next = self.head
            self.head = n
            self.length +=1 


#* 4 : 
# Graphs
# 1.	Given a graph where the nodes are cities and the edges are the routes connecting them. Write a function that takes as input two cities and returns true if there is a route connecting them, false otherwise.
# Write another function that takes as input one city and prints all the other cities directly reachable from it.
# 2.	Given a graph, write a function that checks if the graph contains a cycle (the graph is directed).
# 3.	Given a graph that represents the Instagram social media app. The nodes there represent users, and we connect user 1 to user 2 if user 1 follows user 2 (the graph is undirected).
# Write a function that takes as input a two users and prints the list of users they both follow.
# Write another function that prints the list of users none of them follow
