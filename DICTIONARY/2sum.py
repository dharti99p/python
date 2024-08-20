d={}

kn=int(input("Enter the size of key : "))

for i in range(1,kn+1):
    k=input("Enter the key{} : ".format(i))

    vn=int(input("Enter the value  : "))
    d[k]=vn

print("Dictionary : ",d)

print("Sum all values : ",sum(d.values()))