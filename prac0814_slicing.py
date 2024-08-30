# 9 marks debugging of NRIC -> format check, check digit
# 11 marks on 
# 2 user defined functions islower, isupper, top, ceiling

####### STRING SLICING #######
listnums = [1,321,45,634,7,8,43,78,3,789]

# can slice up part of the list

# retrieve the first value from the list
var1 = listnums[-1]
#print(var1)

# retrieve the first 3 items from the list
#[start:stop]
var2 = listnums[0:3] # stop value is up to but not including
#print(var2)

# retrieve the every alternate item from list
# [start: stop: step]
var3 = listnums[1::2]
# print(var3)
# listnum2 = []
# for i in var3:
#     listnum2.append(i*3)
# print(listnum2)

# reverse a list
var4 = listnums[::-1]
#print(var4)

word = "SINGAPORE"
var5 = word[0:3]
#print(var5)

var6 = word[::2]
#print(var6)

# String and List Operators
# Using + to Concatenate
# List Slicing
'''
Question 1: Extract a portion of a list.
Write a function that takes a list and returns a new list 
that contains only the first three elements of the original list.
Example Input: [1, 2, 3, 4, 5]
Example Output: [1, 2, 3]
'''
## Write and test your code here
lst = [2341, 3242, 2343, 4, 5, 4323,5435]
var1 = lst[0 : 3]
print(var1)


'''
Question 2: Get the last three items of a list.
Ask the user for a list of numbers and print the last three items.
Example Input: [10, 20, 30, 40, 50]
Example Output: [30, 40, 50]
'''
## Write and test your code here
lst = [10, 20, 30, 40, 50]
var2 = lst[-3 : ]
print(var2)
'''
Question 3: Create a sub-list from a list using slicing.
Given a list of elements, write a function that returns a 
sublist from the second element to the second last element.
Example Input: [0, 1, 2, 3, 4, 5]
Example Output: [1, 2, 3, 4]
'''
## Write and test your code here
lst = [0, 1, 2, 3, 4, 5]
var3 = lst[1 : -1]
print(var3)

'''
Question 4: Reverse a list using slicing.
Write a function that takes a list and returns it reversed.
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]
'''
## Write and test your code here
lst = [1, 2, 3, 4, 5]
var4 = lst[::-1]
print(var4)


'''
Question 5: Slice a list into halves.
Divide a list into two equal halves and returns both halves.
You may assume that the list has an even number of items
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 2, 3]  [4, 5, 6]
'''
## Write and test your code here
lst = [1, 2, 3, 4, 5, 6,7,8,9]
var5 = lst[0:3]
var6 = lst[3:]
print(var5)
print(var6)

'''
Question 6: Extract every second element from a list.
Write a function that returns a list of every second element from the given list.
Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
Example Output: ['b', 'd', 'f']
'''
## Write and test your code here
lst =  ['a', 'b', 'c', 'd', 'e', 'f']
alpha1  = lst[ 1 : : 2]
print(alpha1)


'''
Question 7: Remove the first and last elements of a list using slicing.
Create a function that takes a list and returns it without 
the first and last elements.
Example Input: [0, 1, 2, 3, 4]
Example Output: [1, 2, 3]
'''
## Write and test your code here



'''
Question 8: Create a function to reverse the order of elements in a 
list only from the second to the last but one.
Example Input: [1, 2, 3, 4, 5, 6]
Example Output: [1, 5, 4, 3, 2, 6]
'''
## Write and test your code here
# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
def reverseinthemiddle(inlist):
    # retrieve the items in the middle
    middle = inlist[1:-1]

    # reverse the items in the middle
    revmiddle = middle[::-1]

    # return the 1st + middlereverse + last
    return [inlist[0]] + revmiddle + [inlist[-1]]

testlist = [1, 2, 3, 4, 5, 6,354,356,345,345,345,345,2,41,24,23,4,21,1,1]
print(reverseinthemiddle(testlist))

'''
# Question 9: Extract the first three characters from a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here

'''
# Question 10: Extract the last three characters from a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here


'''
# Question 11: Extract a subset of a list from index 2 to 5
# Test case 1: example input: 1 2 3 4 5 6 7, 
example output: [3, 4, 5, 6]
# Test case 2: example input: 10 20 30 40 50 60, 
example output: [30, 40, 50]
'''
## Write and test your code here


'''
# Question 12: Extract every second character from a string
# Test case 1: example input: hello, example output: hlo
# Test case 2: example input: Python, example output: Pto
'''
## Write and test your code here



'''
# Question 13: Extract the middle three characters from a string
# You may assume the number of characters is even
# Test case 1: example input: abcdefg, example output: cde
# Test case 2: example input: helloworld, example output: low
'''
## Write and test your code here


'''
# Question 14: Extract the first half of a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here


'''
# Question 15: Extract the second half of a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here

'''
Question 16:
Write a function to split a string into half
and return the first half
Your function must handle an odd number length of characters
# If the length is odd, you will ignore the middle character
Example Input: "SINGING" Example Output: SIN
Example Input: "FLYING" Example Output: FLY
'''

'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''

'''
# Challenge 2:
Write a function `is_valid_username(username: str) -> bool` to 
check if a username is correctly generated. A valid username 
should be at least 6 characters long, should not contain any spaces, 
and must start with an uppercase letter followed by lowercase letters.

Normal Test: Input: "Johndoe", Output: True
Error Test: Input: "johnDoe", Output: False
Boundary Test: Input: "John", Output: False
'''

'''
# Challenge 3:
Write a function `validate_license_plate(plate: str) -> bool` 
to check if a vehicle license plate is valid. 
A valid plate starts with 3 uppercase letters, followed by 4 digits, 
and ends with an uppercase letter.

Normal Test: Input: "SAB1234Z", Output: True
Error Test: Input: "SA1234Z", Output: False
Boundary Test: Input: "SAB123Z", Output: False
'''

'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) -> bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''

'''
# Challenge 5:
Write a function `validate_date_format(date_str: str) -> bool` 
to check if a date string is in the format "DD/MM/YYYY" 
where DD, MM, and YYYY are valid digits. 

The function should ensure that DD is between 01 and 31, 
MM is between 01 and 12, and YYYY is a valid 4-digit positive integer.

Normal Test: Input: "29/02/2020", Output: True
Error Test: Input: "32/13/2020", Output: False
Boundary Test: Input: "01/01/0001", Output: True
'''