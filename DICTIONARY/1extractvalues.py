d={}
kn=int(input("Enter the size of key : "))

for i in range(1,kn+1):
    v=[]
    k=input("enter the key {} = ".format(i))
    
    vn=int(input("enter the values of size {} : ".format(k)))
    for j in range(1,vn+1):
        v.append(eval(input("Enter the values {} {} : ".format(k,j))))
    
    d[k]=v

print(d)

result=list(sorted({ele for val in d.values() for ele in val}))

print(result)


# key={
#     'k1':[2,7,3],
#     'k2':[9,8,6],
#     'k3':[4,1,0],
#     'k4':[43,67,12]
# }

# result=list(sorted({ele for val in key.values() for ele in val}))

# print(result)
