#Applications of stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} popped from stack.")
        else:
            print("Stack is empty. Nothing to pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top element is: {self.stack[-1]}")
        else:
            print("Stack is empty.")

    def display(self):
        if not self.is_empty():
            print("Stack elements are:", self.stack)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0


