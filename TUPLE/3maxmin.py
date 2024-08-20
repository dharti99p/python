#3. Python – Maximum and Minimum K elements in Tuple 

'''t=tuple(input("Enter the value : ").split())
print(t)
print("Maximum number : ",max(t))
print("Minimum number : ",min(t))'''

a=[]
n=int(input("Enter the size of list : "))

for i in range(1,n+1):
    a.append(eval(input("Enter the value {} : ".format(i))))

a=tuple(a)

print("Maximum number : ",max(a))
print("Minimum number : ",min(a))

'''t=(1,2,3,4,5,6,7,8,9,11)
print(max(t))
print(min(t))'''