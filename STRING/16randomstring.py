# 16.GeneraƟng random strings unƟl a given string is generated

import string
import random

str=input("Enter the string : ")

prs=string.ascii_lowercase + string.digits + string.ascii_uppercase + " " 

tryamp=0
str1=""
i=0

while i<len(str):
    again=True
    while again:
        tryamp+=1
        t=random.choice(prs)
        if t==str[i]:
            str1+=t
            again=False
    i+=1

print(str,"is that genrated by computer in ",tryamp,"Attempt")



# import string
# import random

# str=input("Enter the string : ")

# prs=string.ascii_lowercase + string.digits + string.ascii_uppercase + " " 

# s=""
# tryamp=0
# t=""
# for i in str:
#     while i!=t:
#         tryamp+=1
#         t=random.choice(prs)
#         if i==t:
#             s+=t
#         tryamp+=1

# print(str,"is that genrated by computer in ",tryamp,"Attempt")


