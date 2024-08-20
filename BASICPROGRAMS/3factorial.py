# 3. Python Program for factorial of a number 

fact=1

n=int(input("Enter the number : "))

for i in range(1,n+1):
    fact=fact*i
    print(fact)

print(fact)