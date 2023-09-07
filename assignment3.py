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



class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

#
def is_valid_expression(expression):
    # Create a mapp of  parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}

    # Create an instance of the custom Stack class
    stack = Stack()

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening parenthesis or curly brace, push it onto the stack
        if char in '({[':
            stack.push(char)
        # If the character is a closing parenthesis or curly brace, check for a matching opening character
        elif char in ')}]':
            # If the stack is empty, there's no matching opening character, so return False
            if not stack.elements:
                return False
            # Check if the last character in the stack matches the expected opening character
            if stack.pop() == parentheses_map.get(char):
                continue  # Match found, continue checking the next character
            else:
                return False

    # After iterating through the entire expression, check if the stack is empty (all characters were balanced)
    return not stack.elements

# Get user input for the expression to be checked
user_input = input("Enter an expression: ")

# Check if the entered expression contains valid combinations of parentheses and curly braces using the is_valid_expression function
if is_valid_expression(user_input):
    print("True")
else:
    print("False")
#--------------------------------------------------------------------------------------------------






