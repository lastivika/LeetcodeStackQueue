'''module implementing queue using stacks'''

class Stack:
    '''class stack'''
    def __init__(self):
        self.stack_data = []

    def push(self, x: int) -> None:
        '''adds element to stack'''
        self.stack_data.append(x)

    def pop(self) -> int:
        '''returns and deletes element from stack'''
        return self.stack_data.pop()

    def peek(self) -> int:
        '''returns first element of stack'''
        return self.stack_data[-1]

    def size(self) -> int:
        '''returns length of stack'''
        return len(self.stack_data)

    def is_empty(self) -> bool:
        '''returns bool if stack is empty'''
        return len(self.stack_data) == 0

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
