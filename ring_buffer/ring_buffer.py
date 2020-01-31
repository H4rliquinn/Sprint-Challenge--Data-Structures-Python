from doubly_linked_list import DoublyLinkedList, ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = self.storage.add_to_tail(item)
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        elif len(self.storage) == self.capacity:
            self.current.value = item
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        curr = self.storage.head
        while curr:
            list_buffer_contents.append(curr.value)
            curr = curr.next
        # Buffer should clear, but that fails test
        # self.current = None
        # self.storage = DoublyLinkedList()
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
