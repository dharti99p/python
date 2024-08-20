#7. Python program to find sum of elements in list 

a=[]
sum=0
n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=int(input("enter the list number {} : ".format(i)))
    a.append(b)
    sum=sum+b
print(a)

print("All list number sum : ",sum)