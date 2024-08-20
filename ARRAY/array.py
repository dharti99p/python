#q44
'''a=bytearray(10)
n=int(input("enter the array of size : "))
print("enter the elements of array ")
for i in range (n):
    a[i]=int(input("a[{}]:".format(i)))
print("")
for i in range (n):
    #print("a[{}]={}".format(i,a[i]))
    print("a[",i,"]:",a[i])'''

#q45
'''sum=0
a=bytearray(100)
n=int(input("enter the size of array "))
print("enter the element of array ")
for i in range (n):
    a[i]=int(input("a[{}] : ".format(i)))
print("")
for i in range (n):
    print("a[{}]={}".format(i,a[i]))
    sum+=a[i]
print("sum = ",sum)'''

#q46
'''a=bytearray(10)
n=int(input("enter the array of size "))
print("enter the element of array ")
for i in range(n):
    a[i]=int(input("a[{}] : ".format(i)))
print("")
max=min=a[0]
for i in range(n):
    print("a[{}] = {}".format(i,a[i]))
    if(max<a[i]):
        max=a[i]
    if(min>a[i]):
        min=a[i]
print("max a[{}]= ".format(i),max)
print("min a[{}]= ".format(i),min)'''

#q47
'''a=bytearray(10)
b=bytearray(10)
c=bytearray(20)

n1=int(input("enter the array a of size "))
print("enter the element of array a ")
for i in range(n1):
    a[i]=int(input("a[{}] = ".format(i)))
print("")
for i in range(n1):
    print("a[{}] = {}".format(i,a[i]))
    c[i]=a[i]
n3=i

n2=int(input("enter the array b of size "))
print("enter the element of array b ")
for i in range(n2):
    b[i]=int(input("b[{}] = ".format(i)))
print("")
for i in range(n2):
    print("b[{}] = {}".format(i,b[i]))
    c[n3]=b[i]
    n3+=1

print("merge a and b array ")
for i in range(n3+1):
    print(c[i])'''


a=bytearray(10)
b=bytearray(10)
c=bytearray(20)

n=int(input("enter the array a of size "))
print("enter the element of array a ")
for i in range(n):
    a[i]=int(input("a[{}] = ".format(i)))
print("")
for i in range(n):
    print("a[{}] = {}".format(i,a[i]))

#n2=int(input("enter the array b of size "))
print("enter the element of array b ")
for i in range(n):
    b[i]=int(input("b[{}] = ".format(i)))
print("")
for i in range(n):
    print("b[{}] = {}".format(i,b[i]))

for i in range(n*2):
    if i<n:
        c[i]=a[i]
    else:
        c[i]=b[i-n]
    print(c[i])

