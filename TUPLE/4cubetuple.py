#4. Create a list of tuples from given list having number and its cube in each tuple

a=[]
t=[]
n=int(input("Enter the list of size : "))

for i in range (1,n+1):
    a.append(eval(input("Enter the value : ")))

for i in a:
    t.append((i**3))
t=tuple(t)
print(t)