#8. Python | MulƟply all numbers in the list

a=[]
mul=1
n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=int(input("enter the list number {} : ".format(i)))
    a.append(b)
    mul*=b
print(a)

print("All list number multiplication : ",mul)