import array
class Queue:
    def __init__(self,n):
        self.q=array.array('i',[0]*n)
        self.front=-1
        self.rear=-1
        self.size=n

    def is_empty(self):
        return print((self.front==-1))
    
    def is_full(self):
        return print((self.rear==self.size-1))
    
    def insert(self,x):
        if self.is_full():
            print('Overflow')
        elif self.front==-1:
            self.front=0
            self.rear=self.rear+1
            self.q[self.rear]=x
        else:
            self.rear=self.rear+1
            self.q[self.rear]=x

    def remove(self):
        if self.is_empty():
            print('Underflow')
            return None
        else:
            self.q.pop(self.front)
    
    def display(self):
        if self.is_empty():
            print('Empty Queue')
        else:
            for i in range(self.front,self.rear):
                print(self.q[i])
    
        
        

            
    