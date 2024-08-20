# 12.Python program to find N largest elements from a list 

a=[]
sum=0
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=input("Enter the list number {} : ".format(i))
    a.append(b)
print(a)

a.sort(reverse=True)

b=a[0]

print("Largest number : ",a[0])

for i in range(len(a)):
    if(a[i]==b):
        sum+=1

print("Enter largest element of list : ",sum)