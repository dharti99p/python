l=[1,2,3,4]
sum = 0
for i in l:
    if i==1:
        raise Exception("Expection :1 is exception")
    else:
        sum+=i