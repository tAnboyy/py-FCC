# ordered, immutable, allows duplicate elements

# myTuple = ("Thanmay", 1, 2)
# myTuple = "thanmay", 2  # () optional

myTuple = "thanmay"  # not a tuple, just a string (just py syntax)
# myTuple = ("thanmay", )  # now a tuple
print(type(myTuple))

# myTuple = tuple([1, 2, 3])

print(myTuple)
print(myTuple[-1])

# myTuple[0] = "Tim"  # not possible

for i in myTuple:
    print(i)

if "thanmay" in myTuple:
    print("yep")
else:
    print("nope")

myTuple = ('a', "p", 'p', 'l', 'e')
print(len(myTuple))
print(myTuple.count('p'))
print(myTuple.index('p'))

my_list = list(myTuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)

# slicing works the same way as for lists

# unpacking a tuple
my_tuple3 = "Max", 21, "Mangalore"
name, age, city = my_tuple3
print(name)
print(age)
print(city)

my_tuple4 = 1, 2, 3, 4, 5
i1, *i2, i3 = my_tuple4
print(i1)  # 1
print(i3)  # 5
print(i2)  # [2,3,4]

import sys
my_list = [0, 1, 2, "testing"]
my_tuple = (0, 1, 2, "testing")
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=10000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=10000000))

# tuples more efficient than lists, due to internal optimisations as it's immutable

