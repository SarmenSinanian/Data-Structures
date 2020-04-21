import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare root now
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # If something is already there, recurse
                self.left.insert(value)
        else: # Value is >= Node
            # if greater go to right child
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # If something already there, recurse
                self.right.insert(value)

        # if lesser go left child

        # if greater go right child
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target) # using a return to report what we have found
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: # RECURSIVE SOLUTION BEGINS
            return self.value
        else:
            return self.right.get_max() # RECURSIVE SOLUTION ENDS

        # max_value = self.value
        # # create a reerence to the current node and update it
        # # as we traverse the tree
        # current = self # effectively a CURSOR/NODE that we can update;
        # #                 current = another name for the node;
        # while current:
        #     # current.value += 1 # adding to the 'self' node
        #     # print(self.value)
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        #
        # return max_value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb): # to call the same function on every single node
        #                      in the tree
        cb(self.value) # cb is from the test file

        # recurse
        if self.left: # IF THERE IS A LEFT NODE
            self.left.for_each(cb) # THEN RUN FOR_EACH FUNCTION AGAIN ON THE LEFT BRANCH; cb is the node value
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left != None and self.righ != None:

            if self.left:
                print(self.left.value)
        else:
            pass
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
