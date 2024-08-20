# 11.Python | Count the Number of matching characters in a pair of string 

str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

a=0
b=0

for i in str1:
    if str2.find(i)>0 and b==str1.find(i): 
        a+=1
    b+=1

print(a)



# str1 = input("Enter the first string : ")
# str2 = input("Enter the second string : ")

# count = 0

# for i in range(len(str1)):
#     if (str1[i]==str2):
#         count+=1

# print("The total Number of Times ",str2,"has Occured = ",count)