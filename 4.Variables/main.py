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