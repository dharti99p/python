# 4. Ways to remove i’th character from string in Python 

str=input("Enter the string : ")

n=int(input("Enter the i number : "))

a=str[0:n-1]
b=str[n:]

print("with i'th number delete : ",a+b)