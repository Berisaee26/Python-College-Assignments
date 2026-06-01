import array
class Stack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=array.array('i',[0]*capacity)
        self.top=-1
    
    def push(self,item):
        if self.top==self.capacity-1:
            print("Stack Overflow")
            return
        self.top+=1
        self.stack[self.top]=item
        
    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return None
        item=self.stack[self.top]
        self.top-=1
        return item 
    
    def peek(self):
        if not self.is_empty():
            return print(self.stack[self.top])
        else:
            print("Stack is empty. Cannot peek.")
            return None
        
    def size(self):
        print(len(self.stack))
    
    def is_empty(self):
        return print(self.top==-1)

s=Stack(3)
s.push(1)
s.push(2)
s.push(3)
s.peek()
