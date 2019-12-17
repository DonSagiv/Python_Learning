import numpy as np

class SinglyLinkedList():
    '''Functions involving singly-linked list nodes.'''

    def __init__(self):
        self.head = None #The head (first value) of the singly-linked list.
        self.tail = None #The tail (last value) of the singly-linked list.
        self.count = 0 #The number of items in the singly-linked list.

    def insert(self, index, value):
        ''' Inserts the value to the nth index of the linked list. If n is greater than number of items, sets as last value.'''

        newNode = SinglyLinkedListNode(value)

        # Sets the head if the linked list is empty.
        if self.head == None:
            self.head = newNode
            self.tail = self.head

        # If index is greater than count, set tail to the new value.
        elif(index >= self.count):
            self.tail.next = newNode
            self.tail = newNode

        # If index is 0, set head to new value.
        elif(index == 0):
            newNode.next = self.head
            self.head = newNode

        else:
            node = self.head

            #Iterating to obtain the index node
            for _ in range(0, index - 1):
                node = node.next
        
            newNode.next = node.next
            node.next = newNode

        self.count += 1

    def append(self, value):
        ''' appends a value to the singly-linked list, and sets it as the tail.'''
        self.insert(self.count, value)

    def remove(self, index):
        ''' removes a value from the linked list based on its index '''
        if self.head == None:
            return None
        
        # returns none if index is greater than count
        elif(index > self.count):
            return None

        # returns head if index = 0
        elif(index == 0):  
            node = self.head
            self.head = node.next

        else:
            parentNode = self.head

            # iterates through nodes until parent node whose child is index.
            if(index > 1):
                for _ in range(0, index - 2):
                    parentNode = parentNode.next

            node = parentNode.next
            newNext = node.next

            parentNode.next = newNext

            # sets parent node to tail if parent node's child is the tail.
            if(newNext == None):
                self.tail = parentNode

        self.count -= 1

        return node.value

    def removeFirst(self):
        '''Removes the first (head) node from the singly-linked list.'''

        # if there are no values in the linked list, return.
        return self.remove(0)

    def removeLast(self):
        '''Removes the last (tail) node in the singly-linked list.'''
        return self.remove(self.count)

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

    def __init__(self, value=None):
        self.value = value # The current value of the node.
        self.next = None #The node that comes after the current node.