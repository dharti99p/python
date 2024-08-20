#2. Python program to Find the size of a Tuple 

a=[]
n=int(input("Enter the list size : "))
for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)
c=tuple(a)
print(c)
print("Size of Tuple : ",len(c))

'''t=(1,True,"apple")
print(len(t))'''