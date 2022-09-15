import random

# pseudo random numbers (reproducible)
a = random.random()  # random float between 0 and 1
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10)  # includes upper bound
a = random.randrange(1, 10)  # excludes upper bound

mylist = list("ABCDEFG")
a = random.choice(mylist)
print(a)

a = random.sample(mylist, 3)  # unique elements
print(a)
a = random.choices(mylist, k=3)  # allows duplicates
print(a)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(1)  # re-seed
print(random.random())
print(random.randint(1, 10))

# for security purposes, avoid random
import secrets  # used for passwords, security tokens, acc authentication.. generates truly random numbers

a = secrets.randbelow(10)  # exclusive upper bound
print(a)

a = secrets.randbits(4)  # 0000 - 1111
print(a)

a = secrets.choice(mylist)
print(a)

# for arrays of random numbers
import numpy as np

a = np.random.rand(3)
a = np.random.rand(3, 3)
a = np.random.randint(0, 10, 3)
a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr)

np.random.seed(1)  # works same as random.seed()



