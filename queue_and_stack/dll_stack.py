import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# ^ IMPORTING FROM THE doubly_linked_list DIRECTORY
# CAN'T USE LISTS IN THIS HOMEWORK


class Stack:
    def __init__(self):

        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        self.length = 1 if self.storage == 1 else 0
        # self.storage = value
        # self.prev = prev
        # self.next = next


    def push(self, value):
        self.storage.add_to_tail(value)
        self.length += 1
        # current_next = self.next
        # self.next = Stack(value, self, current_next)
        # if current_next:
        #     current_next.prev = self.next

        return value

    def pop(self):
        # value = self.tail.value
        # self.delete(self.tail)
        # return value
        # node = self.next
        if self.length != 0:
            # value = self.storage.tail.value
            # self.storage.delete(self.storage.tail)
            # self.length -= 1
            self.length -= 1
            return self.storage.remove_from_tail()
        else:
            pass

    def len(self):
        # self.length
        return self.length


# print(DoublyLinkedList(node=[2,2,3,1,5]))
# s = Stack()
# print(s.len())
# print(s.push(5))
# print(s.len())
# # print(s.pop())
# print(s.push(1))
# print(s.len())
# print(s.pop())

# current = s.storage.
# while current:
#     print(current.value)
#     current = current.next