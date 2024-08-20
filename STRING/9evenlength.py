# 9. Python program to print even length words in a string 

str=input("Enter the string : ")

a=str.split()

for i in a:
    if len(i)%2==0:
        print(i,"=>",len(i))