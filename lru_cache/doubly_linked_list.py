"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        # Since there are two pointers DIRECTLY BELOW, this is a doubly-linked list
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # ALL CODE BELOW ADDED BY FOLLOWING LECTURER
        new_node = ListNode(value, None, None) # (value, None, None) because the added node doesn't have pointers yet
        # Adding one to list length in the __init__ method
        self.length += 1
        if not self.head and not self.tail: # if there is no head and there is no tail then the list must be empty
            self.head = new_node # then the new node is both the head
            self.tail = new_node # and the tail
        else: # Otherwise
            new_node.next = self.head # new_node.next is the pointer to the  actual old head (which is still called self.head); so we create the pointer with this line
            self.head.prev = new_node # the old head's previous becomes our new node; so we update the pointer to it here
            self.head = new_node # now that we've updated the pointers, we can update what the head is (have to
                                 # update pointers first or we lose the way to reference the node which means it is
                                 # effectively deleted)

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value # grabbing the value
        self.delete(self.head) # deleting the value
        return value # return the value of the removed node

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # ALL CODE BELOW ADDED BY FOLLOWING LECTURER
        new_node = ListNode(value, None, None) # (value, None, None) because the added node doesn't have pointers yet
        # Adding one to list length in the __init__ method
        self.length += 1
        if not self.head and not self.tail: # if there is no head and there is no tail then the list must be empty
            self.head = new_node # then the new node is both the head
            self.tail = new_node # and the tail
        else: # Otherwise
            new_node.prev = self.tail # new_node.prev is the pointer to the  actual old tail (which is still called self.tail); so we create the pointer with this line
            self.tail.next = new_node # the old head's previous becomes our new node; so we update the pointer to it here
            self.tail = new_node # now that we've updated the pointers, we can update what the head is (have to
                                 # update pointers first or we lose the way to reference the node which means it is
                                 # effectively deleted)

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value # grabbing the value
        self.delete(self.tail) # deleting tail value
        return value # return the value of the removed node

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node) # Using function we have already
        self.add_to_head(value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # ALL CODE BELOW ADDED BY FOLLOWING LECTURER
        self.length -= 1 # decrements the length to delete the tail

        #If LL is empty
        if not self.head and not self.tail:
            # TODO: Error handling
            return
        # If head and tail
        if self.head == self.tail:
            self.head = None # Deleting pointer to head; garbage collector then deletes
            self.tail = None # Deleting pointer to tail; garbage collector then deletes

        # If head
        elif self.head == node: # if the node chosen is the head
            self.head = self.head.next # point the head to the value after the current head
            node.delete() # delete the node

        # If tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()

        # Otherwise
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

# node(10)
# print()
# dll = DoublyLinkedList()
# dll.add_to_head('x')
# dll.add_to_head('y')
# new = ListNode('z')
# dll.move_to_front(new)
# print(f'final length: {len(dll)}')
# current = dll.head
# while current:
#     print(current.value)
#     current = current.next
#
# dll = DoublyLinkedList()
# dll.add_to_head('x')
# dll.delete('nonsense')

