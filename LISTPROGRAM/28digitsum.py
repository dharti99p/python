# 28.Python | Sum of number digits in List 

a=[]
n=int(input("Enter the size of list : "))

for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)
print(a)

c=[]

for i in a:
    sum=0
    for d in str(i):
        sum+=int(d)
    c.append(sum)

print("Digit Sum List : ",c)