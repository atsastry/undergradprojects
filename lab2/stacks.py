'''
        1. Implement a stack class
        2. the stack class takes as input a length
        3. The stack class has the following methods
            - push() - adds an element to the stack
            - stack_length() - returns the number of elements in the stack
            - pop() - returns the last element in the stack and deletes the last item
            - peek() - returns the top element in the stack
            - is_empty() - returns True if the stack is empty else False
            - print() - prints all the numbers present in the stack
    '''

class Stack:
    def __init__(self, length):
        self.minimum = 9999999999999
        self.length = length
        self.num_items = 0
        self.items = [None] * length

    '''
        write a function called InsertAt which takes in a value and an index and inserts that value into the stack at the given index 
        '''
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
        # if item < self.minimum:
        #     self.minimum = item
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



    "Given the below string, return true if it is a valid set of parenthesis else False"
    "Input: 1. '{{{{{}[]()}}}}', 2. '(])', 3. ']]]][[[[[' "

    '''
    algorthim:
    1. check if string has a length of 1 --> return false if so 
    2. else: iterate through string to access each character
    3. check if each character is an opening character --> [, (, { 
        a. if so, push that character
    4. else (character is a closing character): call pop and store the top of the stack in a variable 
        a. check if the top of the stack matches correctly with the character (separate if statements for the different characters)
            i. if it does match correctly, continue iterating
            ii. else: return False
    5. once you have finished iterating through the whole string, check if the stack is empty
        a. if so, return True
        b. else: return False 
    '''

    def valid_paren(self, parens):
        if len(parens) == 1:
            return False
        if parens[0] == ")" or parens[0] == "]" or parens[0] == "}":
            return False
        for char in parens:
            if char == "(" or char == "[" or char == "{":
                self.push(char)
            else:
                top = self.pop()
                if char == ")" and top == "(":
                    continue
                if char == "]" and top == "[":
                    continue
                if char == "}" and top == "{":
                    continue
                else:
                    return False
        if self.is_empty():
            return True
        return False

    'Write a function popAt(index) that removes the element at the index and returns the popped element'

    def popAt(self, index):
        if index < 0 or index > len(self.items) - 1:
            raise IndexError
        self.items = self.items[:index] + self.items[index + 1:]
        self.num_items -= 1
        return self.items[index]


    '''    
    algorithm:
    1. iterate through every number in the stack 
    ex. 1 2 3 4
    2. assume the first number in the stack is the minimum value 
    3. compare it with the rest of the values in the list 
        i. if a value in the rest of the list is less than the minimum, set the minimum to that value and continue comparing
        ii. else: continue comparing with the rest of the values
    4. once you have finished iterating return the minimum
    '''
    '''
    "Add a function minimum that returns the minimum item in the stack"
    '''
    def find_min(self):
        # minimum = self.items[0]
        # for i in range(1, len(self.items)):
        #     if self.items[i] < minimum:
        #         minimum = self.items[i]
        #     else:
        #         continue
        return self.minimum


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
    # print(stack.items)
    # stack.insertAt(5, 1)
    # print(stack.items)
    # print(stack.valid_paren("()"))
    # print(stack.valid_paren("({{{{{}[]()}}}})"))
    # print(stack.valid_paren("(])"))
    # print(stack.valid_paren("]]]][[[[["))
    # print(stack.valid_paren("]"))
    # print(stack.valid_paren("["))
    # stack.push(10)
    # stack.push(9)
    # stack.push(89)
    # stack.push(7)
    # stack.push(9)
    # stack.push(0)
    # stack.push(100)
    # stack.push(12)
    # stack.push(56)
    # stack.push(32)
    # stack.find_min()
    # stack.push("a")
    # print(stack.items)
    # stack.push("b")
    # print(stack.items)
    # stack.push("c")
    # print(stack.items)
    # stack.push("d")
    # print(stack.items)
    # # stack.insertAtTop("e")
    # # print(stack.items)
    # # stack.insertAtTop("f")
    # # stack.insertAtTop("g")
    # # stack.push("e")
    # # stack.push("f")
    # # stack.push("g")
    # stack.insertAt("d", 5)
    # stack.popAt(2)
    # print(stack.items)
    #stack.print()
    #print(stack.reverse_stack())
    # print(stack.popAt(1))
    # print(stack.stack_length())
    #
    # print(stack.popAt(-1))
    # print(stack.popAt(10000))

    # stack.pop()
    # stack.pop()
    # stack.pop()
    #
    # print(stack.popAt(0))
