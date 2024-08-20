#4. Python | Ways to check if element exists in list

a=[]
n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=input("Enter the list number {} : ".format(i))
    a.append(b)
print(a)

c=input("Enter the exist list number : ")

if (c in a):
    print("It is exists in list.")
else:
    print("It is not exits in list.")
