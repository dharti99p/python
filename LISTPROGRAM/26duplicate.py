#26.Python | Program to print duplicates from a list of integers 

a=[]
c=[]
n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=int(input("Enter the list number {} : ".format(i)))
    a.append(b)
print(a)

for i in a:
    d=a.count(i)
    if d>1:
        if c.count(i)==0:
            c.append(i)

print("Duplicate print : ",c)

# duplicate remove
'''a=[]
n=int(input("Enter the number of list size : "))
for i in range(1,n+1):
    b=int(input("Enter the list number {} : ".format(i)))
    a.append(b)
print(a)

for i in a:
    if a.count(i)>1:
        while a.count(i)!=0:
            a.remove(i)
print(a) '''