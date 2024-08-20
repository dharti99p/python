# 6521 5112 2014 8772

n = input("Enter the debit card number : ")
n=n.replace(" ","")
n=n.replace("-","")
sum = 0
# n=[x*2 if x%2==0 else x*3 for x in range(1,10+1)]
# n=[int(x)*2 if int(x)%2==0 else int(x)*3 for x in f]
# a=int(n[i]*2)
# f=[a=int(n[i]*2) if i%2==0 d=a%10 k=a//10 sum+=d+k if a>9  else sum+=a else sum+=int(n[i]) for i in range(len(n))]
for i in range(len(n)) :
    if i%2==0:
        a=int(n[i])*2
        if a > 9 :
            d = a % 10
            k = a // 10
            sum += d + k
        else :
            sum += a
    else :
        sum += int(n[i])

print("Card is valid. ") if sum % 10 == 0 else print("Card is not valid.")








'''
sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card # : ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

print("card number",card_number)

for x in card_number[::2] :
    sum_odd_digits += int(x)
print("sum odd",sum_odd_digits)

for x in card_number[1::2] :
    x = int(x)*2
    print("mul*2 =",x,end=" ")
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
        print("sum even = ",sum_even_digits)
    else:
        sum_even_digits += x
        print("sum even = ",sum_even_digits)

total = sum_odd_digits+sum_even_digits


print("total",total)

if total % 10 == 0:
    print("InValid")
else:
    print("Valid")
'''



# atm=input("Enter the card number : ")

# print(atm)

# atm=atm.replace(" ","")
# print(atm)

# for i in range(0,len(atm),2):
#     # checkDigit=(atm.pop(-1))
#     atm[i]=atm[i]*2
#     print(atm[i])
#     # if atm[i]%2==0:
#         # print(i)



# def digits_of(n):
#     return [int(d) for d in str(n)]
# digits=digits_of("4532015112830366")
# print(digits)

# odd_digits=digits[-1::-2]
# even_digits=digits[-2::-2]
# print(odd_digits)
# print(even_digits)

# checksum=0
# for d in even_digits:
#     checksum+=sum(digits_of(d*2))
# print("even",checksum)

# checksum+=sum(odd_digits)
# print("odd",checksum)

# print("valid") if checksum%90==0 else print("invalid")