# 2. Python program to check whether the string is Symmetrical or Palindrome 

str=input("Enter the string : ")

h=int(len(str)/2)

fs=str[:h]
ls=str[h:]

print(fs)
print(ls)

if fs == ls :
    print(str,"is Symmetrical word...")
else:
    print(str,"is not Symmetrical word...")

if fs == ls[::-1]:
    print(str,"is Palindrome word...")
else:
    print(str,"is not Palindrome word...")