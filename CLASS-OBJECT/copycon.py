import copy 

class A :
    a,b = 0 , 0

    def __init__ (self) :
        self.a = int(input("Enter a : "))
        self.b = int(input("Emter b : "))

    def show (self) :
        print("a = {} \nb = {}".format(self.a,self.b))

aa = A()
aa1 = copy.deepcopy(aa)
aa1.show()