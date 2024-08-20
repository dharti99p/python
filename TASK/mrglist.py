# mother = {"vinubhai","jalpadi","kinjaldi","swetadi"}
# father = {"vinubhai","krishnadi","himanshi","tisha"}
# brother = {"jalpadi","karishma","kinjal","amidi"}
# sister = {"vinubhai","amidi","kano","dharti"}

# mother.update(father,brother,sister)

# print(mother)

# for i in mother :
#     print(i)

mother = set()
father = set()
brother = set()
sister = set()

n =  int(input("enter the set of size : "))

for i in range(1,n+1) :
    mother.add(input("Enter the set of element {} : ".format(i)))

n =  int(input("enter the set of size : "))

for i in range(1,n+1) :
    father.add(input("Enter the set of element {} : ".format(i)))

n =  int(input("enter the set of size : "))

for i in range(1,n+1) :
    brother.add(input("Enter the set of element {} : ".format(i)))

n =  int(input("enter the set of size : "))

for i in range(1,n+1) :
    sister.add(input("Enter the set of element {} : ".format(i)))

print("mother = ",mother)
print("father = ",father)
print("brother = ",brother)
print("sister = ",sister)

mother.update(father,brother,sister)

print(mother)