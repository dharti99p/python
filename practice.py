'''l=5
b=9
rectangle=l*b
print("area of rectangle ",rectangle)

l=int(input("enter the value l "))
b=int(input("enter the value b "))
rectangle=l*b
print("area of rectangle ",rectangle)

if(b>l):
    print("b is max...")
else:
    print("l is a max...")

l=int(input("enter "))
print("enter l is ",l)
'''

'''a=2
print(a<<2)'''

'''c=0
n=int(input("enter the number "))
for i in range(2,n):
    if(n%i==0):
        c+=1
if(c==2):
    print("not prime")
else:
    print("prime") '''

'''a="weetech it hub"
print(a[::-1])
print(a[3::2])'''

'''a="Hello World"
print(len(a))
print(a[1:5])
print(a[-4:])
b=(a[1:5])
c=(a[-4:])
d=b+c
print(d)'''

#monday 
'''str=""
i=1
a=input("enter the string ")
while(i<len(a)):
    if a[i]==" ":
        i+=2
    str+=a[i]
    i+=1
print(str)'''

#################################################
'''count = 0
a=input("enter the string ")
for i in range (len(a)): 
    if a[i]==" ":
        i+2
    count+=a[i]
    i+=1
print (count)'''


'''count=0
n=input("enter th e string ")
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        a=n%10
        n=n//10
        print(i)
    
for i in s:
    if len(i)%2==0:
        i=(len(i))
        count+=i
        print(count)'''

'''count=1
a=input("enter the string : ")
for i in range(len(a)):
    if(a[i]==" " or a[i]=="\t"):
        count+=1
print(count)
if (a[i]>)'''




'''a=input("enter the string ")
print(len(a))
print(a.upper())
print(a.lower())
print(a.toggle())'''

'''lower=""
a=input("enter the string : ")
for i in range(len(a)):
    if(a[i]>='A' and a[i]<='Z'):
        lower+=chr(ord(a[i])+32)
    else:
        lower+=a[i]
print("lower string : ",lower)'''

'''upper=""
a=input("enter the string : ")
for i in range(len(a)):
    if(a[i]>='a' and a[i]<='z'):
        upper+=chr(ord(a[i])-32)
    else:
        upper+=a[i]
print("upper string : ",upper)'''

'''toggle=""
a=input("enter the string : ")
for i in range(len(a)):
    if(a[i]>='a' and a[i]<='z'):
        toggle+=chr(ord(a[i])-32)
    elif(a[i]>='A' and a[i]<='Z'):
        toggle+=chr(ord(a[i])+32)
    else:
        toggle+=a[i]
print("toggle string : ",toggle)'''

'''a=int(input("enter the number "))
match(a):
    case 10:
        print("12")
    case 11:
        print("12")
    case 12:
        print("12")
    case 13:
        print("13")
    case 50:
        print("50")
    case _:
        print("not available this number")'''

#tuesday
'''a="hello WORLd"
b="SURAT"
c="surat"
d="surat is smart city."
print(a.capitalize())
print(a.count('e'))
print(d.count('smart'))
print(a.index('W'))
print(d.index('smart'))
print(a.find('z'))
print(b.lower())
print(b.casefold())
print(b.swapcase())
print(c.upper())
print(d.split(" "))'''



'''url="   Wee Tech       "
print(url.center(50,'#'))
print(url.lstrip())
print(url.strip())
print(url.rstrip())
print(url.endswith("     "))
print(url.endswith("h"))
print(url.endswith("4"))'''

'''url="www.google.com/?username=WeeTech@gmail.com&password=WeeTech@1234"
#url=input("enter the website ")
a,b=(url.split("?"))
d,e=(b.split("&"))
print(d)
print(e)'''


'''a="hello 😊 "
print(a.encode(encoding="ascii",errors="ignore"))
print(a.encode(encoding="ascii",errors="namereplace"))
print(a.encode(encoding="ascii",errors="xmlcharrefreplace"))
print(a.encode(encoding="ascii",errors="replace"))
print(a.encode(encoding="ascii",errors="backslashreplace"))'''


#wednesday

'''a="google.com"
print(a.endswith("m"))'''

'''a="abc.txt"
print(a.startswith("abc"))
print(a.startswith("b"))'''

'''a="a\tb\tc\t.txt"
print(a.expandtabs(2))'''

'''a="abc.txt"
print(a.replace(".txt",".py"))'''

'''name=input("enter your name : ")
age=int(input("enter your age : "))
a="Hello my self {} & I am {} years old."
print(a.format(name,age))'''

'''a="hello123"
b="hello@123"
print(a.isalnum())
print(b.isalnum())'''

'''a="abc"
print(a.isalpha())'''

'''a=input("enter the symbol ")
print(a.isascii())'''

'''a=(input("enter the number : "))
print(a.isdecimal())'''

'''# subscript
print(u'H\u2082SO\u2084')  # H₂SO₄
  
# superscript
print("x\u00b2 + y\u00b2 = 2")  # x² + y² = 2'''

'''a="1234"
print(a.isdigit())'''

'''a="a_123"
print(a.isidentifier())'''

'''a="123"
print(a.isnumeric())'''

'''a="a*b\t"
print(a.isprintable())'''

'''a=" "
print(a.isspace())'''

'''a="WeeTech It Hub"
for i in a:
    if i.isspace():
        a=a.replace(i,"😍")
print(a)'''

'''a="Wee Tech It Hub"
print(a.istitle())'''

'''a="DHARTI MIROLIYA"
print(a.isupper())'''

'''a="dharti miroliya"
print(a.islower())'''

'''p=["hello","how","are","you"]
a=" ".join(p)
print(a)'''

'''b="om"
a="hello i m"
c=b.ljust(20)
print(c,a)'''

'''b="om"
a="hello i am"
c=b.rjust(10)
print(a,c)'''

'''txt="banana"
x=txt.ljust(20)
print(x,"is my favourite fruit.")'''

#26-08-2023
'''a="WeeTech IT Hub"
x=str.maketrans("H","P")
print(a.translate(x))'''

'''a="weetech it hub"
print(a.partition("it"))'''

'''a="WeeTech It Hub"
print(a.rindex("H"))'''

'''a="WeeTech It Hub"
print(a.rfind("a"))'''

'''a="WeeTech It Hub"
print(a.rpartition("It"))'''

'''a="WeeTech\nIt Hub"
print(a.splitlines())'''

'''a="apple"
print(a.zfill(10))'''

'''a=input("enter the sentens : ")
print(a.replace("is","are"))'''
        
'''a="enter the name"
print(a[::-1])'''

# str=" "
# a="surat is smart city "
# b=a.split(" ")
# for i in range(len(b)):
#     if b[i]==" ":
#         str=b[ : :-1]
#     str+=b[i]
# print(b)
# print(a)
# print(str)

'''a=[1,3.4,"string","5t6j","true"]
for index,value in enumerate(a):
    print("a[{}]:{}".format(index,value))'''

'''a=[]
n=int(input("enter "))
for i in range(n+1):
    a.append(i)
print(a)'''

''' a=[1,3.4,"string","5+6j","true"]
a[a.index("string")]="weeTech"
print(a)'''

# a=[1,3.4,"string","5t6j",True]
# a.insert(2,False)
# print(a)

'''a=[1,3.4,"string","5t6j","true"]
a.clear()
print(a)'''


'''a=["string","string","5t6j","true"]
b=a.count("string")
print(b)'''

'''a=["string","ddd","rrr"]
print(len(a))'''

'''a=[1,3.4,"string","5t6j","true"]
b=a.copy()
a.insert(2,100)
print(b)
print(a)'''


i=1
a=input("enter the string ")
while(i<len(a)):
    if a[i]==" ":
        i+=2
    str+=a[i]
    i+=1
print(str)

#28-08-2023 MONDAY
#29-08-2023 TUESDAY

#a=[1,2,3,[4,5,6,7],8,9,10,[11,12,[14,15,16,17],18],19,20]
#b=a[7]
#c=b[2]
#c[1]=50
#a[7][2][1]=50
#print(a)

'''a=["string","aple","pie",["dsdf","ffddf",["dsdds","rererr",["des","ytr"],56],"rere"]]
a[3][2][2][0]="dm"
print(a)'''

'''dict={"key":"value","key1":"value1","key":"value3"}
print(dict)
print(dict["key1"])'''

'''dict={"foundation":["c lang","cpp lang","java lang"],
        "duration":["1m","20days","1.5m"],
        "fees":["5k","5k","10k"]}
print(dict)
dict["duration"][1]="1m"
print(dict["duration"])'''

'''dict={"foundation":{"basic":["c","cpp","java"],
                    "duration":["1m","1m","1.5m"],
                    "fees":["5k","5k","10k"]},

        "advances":{"basic":["python","d.s","d.a"],
                    "duration":["1m","3m","3m"],
                    "fees":["30k","30k","30k"]},

"robotics":{"robo":["stme","bassic","advance"],
"duration":["3m","3m","3m"],
"fees":["5k","10k","38k"]}}

dict["foundation"]["duration"][2]="2m"
print(dict)'''

'''a=[1,2,1,6,1,7,7,5,6,4,0]
for i in a:
    print("{} repeated {} time ".format(i,a.count(i)))
    for j in a:
        if i in a:
            a.remove(i)
print("{} repeated {} time ".format(a[0],a.count(a[0])))'''

'''a=[1,2,1,6,5,5,7,7,7,7,1]
while len(a)>0:
    k=a[0]
    print("{} repeated {} time ".format(k,a.count(k)))
    for j in a:
        if k in a:
            a.remove(k)'''

'''a=[1,2,1,6,5,5,7,7,7,7,1]
while len(a)>0:
    k=a[0]
    print("{} repeated {} time ".format(k,a.count(k)))
    while k in a:
        a.remove(k)'''


# LIST COMPREHENSION

# f=["1","2","5","6","7"]

# # # n=[int(x)*2 for x in f if int(x)%2==0]

# n=[int(x)*2 if int(x)%2==0 else int(x)*3 for x in f]
# n=[x*2 if x%2==0 else x*3 for x in range(1,10+1)]
# print(n)

# f=f.pop()
# print(f)

# f=()
# print(type(f))