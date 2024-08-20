# 12.Remove all duplicates from a given string in Python 

str=input("Enter the string : ")

s=""

for i in str:
    if i not in s:
        s+=i

print("Remove all Duplicates from string : ",s)