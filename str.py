# String 
# String is a sequence of characters.

# String is surrounded by either single quotation marks, or double quotation marks. works as same.

# Both the double quotes and single quotes can be used in one string unless the string is not enclosed in the same type of quotes.

# Assign String to a Variable
a= "Nirmal"
print(a)  #Nirmal

# Multiline Strings
# Three double quotes or three single quotes to create a multiline string.
a= """Laborum aliqua anim consequat amet enim esse Lorem ex nostrud aute ea nulla eiusmod.Eu ad esse exercitation occaecat incididunt pariatur ipsum deserunt cillum eiusmod voluptate tempor.Cupidatat occaecat aliquip tempor ullamco anim eu proident veniam ex. Cupidatat nostrud velit adipisicing ut reprehenderit ad et anim ad. Ipsum ea excepteur incididunt aute fugiat officia non quis eiusmod aute reprehenderit. Occaecat enim magna magna mollit ipsum et sint pariatur Lorem deserunt. Minim enim commodo aliqua fugiat. Voluptate nulla in nulla non tempor cillum cupidatat aliqua dolor."""

print(a)  #Laborum aliqua anim consequat amet enim esse Lorem ex nostrud aute ea nulla eiusmod.Eu ad esse exercitation occaecat incididunt pariatur ipsum deserunt cillum eiusmod voluptate tempor.Cupidatat occaecat aliquip tempor ullamco anim eu proident veniam ex. Cupidatat nostrud velit adipisicing ut reprehenderit ad et anim ad. Ipsum ea excepteur incididunt aute fugiat officia non quis eiusmod aute reprehenderit. Occaecat enim magna magna mollit ipsum et sint pariatur Lorem deserunt. Minim enim commodo aliqua fugiat. Voluptate nulla in nulla non tempor cillum cupidatat aliqua dolor.

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
x= "Nirmal"
print(x[0])  #N
print(x[5])  #l

# Looping through a string
for i in x:
    print(i)  #N i r m a l

# String Length
# len() function to return the length of a string.
print(len(x))  #6

# Check String
# in is used to check if a specified phrase or character is present in a string or not and returns True or False accordingly.
txt= "The Programmer is Nirmal"
print("Nirmal" in txt)  #True

# if and if NOT return True or False accordingly.
# if
if "Nirmal" in txt:
    print("Yes, Nirmal is present in the string")  #Yes, Nirmal is present in the string

# if NOT 
if "Sujan" not in txt:
    print("No, Sujan is not present in the string") #No, Sujan is not present in the string

# Slicing
# Slcing is used to get the specific part of the string.
# Specify the start index and the end index, separated by a colon, to return a part of the string.The end index is not included.

name= "Nirmal Gajurel"
print(len(name))  #14
print(name[0:6])  #Nirmal
print(name[7:14])  #Gajurel
print(name[5:8])  #l G
print(name[:6])  #Nirmal
print(name[7:])  #ajurel
print(name[-6:-1])  #ajure

# Modify Strings
# Upper Case
print(name.upper())  #NIRMAL GAJUREL

# Lower Case
print(name.lower())  #nirmal gajurel

# Remove Whitespace
# strip() method removes any whitespace from the beginning or the end.
name= " Nirmal Gajurel     "   
print(name.strip())  #Nirmal Gajurel

# Replace String 
# replace() method replaces a string with another string.
print(name.replace("Gajurel", "Gaju "))  # Nirmal Gaju

# Split String 
# split() method splits the string into substrings if it finds instances of the separator.
print(name.split())  #['Nirmal', 'Gajurel']

# Format String
# format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.
age= 22
txt= "My name is Nirmal and I am {}"
print(txt.format(age))  #My name is Nirmal and I am 22

# f-string
# f-string is used to format the string.
age= 22
txt= f"My name is Nirmal and I am {age}"
print(txt)  #My name is Nirmal and I am 22

# placeholer 2f is used to format the float number upto 2 decimal point.
price = 69
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 69.00 dollars

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# / is used to escape the character.

txt= "We are the so-called \"Vikings\" from the north."
print(txt)  #We are the so-called "Vikings" from the north.

# \t 	Tab 	
# \n 	New Line 	
# \\ 	Backslash 	
# \' 	Single Quote 	
# \r 	Carriage Return 	
# \b 	Backspace 	
# \f 	Form Feed 	
# \ooo 	Octal value 	
# \xhh 	Hex value

# Examples for each of the escape sequences
# Tab
txt = "Hello\tWorld"
print(txt)  # Hello    World

# New Line
txt = "Hello\nWorld"
print(txt)  # Hello
            # World

# Backslash
txt = "This is a backslash: \\"
print(txt)  # This is a backslash: \

# Single Quote
txt = 'It\'s a beautiful day'
print(txt)  # It's a beautiful day

# Carriage Return
txt = "Hello\rWorld"
print(txt)  # World

# Backspace
txt = "Hello\bWorld"
print(txt)  # HellWorld

# Form Feed
txt = "Hello\fWorld"
print(txt)  # Hello
            #      World

# Octal value
txt = "\110\145\154\154\157"
print(txt)  # Hello

# Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)  # Hello


# String Methods
# Method    	    Description
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle() 	    Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()           Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

# Examples for each of the string methods with a brief description

# capitalize() - Converts the first character to upper case
txt = "hello world"
print(txt.capitalize())  # Hello world

# casefold() - Converts string into lower case
txt = "HELLO WORLD"
print(txt.casefold())  # hello world

# center() - Returns a centered string
txt = "hello"
print(txt.center(20))  # '       hello       '

# count() - Returns the number of times a specified value occurs in a string
txt = "hello world"
print(txt.count("l"))  # 3

# encode() - Returns an encoded version of the string
txt = "hello world"
print(txt.encode())  # b'hello world'

# endswith() - Returns true if the string ends with the specified value
txt = "hello world"
print(txt.endswith("world"))  # True

# expandtabs() - Sets the tab size of the string
txt = "hello\tworld"
print(txt.expandtabs(4))  # 'hello   world'

# find() - Searches the string for a specified value and returns the position of where it was found
txt = "hello world"
print(txt.find("world"))  # 6

# format() - Formats specified values in a string
txt = "My name is {name} and I am {age}"
print(txt.format(name="Nirmal", age=22))  # My name is Nirmal and I am 22

# format_map() - Formats specified values in a string
txt = "My name is {name} and I am {age}"
print(txt.format_map({"name": "Nirmal", "age": 22}))  # My name is Nirmal and I am 22

# index() - Searches the string for a specified value and returns the position of where it was found
txt = "hello world"
print(txt.index("world"))  # 6

# isalnum() - Returns True if all characters in the string are alphanumeric
txt = "hello123"
print(txt.isalnum())  # True

# isalpha() - Returns True if all characters in the string are in the alphabet
txt = "hello"
print(txt.isalpha())  # True

# isascii() - Returns True if all characters in the string are ascii characters
txt = "hello"
print(txt.isascii())  # True

# isdecimal() - Returns True if all characters in the string are decimals
txt = "12345"
print(txt.isdecimal())  # True

# isdigit() - Returns True if all characters in the string are digits
txt = "12345"
print(txt.isdigit())  # True

# isidentifier() - Returns True if the string is an identifier
txt = "hello"
print(txt.isidentifier())  # True

# islower() - Returns True if all characters in the string are lower case
txt = "hello"
print(txt.islower())  # True

# isnumeric() - Returns True if all characters in the string are numeric
txt = "12345"
print(txt.isnumeric())  # True

# isprintable() - Returns True if all characters in the string are printable
txt = "hello"
print(txt.isprintable())  # True

# isspace() - Returns True if all characters in the string are whitespaces
txt = "   "
print(txt.isspace())  # True

# istitle() - Returns True if the string follows the rules of a title
txt = "Hello World"
print(txt.istitle())  # True

# isupper() - Returns True if all characters in the string are upper case
txt = "HELLO"
print(txt.isupper())  # True

# join() - Joins the elements of an iterable to the end of the string
txt = ["hello", "world"]
print(" ".join(txt))  # hello world

# ljust() - Returns a left justified version of the string
txt = "hello"
print(txt.ljust(10))  # 'hello     '

# lower() - Converts a string into lower case
txt = "HELLO"
print(txt.lower())  # hello

# lstrip() - Returns a left trim version of the string
txt = "   hello"
print(txt.lstrip())  # 'hello'

# maketrans() and translate() - Returns a translation table to be used in translations
txt = "hello world"
trans = txt.maketrans("h", "j")
print(txt.translate(trans))  # jello world

# partition() - Returns a tuple where the string is parted into three parts
txt = "hello world"
print(txt.partition(" "))  # ('hello', ' ', 'world')

# replace() - Returns a string where a specified value is replaced with a specified value
txt = "hello world"
print(txt.replace("world", "Python"))  # hello Python

# rfind() - Searches the string for a specified value and returns the last position of where it was found
txt = "hello world world"
print(txt.rfind("world"))  # 12

# rindex() - Searches the string for a specified value and returns the last position of where it was found
txt = "hello world world"
print(txt.rindex("world"))  # 12

# rjust() - Returns a right justified version of the string
txt = "hello"
print(txt.rjust(10))  # '     hello'

# rpartition() - Returns a tuple where the string is parted into three parts
txt = "hello world"
print(txt.rpartition(" "))  # ('hello', ' ', 'world')

# rsplit() - Splits the string at the specified separator, and returns a list
txt = "hello world"
print(txt.rsplit())  # ['hello', 'world']

# rstrip() - Returns a right trim version of the string
txt = "hello   "
print(txt.rstrip())  # 'hello'

# split() - Splits the string at the specified separator, and returns a list
txt = "hello world"
print(txt.split())  # ['hello', 'world']

# splitlines() - Splits the string at line breaks and returns a list
txt = "hello\nworld"
print(txt.splitlines())  # ['hello', 'world']

# startswith() - Returns true if the string starts with the specified value
txt = "hello world"
print(txt.startswith("hello"))  # True

# strip() - Returns a trimmed version of the string
txt = "   hello   "
print(txt.strip())  # 'hello'

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
txt = "Hello World"
print(txt.swapcase())  # hELLO wORLD

# title() - Converts the first character of each word to upper case
txt = "hello world"
print(txt.title())  # Hello World

# translate() - Returns a translated string
txt = "hello world"
trans = txt.maketrans("h", "j")
print(txt.translate(trans))  # jello world

# upper() - Converts a string into upper case
txt = "hello"
print(txt.upper())  # HELLO

# zfill() - Fills the string with a specified number of 0 values at the beginning
txt = "42"
print(txt.zfill(5))  # 00042

