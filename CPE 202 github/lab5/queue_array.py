# FIFO - first in, first out (enqueue to the back, dequeue from the front)
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

    def enqueue(self, item):
        if self.is_full():
            new = [None] * self.capacity
            self.items = self.items + new
            self.items[self.back] = item
            self.back += 1
            self.capacity *= 2
        else:
            self.items[self.back] = item
            self.back += 1
        self.num_items += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        original_front = self.items[self.front]
        # print("index", self.front)
        # print("val", original_front)
        self.items = self.items[self.front + 1:]
        self.num_items -= 1
        return original_front

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def size(self):
        return self.num_items

    def print(self):
        print(self.items)

    def dequeue_at(self, index):
        if index < 0 or index > (len(self.items) - 1) or self.is_empty():
            raise IndexError
        store = self.items[index]
        self.items = self.items[:index] + self.items[index + 1:]
        self.num_items -= 1
        return store

    def enqueue_at(self, index, val):
        if index < 0 or index > (len(self.items) - 1) or self.is_full():
            raise IndexError
        if self.items[index] is None:
            self.items[index] = val
        else:
            self.items = self.items[:index] + [val] + self.items[index:]
        self.num_items += 1
