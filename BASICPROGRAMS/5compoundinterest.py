# 5. Python Program for compound interest 

p=int(input("Enter the principle amt : "))
t=int(input("Enter the Time : "))
r=int(input("Enter the rate : "))

amt=p*pow((1+r/100),t)
ci=amt-p

print("Compound interest : ",ci)