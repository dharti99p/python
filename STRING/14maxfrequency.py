# 14.Python | Maximum frequency character in String 

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

index_no = n.index(max(n))
print("Max character is => ",ch.pop(index_no))
    # print("Frequency of ",b[i],"=> ",str.count(b[i]))
    # if max < b[i]:
    #     max=b[i]

# print(max(b,str.get))



