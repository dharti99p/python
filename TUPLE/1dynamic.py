t=[]
n=int(input("Enter the size of tuple : "))
for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    t.append(b)
g=tuple(t)
print(g)