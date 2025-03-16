#type casting

x=str(99)
y=int(99)
z=float(99)
print(x) #str
print(type(x))

print(y) #int
print(type(y))

print(z) #float
print(type(z))

# Multiple value variable
x,y,z="Orange","Banana","Cherry" #x="Orange",y="Banana",z="Cherry"
print(x)
print(y)
print(z)   

# One value to multiple variable
x=y=z="Orange" #x="Orange",y="Orange",z="Orange"
print(x)
print(y)
print(z)

# Output variable
x="Great"
print("Python is "+x)   #Python is great


# only same type of variable can be added
x= "Nirmal " # space is added to make the output more readable
y= "Gajurel"
z= x+y
print(z)   #Nirmal Gajurel

# error after the different type of variable added
# x=5
# y="Nirmal" 
# z=x+y
# print(z)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Multiple value printed using a single print statement
x="Nirmal"
y="Gajurel"
z="is a good boy"
print(x,y,z) #Nirmal Gajurel is a good boy

# best practice is to use comma to separate the variable for output more readable


# Global variable
# Globel variable is created outside the function and can be used inside and outside the function
x="Nirmal"
def myfunc():
    print("The Programmer is "+x)
myfunc()  #Programmer is Nirmal

# Local variable
# if the variable is created inside the function then it is called local variable
def myfunc():
    x="Nirmal"
    print("The Programmer is "+x)
myfunc()  #The Programmer is Nirmal

# if the same name of variable is created inside and outside the function then the local variable is used and globel remains constant throughout the the program. There will be no error

# if the variable is creeated inside with the globel keyword then it is considered as globel variable

def myfunc():
    global x
    x="Nirmal"
myfunc()
print("The Programmer is "+x)  # The Programmer is Nirmal

x="Sujan"
def myfunc():
    global x
    x ="Nirmal"
    print("The Programmer is "+x)
myfunc()
print("The Programmer is "+x)  #The Programmer is Nirmal
# Sujan is overrided by Nirmal due to the assignment of the globel keyword to the x variable inside the function