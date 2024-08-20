#5. Python – Adding Tuple to List and vice – versa 

a=[]
b=()
b=list(b)
n=int(input("Enter the size of list : "))

for i in range(1,n+1):
    a.append(eval(input("Enter the list {} : ".format(i))))

for i in range(1,n+1):
    b.append(eval(input("Enter the tuple {} : ".format(i))))

a=tuple(a)

print(a)
print(b)

'''a=[(1,"string",False,"5t6j")]
b=[(True)]
a+=b
print(a)'''