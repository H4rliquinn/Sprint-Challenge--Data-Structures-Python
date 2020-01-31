from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'BST:{self.value}L[{self.left}]R[{self.right}]'
    # Insert the given value into the tree

    def insert(self, value):
        curr_node = self
        new_node = BinarySearchTree(value)
        while True:
            if value > curr_node.value:
                if curr_node.right == None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right
            elif value < curr_node.value:
                if curr_node.left == None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            else:
                break
                # print("Anarchy!")
        return new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curr_node = self
        while True:
            if curr_node.value == target:
                return True
            elif target > curr_node.value:
                if curr_node.right == None:
                    return False
                else:
                    curr_node = curr_node.right
            else:
                if curr_node.left == None:
                    return False
                else:
                    curr_node = curr_node.left

    # Return the maximum value found in the tree
    def get_max(self):
        curr_node = self
        while True:
            if curr_node.right != None:
                curr_node = curr_node.right
            else:
                return curr_node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        curr_node = node
        if curr_node.left:
            curr_node.left.in_order_print(curr_node.left)
        print(curr_node.value)
        if curr_node.right:
            curr_node.right.in_order_print(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        curr_node = node
        q = Queue()
        q.enqueue(curr_node)
        while len(q) > 0:
            curr_node = q.dequeue()
            print(curr_node.value)
            if curr_node.left:
                q.enqueue(curr_node.left)
            if curr_node.right:
                q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        curr_node = node
        pancakes = Stack()
        pancakes.push(curr_node)
        while len(pancakes) > 0:
            if curr_node.right:
                pancakes.push(curr_node.right)
            if curr_node.left:
                pancakes.push(curr_node.left)
            print(curr_node.value)
            curr_node = pancakes.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BinarySearchTree(6)
# bst.insert(2)
# bst.insert(8)
# print(bst)
# bst.insert(17)
# print(bst.contains(6), bst.contains(17), bst.contains(4))
# bst.insert(23)
# bst.insert(18)
# print(bst)
# print(bst.get_max())
# print("***")

# arr = []


# def cb(x): return arr.append(x+10)
# def cb(x): return x+10


# bst.for_each(lambda x: x+10)
# print(bst)
# print(arr)
