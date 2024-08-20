# 25.Python | Remove empty tuples from a list

# l=[(),(1,2,3),1,2,3]

# for i in l:
#     if i==():
#         l.remove(i)

# print(l)


# for i in l:
#     if type(i)==tuple:
#         if len(i)==0:
            # l.remove(i)
# print(l)

l=[]

n=int(input("Enter the list of size : "))

for i in range(n):
    l.append(eval(input("Enter the list of element {} :".format(i))))

print("List of l : ",l)

for i in l :
    if i == ():
        l.remove(i)

print("Answer : ",l)



