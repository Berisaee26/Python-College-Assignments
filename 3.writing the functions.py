#writing the functions

ip=input('Input the temperature you want to convert(for eg: 45F or 102C) :')

if ip[-1]=='F':
    t=int(ip.rstrip('F'))
    c=(5/9)*(t-32)
    print('The temperature in Celsius is',c,'C') 
else:
    t=int(ip.rstrip('C'))
    c=((9/5)*t)+32
    print('The temperature in Fahrenheit is',c,'F')

#2.

l=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        l.append(i)
print('Numbers divisible by 7 and a multiple of 5:',l)

#3.
for i in range(1,51):
    if (i%3==0 and i%5==0):
        print(i,':','Fizzbuzz')
    elif(i%5==0):
        print(i,':','Buzz')
    elif(i%3==0):
        print(i,':','Fizz')

#4.
list=[]        
flag=True
while(flag):
    line=input('Enter line:')
    list.append(line)
    if line=='':
        flag=False
for l in list:
    print(l.lower())