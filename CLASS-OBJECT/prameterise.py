class A :
    a, b = 0, 0 

    def __init__(self,a,b) :
        self.a = a
        self.b = b

    def show(abc) :
        print("a = {}\nb = {}".format(abc.a,abc.b))

aa = A(10,29)
x = int(input("Enter x : "))
y = int(input("Enter y : "))
aa1 = A(x,y)
aa1.show()
