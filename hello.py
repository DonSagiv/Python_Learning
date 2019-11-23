from LinkedList import SinglyLinkedList
from LinkedList import SinglyLinkedListNode

linkedList = SinglyLinkedList()

linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)

linkedList.iterate()

# removing the last value in the list
removedValue = linkedList.removeLast()
print('Removed last value: {}.'.format(removedValue))

linkedList.iterate()

# adding a value
valueToAdd = 2
print('Adding Value {}'.format(valueToAdd))
linkedList.add(valueToAdd)

linkedList.iterate()

# removing a value
itemToRemove = 2
print('Removing {} from linked list.'.format(itemToRemove))
linkedList.removeFirstEquals(itemToRemove)

linkedList.iterate()

#removing the first value
removedValue = linkedList.removeFirst()
print('Removed first value: {}.'.format(removedValue))

linkedList.iterate()

print('Linked list operation completed')