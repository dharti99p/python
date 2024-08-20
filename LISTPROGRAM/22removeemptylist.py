# 22.Python – Remove empty List from List 

a=[]
n=int(input("Enter the list number : "))

for i in range(1,n+1):
    b=eval(input("Enter the value {} : ".format(i)))
    a.append(b)
print(a)

for i in a:
    if(i==[]):
        a.remove(i)

print("\nRemove element after list :- ",a)