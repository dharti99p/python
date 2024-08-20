#10.Python program to find largest number in a list 

a=[]
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=input("Enter the list number {} : ".format(i))
    a.append(b)
print(a)

a.sort(reverse=True)

print("Largest number : ",a[0])