class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50
        but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.items = [] * capacity
        self.num_items = 0

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other
           items using the < operator'''
        if self.is_full():
            return False
        self.num_items += 1
        self.items.append(item)
        if self.num_items == 1:
            return True
        self.perc_up(self.num_items)
        return True
        # Should call perc_up

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.items[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        root = self.items[1]
        self.items[1] = self.items[self.num_items]
        self.items = self.items[:self.num_items]
        self.num_items -= 1
        counter = self.num_items // 2
        while 0 < counter:
            self.perc_down(1)
            counter -= 1
        return root
        # Should call perc_down

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.items[1:]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate
        exactly the number of items in alist'''
        # Bottom-Up construction. Do NOT call enqueue
        if self.capacity < len(alist):
            self.capacity = len(alist)
        self.items = [None] + alist
        self.num_items = len(alist)
        for i in range(len(alist), 0, -1):
            self.perc_down(i)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.num_items == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.capacity == self.num_items

    def get_capacity(self):
        '''this is the maximum number of entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.num_items

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        child_index = i
        while (child_index * 2) <= self.num_items:
            max_index = self.get_max(child_index)
            if self.items[child_index] < self.items[max_index]:
                self.items[child_index], self.items[max_index] = self.items[max_index], self.items[child_index]
            child_index = max_index

    def get_max(self, i):
        left_child = i * 2
        right_child = i * 2 + 1
        if self.num_items < right_child:
            return left_child
        else:
            if self.items[right_child] < self.items[left_child]:
                return left_child
            else:
                return right_child

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        child_index = i
        parent_index = i // 2
        child_index = i
        while 0 < parent_index:
            parent_index = child_index // 2
            try:
                if self.items[parent_index] < self.items[child_index]:
                    parent = self.items[parent_index]
                    self.items[parent_index] = self.items[child_index]
                    self.items[child_index] = parent
                child_index = parent_index
            except:
                child_index = parent_index

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        newL = []
        while 0 < self.num_items:
            newL.append(self.dequeue())
        alist[:] = reversed(newL)