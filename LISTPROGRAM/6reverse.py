#6. Python | Reversing a List 

a=[]
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=input("Enter the list number {} : ".format(i))
    a.append(b)
print(a)

print(a.reverse())

print("Reverse : ",a)