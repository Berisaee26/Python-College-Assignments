#Applicatios of queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return f"{item} added to the queue."

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        return f"{self.queue.pop(0)} removed from the queue."

    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Front element is {self.queue[0]}."

    def display(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Queue contents: {self.queue}"

    def is_empty(self):
        return len(self.queue) == 0


