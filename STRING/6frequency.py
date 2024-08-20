# 6. Python – Words Frequency in String Shorthands 
'''
s=input("Enter the string : ")

d={key : s.count(key) for key in s.split()}

print("The frequency : "+ str(d))
'''

str=input("Enter the string: ")

b=[]

for i in str:
    if i not in b :
        b.append(i)

for i in range(len(b)):
    print("Frequency of ",b[i],"=>",str.count(b[i]))
    