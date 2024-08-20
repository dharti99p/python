# 10.Python program to accept the strings which contains all vowels 

str=input("Enter the string : ")

str=str.replace(" ","")
str=str.lower()
vowel=(str.count("a"),str.count("e"),str.count("i"),str.count("o"),str.count("u"))

if vowel.count(0)>0:
    print("not accepted.")
    print("All vowels are not present...")
else:
    print("accepted.")
    print("All vowels are present...")
