# Data types in Python.

# Built-in Data Types

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview    #new for me...
# None Type: 	NoneType


# Getting the Data Type
# Text Type
text = "Hello, World!"
print(type(text))  # <class 'str'>

# Numeric Types
integer = 10
print(type(integer))  # <class 'int'>

floating = 10.5
print(type(floating))  # <class 'float'>

complex_num = 1 + 2j
print(type(complex_num))  # <class 'complex'>

# Sequence Types
list_example = [1, 2, 3]
print(type(list_example))  # <class 'list'>

tuple_example = (1, 2, 3)
print(type(tuple_example))  # <class 'tuple'>

range_example = range(5)
print(type(range_example))  # <class 'range'>

# Mapping Type
dict_example = {"name": "Alice", "age": 25}
print(type(dict_example))  # <class 'dict'>

# Set Types
set_example = {1, 2, 3}
print(type(set_example))  # <class 'set'>

frozenset_example = frozenset({1, 2, 3})
print(type(frozenset_example))  # <class 'frozenset'>

# Boolean Type
bool_example = True
print(type(bool_example))  # <class 'bool'>

# Binary Types
bytes_example = b"Hello"
print(type(bytes_example))  # <class 'bytes'>

bytearray_example = bytearray(5)
print(type(bytearray_example))  # <class 'bytearray'>

memoryview_example = memoryview(bytes(5))
print(type(memoryview_example))  # <class 'memoryview'>

# None Type
none_example = None
print(type(none_example))  # <class 'NoneType'>


# Setting the Data Type
# Text Type
text = str("Hello, World!")
print(type(text))  # <class 'str'>

# Numeric Types
integer = int(10)
print(type(integer))  # <class 'int'>

floating = float(10.5)
print(type(floating))  # <class 'float'>

complex_num = complex(1, 2)
print(type(complex_num))  # <class 'complex'>

# Sequence Types
list_example = list([1, 2, 3])
print(type(list_example))  # <class 'list'> 

tuple_example = tuple((1, 2, 3))
print(type(tuple_example))  # <class 'tuple'>

range_example = range(5)
print(type(range_example))  # <class 'range'>

# Mapping Type
dict_example = dict(name="Alice", age=25)
print(type(dict_example))  # <class 'dict'>

# Set Types
set_example = set([1, 2, 3])
print(type(set_example))  # <class 'set'>

frozenset_example = frozenset([1, 2, 3])
print(type(frozenset_example))  # <class 'frozenset'>

# Boolean Type
bool_example = bool(True)
print(type(bool_example))  # <class 'bool'>

# Binary Types
bytes_example = bytes("Hello", "utf-8")
print(type(bytes_example))  # <class 'bytes'>

bytearray_example = bytearray(5)
print(type(bytearray_example))  # <class 'bytearray'>

memoryview_example = memoryview(bytes(5))
print(type(memoryview_example))  # <class 'memoryview'>

# None Type
none_example = type(None)()
print(type(none_example))  # <class 'NoneType'>

# Note: The type() function is used to get the data type of an object. The object can be any value, function, or class. The type() function returns the type of the object.

# Python Numbers

# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

# Type Conversion
x = 5    # int
y = 2.8  # float    
z = 5j   # complex

a= float(x)  # 5.0
b= int(y)    # 2
c= complex(x)  # (5+0j)

print(a)
print(b)   
print(c)

# Cant convert complex to another number
# a= int(z)  #TypeError: can't convert complex to int
# print(a)


# Random Number generation
import random
a= random.randrange(1,10); #random number between 1 to 10
print(a)