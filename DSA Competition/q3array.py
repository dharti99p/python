import statistics

a = []
n = int(input("enter the list size : "))
for i in range(1, n+1) :
    b = int(input("enter the number {} : ".format(i)))
    a.append(b)
print('List : ', a)

b = []
n = int(input("enter the list size : "))
for i in range(1, n+1) :
    c = int(input("enter the number {} : ".format(i)))
    b.append(c)
print('List : ', b)

d = []
d = a + b
print(d)
n = len(d)
if n % 2 == 0 :
    c = (d[n//2-1] + d[n//2]) / 2
    print(c)
    median = statistics.median(d)
    print("Median : ", median)
else :
    c = d[n//2]
    print(c)
    median = statistics.median(d)
    print("Median : ", median)