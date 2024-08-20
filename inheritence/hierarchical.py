class A :
    a, b = 0, 0
    def __init__(self) :
        self.a = int(input("Enter a : "))
        self.b = int(input("Enter b : "))
        print("a + b = {}".format(self.a + self.b))
    
class B(A) :
    def __init__(self) : 
        A.__init__(self)
        print("a - b = {}".format(self.a - self.b))

class C(A) :
    def __init__(self) :
        super().__init__()
        print("a * b = {}".format(self.a * self.b))

bb = B()
cc = C()