#9. Python program to find smallest number in a list 

a=[]
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=input("Enter the list number {} : ".format(i))
    a.append(b)
print(a)

a.sort()

print("Smallest number : ",a[0])