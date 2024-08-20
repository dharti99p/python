# 1. Python Program to find sum of array 

sum=0
a=bytearray(100)
n=int(input("enter the size of array : "))

print("enter the element of array : ")

for i in range (n):
    a[i]=int(input("a[{}] : ".format(i)))

print("")

for i in range (n):
    print("a[{}]={}".format(i,a[i]))
    sum+=a[i]

print("sum = ",sum)