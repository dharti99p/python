'''d={
    "Local":["Admin","UserA"],
    "Admin":["Admin","UserB"],
    "Public":["UserA","UserB"]
}'''


'''OUTPUT :"Admin":["Local","Admin"]
         "UserA":["Local","Public"]
         "UserB":["Admin","Public"]'''


d={}
kn=int(input("Enter the key size : "))

for i in range(1,kn+1):
    v=[]
    k=input("Enter the key {} : ".format(i))
    
    vn=int(input("Enter the {} value size : ".format(k)))
    
    for j in range(1,vn+1):
        v.append(input("Enter the value of {} {} : ".format(k,j)))
    
    d[k]=v

print(d)

s={}

for k,v in d.items():
    for j in v:
        if j not in s:
            s[j]=[k]
        else:
            s[j].append(k)
print(s)
