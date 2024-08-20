#7. Python – Join Tuples if similar initial element

'''a=("dharti","ami","parth")
b=(1,2,3)
c=a+b
print(c)'''

a=((5,6),(5,7),(5,8),(5,9),(10,11,12,13))
l=[]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i][0]==a[j][0]:
            l.append(list(set(a[i],a[j])))
        j+=1
l.append(a[i])
i+=1
print(l)