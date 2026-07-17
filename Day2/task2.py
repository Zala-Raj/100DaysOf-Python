'''
Task-2: Type Error, Checking and Conversion

Type Error
These errors occur when you are using the wrong data type. e.g. len(12345)
Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

PAUSE 1. Fix the len() function so it has no more warnings or errors.
Type Checking
You can check the data type of any value or variable in python using the type() function.
print(type("abc")) #will give you <class 'str'>

PAUSE 2. Write out 4 type checks to print all 4 data types
Using the type() and print() functions to print out 4 lines into the output area so we get the full collection of data types that we learnt about. <class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

Type Conversion
You can convert data into different data types using special functions. e.g.
float()
int()
str()

PAUSE 3. Make this line of code run without errors
print("Number of letters in your name: " + len(input("Enter your name")))
'''

# type error - len(12345)

# type checking
print(type("Hello World")) # output: <class 'str'>
print(type(123)) # output: <class 'int'>
print(type(3.14)) # output: <class 'float'>
print(type(True)) # output: <class 'bool'>

# type conversion
print(int("123") + int("345")) # output: 468

# solving error
name = len(input("Enter your name:"))
print("Number of letters in your name: " + str(name)) 

# only string + string is possible