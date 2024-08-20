# f = open("D:\Python\Programs\FILE HANDLING\dm.txt", 'a')
 
# print(f.read())

# print(f.read(3))

# print(f.readline())

# print(f.readlines())

# for x in f :
#     print(x)

# print(f.readline())
# f.close()


f = open("D:\Python\Programs\FILE HANDLING\dm.txt",'a')

f.write("Now the file has more content!")
f.close()

f = open("D:\Python\Programs\FILE HANDLING\dm.txt",'r')
print(f.read())