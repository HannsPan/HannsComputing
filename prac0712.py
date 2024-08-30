
'''
abs(): The abs() function in Python returns the absolute 
value of a given number. It can handle integers, 
floating-point numbers, and even complex numbers, 
returning their magnitude.
'''
# Example 1:
# Using abs() with a negative integer
negative_integer = -10
absolute_value = abs(negative_integer)
print(absolute_value)  # Output: 10
# Explanation: abs(-10) returns 10, the absolute value of -10.

# Example 2:
# Using abs() with a floating-point number
floating_number = -3.14
absolute_value = abs(floating_number)
print(absolute_value)  # Output: 3.14
# Explanation: abs(-3.14) returns 3.14, the absolute value of -3.14.

#####################################################################



'''
ceil(): The ceil() function in Python, 
available in the math module, returns the smallest 
integer greater than or equal to a given number.
'''
# Example 1:
# Using ceil() with a positive floating-point number
import math
number = 4.3
result = math.ceil(number)
print(result)  # Output: 5
# Explanation: math.ceil(4.3) returns 5, 
# the smallest integer greater than 4.3.

# Example 2:
# Using ceil() with a negative floating-point number
number = -4.3
result = math.ceil(number)
print(result)  # Output: -4
# Explanation: math.ceil(-4.3) returns -4, 
# the smallest integer greater than -4.3.


##########################################################################


'''
floor(): The floor() function in Python, 
# available in the math module, returns the largest 
integer less than or equal to a given number.
'''
# Example 1:
# Using floor() with a positive floating-point number
import math
number = 4.7
result = math.floor(number)
print(result)  # Output: 4
# Explanation: math.floor(4.7) returns 4, 
# the largest integer less than 4.7.

# Example 2:
# Using floor() with a negative floating-point number
number = -4.7
result = math.floor(number)
print(result)  # Output: -5
# Explanation: math.floor(-4.7) returns -5, 
# the largest integer less than -4.7.


#####################################################################




'''
pow(): The pow() function in Python returns the value of a 
number raised to the power of 
another number. It can also take an optional modulus argument.
'''
# Example 1:
# Using pow() with two arguments
result = pow(2, 3)
print(result)  # Output: 8
# Explanation: pow(2, 3) 
# returns 2 raised to the power of 3, which is 8.

# Example 2:
# Using pow() with three arguments
result = pow(2, 3, 5)
print(result)  # Output: 3
# Explanation: pow(2, 3, 5) 
# returns (2 ** 3) % 5, which is 8 % 5 = 3.


######################################################################



'''
sqrt(): The sqrt() function in Python, 
available in the math module, returns the square 
root of a given number.
'''
# Example 1:
# Using sqrt() with a positive number
import math
number = 16
result = math.sqrt(number)
print(result)  # Output: 4.0
# Explanation: math.sqrt(16) 
# returns the square root of 16, which is 4.0.

# Example 2:
# Using sqrt() with a floating-point number
number = 7.5
result = math.sqrt(number)
print(result)  # Output: 2.7386127875258306
# Explanation: math.sqrt(7.5) 
# returns the square root of 7.5, which is approximately 2.74.


##################################################################


'''
trunc(): The trunc() function in Python, 
available in the math module, returns the integer 
part of a number by removing any fractional digits.
'''
# Example 1:
# Using trunc() with a positive floating-point number
import math
number = 4.7
result = math.trunc(number)
print(result)  # Output: 4
# Explanation: math.trunc(4.7) 
# returns the integer part of 4.7, which is 4.

# Example 2:
# Using trunc() with a negative floating-point number
number = -4.7
result = math.trunc(number)
print(result)  # Output: -4
# Explanation: math.trunc(-4.7) 
# returns the integer part of -4.7, which is -4.


############################################################


'''
round(): The round() function in Python 
returns a floating-point number rounded to the 
specified number of decimals.
'''
# Example 1:
# Using round() with one decimal place
number = 3.14159
rounded_number = round(number, 2)
print(rounded_number)  # Output: 3.14
# Explanation: round(3.14159, 2) rounds the number to 2 decimal places.

# Example 2:
# Using round() without specifying decimals
number = 3.5
rounded_number = round(number)
print(rounded_number)  # Output: 4
# Explanation: round(3.5) rounds the number to the nearest integer.



######################################################################



'''
max(): The max() function in Python returns the 
largest item in an iterable or the largest 
of two or more arguments.
'''
# Example 1:
# Using max() with a list
numbers = [1, 2, 3, 4, 5]
maximum = max(numbers)
print(maximum)  # Output: 5
# Explanation: max([1, 2, 3, 4, 5]) 
# returns 5, which is the largest number in the list.

# Example 2:
# Using max() with multiple arguments
maximum = max(1, 2, 3, 4, 5)
print(maximum)  # Output: 5
# Explanation: max(1, 2, 3, 4, 5) 
# returns 5, which is the largest number among the arguments.


#####################################################################



'''
min(): The min() function in Python returns the smallest item 
in an iterable or the smallest of two or more arguments.
'''
# Example 1:
# Using min() with a list
numbers = [1, 2, 3, 4, 5]
minimum = min(numbers)
print(minimum)  # Output: 1
# Explanation: min([1, 2, 3, 4, 5]) 
# returns 1, which is the smallest number in the list.

# Example 2:
# Using min() with multiple arguments
minimum = min(1, 2, 3, 4, 5)
print(minimum)  # Output: 1
# Explanation: min(1, 2, 3, 4, 5) 
# returns 1, which is the smallest number among the arguments.

##################################################################


'''
random(): The random() function in Python, a
vailable in the random module, returns a 
random floating-point number N such that 0 <= N < 1.
'''
# Example 1:
# Using random() to generate a random floating-point number 
# between 0 and 1
import random
random_float = random.random()
print(random_float)  # Output: A random float between 0 and 1
# Explanation: random.random() 
# generates a random floating-point number between 0 and 1.

# Example 2:
# Using random() and scaling to 
# generate a random float between 0 and 10
random_float = random.random() * 10
print(random_float)  # Output: A random float between 0 and 10
# Explanation: random.random() * 10 
# scales the random float to the range 0 to 10.


#################################################################


'''
randint(): The randint() function in Python, available in the 
random module, returns a random integer N such that a <= N <= b.
'''
# Example 1:
# Using randint() to generate a random integer between 1 and 10
import random
random_integer = random.randint(1, 10)
print(random_integer)  # Output: A random integer between 1 and 10
# Explanation: random.randint(1, 10) 
# generates a random integer between 1 and 10.

# Example 2:
# Using randint() to generate a random integer between -5 and 5
random_integer = random.randint(-5, 5)
print(random_integer)  # Output: A random integer between -5 and 5
# Explanation: random.randint(-5, 5) 
# generates a random integer between -5 and 5.


###########################################################