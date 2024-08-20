import re

# # starts with "The" and ends with "spain" : 

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x : 
#     print("YES! we have a match!")
# else :
#     print("no match")

# # findall() function : 

# txt = "The rain in Spain"
# x = re.findall("ai", txt)

# print(x)

# # search() function : 

# txt = "The rain in Spain"  #t=0 h=1 e=2 space=3
# x = re.search("\s", txt)

# print("The first white-space character is located in position : ", x.start())

# # spilt() function : 

# txt = "The rain in Spain" 
# x = re.split("\s", txt)
# print(x)\

# # sub() function : 

# txt = "The rain in Sapin"
# x = re.sub("\s", "9", txt)
# print(x)

# # Metacharacters

# txt = "The rain in Spain"
# x = re.findall("[a-m]",txt) # A set of characters
# print(x)


# txt = "That will be 59 dollars"
# x = re.findall("\d", txt) # Find all digit characters
# print(x)


# txt = "hello planet"
# x = re.findall("he..o",txt) # search for a sequence that starts with "he", followed by two (any) characters, and an "o"
# print(x)


# txt = "hello planet"
# x = re.findall("^hello", txt) # check if the string starts with 'hello'
# if x :
#     print("yes, the sring starts with 'hello'")
# else :
#     print("no match")


# x = re.findall("planet$",txt) # check if the string ends with 'planet' 
# if x :
#     print("yes, the string ends with 'planet'")
# else :
#     print("No match")


# txt = "hello planet"
# x = re.findall("he.*o",txt) # zero or more occurences
# print(x)


# x = re.findall("he.+o",txt) # serach fo a sequence that starts with "he", followed by 1 or more (any) characters, and an "o"
# print(x)


# x = re.findall("he.?o",txt) # serach for a sequence that starts with "he" , followed by 0 or 1(any) character, and an "o"
# print(x) # this time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


# x = re.findall("he.{2}o",txt) #  search for a sequence that starts with "he" , followed excactly 2 (any) charachters, and an "o"
# print(x)


# txt = "The rain in Spain falls mainly in the plain!"
# x = re.findall("falls | stays", txt) # check if the string contains either "falls" or "stays"
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")
# # () capture and group


# # SPECIAL SEQUENCES

# # \A returns a match if the specified characters are at the beginnin of the string : 

# txt = "The rain in Spain"
# x = re.findall("\AThe",txt)
# print(x)
# if x :
#     print("Yes, there is a match!")
# else :
#     print("No match")


# # check if 'ain' is present at the beginning of a word :

# x = re.findall(r"\bain",txt)
# print(x)
# if x :
#     print("Yes, there is at least one match!")
# else :
#     print("no match")


# # check if "ain" is present at the end of a WORD :

# x = re.findall(r"ain\b",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # check if "ain" is present, but NOT at the beginning of a word :

# x = re.findall(r"\Bain",txt)
# print(x)
# if x :
#     print("yes, there is at lats one match!")
# else :
#     print("no match")


# # check if "ain" is present, but NOT at the end of a word :

# x = re.findall(r"ain\B",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # check if the string contains any digits(numbers from 0 -9) :

# x = re.findall("\d",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # return a match at every no-digit character :

# x = re.findall("\D",txt)
# print(x)
# if x :
#     print("yez, there is at least one match!")
# else :
#     print("no match")


# # return a match at every white-space charcter :

# x = re.findall("\s",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # return a match at every NON white-space character :

# x = re.findall("\S",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # return a match at every word character (characters from a to Z, digits from 0 - 9, and the underscore _ character) :

# x = re.findall("\w",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.) :

# x = re.findall("\W",txt)
# print(x)
# if x :
#     print("yes, there is at least one match!")
# else :
#     print("no match")


# # Check if the string ends with "Spain":

# x = re.findall("Spain\Z", txt)
# print(x)
# if x :
#     print("yes, there is a match!")
# else :
#     print("no match")



# Sets :


# check if the string has any a, r, or n characters :

txt = "The rain in Spain"
x = re.findall("[arnS]", txt)
print(x)
if x :
    print("yes, there is at least one match!")
else :
    print("no match")


# check if the string has any charcters between a and n :

x = re.findall("[a-n]",txt)
print(x)
if x :
    print("yes, there is at least one match!")
else :
    print("no match")


# check if the string has other characters than a, r, or n :

x = re.findall("[^arn]",txt)
print(x)
if x :
    print("yes there is at leastone match!")
else :
    print("no match")


# check if the string has any 0, 1, 2, or 3 digits :

x = re.findall("[0123]",txt)
print(x)
if x :
    print("yes there is at leastone match!")
else :
    print("no match")


# check if the string has any digits :

x = re.findall("[0-9]",txt)
print(x)
if x :
    print("yes there is at leastone match!")
else :
    print("no match")


# check if the string hs any two-digit numbers, from 00 to 59 :

x = re.findall("[0-5][0-9]",txt)
print(x)
if x :
    print("yes there is at leastone match!")
else :
    print("no match")


# check if the string has any characters from a to z lower case, and A to Z upper case :

x = re.findall("[a-zA-Z]",txt)
print(x)
if x :
    print("yes there is at leastone match!")
else :
    print("no match")


# in sets, +, *, ., |, (), $, {} has no special meaning, so [+] means: return a match for any + character in the string :

x = re.findall("[+]",txt)
print(x)
if x :
    print("yes, there is at least one match!")
else :
    print("no match")