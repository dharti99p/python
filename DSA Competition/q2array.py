a=[]

n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=int(input("enter the number {} : ".format(i)))
    a.append(b)
    a.sort()
print('sorted list : ',a)
 
m = int(input("target : "))
a.append(m)
a.sort()
print(a)

x = a.index(m)
print(x)