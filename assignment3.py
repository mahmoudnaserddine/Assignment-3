#question 1:



# class Node:
#     def __init__(self, info, next=None):
#         self.info = info
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0  # number of nodes in my LL
#
#     def addToTail(self, info):  # O(1)
#         n = Node(info)
#         if self.size == 0:  # LL is empty
#             self.head = n
#             self.tail = n
#             self.size += 1
#         else:
#             self.tail.next = n
#             self.tail = n
#             self.size += 1
#
#     def deleteHead(self):  # O(1)
#         if self.size == 0:
#             return None
#         if self.size == 1:
#             temp = self.head.info
#             self.head = None
#             self.tail = None
#             self.size = 0
#             return temp
#
#         temp = self.head.info
#         self.head = self.head.next
#         self.size -= 1
#         return temp
#
# class Queue:
#     def __init__(self):
#         self.elements = LinkedList()
#
#     def enqueue(self, item):
#         self.elements.addToTail(item)
#
#     def dequeue(self):
#         return self.elements.deleteHead()



# def isPalindrome(s):
#     # Create a queue to store characters
#     q = Queue()
#
#     # Clean the input string by removing non-alphanumeric characters and making it lowercase
#     cleaned_s = "".join(char.lower() for char in s if char.isalnum())
#
#     # Enqueue(add) each character from the cleaned string into the queue
#     for char in cleaned_s:
#         q.enqueue(char)
#
#     # Initialize an empty string to store the reversed version of the cleaned string
#     reversed_str = ""
#
#     # Continue as long as there is something in the queue (q.elements.head is not empty)
#     while q.elements.head:
#         # Dequeue (remove) a character from the front of the queue and add it to the reversed string
#         reversed_str += q.dequeue()
#
#     # Check if the original cleaned string (cleaned_s) is equal to its reverse (reversed_str)
#     return cleaned_s == reversed_str[::-1]  # Compare the cleaned string with its reverse
#
#
#
# user_input = input("Enter a string: ")
# # Check if the cleaned input string is a palindrome
# if isPalindrome(user_input):
#     print(f"'{user_input}' is a palindrome.")
# else:
#     print(f"'{user_input}' is not a palindrome.")




#----------------------------------------------------------------------------------------

#question 2:



# class Stack:
#     def __init__(self):
#         self.elements = []
#
#     def push(self, item):
#         self.elements.append(item)
#
#     def pop(self):
#         if len(self.elements) == 0:
#             return None
#         return self.elements.pop()
#
# #
# def is_valid_expression(expression):
#     # Create a mapp of  parentheses
#     parentheses_map = {')': '(', '}': '{', ']': '['}
#
#     # Create an instance of the custom Stack class
#     stack = Stack()
#
#     # Iterate through each character in the expression
#     for char in expression:
#         # If the character is an opening parenthesis or curly brace, push it onto the stack
#         if char in '({[':
#             stack.push(char)
#         # If the character is a closing parenthesis or curly brace, check for a matching opening character
#         elif char in ')}]':
#             # If the stack is empty, there's no matching opening character, so return False
#             if not stack.elements:
#                 return False
#             # Check if the last character in the stack matches the expected opening character
#             if stack.pop() == parentheses_map.get(char):
#                 continue  # Match found, continue checking the next character
#             else:
#                 return False
#
#     # After iterating through the entire expression, check if the stack is empty (all characters were balanced)
#     return not stack.elements
#
# # Get user input for the expression to be checked
# user_input = input("Enter an expression: ")
#
# # Check if the entered expression contains valid combinations of parentheses and curly braces using the is_valid_expression function
# if is_valid_expression(user_input):
#     print("True")
# else:
#     print("False")
#--------------------------------------------------------------------------------------------------

#question 3:



#
#
# class Node:
#     def __init__(self, info, next=None):
#         self.info = info
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0  # number of nodes in my LL
#
#     def addToTail(self, info):
#         n = Node(info)
#         if self.size == 0:
#             self.head = n
#             self.tail = n
#             self.size += 1
#         else:
#             self.tail.next = n
#             self.tail = n
#             self.size += 1
#
#     def deleteHead(self):
#         if self.size == 0:
#             return None
#         if self.size == 1:
#             temp = self.head.info
#             self.head = None
#             self.tail = None
#             self.size = 0
#             return temp
#
#         temp = self.head.info
#         self.head = self.head.next
#         self.size -= 1
#         return temp
#
# class Queue:
#     def __init__(self):
#         self.elements = LinkedList()
#
#     def enqueue(self, item):
#         self.elements.addToTail(item)
#
#     def dequeue(self):
#         return self.elements.deleteHead()
#
#     def size(self):
#         return self.elements.size
#
#     def isEmpty(self):
#         return self.elements.size == 0
#
#     def front(self):
#         if self.isEmpty():
#             return None
#         return self.elements.head.info
#
# # Car class to represent car information
# class Car:
#     def __init__(self, make, color, plate_number):
#         self.make = make
#         self.color = color
#         self.plate_number = plate_number
#
#
#
#
# # Create a queue to manage cars waiting for a car wash
# car_queue = Queue()
#
# # Create an infinite loop to display the car wash menu until the user quits
# while True:
#     # Display the car wash menu options
#     print("Car Wash Menu:")
#     print("1. Insert a car to the queue")
#     print("2. To remove the car from the queue")
#     print("3. Quit")
#
#     # Prompt the user for their choice
#     choice = input("Enter your choice: ")
#
#
#     if choice == '1':
#         # Prompt the user for car details and create a car object
#         make = input("Enter car make: ")
#         color = input("Enter car color: ")
#         plate_number = int(input("Enter car plate number: "))
#         car = Car(make, color, plate_number)
#
#         # Add the car to the queue and provide feedback
#         car_queue.enqueue(car)
#         print(f"{car.make} {car.color} ({car.plate_number}) has been added to the queue.")
#
#     elif choice == '2':
#         # Check if the queue is empty before attempting to dequeue
#         if car_queue.isEmpty():
#             print("The car wash queue is empty.")
#         else:
#             # Dequeue the next car and display a message
#             car = car_queue.dequeue()
#             print(f"Car washed: {car.make} {car.color} ({car.plate_number})")
#
#     elif choice == '3':
#         # Exit the loop if the user chooses to quit
#         break
#     else:
#         # Handle invalid choices
#         print("Invalid choice. Please select a valid option.")

#------------------------------------------------------------------------------------

#question 4:

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0



def decode_mib_message(message):
    # Create a stack to store characters
    stack = Stack()
    # Initialize a list to store the decoded characters
    decoded_message = []

    # Iterate through each character in the input message
    for char in message:
        # Check if the character is an alphabetical character or a space
        if char.isalpha() or char.isspace():
            # Push the character onto the stack
            stack.push(char)
        # Check if the character is an asterisk ('*')
        elif char == '*':
            # Pop a character from the stack if it's not empty
            popped_char = stack.pop()
            if popped_char is not None:
                # Append the popped character to the decoded message
                decoded_message.append(popped_char)

    # Pop any remaining characters from the stack
    while not stack.is_empty():
        # Pop a character from the stack
        popped_char = stack.pop()
        if popped_char is not None:
            # Append the popped character to the decoded message
            decoded_message.append(popped_char)

    # Join the characters to form the decoded message as a string
    return ''.join(decoded_message)

# Get user input for the message to decode
user_input = input("Enter the message: ")
# Call the decoding function and store the result in 'decoded_message' and print it
decoded_message = decode_mib_message(user_input)

print("Decoded Message:", decoded_message)




