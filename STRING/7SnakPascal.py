# 7. Python – Convert Snake case to Pascal case 

str=input("Enter the string : ")

s=str.replace("_"," ")

s=s.title()

s=s.replace(" ","")

print(s)