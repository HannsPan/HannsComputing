'''
# Exercise 1: Sum of ASCII Values
# Write a Python program that calculates the sum of the ASCII values of 
all characters in a given string.
# Example input: text = "hello"
# Expected output: 532
'''
word = "hello"
sumvalue = 0
sum = 0

for i in word:
    sumvalue = ord(i)
    sum = sum + sumvalue
    
print(sum)

# Solution for Exercise 1



'''
# Exercise 2: Character from ASCII Value
# Write a Python program that takes an ASCII value as input and prints 
the corresponding character.
# Example input: ascii_value = 97
# Expected output: 'a'
'''
ans = ord("a")
print(ans)



'''
# Exercise 3: Uppercase to Lowercase Conversion
# Write a Python program that converts an uppercase letter to its lowercase 
equivalent using ASCII values.
# Example input: letter = 'A'
# Expected output: 'a'
'''



'''
# Exercise 4: Lowercase to Uppercase Conversion
# Write a Python program that converts a lowercase letter to its 
uppercase equivalent using ASCII values.
# Example input: letter = 'b'
# Expected output: 'B'
'''


'''
# Exercise 5: ASCII Value Difference
# Write a Python program that calculates the difference between the 
ASCII values of two characters.
# Example input: char1 = 'a', char2 = 'd'
# Expected output: 3
'''


'''
# Exercise 6: Alphabetical Sequence
# Write a Python program that prints the next 5 characters in the ASCII 
sequence from a given character.
# Example input: start_char = 'x'
# Expected output: 'y', 'z', '{', '|', '}'
'''
##var_1 = input("Enter your char: ")

##x = ord(var_1)

##for i in range(1, 6):
    ##sum = chr(x + i)

    ##print(sum)


# for i in var_1:
#     var_2 = ord(i)
#     var_3 = var_2 + 1
#     var_4 = var_2 + 2
#     var_5 = var_2 + 3
#     var_6 = var_2 + 4
#     var_7 = var_2 + 5

#     var_8 = chr(var_3)
#     var_9 = chr(var_4)
#     var_10 = chr(var_5)
#     var_11 = chr(var_6)
#     var_12 = chr(var_7)

#     print(var_8,var_9,var_10,var_11,var_12)

'''
# Exercise 7: Sum of ASCII Values of Digits
# Write a Python program that calculates the sum of the ASCII values of all 
digit characters in a given string.
# Example input: text = "a1b2c3"
# Expected output: 150
'''
import math

string = input("Enter given string: ")
x = 0
sum = 0

for i in string:
    # check if it is digit
    if i.isdigit():
        sum = sum + ord(i)    ##Always remember that it should be (i)

print(sum)

'''
# Exercise 8: Replace Characters with ASCII Sum
# Write a Python program that replaces each character in a string with the 
sum of its ASCII value and a given integer.
# Example input: text = "abc", increment = 1
# Expected output: 'b', 'c', 'd'
'''


