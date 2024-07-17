x = 5 
y = "John"
print(x)
print(y)

x = 5 # x is of type int
x = "Sally" # y is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

""" A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
1.A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4.Variable names are case-sensitive (age, Age and AGE are three different variables)
5.A variable name cannot be any of the Python keywords.
Python keywords
1.False
2.None
3.True
4.and
5.as
6.assert
7.async
8.await
9.break
10.class
11.continue
12.def
13.del
14.elif
15.else
16.except
17.finally
18.for
19.from
20.global
21.if
22.import
23.in
24.is
25.lambda
26.nonlocal
27.not
28.or
29.pass
30.raise
31.return
32.try
33.while
34.with
35.yield
"""

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2mayvar = "John"
my-var = "John"
my var = "John"

"""
There are 3 ways to select a variable:
1.Camel Case
2.Pascal Case
3.Snake Case
"""

#Camel Case
myVariableName = "John"
#Paskal Case
MyVariableName = "John"
#Snake Case
my_variable_name = "John"

#Python Variables - Assign Multiple Values

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana","Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

#Unpack a list:
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)


#Python - Output Variables
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x+y+z)
#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

#Python - Global Variables
"""
Global Variables

1.Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
2.Global variables can be used by everyone, both inside of functions and outside.
"""

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain
as it was, global and with the original value.
"""

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
	x = "fantastic"
	print("Python is " + x)

myfunc()

print("Python is " + x)

"""
The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""

#If you use the global keyword, the variable belongs to the global scope
def myfunc():
	global x
	x = "fantastic"
myfunc()

print("Python is " + x)