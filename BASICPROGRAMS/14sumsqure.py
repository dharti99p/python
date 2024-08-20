# 14.Python Program for Sum of squares of first n natural numbers 

n=int(input("Enter the number "))

sum=0

for i in range(n+1):
    sum+=(i**2)

print(sum)