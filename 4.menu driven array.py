import array
class Array:
    def __init__(self,n):
        self.a=array.array('i',[0]*n)
        self.size=n

    def max(self):
        print (max(self.a))
    
    def min(self):
        print (min(self.a))
    
    def sort(self):
        return (array.array(sorted(self.a)))
    
    def replace(self,item,pos):
        for i in self.a:
            if pos==self.a.index(i):
                self.a[pos]=item
    
    def insert(self,item,pos):
        return (self.a.insert(pos,item))
        
    
    def remove(self,item):
        return (self.a.remove(item))
    
    def is_empty(self):
        return (len(self.a)==0)
    
    def is_full(self):
        return (len(self.a)==self.size)
    
    def display(self):
        if (self.is_empty()):
            return ('Array is empty')
        else:
            for i in range(len(self.a)):
                print(self.a[i])

    



