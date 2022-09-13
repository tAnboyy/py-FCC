# ordered, immutable

myString = 'Thanmay here'  # ''/"" either works
print(myString)

multilineStr = """hey this \
works"""
print(multilineStr)

print(myString[0])

substring = myString[:3:-1]
print(substring)

firstname = "thanmay"
lastname = 'das'
name = firstname + " " + lastname
print(name)

for char in myString:
    print(char)

if 'may' in myString:
    print("yes")
else:
    print("no")

myString = "      whitespace"
myString = myString.strip(' ')  # returns new string bc strings are immutable
print(myString)

print(myString.upper())
print(myString.lower())
print(myString.startswith('H'))
print(myString.endswith('e'))

print(myString.find('x'))
print(myString.count('h'))
print(myString.replace('white', "black"))

myString = "convert into a list"
myList = myString.split()  # " " is the default delimiter

myString2 = "convert,into,a,list"
myList2 = myString2.split(",")
print(myList2)

newString = ' '.join(myList)
print(newString)

my_list = ['a'] * 1000000

# bad py code - since strings are immutable, new string objects created each time
from timeit import default_timer as timer

start = timer()
my_string = ''
for char in my_list:
    my_string += char
stop = timer()
# print(my_string)
print(stop - start)

# good py code
start = timer()
my_string = ''.join(my_list)
stop = timer()
# print(my_string)
print(stop - start)

# string formatting
# %s/d/f/.2f, .format(), f strings
fl = 2 / 7
st = "great"
formattedStr = "the variable is %f" % fl
print(formattedStr)

# formattedStr = "the variable is {}".format(var)
formattedStr = "the variables are {:.2f} and {}".format(fl, st)
print(formattedStr)

print(f"the variables are {fl * 2} and {st}")  # faster, evaluated at runtime, most used
