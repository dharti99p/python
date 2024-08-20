# 23.Python | Cloning or Copying a list 

a=[]
n=int(input("Enter the list size a : "))

for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)

b=[]
n=int(input("Enter the list size b : "))

for i in range(1,n+1):
    c=eval(input("Enter the value {} : ".format(i)))
    b.append(c)

print("a list : ",a)
print("b list : ",b)

'''b=a.copy()
print("copy list : ",b)'''

b=a
print(b)