# 8. Python program to print all Prime numbers in an Interval 

n=int(input("Enter the number : "))

for i in range(2,n+1):
    p=1
    # print(i)
    for j in range(2,i):
        if(i%j==0):
            # print(j)
            p=0
    if p:
        print(i)
