'''module implementing queue using stacks'''
class Node:
    '''class node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''class stack'''
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x: int) -> None:
        '''adds element to stack'''
        node = Node(x)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self) -> int:
        '''returns and deletes element from stack'''
        res = self.top.data
        self.top = self.top.next
        self.length -= 1
        return res

    def peek(self) -> int:
        '''returns first element of stack'''
        return self.top.data

    def size(self) -> int:
        '''returns length of stack'''
        return self.length

    def is_empty(self) -> bool:
        '''returns bool if stack is empty'''
        return self.top is None

class MyQueue:
    '''class queue'''
    def __init__(self):
        self.input_stack = Stack()
        self.output_stack = Stack()

    def push(self, x: int) -> None:
        '''adds element to queue'''
        self.input_stack.push(x)

    def pop(self) -> int:
        '''returns and deletes element from queue'''
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self) -> int:
        '''returns first element of queue'''
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        return self.output_stack.peek()


    def empty(self) -> bool:
        '''returns bool if queue is empty'''
        return self.input_stack.is_empty() and self.output_stack.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
