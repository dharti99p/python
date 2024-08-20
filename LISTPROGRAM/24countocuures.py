# 24.Python | Count occurrences of an element in a list 

# a=[1,2,1,6,5,5,7,7,7,7,1]

# while len(a)>0:
#     k=a[0]
#     print("{} repeated {} time ".format(k,a.count(k)))
#     while k in a:
#         a.remove(k)

a=[]
n=int(input("Enter the size of list : "))

for i in range(1,n+1):
    a.append(eval(input("Enter the list of element {} : ".format(i))))

print("List : ",a)

while len(a)>0:
    k=a[0]
    print("{} repeated {} time ".format(k,a.count(k)))
    while k in a:
        a.remove(k)