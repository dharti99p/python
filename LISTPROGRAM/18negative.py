# 18.Python program to print negaƟve numbers in a list

a=[]
neg=0
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=int(input("Enter the list number {} : ".format(i)))
    a.append(b)
print(a)

for i in range(len(a)):
    if(a[i]<0):
        neg=a[i]
        print(a[i])