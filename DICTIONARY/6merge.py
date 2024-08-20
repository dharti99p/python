d1={}
kn=int(input("Enter the size of key : "))

for i in range(1,kn+1):
    v=[]
    k=input("Enter the key : ")

    vn=int(input("Enter the size of value : "))
    for j in range(1,vn+1):
        v.append(input("enter the value : "))
    d1[k]=v

print()
d2={}
kn=int(input("Enter the size of key : "))

for i in range(1,kn+1):
    v=[]
    k=input("Enter the key : ")

    vn=int(input("Enter the size of value : "))
    for j in range(1,vn+1):
        v.append(input("enter the value : "))
    d2[k]=v

print("Dictionary 1 : ",d1)
print("Dictionary 2 : ",d2)

d1.update(d2)
print("Merge two Dictionary : ",d1)