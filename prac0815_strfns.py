'''
Question 1: Format a string to include variables for a user's name and age using str.format().
example input:
name = 'John', age = 30
expected output:
'Hello, John. You are 30 years old.'
'''
# Write and test your code here
# name = input("Your name : ")
# age = int(input("Your age: "))
# print("Hello, {}. You are {} years old.".format(name, age))


'''
Question 2: Check if the string 'Coding123' is alphanumeric using str.isalnum().
example input:
'Coding123'
expected output:
True
'''

#t = int(input("Enter something: "))
# if t.isdigit():
#     t = int(t) # convert
# else:
#     print("Invalid integer")

# Write and test your code here
# code = input("Enter your string you want to input: ")
# print(code.isalnum())
# if code.isalnum():
#     print("{} contains alpha or numeric".format(code))
# else:
#     print("{} does not contain alpha or numeric".format(code))
# #if code ==  str.isalnum(code):


'''
Question 3: Determine if the string 'Python' is alphabetic using str.isalpha().
example input:
'Python'
expected output:
True
'''
# Write and test your code here
# code = input("Enter your string: ")
# print(code.isalpha())
# if code.isalpha():
    

'''
Question 4: Verify if the string '2023' consists only of digits using str.isdigit().
example input:
'2023'
expected output:
True
'''
# Write and test your code here
# code = input("ENTER INPUT: ")
# print(code.isdigit())

'''
Question 5: Check if the string '    ' (four spaces) is composed only of whitespace using str.isspace().
example input:
'    '
expected output:
True
'''
# Write and test your code here
# code = input("Enter Input: ")
# print(code.isspace())

'''
Question 6: Determine if the string 'MixedCASE' is entirely lowercase using str.islower().
example input:
'MixedCASE'
expected output:
False
'''
# Write and test your code here
# code = input("Enter Input: ")
# print(code.islower())

'''
Question 7: Check if the string 'LOUD' is in uppercase using str.isupper().
example input:
'LOUD'
expected output:
True
'''
# Write and test your code here
# code = input("Enter Input: ")
# print(code.isupper())

'''
Question 8: Convert the string 'Java' to lowercase using str.lower().
example input:
'Java'
expected output:
'java'
'''
# Write and test your code here
# code = input("Enter Input: ")
# code = code.lower()
# print(code)

'''
Question 9: Convert the string 'javascript' to uppercase using str.upper().
example input:
'javascript'
expected output:
'JAVASCRIPT'
'''
# Write and test your code here
# code = input("Enter Input: ")
# code = code.upper()
# print(code)

'''
Question 10: Format a string to display a floating-point number with 2 decimal places using str.format().
example input:
number = 3.14159
expected output:
'3.14'
'''
# Write and test your code here
# code = float(input("Enter Num: "))
# code = float(round(code, 2))
# print(code)

'''
Question 11:
Create a Password Validator program that checks if a password is strong.
1. Ask the user to input a password.
2. Check if the password is at least 8 characters long. len()
3. Check if it contains at least one uppercase letter and one lowercase letter is.upper() is.lower()
4. Check if it contains one digit. is.digit()
5. Check if it contains a special character "!@#$%^&*()" "something" in "!@#$%^&*()"
6. Provide feedback on which criteria the password pass/ or fail.
7. Indicate if the password is strong if all criteria are met.
'''
# Write and test your code here
# if "!" in "!@#$%^&*()": # check for existence using in keyword
#     print("inside")
# else:
#     print("not inside")

while True:
    lenflag = False
    upper = False
    lower = False
    digit = False        #everything ill reset to false
    special = False
    
    pw = input("Enter a password: ") #Pass123!@#
    if len(pw) >= 8:
        lenflag = True
        print("Length is ok")

    for c in pw: 
        if c.isupper() and upper == False:
            upper = True
            print("Upper is ok")
        elif c.islower() and lower == False:
            lower = True
            print("Lower is ok")
        elif c.isdigit() and digit == False:
            digit = True
            print("Digit is ok")
        elif c in "!@#$%^&*()" and special == False:
            special = True
            print("Special is ok")

    if lenflag and upper and lower and digit and special:
        print("{} is valid".format(pw))
        break
    else:
        print("{} is not valid".format(pw))
        
    





'''
Question 12: Use str.format() to structure a sentence with multiple variables.
example input:
name = 'Alice', age = 28, city = 'New York'
expected output:
'Alice is 28 years old and lives in New York.'
'''
# Write and test your code here

'''
Question 13: Check if the string '12345' is alphanumeric using str.isalnum().
example input:
'12345'
expected output:
True
'''
# Write and test your code here


'''
Question 14: Determine if the string 'AlphaBeta' is alphabetic using str.isalpha().
example input:
'AlphaBeta'
expected output:
True
'''
# Write and test your code here


'''
Question 15: Verify if the string '100% Real' consists only of digits using str.isdigit().
example input:
'100% Real'
expected output:
False
'''
# Write and test your code here


'''
Question 16: Check if the string ' \t\n' (space, tab, newline) is composed only of whitespace using str.isspace().
example input:
' \t\n'
expected output:
True
'''
# Write and test your code here


'''
Question 17: Determine if the string 'multicase' is entirely lowercase using str.islower().
example input:
'multicase'
expected output:
True
'''
# Write and test your code here


'''
Question 18: Check if the string 'QUIET' is in uppercase using str.isupper().
example input:
'QUIET'
expected output:
True
'''
# Write and test your code here


'''
Question 19: Convert the string 'CSharp' to lowercase using str.lower().
example input:
'CSharp'
expected output:
'csharp'
'''
# Write and test your code here


'''
Question 20: Convert the string 'data' to uppercase using str.upper().
example input:
'data'
expected output:
'DATA'
'''
# Write and test your code here


'''
Question 21: Use str.format() to format a large integer with commas as thousands separators.
example input:
number = 1000000
expected output:
'1,000,000'
'''
# Write and test your code here

'''
Question 22:
# Write a function for the below
# Question 11: Write a program that takes a string and reverses it.
# Test case 1: example input: SINGAPORE, example output: EROPAGNIS
# Test case 2: example input: MALAYSIA, example output: AISYALAM
# CHALLENGE: DO THIS WITHOUT STRING SLICING.
'''
############ Write your code here #####################
