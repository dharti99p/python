'''txt=[1,2,3,[4,5,6],[7,8,[9,10,11,12,13,14,15],22],21,22]
txt[4][2][4]=99
print(txt)'''



'''a=[]
n=int(input("enter the size of list : "))

for i in range(n):
    a.append(eval(input("enter element : ")))

choice=input("yes if create inner list no for not create inner list : ")
match(choice):
    case "yes":
        b=[]
        m=int(input("enter inner size : "))
        for i in range(m):
            b.append(eval(input("enter element : ")))
        a.append(b)

        choice=input("chice of yes or no : ")
        match(choice):
            case "yes":
                c=[]
                k=int(input("enter inner list size : "))
                for e in range(k):
                    c.append(eval(input("enter element : ")))
                b.append(c)
            case "no":
                b=eval(input("Enter list outside element : "))
                a.append(b)
    case "no":
        b=eval(input("Enter the list outside element : "))
        a.append(b)
print(a)'''