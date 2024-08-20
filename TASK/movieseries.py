print("   Menu drive system of Movie and Web Series   ")
movies=[]
webseries=[]
a=int(input("1.MOVIE  \n2.WEBSERIES \nEnter the choice : "))
match(a):
    case 1:
        print("You choice MOVIES")
        n=int(input("Enter the range of MOVIES : "))
        for i in range(1,n+1):
            print(i,end=" ")
            m=input("Enter the MOVIE name : ")
            movies.append(m)
        print(movies)
    case 2:
        print("You choice WEBSERIES")
        n=int(input("Enter the range of WEBSERIES : "))
        for i in range(1,n+1):
            print(i,end=" ")
            w=input("Enter the WEBSERIES name : ")
            webseries.append(w)
        print(webseries)

while 1:
    print('   Enter the choice   ')
    print("1.add list")
    print("2.remove list")
    print("3.sort list")
    print("4.new add list")
    print("5.extend list")
    print("6.count list")
    print("7.exit list")
    
    x=int(input("Enter your choice : "))
       
    match x:
        case 1:
            print("1.MOVIE  \n2.WEBSERIES")
            b=int(input("Enter the Choice : "))

            z="ADD LIST"
            print(z.center(100,"-"))
            match b:
                case 1:
                    print("You choice MOVIES ")
                    n=int(input("Enter the add MOVIE number : "))
                    for i in range(1,n+1):
                        print(i,end=" ")
                        m=input("Enter the add MOVIE name : ")
                        movies.insert(0,m)
                    print(movies)
                case 2:
                    print("You choice WEBSERIES")
                    n=int(input("Enter the add WEBSERIES number : "))
                    for i in range(1,n+1):
                        print(i,end=" ")
                        w=input("Enter the add WEBSERIES name : ")
                        webseries.insert(0,w)
                    print(webseries)
        case 2:
            print("1.MOVIE  \n2.WEBSERIES")
            b=int(input("Enter the Choice : "))

            z="REMOVE LIST"
            print(z.center(100,"-"))
            
            match b:
                case 1:
                    print("You choice MOVIES ")
                    m=input("Enter the delete MOVIE name : ")
                    movies.remove(m)
                    print(movies)
                case 2:
                    print("You choice WEBSERIES")
                    w=input("Enter the delete WEBSERIES name : ")
                    webseries.remove(w)
                    print(webseries)
        case 3:
            print("1.MOVIE  \n2.WEBSERIES")
            b=int(input("Enter the Choice : "))

            z="SORT LIST"
            print(z.center(100,"-"))
            
            match b:
                case 1:
                    print("You choice MOVIES ")
                    movies.sort()
                    print(movies)
                case 2:
                    print("You choice WEBSERIES")
                    webseries.sort(reverse=True)
                    print(webseries)
        case 4:
            print("1.MOVIE  \n2.WEBSERIES")
            b=int(input("Enter the Choice : "))

            z="NEW ADD LIST"
            print(z.center(100,"-"))
        
            match b:
                case 1:
                    print("You choice MOVIES ")
                    n=int(input("Enter the new add MOVIE number : "))
                    for i in range(1,n+1):
                        print(i,end=" ")
                        m=input("Enter the add MOVIE name : ")
                        movies.insert(0,m)
                    print(movies)
                case 2:
                    print("You choice WEBSERIES")
                    n=int(input("Enter the new add WEBSERIES number : "))
                    for i in range(1,n+1):
                        print(i,end=" ")
                        w=input("Enter the add WEBSERIES name : ")
                        webseries.insert(0,w)
                    print(webseries)   
        case 5:
            z="EXTEND LIST"
            print(z.center(100,"-")) 
            movies.extend(webseries)
            print(movies)    
        case 6 :
            print("1.MOVIES\n2.WEBSERIES")
            b=int(input("Enter the choice : "))

            z="COUNT LIST"
            print(z.center(100,"-"))

            match b:
                case 1:
                    print("You choice MOVIES : ")
                    print(len(movies))
                case 2:
                    print("You choice WEBSERIES : ")
                    print(len(webseries))
        case 7:
            z="You are EXIT"
            print(z.center(100,"-"))
            break