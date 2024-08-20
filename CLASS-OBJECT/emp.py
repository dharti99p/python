class emp :
    id, nm, phoneno, email, role, salary, total, da, hra, ra, = 0, '', 0, '', '', 0, 0.0, 0, 0, 0

    def set (self) :
        self.id = int(input("Enter the emp id : ")) 
        self.nm = input("Enter the emp name : ")
        self.phoneno = int(input("Enter the emp mobile no : ")) 
        self.email = input("Enter the emp email : ")
        self.role = input("Enter the emp role : ") 
        self.salary = int(input("Enter the emp salary : "))
        self.da = self.salary * 0.4
        self.hra = self.salary * 0.2
        self.ra = self.salary * 0.1
        self.total = self.salary + self.da + self.hra + self.ra

    def display(self) :
        print("\n Employee id : {} \n Employee name : {} \n Employee phone no : {} \n Employee email : {}\n Employee role : {}\n Employee salary : {}\n Employee da : {}\n Employee hra : {}\n Employee ra : {}\n Employee total salary : {}".format(self.id, self.nm, self.phoneno, self.email, self.role, self.salary, self.da, self.hra, self.ra, self.total))

e = emp()
e.set()
e.display()