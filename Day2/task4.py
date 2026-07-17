'''
Task-4: Number Manipulation

Flooring a Number
You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).
int(3.738492) # Becomes 3

Rounding a Number
However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. 
Then you can use the python round() function.
round(3.738492) # Becomes 4
round(3.14159) # Becomes 3
round(3.14159, 2) # Becomes 3.14

Assignment Operators
Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
+=
-=
*=
/=

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.
age = 12
print(f"I am {age} years old")
# Will output I am 12 years old.
'''

# rounding a number
bmi = 84 / 1.65 ** 2
print(bmi) # 30.85399449035813
print(int(bmi)) # 30
print(round(bmi)) # 31
print(round(bmi,2)) # 30.85

# assignment operator
score = 0
score += 1 # same as -=, *=, /=
print(score)

# f-string
score = 5
points = 50
is_wining = True
print(f"Your score = {score}, your points ={points}.\nYou are winning is {is_wining}.")
# also can use print(f'')