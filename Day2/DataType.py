#subscripting
print("Hello Belete"[0])  # this will pring the first letter. Remember space also count as a character

#   string
username ="Belete"

# int

age = 30
large_int= 125_235_56
print(large_int) # will print 12523556. Underscore is to make the large number more readable

# float or double is any decimal points

float_num=3.5
float_lnum = 734_675.76

print(float_lnum)

# Boolean : is either True or False

isTrue= True
isfalse = False

print(isfalse)


#TypeError
#len(123456) # This will fail as type error becuase the len() function is only works string
len("123456") # is a fix
#len()
#Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range)
# or a collection (such as a dictionary, set, or frozen set).


# Type Conversion
# You can convert data into different data types using special functions. e.g.
#
# float()
#
# int()
#
# str()
#
#  Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))
#

name = input("Enter your name: ")
length=len(name)
print(type(length))

print("Number of letters in your name: " + str(length))


