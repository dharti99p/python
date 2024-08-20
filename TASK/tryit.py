# list = ["apple","banana","kiwi","mango"]
# s = "surat is smart city"
# myit = iter(list)

# print(next(myit))
# print(next(myit))


class number:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if(self.a <= 100):
            x=self.a
            self.a+=1
            return x
        else:
            print("Don't Do This Type Of Error In COde")


y = number()
z = iter(y)

for i in z:
    print(i)