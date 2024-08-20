# 13.Python – Least Frequent Character in String

str=input("Enter the string : ")

n=[]
b=[]
ch=[]

for i in str:
    if i not in b:
        b.append(i)

for i in range (len(b)):
    ch.append(b[i])
    n.append(str.count(b[i]))

index_no = n.index(min(n))
print("Min character is => ",ch.pop(index_no))