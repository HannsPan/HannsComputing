##### VARIABLES ######
# x = 10 # integer variable
# y = 20
# z = x + y
# print(z)

# different variables have different types
var1 = "hanns" # string variable
var2 = "23234"

var3 = 10
var4 = 20
var5 = var3 + var4 # integer variables will add
print(var5)

var6 = var1 + var2 # 2 string variable will join/ concatenate
print(var6)

print(str(var5) + var6)

#type conversion
# int() str()

'''
# Exercise 1: Variable Assignment
# Assign a value to a variable and print it.
# Example input: x = 5
# Expected output: 5
'''
# Write your code here
x = 5
print(5)

'''
# Exercise 2: String Assignment
# Assign a string to a variable and print it.
# Example input: name = 'Alice'
# Expected output: Alice
'''
# Write your code here
name = "Alice"
print(name)

'''
# Exercise 3: Integer Addition
# Assign values to two integer variables, add them, and print the result.
# Example input: a = 3, b = 4
# Expected output: 7
'''
# Write your code here
a = 3
b = 4
print(a+b)

'''
# Exercise 4: String Concatenation
# Assign values to two string variables, concatenate them, and print the result.
# Example input: first_name = 'John', last_name = 'Doe'
# Expected output: John Doe
'''
# Write your code here
first_name = "John"
last_name = "Doe"
print(first_name + " " +last_name)

'''
# Exercise 5: String and Integer Formatting
# Format a string to include variables for a user's name and age.
# Example input: name = 'John', age = 30
# Expected output: Hello, John. You are 30 years old.
'''
# Write your code here
# name = input("Please enter the person's name: ")
# age = input("Please enter the person's age: ")
# print("Hello, {}. You are {} years old.".format(name, age))


#### print string formatting
#print("Hello", name, "You are", age, "years old")
#print("Hello,{}. You are {} years old.".format(name, age))
#print(f"Hello,{name}. You are {age} years old.")

'''
# Exercise 6: Variable Reassignment
# Reassign a variable's value and print both the old and new values.
# Example input: x = 5, x = x + 3
# Expected output: 5, 8
'''
# Write your code here
x = 5
print(x)
y = x + 3
print(x, y) # /n

# for i in range(10):
#     print(i, end = " " )


'''
# Exercise 7: Define and Use a Constant
# Define a constant for the value of pi and use it to calculate the 
# circumference of a circle with radius 5.
# Example input: PI = 3.14159, radius = 5
# Expected output: Circumference is 31.4159
'''
# Write your code here
# 2 x pi x r
# PI = 3.14159
# radius = int(input("Enter Radius: "))
# circumfrence = 2 * PI * radius
# print("Circumfrence is {}" .format(circumfrence))

'''
# Exercise 8: Using Input Function
# Prompt the user to enter their name and print a greeting message.
# Example input: (user inputs 'Alice')
# Expected output: Hello, Alice!
'''
# Write your code here
# name = input("Please enter your name: ")
# print("Hello, {}!" .format(name))

'''
# Exercise 9: String Length
# Assign a string to a variable and print its length.
# Example input: text = 'Hello, world!'
# Expected output: The length of the string is 13
'''
# Write your code here

# text = input("Please input a text: ")
# print("The length of the strng is {}".format(len(text)))


'''
# Exercise 10: Calculate Sum of Three Numbers
# Assign values to three integer variables, calculate their sum, and print the result.
# Example input: a = 2, b = 4, c = 6
# Expected output: 12
'''
# Write your code here
# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# c = int(input("Input third number: "))
# print(a + b + c)


################################################################
## BOOLEAN ###

'''
# Exercise 1: Boolean Assignment
# Assign a boolean value to a variable and print it.
# Example input: is_student = True
# Expected output: True
'''
# Write your code here


'''
# Exercise 2: Simple if Statement
# Use an if statement to check if a number is positive.
# Example input: number = 5
# Expected output: 'The number is positive.'
'''
# Write your code here
# number = int(input("Please input a number: "))

# if number > 0:
#     print("{} is a positive number." .format(number))
# elif number == 0:
#     print("{} is zero." .format(number))
# else:
#     print("{} is a negative number." .format(number))


'''
# Exercise 3: if-else Statement
# Use an if-else statement to check if a number is positive or negative.
# Example input: number = -3
# Expected output: 'The number is negative.'
'''
# Write your code here
# number = int(input("Enter the number: "))
# if number > 0:
#     print("It's a positive number")
# elif number == 0:
#     print("It's zero")
# else:
#     print("It's a negative number")

'''
# Exercise 4: if-elif-else Statement
# Use an if-elif-else statement to check if a number is positive, negative, or zero.
# Example input: number = 0
# Expected output: 'The number is zero.'
'''
# Write your code here


'''
# Exercise 5: Boolean Comparison
# Assign values to two variables and use a boolean comparison to check if they are equal.
# Example input: a = 10, b = 10
# Expected output: 'a and b are equal.'
'''
# Write your code here
# a = int(input("Enter a number: "))
# b = int(input("Enter the other number: "))
# if a == b:
#     print("a and b are equal")
# else:
#     print("a and b is not equal")


'''
# Exercise 6: Check Even or Odd
# Use an if-else statement to check if a number is even or odd.
# Example input: number = 4
# Expected output: 'The number is even.'
# hint: use the mod %, any number divisible by 2 is even
'''
# Write your code here
# num = int(input("Please input the number: "))
# if num % 2 == 0:
#     print("It's even")
# else:
#     print("It's odd")


'''
# Exercise 7: Age Group Classification
# Use if-elif-else statements to classify a person into age groups.
 < 13 = child
 < 20 = teenager
# Example input: age = 25
# Expected output: 'You are an adult.'
'''
# Write your code here
# age = int(input("Please enter the person's age: "))
# if age < 13:
#     print("CHILD")
# elif age < 20:
#     print("TEENAGER")
# else: 
#     print("ADULT")

'''
# Exercise 8: Temperature Check
# Use if-elif-else statements to check if a temperature is cold, warm, or hot.
# use your own values to determine what is cold, warm or hot.
# Example input: temperature = 30
# Expected output: 'It is warm.'
'''
# Write your code here
# temperature = int(input("Enter the temperature: "))
# if temperature < 20:
#     print("COLD")
# elif temperature < 33:
#     print("WARM")
# else:
#     print("HOT")

'''
# Exercise 9: Validating Age Input
# Use if-else statements to validate if the entered age is a positive number.
# Example input: age = -5
# Expected output: 'Invalid age.'
'''
# Write your code here


'''
# Exercise 10: Greeting Based on Time
# Use if-elif-else statements to print a greeting based on the time of the day.
# Good morning, Good afternoon, Good evening, Good night
# assume time is based on 24 hour clock, i.e 13 is 1.00pm
# Example input: time = 15
# Expected output: 'Good afternoon.'
'''
# Write your code here


'''
# Exercise 11: Grade Evaluation
# Use if-elif-else statements to evaluate a grade.
>= 90 = A*
>= 80 = A
>= 70 = B
>= 60 = C
anything lesser is a D
# Example input: grade = 85
# Expected output: 'You got an A.'
'''
# Write your code here


'''
# Exercise 12: Boolean Logic
# Assign boolean values to two variables and print the result of their logical AND.
# Example input: is_sunny = True, has_umbrella = False
# Expected output: False
'''
# Write your code here


'''
# Exercise 13: Voting Eligibility
# Use if-else statements to check if a person is eligible to vote.
# Example input: age = 17
# Expected output: 'You are not eligible to vote.'
'''
# Write your code here


'''
# Exercise 15: Password Validation
# Use if-else statements to check if a password meets a minimum length requirement.
# Example input: password = 'abc123'
# Expected output: 'Password is too short.'
'''
# Write your code here
