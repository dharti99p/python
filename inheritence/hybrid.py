class A :
    a, b = 0, 0

    def __init__ (self) :
        self.a = int(input("Enetr a : "))
        self.b = int(input("Enter b : "))
        
        print("a + b = {}".format(self.a + self.b))

class B(A) :
    def __init__(vc) :
        A.__init__(vc)
        print("a - b = {}".format(vc.a - vc.b))

class C(A) :
    def __init__(xyz) :
        A.__init__(xyz)
        print("a * b = {}".format(xyz.a * xyz.b))

class D(B, C) :
    def __init__(abc) :
        B.__init__(abc)
        C.__init__(abc)
        print("a / b = {}".format(abc.a / abc.b))

dd = D()