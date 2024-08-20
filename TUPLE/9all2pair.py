# 9.Python – All pair combinations of 2 tuples

# t1=(2,3)
# t2=(4,5)

# result=[(a,b) for a in t1 for b in t2]
# result=result+[(a,b) for a in t2 for b in t1]

# result=tuple(result)

# print(result)

t1=[]
t2=[]
n1=int(input("Enter the size of Tuple 1 : "))

for i in range(1,n1+1):
    t1.append(eval(input("Enter the t1 element {} : ".format(i))))

t1=tuple(t1)

n2=int(input("Enter the size of Tuple 2 : "))

for i in range(1,n2+1):
    t2.append(eval(input("Enter the t2 element {} : ".format(i))))

t2=tuple(t2)

print("Tuple 1 : ",t1)
print("Tuple 2 : ",t2)

result=[(a,b) for a in t1 for b in t2]
result+=[(a,b) for a in t2 for b in t1]

print("All pair combination : ",result)