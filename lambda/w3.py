# x = lambda a : a

# print(x(4))


# x = lambda a : a + 3

# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 5))


# x = lambda a, b, c : a + b + c
# print(x(3, 1, 2))


# def myfunc(n) :
#     return lambda a, b : a * b * n

# f1 = myfunc(4)

# print(f1(3, 5))


# def myfunc(n) :
#     return lambda a : a + n

# f1 = myfunc(3)
# f2 = myfunc(4)
# f3 = myfunc(5)

# print("f1 ",f1(2))
# print("f2 ",f2(2))
# print("f3 ",f3(5))

# def my(a) :
#     return lambda a : a
# a1 = my(6)
# print(a1(9))


# cal = lambda num : "even num" if num % 2 == 0 else "odd num"
# print(cal(int(input("Enter the number : "))))


# s = "abdcd"
# print(lambda string : s)


# s = lambda a : "".join([i for i in a if not i.isdigit()])
# s = lambda a : "".join([i for i in a if i.isalpha()]) 
# print(s(input("Enter the alphanum : ")))


# s = lambda a : a + '!'
# print(s(input("Enter the string : ")))


# s = lambda a : sum([int(i) for i in a])
# print(s(input("Enter the number : ")))


# def num(y) :
#     return y * y * y

# x = lambda a : a**3 

# print("def function cube : ",num(int(input("enter the number function : "))))
# print("lambda function cube : ",x(int(input("Enter the  number lambda function : "))))


# x = [1,2,3,4,5,0,-1,-2,-3,55,78]

# print(list(sorted(x, key = lambda x : int(x))))

# print(sorted(x, key = lambda x : int(x)))


# x = [1,2,3,4,5,0,-1,-2,-3,55,78]

# print(list(map(lambda a : str(int(a) + 10),x)))


x = [1,2,3,4,5,0,-1,-2,-3,55,78]

print(list(filter(lambda a : not (int(a) % 2 == 0 and int(a) > 0),x)))