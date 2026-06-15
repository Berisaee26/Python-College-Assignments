class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self,size):
        return len(self.stack)==size

    def display(self):
        if not self.is_empty():
            print("Stack elements are:")
            for item in self.stack:
                print(item)
        else:
            print("Stack is empty")
            
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self,size):
        return len(self.queue)==size

    def display(self):
        if not self.is_empty():
            print("Queue elements are:")
            for item in self.queue:
                print(item)
        else:
            print("Queue is empty")
