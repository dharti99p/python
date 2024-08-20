# # 6. Python Program to check Armstrong Number

# l=0
# arm=0

# n=int(input("Enter the number : "))

# c=n

# while(n>0):
#     n//=10
#     l+=1

# n=c

# while(n>0):
#     r=n%10
#     arm+=(r**l)
#     n//=10

# print("Armstrong number sum : ",arm)
20

# if arm==c:
#     print(c," is Armstrong number.")
# else:
#     print(c,"is not armstrong number.") 


num = int(input("enter the num "))
num_str = str(num)
num_digits = len(num_str)
sum_cubes = sum(int(i)**num_digits for i in num_str)
if sum_cubes==num:
    print("yes")