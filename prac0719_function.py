### Basic 1: Functions with no parameters, no return value
'''
# Question 1: Declare a function that prints "Hello, World!" 
# and call the function.
# Example input: 
# Expected output: Hello, World!
'''
# Write your code here
# def ergasqwqwvqwv(name):
#   print("Hello, {}".format(name))

# ergasqwqwvqwv("Lim")

### Basic 2: Functions with 1 or more parameters
'''
# Question 2: Declare a function greet that takes a 
# name as a parameter and prints a greeting message.
# Example input: name = 'John'
# Expected output: 'Hello, John!'
'''
# Write your code here
###def person(name):
  # if name == "Lim":
    ### print("Hello, {}".format(name))
  # else:
  #   print("Not in system")
 
# name2 = input("What is your name? ")
# person(name2)
## call the function and put the input value into the function

'''
# Question 3: Declare a function greet that takes yourname and myname
# as parameters and prints a introduction message.
# Example input: yourname = 'John', myname="Marcus"
# Expected output: 'Hello, John! I'm Marchus, nice to meet you!'
'''
# Write your code here
# def greeting(yourname, myname):
#   print(f"Hello, {yourname}! I'm {myname}, nice to meet you!")

# friend = "JOhn"
# me = "Hanns"
# greeting(friend, me)

### Basic 3: Functions with parameters and return value

'''
# Question 4: Declare a function that takes two numbers 
# as parameters and returns their sum.
# Example input: a = 5, b = 3
# Expected output: 8
'''
# Write your code here
# def sum(a, b):
#   return (a+b)    ##it returns something to me :)

# num1 = int(input("Enter first no. : "))
# num2 = int(input("Enter second no. : "))
# answer = sum(num1, num2) ## diff from def, is okk
# print(answer)

####### EXPLANATION ON WHY WE NEED TO RETURN #######
###if you return a value, it allows you to use it for different scenarios###
#### define a function to calculate the area of triangles
# def areatriangle(base, height):
#     area = 0.5 * base * height
#     return area

# 3 triangles
# t1 = areatriangle(45, 98)
# t2 = areatriangle(123, 4334546)
# t3 = areatriangle(123, 23423423)

# print(t1 + t2 + t3) # total area of 3 triangles

# print(add(5, 3)) #this code will test your function

'''
# Question 5: Declare a function that takes a number as a parameter 
# and returns True if the number is even, otherwise False.
# Example input: number = 4
# Expected output: True
'''
# Write and test your code here

def numberss(no):
    if no % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number to check if even or odd "))
print(numberss(num))

for i in range(1, 101):
    print(f'Number {i} is even = {numberss(i)}')
      
# '''
# ctrl + a ==> select all
# ctrl + z ==> undo
# ctrl + c ==> copy
# ctrl + v ==> paste
# ctrl + ? ==> comment/ toggle
# ctrl + [ ==> left indent
# ctrl + ] ==> right indent
# '''