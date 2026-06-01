#q1 1 to n 
list1=['p','q']
n=['1','2','3','4','5']
new_list=[x+y for x in list1 for y in n]
print(new_list)

#q2 longer than n 
def long_words(n,str):
    str=str.split()
    new_list=[char for char in str if len(char)>n]
    print(new_list)   
long_words(3, "The quick brown fox jumps over the lazy dog")

#q3 count the number
list1=['xyz','abc','aba','1221']

new_list=[char for char in list1 if len(char)>2 and char[0]==char[-1]]
print(len(new_list))

#q4 cube of all elements
inp=[2,5,7,9,12]
out=[pow(char,3) for char in inp]
print(out)

#q5 combine and print elements
l1=[10,20,30]
l2=[30,10,40]

new_list=[(x,y) for x in l1 for y in l2 if x!=y]
print(new_list)

#q6 length of each word
sequence="the quick brown fox jumps over the lazy dog"
list1=sequence.split()
out=[len(word) for word in list1 if word!='the']
print(out)

#q7 square is greater than 50
import random

list1=list()
a=int(input("Enter the starting number:"))
b=int(input("Enter the ending number:"))
for i in range(b):
    x=random.randint(a, b)
    list1.append(x)

print("Original list:",list1)

new_list=[pow(num,2) for num in list1 if pow(num,2)>50]

print("Required list:",new_list)