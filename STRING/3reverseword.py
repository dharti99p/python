# 3. Reverse words in a given String in Python 

str=input("Enter the sentence : ")

s=str.split()[::-1]

print(" ".join(s))


'''
str=input("Enter the sentence : ")

str1=""

a=str.split()

for i in a:
    str1+=i[::-1]+" "
    # str1+=i[::-1]+" "

print(str1)
'''