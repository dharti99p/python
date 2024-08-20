# l = [10, -25, -1, 35, 11]
l = []

n = int(input("Enter the size of list : "))

for i in range(1, n+1) : 
    l.append(int(input("enter the list {} :".format(i))))

l.sort()
print(l)

ch = int(input("Enter the choice : "))

left = 0
right = n-1

while left < right :
    mid = (left + right)//2
    if l[mid] == ch :
        f = 1
        break
    elif l[mid] < ch : 
        left = mid + 1
    elif l[mid] > ch : 
        right = mid - 1

if f == 1 :
        print("index number : ",mid)
else :
        print("not find")


