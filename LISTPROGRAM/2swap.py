#2. Python program to swap two elements in a list 

a=[]
b=[]
n=int(input("enter the number : "))

for i in range(n):
    c=input("enter value : ")
    a.append(c)
print(a)

for i in range(n):
    d=input("enter value : ")
    b.append(d)
print(b)

print("swap : ")

a,b=b,a

print(a,b)