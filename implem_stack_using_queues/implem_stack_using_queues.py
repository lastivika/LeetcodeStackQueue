'''module implementing stack using queues'''

class Node:
    '''class node'''
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    '''class queue'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, x: int) -> None:
        '''adds element to the back of queue'''
        node = Node(x)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.length += 1

    def pop(self) -> int:
        '''returns and deletes first element from queue'''
        res = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return res

    def peek(self) -> int:
        '''returns first element of queue'''
        return self.head.data

    def size(self) -> int:
        '''returns length of queue'''
        return self.length

    def is_empty(self) -> bool:
        '''returns bool if queue is empty'''
        return self.head is None

class MyStack:
    '''class stack implemented via two queues'''
    def __init__(self):
        self.input_queue = Queue()
        self.output_queue = Queue()

    def push(self, x: int) -> None:
        '''adds element to stack'''
        self.input_queue.push(x)

    def pop(self) -> int:
        '''returns and deletes the last added element from stack'''
        while self.input_queue.size() != 1:
            self.output_queue.push(self.input_queue.pop())
        res = self.input_queue.pop()
        self.input_queue, self.output_queue = self.output_queue, self.input_queue
        return res

    def top(self) -> int:
        '''returns last added element of stack'''
        while self.input_queue.size() != 1:
            self.output_queue.push(self.input_queue.pop())
        res = self.input_queue.peek()
        self.output_queue.push(self.input_queue.pop())
        self.input_queue, self.output_queue = self.output_queue, self.input_queue
        return res

    def empty(self) -> bool:
        '''returns bool if stack is empty'''
        return self.input_queue.is_empty() and self.output_queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
