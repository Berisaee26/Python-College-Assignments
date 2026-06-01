#Set A
# Q1 extract digits 
str=input("Enter the string: ")
for ele in str:
    if ele.isdigit():
        print(ele,end=" ")

# Q2 remove all recurring characters
str=input("Enter the string: ")
new_str=" "
for ele in str:
    if ele not in new_str:
        new_str+=ele
print(new_str)

# Q3 strip set of characters
str=input("Enter the string: ")
strip=input("Enter set of characters: ")
new_str=" "
for ele in str:
    if ele not in strip:
        new_str+=ele
print(new_str)

# Set B
# Q1 sorting function 
list=[1,9,3,4,0,5,8]
def mysort(l):
    n=len(l)-1
    new_list=[]
    for ele1 in range(n):
        for ele2 in range(0,n-ele1):
            if l[ele2]<l[ele2+1]:
                l[ele2],l[ele2+1]=l[ele2+1],l[ele2]
    return l
output=mysort(list)
print(output)

# Q2
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=input("Enter the string: ")
shift=int(input("Enter shift with numbers: "))
ans=" "
for i in str:
    if i.isupper():
        index=list.index(i.lower())
        new_ind=index+shift
        if new_ind>25:
            new_ind-+26
        ans+=list[new_ind].upper()
    else:
        index=list.index(i)
        new_ind=index+shift
        if new_ind>25:
            new_ind-+26
        ans+=list[new_ind]
print(ans)
