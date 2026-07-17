'''
Task-3: Mathematical Operations

Basic Operators
Learn to use the basic mathematical operators, +, -, *, /, // and **

PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

PAUSE 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

PAUSE 2. Change the code so it outputs 3?
print(3 * 3 + 3 / 3 - 3)
'''

print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)   # float - 2.0      e.g. 5/3 = 1.66
print(6 // 3) # integer - 2     e.g. 5/3 = 1
print(2**2)  # power - 2^2 = 4

# PEMDAS - left to right
print(3 * 3 + 3 / 3 - 3)

# to make output 3
print(3 * 3 + 3 / 3 - 3 - 4)     # 9+1-7=3
print(3 * (3 + 3) / 3 - 3)       # (3*6)/3 - 3 = 3