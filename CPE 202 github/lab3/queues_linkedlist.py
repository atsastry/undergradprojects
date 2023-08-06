class Node:
    def __init__(self, item):
        self.item = item
        self.next = next


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

# methods: is_empty, is_full, enqueue, dequeue, size
    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def size(self):
        return self.num_items

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        if self.is_empty():
            new = Node(item)
            self.front = new
            self.back = new
            self.num_items += 1
            return
        if self.size() == 1:
            new = Node(item)
            self.front.next = new
            self.back = new
            self.num_items += 1
            return
        if self.size() > 1:
            current = self.back
            new = Node(item)
            self.back = new
            current.next = self.back
            self.back += 1
            self.num_items += 1
            return

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        self.front = self.front.next
        self.num_items -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
