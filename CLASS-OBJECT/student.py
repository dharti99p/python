class student :
    rn, nm, std, div, marks, total, per = 0, '', 0, '', [], 0, 0

    def set(self):
        self.marks = []
        self.rn = (int(input("Enter the student roll no : ")))
        self.nm = (input("Enter the student name : "))
        self.std = int(input("Enter the student standard : "))
        self.div = input("Enter the student division : " )
        
        n = int(input("Enter the number of subject : "))
        for i in range(n) : 
            shivay.marks.append(eval(input("subject marks : ")))
        shivay.total = sum(shivay.marks)
        shivay.per = shivay.total/n

    def show(self) :
        print(" Name  : {} Roll no : {} Std : {} Division : {} Marks : {} Total : {} Per : {}".format(self.nm, self.rn, self.std, self.div, self.marks, self.total, self.per))

shivay = student()
shivay.set()
shivay.show()