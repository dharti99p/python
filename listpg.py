#q-2
'''print("hello world")'''

#q3
'''a=3
print(a)'''

#q4
'''a=3.4
print(a)'''

#q5
'''a=int(input("enter the value a "))
print("ente the a ",a)'''

#q6
'''a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))
print("addition ",a+b+c)'''

#q7
'''mul=a*b*c
print("multiplication ",mul)'''

#q8
'''sum=a+b+c
avg=sum/3
print("average ",avg)'''

#q9
'''import math as M
r=float(input("enter the radius "))
circle=M.pi*r*r
print("area of circle ",circle)'''

'''l=5
b=9
rectangle=l*b
print("area of rectangle ",rectangle)'''

'''l=int(input("enter the value l "))
b=int(input("enter the value b "))
rectangle=l*b
print("area of rectangle ",rectangle)

if(b>l):
    print("b is max...")
else:
    print("l is a max...")'''

#q10
'''p=float(input("enter p "))
r=float(input("enter r "))
n=float(input("enter n "))
si=p*r*n/100
print("si = ",si)'''

#q11
'''import math as M
r=float(input("enter the radius "))
perimeter=2*M.pi*r
print("perimeter of circle ",perimeter)'''

#q12
'''f=float(input("enter the Fahrenheit "))
c=(5/9)*(f-32)
print("temperature in Fahrenheit to celsius ",c)'''

#q13
'''n=int(input("enter the value n "))
#t3=n%10  n//100 sum=n+t3
t3=n%10
n=n//10
s2=n%10
n=n//10
f1=n%10

sum=f1+t3
print("f1 ",f1)
print("s2 ",s2)
print("t3 ",t3)
print("sum",sum)'''

#q14
'''n=int(input("enter the five digit number"))
s5=n%10
n=n//10
s4=n%10
n=n//10
s3=n%10
n=n//10
s2=n%10
n=n//10
s1=n%10

sum=s1+s2+s3+s4+s5
print("f1 ",s1)
print("s2 ",s2)
print("t3 ",s3)
print("t4 ",s4)
print("t5 ",s5)
print("sum",sum)'''

#q15
'''a=int(input("enter number a "))
b=int(input("enter number b "))
#c=a
#a=b
#b=c
a=a+b
b=a-b
a=a-b
print("a is ",a)
print("b is ",b)'''

#q16
'''l=int(input("enter the number l "))
b=int(input("enter the number b "))
perimeter=2*l+2*b
print("perimeter of rectangle ",perimeter)'''

#q17
'''basic=int(input("enter the basic salary "))
da=basic*0.40
hra=basic*0.20
ra=basic*0.10
salary=int(basic+da+hra+ra)
print("total salary ",salary)'''

#q18
'''import math as M
r=float(input("enter the radius "))
diameter=int(2*r)
area=M.pi*r*r
perimeter=2*M.pi*r

print("diameter ",diameter)
print("area ",area)
print("perimeter ",perimeter)'''

#q19
'''a=str(input("enter the number "))
print("ascii value ",ord(a))''' #method use to ascii value
'''a=int(input("enter the number "))
b=chr(a)
print(b)'''

#q20
'''x=int(input("enter the value of x "))
y=6*(x**2)+3*x+8
print("y = ",y)'''

#q21
'''a=int(input("enter the number "))
print("increment for loop ")
for i in range(0,a+1):
    print(i)    
print("decrement for loop ")
for i in range(a,-1,-1):
    print(i)'''

#q22
'''a=int(input("enter the number a "))
b=int(input("enter the number b "))
print("a&b ",a&b)
print("a|b ",a|b)
print("a^b ",a^b)
print("a~b ",~b)
print("a<< ",a<<2)
print("b>> ",b>>2)'''

#q23
'''n=int(input("enter the number "))
if(n>100):
    print("greater than 100 ")
else:
    print("less than 100 ")'''

#q23
'''n=int(input("enter the numer :- "))
if (n%2==0):
    print(n," is even number ")
else:
     print(n," is odd number ")'''

#q24
'''n=int(input("enter the value n "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''

#q25
'''n=int(input("enter the number "))
rev=0
for i in range(n):#while(n>0) 
    a=n%10
    rev=(rev*10)+a
    n=n//10
print("reverse number ",rev)'''

#q26
'''days=int(input("enter the days "))
year=int(days/365)
weeks=int((days%365)/7)
days=int((days%365)%7)

print("years is ",year)
print("weeks is ",weeks)
print("days is ",days)'''

#q27
'''a=int(input("enter the a number "))
b=int(input("enter the b number "))
if (a>b):
    print("a is max ")
else:
    print("b is max ")
if(a<b):
    print("a is min ")
else:
    print("b is min ")'''

#q28
'''a=int(input("enter the a number "))
b=int(input("enter the b number "))
c=int(input("enter the c number "))
if (a>b and a>c):
    print("a is max ")
elif(b>a and b>c):
    print("b is max ")
else:
    print("c is max ")
if(a<b and a<c):
    print("a is min ")
elif (b<a and b<c):
    print("b is min ")
else:
    print("c is min ")'''

#q29
'''maths=int(input("maths mark "))
guj=int(input("gujarati marks "))
eng=int(input("english marks "))
sci=int(input("science marks "))
ss=int(input("social scienc marks "))

per=(maths+guj+eng+sci+ss)/5
print("percentage ",per)

if (per>70):
    print("distinction")
elif(60<per<70):
    print("first class")
elif(60>per>50):
    print("second class")
elif(40<per<50):
    print("third class")
else:
    print("fail ")'''

#q30
'''n=int(input("enter the number "))
f=0
for i in range(2,n):
    if(n%i==0):
        f=1
if(f==0):
    print("prime number ")
else:
    print("not prime number ")'''

'''n=int(input("enter the number "))
for i in range(2,n):
    if(n%i==0):
        print("not prime number ")
if(n==i):
    print("prime number ")
    print("prime number ")'''

#q31
'''n=int(input("enter number "))
for i in range(1,n,2):
    if (i==5):
        continue
    print(i)

n=int(input("enter number "))
for i in range(1,n,2):
    if (i==5):
        break
    print(i)'''

#q32

#q33
'''cal=str(input("enter the + - * / : "))
a=int(input("enter the value of a - "))
b=int(input("enter the value of b - "))
match(cal):
    case '+' :
        print("addition = ",a+b)
    case '-' :
        print("substraction = ",a-b)
    case '*' :
        print("multiplication = ",a*b)
    case '/' :
        print("devide = ",a/b)
    case _ :
        print("invalid option ")'''

#q34
#n=int(input("enter the number "))
'''for i in range(1,n+1):
    print(i)'''

'''i=1
while(i<=n):
    print(i)
    i+=1'''

#q35
#q36-1...............................................
'''n=int(input("enter the number : "))
for i in range(n):
    for j in range(n):
        if(j<=i):
            (j%2==0^i%2==1)not print("1",end=" "):print("0",end=" ")
        else:
            print(" ",end=" ")
    print("")'''

#q36-2
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>=n-i+1):
            print(" ",i,end=" ")
        else:
            print(" ",end=" ")
    print()'''

#q36-3................................................
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>=n-i+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#q37-1
'''k=1
n=int(input("enter the number "))
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(" ",k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()'''

#q37-2
'''k=1
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j+i>=n+1):
            print(" ",k,end=" ")
            k+=2
        else:
            print(" ",end=" ")
    print()'''

#q37-3
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=n-i+1):
            print("",n-j+1,end="")
        else:
            print("",end="")
    print()'''

#q37-4
'''k=1
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=i):
            print("",k,end=" ")
            k+=2
        else:
            print(" ",end=" ")
    print()'''

#q37-5
'''k=2
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=i):
            print("",k,end=" ")
            k+=2
        else:
            print(" ",end=" ")
    print()'''

#q38-8
#q38-9...................................
'''k=1
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if( or i<=n ):
            print("",k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()'''

#38-10
'''k=65
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=j):#i<=j
            print(" ",chr(k),end=" ")            
        else:
            print(" ",end=" ")
    k+=1
    print()'''

#38-11
'''k=64
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=j):#(j<=n-i+1):
            print(" ",chr(k+j),end=" ")            
        else:
            print(" ",end=" ")
    print()'''

#38-14
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==2 or i==n//2+1):
            print("*",end=" ")            
        else:
            print(" ",end=" ")
    print()'''

#38-13
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i+j)%2==0):
            print("*",end=" ")            
        else:
            print(" ",end=" ")
    print()'''

#38-15
'''n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j>=n-i+1):
            print(" * ",end=" ")            
        else:
            print(" ",end=" ")
    print()'''

#38-16
k=n/2+2
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if():
            print("*",end=" ")            
        else:
            print(" ",end=" ")
    print()
    
#q40
'''a=0
b=1
n=int(input("enter the number "))
print("fibonnaci series ")
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c'''

#q41
'''fact=1
n=int(input("enter the number "))
print("factorial series")
for i in range(1,n+1):
    fact*=i
print(fact)'''

#q42
'''n=int(input("enter the number "))
for i in range(2,n):
    p=1
    for j in range(2,i):
        if(i%j==0):
            p=0
    if p:
        print(i)'''

#q43
'''l=0
arm=0
n=int(input("enter the number "))
c=n
while n>0:
    n//=10
    l+=1
n=c
while n>0:
    r=n%10
    arm+=(r**l)
    n//=10
print("armstrong number sum = ",arm)
if(arm==c):
    print("armstrong number ")
else:
    print("not armstrong number ")'''





#q50
'''sum=0
n=eval(input("enter the range "))
for i in range(1,n+1):
    if(i%2==0):
        sum-=i**2
    else:
        sum+=i**2
print("sum = ",sum)'''


    

 




'''n=int(input("enter "))
for i in range(n):
    for j in range(n):
        if (i+j>=n-1): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
