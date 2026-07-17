'''
Task-6: Band Name Generaor Project

Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.

Hint 1
You can use String Concatenation to combine strings with variables too! 
e.g. print("My name is " + name)
Make sure the input cursor shows on a new line:

Hint 2
Think about how you used \n to add a new line to a string. 
Try putting it in some different places in your code until it does what you expect. 
Note, when you click into the output area you will be able to click on the end of the line as well as the new line. 
See the video solution for how it looks on my system.
'''

# prints greeting
print("Welcome to the Band Name Generator.")

# prints the name of the city
city = input("What's the name of the city you grew up in?\n")

# prints the name of the pet
pet = input("What's your pet's name?\n")

# prints the name of the band
print("Your band name could be " + city + " " + pet)

'''
Demo
https://appbrewery.github.io/python-day1-demo/
'''