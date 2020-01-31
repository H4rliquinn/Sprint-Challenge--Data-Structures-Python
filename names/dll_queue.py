
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('/doubly_linked_list')


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        """DLL is a good choice because it is O(1) to add to the beginning or pop off the end"""

        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.len() > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
