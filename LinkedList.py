import numpy as np


class SinglyLinkedList():
    '''Functions involving singly-linked list nodes.'''

    def __init__(self):
        self.head = None #The head (first value) of the singly-linked list.
        self.tail = None #The tail (last value) of the singly-linked list.
        self.count = 0 #The number of items in the singly-linked list.

    def add(self, value):
        '''Adds a value to the singly-linked list, and sets it as the tail.'''

        # create new list node
        nodeToAdd = SinglyLinkedListNode(value)

        # If the linked list is empty, the head and the tail are the newly entered value.
        if self.head == None:
            self.head = nodeToAdd
            self.tail = self.head

        else:
            self.tail.next = nodeToAdd
            self.tail = nodeToAdd

        self.count += 1

    def removeFirst(self):
        '''Removes the first (head) node from the singly-linked list.'''

        # if there are no values in the linked list, return.
        if self.head == None:
            return

        headValue = self.head.value;

        self.head = self.head.next

        return headValue

    def removeFirstEquals(self, valueToRemove):
        '''Removes the first value equal to the input in the singly-linked list.'''

        # if there are no values in the linked list, return.
        if self.head == None:
            return

        currentNode = self.head

        # If the head is the current value
        if(currentNode.value == valueToRemove):
            self.head = currentNode.next
            return

        # iterate list until value is found
        while(currentNode.value != valueToRemove):
            previousNode = currentNode
            currentNode = currentNode.next
            
            # if current node is the tail node, return None.
            if(currentNode == None):
                return

        # if the new node is the tail, set a new tail.
        if(currentNode.next == None):
            previousNode.next = None
            self.tail = previousNode
        else:
            previousNode.next = currentNode.next

        self.count -= 1

    def removeLast(self):
        '''Removes the last (tail) node in the singly-linked list.'''

        # If the linked list is empty, return.
        if self.head == None:
            return

        currentNode = self.head

        # cannot use tail, requires second-to-last node to set to None
        for i in range(0, self.count - 2):
            currentNode = currentNode.next

        nodeToRemove = currentNode.next

        currentNode.next = None

        self.tail = currentNode
        self.count -= 1

        return nodeToRemove.value

    def iterate(self):
        '''Iterates the values in the singly-linked list.'''
        
        if self.head == None:
            return
        
        else:
            linkedListArray = []

            currentValue = self.head

            while currentValue != None:
                linkedListArray.append(str(currentValue.value)) 
                currentValue = currentValue.next

            print(' -> '.join(linkedListArray))

class SinglyLinkedListNode():
    '''A node in a singly-linked list.'''

    def __init__(self):
        self.value = None # The current value of the node.
        self.next = None #The node that comes after the current node.

    def __init__(self, value):
        self.value = value
        self.next = None