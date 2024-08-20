# 15.Python | Program to check if a string contains any special character 
'''
str=input("Enter the string : ")

c=0

s="~!@#$%^&*()_}{][:;<>?/\|"

for i in range(len(str)):
    if str[i] in s:
        c+=1

if c:
    print("String is not accepted.") 
else:
    print("String accepted.")    
'''

str=input("Enter the string : ")

if not (str.isalnum()):
    print("special character.")
else:
    print("not special character.")

