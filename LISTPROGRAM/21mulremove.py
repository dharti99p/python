#21.Remove mulƟple elements from a list in Python

a=[]
n=eval(input("Enter the list of size : " ))

for i in range(1,n+1):
    a.append(eval(input("Enter the value {} : ".format(i))))
print(a)

n=eval(input("Enter your remove element choice : "))

for i in range(n):
    e=eval(input("Enter the elements : "))
    a.remove(e)

print(a)