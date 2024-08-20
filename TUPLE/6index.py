#6. Python – Closest Pair to Kth index element in Tuple 

'''q=[(5,6),(5,7),(5,8),(6,7),(1,2),(6,8)]
o=[]
for i in q:
    for index,value in enumerate(o): 
        if o[index][0]==i[0]:
    #if o and o[-1][0]==i[0]:
            o[-1].extend(i[1:])
        else:
            o.append([e for e in i])

print(o) '''

#q=[(5,6),(1,2),(5,7),(5,8),(1,3),(11,9)]
q=[]
o=[]

n=int(input("Enter the tuple size : "))

for i in range(1,n+1):
    q.append(eval(input("Enter the tuple {} : ".format(i))))
q.sort()

for i in q:
    if o and o[-1][0]==i[0]:
        o[-1].extend(i[1:])
    else:
        o.append([e for e in i])#list comprihension

o=tuple(o)
print(o)