# 15.Python Program for cube sum of first n natural numbers 

n=int(input("Enter the number : "))

sum=0

for i in range(n+1):
    sum+=(i**3)
    print(sum)