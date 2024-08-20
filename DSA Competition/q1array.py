def smallestnum(a):
    mset = set()
    
    for num in a:
        if num > 0:
            mset.add(num)
    
    smallest = 1
    while smallest in mset:
        smallest += 1
    return smallest
# a = [7, 8, 6, 11, 12]
a = []

n=int(input("Enter the number of list size : "))

for i in range(1,n+1):
    b=int(input("Enter the list number {} : ".format(i)))
    a.append(b)
print(a)
print(smallestnum(a))