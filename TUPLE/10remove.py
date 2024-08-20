#10.Python – Remove Tuples of Length K

# input=((1,),(2,3),(2,),(4,5,6))
# output=2
# ((1,),(2,),(4,5,6))

l=[]

n=int(input("Enter the Tuple of size : "))

for i in range(n):
    l.append(eval(input("Enter the tuple : ")))

l=tuple(l)
print("Tuple all element : ",l)

k=int(input("Enter the your choice remove length k : "))

result=(i for i in l if len(i)!=k)

result=tuple(result)

print("With Remove Tuple List : ",result)