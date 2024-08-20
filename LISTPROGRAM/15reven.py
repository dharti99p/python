# 15.Python program to print all even numbers in a range

a=[]
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=int(input("Enter the list number {} : ".format(i)))
    a.append(b)
print(a)

for i in range(len(a)):
    if(a[i]<6):
        if(a[i]%2==0):
            print(a[i])