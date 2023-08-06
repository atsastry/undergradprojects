class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


# make helper functions for recursive functions; remember what he was saying in lecture today
class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy.next == self.dummy

    def add(self, item):
        self.add_helper(item, self.dummy.next)

    def add_helper(self, item, node):
        if self.is_empty():
            new_node = Node(item)
            self.dummy.next = new_node
            new_node.prev = self.dummy
            new_node.next = self.dummy
            self.dummy.prev = new_node
            return True
        else:
            while node != self.dummy and node.item < item:
                return self.add_helper(item, node.next)
            new_node = Node(item)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list)
           returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        current = self.dummy.next
        # identifying item to remove and removes it
        while current.next != self.dummy:
            if current.item == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next
        # removing the item if it's at the end
        if current.item == item:
            current.prev.next = self.dummy
            self.dummy.prev = current.prev
            return True
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        current = self.dummy.next
        idx = 0
        while current.next != self.dummy:
            if current.item == item:
                return idx
            idx += 1
            current = current.next
        if current.item == item:
            return idx
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError
        current = self.dummy.next
        while current.next != self.dummy:
            if index == 0:
                current.prev.next = current.next
                current.next.prev = current.prev
                return current.item
            else:
                index -= 1
                current = current.next
        current.prev.next = self.dummy
        self.dummy.next = current.prev
        return current.item

    def search_own(self, item, current):
        # base cases
        if current.item == item:
            return True
        if current == self.dummy:
            return False
        return self.search_own(item, current.next)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_own(item, self.dummy.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        newL = []
        current = self.dummy.next
        while current != self.dummy:
            newL.append(current.item)
            current = current.next
        return newL

    def python_list_reversed_own(self, current, newL):
        # base case
        if current == self.dummy:
            return newL
        else:
            newL.append(current.item)
            return self.python_list_reversed_own(current.prev, newL)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_own(self.dummy.prev, [])

    def size_own(self, current, cnt):
        # base case
        if current.next == self.dummy:
            return cnt
        else:
            return self.size_own(current.next, cnt + 1)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_own(self.dummy, 0)