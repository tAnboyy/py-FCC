# unordered, mutable, key-value pairs

myDict = {"name": "thanmay", "age": 21, "city": "Mangalore"}
print(myDict)

myDict = dict(name="Thanmay", age=21, city="Mangalore")
print(myDict)

value = myDict["name"]
print(value)

myDict["name"] = "tanboyy"
myDict["email"] = "mdasthanmay@gmail.com"
print(myDict)

# del myDict["email"]
# myDict.pop("age")
myDict.popitem()
print(myDict)

if "name" in myDict:
    print(myDict["name"])
else:
    print("key doesn't exist!")

try:
    print(myDict["address"])
except:
    print("key doesn't exist!")

for key in myDict:
    print(key)

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)

myDictCopy = myDict.copy()
myDictCopy = dict(myDict)

my_dict1 = {"name": "T"}
my_dict2 = {"age": 21}

my_dict1.update(my_dict2)
print(my_dict1)

# int, tuple as key
myDict2 = {1: 10, 2: 20, 3: 30}

tupleKey = (1,2)
myDict3 = {tupleKey: "works"}
print(myDict3)

