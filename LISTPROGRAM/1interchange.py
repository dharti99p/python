#1. Python program to interchange first and last elements in a list 

a=[]
n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=input("enter the number {} : ".format(i))
    a.append(b)

a[0],a[-1]=a[-1],a[0]

print(a)