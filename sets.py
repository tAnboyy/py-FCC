# unordered, mutable, no duplicates

mySet = {1, 2, 3, 4, 4}
print(mySet)

mySet = set([1, 2, 3, 4])
print(mySet)

mySet = set("Hello")  # trick to find unique characters in a string
print(mySet)

notASet = {}  # is a dict
aSet = set()  # is a set

mySet.add("hey")
print(mySet)

mySet.remove('H')
mySet.discard('e')
# mySet.clear()
print(mySet.pop())  # pops random item
print(mySet)

for i in mySet:
    print(i)

if 'l' in mySet:
    print("yup")
else:
    print("nope")

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

union = odds.union(evens)  # returns a set
print(union)

intersection = odds.intersection(evens)
print(intersection)

intersection2 = odds.intersection(primes)
print(intersection2)

difference = evens.difference(primes)
print(difference)

symmdiff = evens.symmetric_difference(primes)
print(symmdiff)

setA = {1, 2, 4}
setB = {1, 2, 4, 5, 6}

# setA.update(setB)  # modifies setA in-place, adds items of setB to setA
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)
setA.symmetric_difference_update(setB)
print(setA)

print(setA.issubset(setB))
print(setB.issuperset(setA))
print(setA.isdisjoint(setB))  # True if no common elements

# setCopy = mySet.copy()
setCopy = set(mySet)
print(setCopy)

# frozen set - immutable version of set
frozenSet = frozenset([1, 2, 3, 3])
print(frozenSet)
# frozenSet.add(4)  # not possible
# frozenSet.remove(2)  # not possible
# union, intersection, difference works

# wrong commit

