import json

# convert from JSON to Python

x = '{"name" : "john", "age" : 30, "city" : "new york"}'

y = json.loads(x)

print(y["age"])

# convert from python to JSON

x = {
    "name" : "json",
    "age" : 30,
    "city" : "new york"
}

y = json.dumps(x)

print(y)

# convert python objecs into JSON strings, and print the values : 

print(json.dumps({"name" : "john", "age" : 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# convert a python object congtaining all the legal data types : 

x = {
    "name" : "john",
    "age" : 30,
    "married" : True,
    "divorced" : False,
    "children"  : ("ann", "billy"),
    "pets" : None,
    "cars" : [
        {
            "model" : "BMW 230", 
            "mpg" : 27.5
        },
        {
            "model" : "ford edge",
            "mpg" : 24.1
        }
    ]
}

print(json.dumps(x))

# use the indent parameter to define the numbers of indents : 
print(json.dumps(x, indent=4))


# ascending order : 
print(json.dumps(x, indent=4, sort_keys=True))