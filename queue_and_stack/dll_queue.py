import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# ^ IMPORTING FROM THE doubly_linked_list DIRECTORY
# CAN'T USE LISTS IN THIS HOMEWORK


class Queue:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        self.length = 1 if self.storage == 1 else 0
        # self.storage = ?

    def enqueue(self, value):
        # should add an item to the back of the queue
        self.storage.add_to_tail(value)
        self.length += 1
        pass

    def dequeue(self):
        # should remove and return an item from the front of the queue
        if self.length != 0:
            value = self.storage.head.value
            self.storage.delete(self.storage.head)
            self.length -= 1
            return value
        else:
            pass

    def len(self):
        # returns the number of items in the queue
        return self.length


