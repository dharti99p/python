print("You choice number : \n1.sum \n2.sub\n3.multiplication\n4.divided\n5.squre\n6.cube\n")

ch=int(input("Enter the your choice number : "))

match ch :

    case 1 :
        def sum(a, b) :
            print("a + b = {}".format(a + b))

    case 2 :
        def sub(a, b) :
            print("a - b = {}".format(a - b))

    case 3 :
        def mul(a, b) :
            print("a * b = {}".format(a * b))

    case 4 :
        def div(a, b) : 
            print("a / b = {}".format(a / b))

    case 5 :
        def squre(a) :
            print("a * a = {}".format(a**2))

    case 6 :
        def cube(a) :
            print("a * a * a = {}".format(a**3))

if __name__ == "__main__" :
    x = int(input("Enter the x : "))
    y = int(input("Enter the y : "))
    sum(x, y)
    sub(x, y)
    mul(x, y)
    div(x, y)
    squre(x)
    cube(x)