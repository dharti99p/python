#3. Python | Ways to find length of list 

a=[]
sum=0
n=int(input("enter the list size : "))

for i in range(1,n+1):
    b=input("enter the list number {} : ".format(i))
    a.append(b)
    
print(a)
print(len(a))