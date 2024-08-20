# 1. Python program to check if a string is palindrome or not 

'''p=0
n=int(input("Enter the number : "))
c=n

while n>0 :
    r=n%10
    p=r+(p*10)
    n=n//10

if p==c:
    print(p,"is palindrome number...")
else:
    print(p,"is not palindrome number...")'''



w=""

a=input("Enter the string : ")

for i in a:
    w=i+w  
    print(w)

if a==w:
    print("Yes,This is Palindrome...")
else:
    print("No,This is not Palindrome...")
