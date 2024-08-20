d={}

kn=int(input("Enter the size of key : "))

for i in range(1,kn+1):
    v=[]
    k=input("Enter the key{} : ".format(i))

    vn=int(input("Enter the size values {} : ".format(k)))
    for j in range(1,vn+1):
        v.append(input("Enter the value {} {} : ".format(j,k)))
    d[k]=v

print("Dictionary : ",d)

choice=input("Enter the choice : ")

del d[choice]

print("with remove : ",d)