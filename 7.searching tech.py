#searching techniques
import array as arr
inp=arr.array('i',[1,2,3,4,4,5])

#a)Linear search

search_val=int(input('Enter value to be searched :'))
found=False
for i in inp:
        if i==search_val:
            print('Value found at position :', inp.index(i)+1)
            found=True
if (found==False):
      print('Search unsuccessful')

 #b) Binary search

search_val=int(input('Enter value to be searched :'))
found=False
n=len(inp)
begin=0
end=n-1

for i in inp:
      mid=int(begin+end//2)

      if(search_val==inp[mid]):
            print('Value found at :', mid+1)
            found=True
            break
      elif(search_val>inp[mid]):
            begin=mid+1
      else:
            end=mid-1
if(found==False):
      print ('Search unsuccessful')   
         
#c) Linear search with multiple occurences

search_val=int(input('Enter value to be searched :'))
count=0
for i in inp:
        if i==search_val:
            print('Value found at position :', inp.index(i)+1)
            count+=1
if (count==0):
      print('Search unsuccessful')