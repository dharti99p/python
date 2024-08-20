a=[]
n=int(input("Enter the Tuple size : "))

for i in range(1,n+1):
    a.append(eval(input("Enter the Tuple items {} : ".format(i))))

for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

a=tuple(a)
print(a)

#list=[['A',26],['b',21],['c',20],['o',1]]
'''list=[]
n=int(input("Enter the size : "))
for i in range(1,n+1):
    list.append(eval(input("Enter the value : ")))

for i in range(len(list)):
    for j in range(len(list)-1):
        if(list[j][1]>list[j+1][1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
list=tuple(list)
print(list)'''