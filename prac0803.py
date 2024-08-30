'''
Practice 1

list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

## Question: Find the maximum number in this list
'''
#range(10) ## for i in this range #whole number must
# list of numbers starting from 0 to 9

list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105,-300]

max = 0
min = list1[0]

# looping through every number in the list
for i in list1:

    # check if this current number is > max variable
    if i > max:
        # remember the current biggest number
        max = i

print("The highest number in the list is: {}".format(max))

for i in list1:
    if i < min:
        min = i

print("The lowest number in the list is: {}".format(min))

'''
Practice 2

word_list = [
    "swimming", "jumping", "hearth", "magnify", "education", "important", "programming", "development",
    "implementation", "strategy", "technology", "platform", "hardware", "software", "interface", "database",
    "network", "internet", "protocol", "algorithm", "analysis", "function", "variable", "constant",
    "structure", "integer", "floating", "boolean", "string", "character", "operation", "encryption",
    "security", "authentication", "authorization", "firewall", "encryption", "decryption", "integrity",
    "availability", "confidentiality", "phishing", "malware", "virus", "spyware", "adware", "ransomware",
    "debugging", "testing", "deployment", "backup"
]

## Question 1: Find the length of the longest word in this list.

## Question 2: Check if there are multiple words with the longest length.
## If there are, print out all the words with the longest length

# Challenge 1: 
- Count the number of vowels in each word. 
- Return the word containing the most vowels.
        e.g. adware = vowel count is 3 (a, a, e)
- If there are multiple words that contains the most number of vowels, 
output all the words into a list and display it.
'''

word = "education"
# count the number of vowels in this word
a = 0
e = 0
i = 0
o = 0
u = 0

for letter in word:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1     
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1  

print("The number of a is {}".format(a))
print("The number of e is {}".format(e))
print("The number of i is {}".format(i))
print("The number of o is {}".format(o))
print("The number of u is {}".format(u))



'''
# Question 4: Declare a function that takes two numbers 
# as parameters and returns their sum.
# Example input: a = 5, b = 3
# Expected output: 8
'''
# Write your code here
def add(num1, num2):
    a = num1 + num2
    return (a)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print(add(num1, num2)) #this code will test your function

'''
# Question 5: Declare a function that takes a number as a parameter 
# and returns True if the number is even, otherwise False.
# Example input: number = 4
# Expected output: True
'''
# Write and test your code here
def evenodd(number):
    if number % 2 == 0:
        return True
    else:
        return False
    # a = number % 2
    # return (a)

number = int(input("Pls input your number: "))
print("Is number {} even? : {}".format(number, evenodd(number)))

# for i in range(1, 101):
#     print("Is number {} even? : {}".format(i, evenodd(i)))

'''
# Question 6: Declare a function that takes a list of numbers 
as a parameter and returns the sum of the list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 15
'''
# Write and test your code here


'''
# Question 7: Declare a function that takes a string 
# as a parameter and returns the string in uppercase.
# Example input: text = 'hello'
# Expected output: 'HELLO'
'''
# Write and test your code here


'''
# Question 8: Declare a function that takes a number as a
parameter and returns a string "positive" if the number is positive, 
"negative" if the number is negative, and "zero" if the number is zero.
# Example input: number = -1
# Expected output: 'negative'
'''
# Write and test your code here


print("This is before the loop")
while True: #infinite loop
    postal = input("What is your postal code? ")

    if postal.isdigit() and len(postal) == 6:
        # accepted
        print("Thank you, your postal code is {}".format(postal))
        break # break out of the loop
    else: # MEANS NOT VALID
        print("A postal code MUST BE 6 digits only.")

print("This is after the loop")