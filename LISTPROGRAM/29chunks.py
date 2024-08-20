#29.Break a list into chunks of size N in Python 

a=[]
L=[]
I=[]

n=int(input("Enter the list of size : "))
for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)

print(a)

c=eval(input("Enter the chunks size : "))

for i in a:
    I.append(i)
    if len(I)==c:
        L.append(I)
        I=[]

print(L)