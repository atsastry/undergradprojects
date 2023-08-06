class Stack:
    def __init__(self, length):
        self.length = length
        self.num_items = 0
        self.items = [None] * length


    def insertAtTop(self, val):
        if stack.is_full():
            current = stack.items
            new = [None] * self.length
            self.items = current + new
        if stack.items[0] is None:
            stack.items[0] = val
        else:
            current = stack.items
            stack.items = [val] + current
        self.num_items += 1


    def insertAt(self, val, index):
        if index < 0 or index > len(self.items) - 1:
            raise IndexError
        if stack.is_full():
            temp = self.items
            # self.length = self.length * 2
            new = [None] * self.length
            self.items = temp + new
        if self.items[index] is None:
            self.items[index] = val
        else:
            before_spot = self.items[:index]
            after_spot = self.items[index:]
            self.items[index] = val
            self.items = before_spot + [self.items[index]] + after_spot
        self.num_items += 1

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.length

    def print(self):
        print(self.items)

    def size(self):
        return self.num_items

    def push(self, item):
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        else:
            top = self.items[self.num_items - 1]
            del(self.items[self.num_items - 1])
            self.num_items -= 1
            return top

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            top = self.items[self.num_items - 1]
            return top

    def reverse_stack(self):
        if self.is_empty():
            raise IndexError
        elif self.size() == 1:
            return self.items
        else:
            for i in range(len(self.items)//2):
                temp = self.items[i]
                self.items[i] = self.items[len(self.items) - (i + 1)]
                self.items[len(self.items) - (i + 1)] = temp
            return self.items


    def popAt(self, index):
        if index < 0 or index > len(self.items) - 1:
            raise IndexError
        self.items = self.items[:index] + self.items[index + 1:]
        self.num_items -= 1
        return self.items[index]


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.items)
    stack.popAt(2)
    print(stack.items)
    stack.insertAt(3, 2)
    print(stack.items)
    stack.insertAtTop("e")
    print(stack.items)
    stack.insertAtTop("f")
    stack.insertAtTop("g")
    stack.push("e")
    stack.push("f")
    stack.push("g")
    stack.insertAt("d", 5)
    stack.popAt(2)
    print(stack.items)
    stack.print()
    print(stack.reverse_stack())
    print(stack.popAt(1))
    print(stack.stack_length())
