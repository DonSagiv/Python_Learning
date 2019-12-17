from LinkedList import SinglyLinkedList
from LinkedList import SinglyLinkedListNode

def createEmptyLinkedList():
    ''' Creates an empty linked list.'''
    
    print('Creating Empty Linked List')
    
    linkedList = SinglyLinkedList()

    return linkedList

def createNewLinkedList():
    ''' Creates a new linked list: 1 -> 2 -> 3 -> 4 -> 5. '''

    print('Creating a new linked list.')

    linkedList = SinglyLinkedList()

    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(4)
    linkedList.append(5)

    linkedList.iterate()

    return linkedList

# --- Test Insert Operations

# insert into empty array using a random index.
linkedList = createEmptyLinkedList()

valueToInsert = 6
indexToInsert = 2
print('Adding Value to empty Linked List in index {}: {}.'.format(indexToInsert, valueToInsert))
linkedList.insert(2, valueToInsert)
linkedList.iterate()

linkedList = createNewLinkedList()
# inserting a value into the linked list, using previous parameters
print('Adding Value to index {}: {}.'.format(indexToInsert, valueToInsert))
linkedList.insert(indexToInsert, valueToInsert)
linkedList.iterate()

# appending a value
valueToAdd = 7
print('Adding Value: {}.'.format(valueToAdd))
linkedList.append(valueToAdd)
linkedList.iterate()

# adding to start of linked list
valueToInsert = 8
print('Adding value {} to start of linked list.'.format(valueToInsert))
linkedList.insert(0, valueToInsert)
linkedList.iterate()

# --- Test Remove Operations

# removing from empty linked list
linkedList = createEmptyLinkedList()
indexToRemove = 2
print('Attempting to remove index {} from empty linked list.'.format(indexToRemove))
removedValue = linkedList.remove(indexToRemove)
print('Removed value: {}'.format(removedValue))
linkedList.iterate()

linkedList = createNewLinkedList()
# removing a value
itemToRemove = 2
print('Removing from linked list index: {}.'.format(itemToRemove))
linkedList.removeFirstEquals(itemToRemove)

linkedList.iterate()

# removing the last value in the list
removedValue = linkedList.removeLast()
print('Removed last value: {}.'.format(removedValue))
linkedList.iterate()

#removing the first value
removedValue = linkedList.removeFirst()
print('Removed first value: {}.'.format(removedValue))
linkedList.iterate()

print('Linked list operation completed')