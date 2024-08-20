'''import random
dict={
    "gmail":["WeeTech","fundookskills","ACDC"],
    "yahoo":["shiv","mahadev","shivshakti"],
    "hotmial":["ganesh","krishna","vishnu"]
}

print(dict["gmail"][0],random.randint(100,1000),"@gmail.com")'''

'''dict={}
n=int(input("enter the number : "))
for i in range(n):
    key,value=input().split()
    dict[key]=value

print(dict)'''

d={}
kn=int(input("key of dict : "))
for i in range(1,kn+1):
    v=[]
    k=input("enter the key {} : ".format(i))
    vn=int(input("enter the value size : "))
    for j in range(1,vn+1):
        v.append(input("enter value of {} {} : ".format(k,j)))
    d[k]=v
print(d)

import random
for i in d:
    print("your key is  -> ",i,"and name is -> ",d[i])
ch=input("enter the your choice key name = ")
for i in d[ch]:
    num=random.randint(100,999)
    #print(f"{i}{num}@{ch}.com")
    print(i,num,"@",ch,".com")
    