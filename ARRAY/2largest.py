# 2. Python Program to find largest element in an array 

a=bytearray(100)
n=int(input("Enter the size of array : "))

print("Enter the element of the array : ")

for i in range(n):
    a[i]=int(input("a[{}] = ".format(i)))

print()

max=a[0]

for i in range(n):
    print("a[{}] = {}".format(i,a[i]))
    if(max<a[i]):
        max=a[i]

print("MAX in array : ",max)