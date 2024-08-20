#30.Python | Sort the values of first list using second list 

a=[]
n=int(input("Enter the list size : "))

for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)
    a.sort()

print(a)

'''a=[[4,6,7],[1,4,10],[7,9,6]]
for i in range(3):
    a.sort()
print(a)'''