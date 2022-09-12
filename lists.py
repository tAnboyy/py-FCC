# ordered, mutable, allows mixed type, allows duplicate elements

myList = ["hi", "Thanmay", 21, True, None]
print(myList)

item = myList[-1]  # last item
print(item)

for val in myList:
    print(val)
    
if "mama" in myList:
    print("yes")
else:
    print("no")

print(len(myList))

anotherList = list()
anotherList.append("appended")
anotherList.insert(1, "inserted")
print(anotherList)

# item = myList.pop()
# item = myList.remove(None)
# myList.clear()
# myList.reverse()
# myList.sort()  # sorts in-place, ie original list changes
# new_list = sorted(myList)  # returns new sorted list, doesn't modify original

myList = [0] * 5
print(myList)

newList = myList + anotherList
print(newList)

# slicing a list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# slicedList = myList[1:5] #[1,5)
# slicedList = myList[:5]
# slicedList = myList[1:]
# slicedList = myList[::2]  # step of 2
slicedList = myList[::-1]  # trick to reverse list
print(slicedList)

# 3 ways to copy a list-
# listCopy = myList.copy()
# listCopy = list(myList)
listCopy = myList[:]

# list comprehension
myList = [1, 2, 3, 4, 5]
myListSquared = [val*val for val in myList]
print(myList)
print(myListSquared)
