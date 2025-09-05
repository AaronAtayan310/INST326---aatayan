#comment with hashtag

#variables: no command to declare
x = 25 #int
y = "hello there" #string - can be declared with "" or ''
print(x)
print(y)

#Casting: to specify the data type
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Getting the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#example of case sensitive variables:
a = 4
A = "Sally"
#A will not overwrite a

#Examples of valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Can assign multiple variables in same line AND same value to multiple in same line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "F1"
print(x)
print(y)
print(z)

#Lists
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)