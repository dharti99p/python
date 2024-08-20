# 27.Python program to find CumulaƟve sum of a list

a=[]
c=[]
sum=0

n=int(input("Enter the size of list : "))

for i in range(1,n+1):
    b=eval(input("Enter the value : "))
    a.append(b)
    sum+=b
    c.append(sum)

print("List of a : ",a)

print("Sum : ",c) 