'''module implementing stack using queues'''
class Queue:
    '''class queue'''
    def __init__(self):
        self.queue_data = []

    def push(self, x: int) -> None:
        '''adds element to queue'''
        self.queue_data.append(x)

    def pop(self) -> int:
        '''returns and deletes first element from queue'''
        return self.queue_data.pop(0)

    def peek(self) -> int:
        '''returns first element of queue'''
        return self.queue_data[0]

    def size(self) -> int:
        '''returns length of queue'''
        return len(self.queue_data)

    def is_empty(self) -> bool:
        '''returns bool if queue is empty'''
        return len(self.queue_data) == 0


class MyStack:
    '''class stack'''
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
        '''returns last element of stack'''
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
