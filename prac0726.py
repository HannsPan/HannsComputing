#### SIMPLE ADDITION PROGRAM
# ask for 2 numbers using input
# add up and print out the answer

# var1 = int(input("Enter first number: "))
# var2 = int(input("Enter second number: "))
# var3 = var1 + var2
# print(var3)

# 10 + 20 = 30

# print(var1,"+", var2, "=", var3)

#print 10 hello

# print number 0 - 10

for i in range(10):
    print("hello")

for j in range (10+1):
    print(j)

# for k in range(3):
#     print("a")
#     print("b")
#     print("c")


for l in range(3):
    print('\na')
    for m in range (3):
        print('b')
        for n in range (3):
            print('c')


# option 2: range(start, stop) ## 21 - 30
for i in range(21, 31):
    print(i)

##### 46 - 98
for i in range(46, 98+1):
    print(i)


# option 3 - range(start, stop, step) 
for i in range(3, 37, 3):
    print(i)

# print multiples of 7 from 7 to 84
for i in range(7, 84+1, 7):
    print(i)

for i in range(10, 0-1, -2):
    print(i)






'''
# Question 1: Print numbers from 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 2 3 4
# Test case 2: example input: 3, example output: 0 1 2
'''
## Write and test your code here
# num1 = int(input("enter number: "))
# for i in range (num1):
#     print(i)

'''
# Question 2: Print numbers from a given start number 
# to a given stop number (exclusive)
# Test case 1: example input: 3 8, example output: 3 4 5 6 7
# Test case 2: example input: 1 5, example output: 1 2 3 4
'''
## Write and test your code here
# start_num = int(input("Hey! Enter your start number: "))
# stop_num = int(input("Enter your STOP number: "))
# for i in range (start_num, stop_num):
#     print(i)
    
'''
# Question 3: Print even numbers from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 0 2 4 6 8
# Test case 2: example input: 7, example output: 0 2 4 6
'''
## Write and test your code here
# end_num = int(input("Enter the end digit: "))
# for i in range(0, end_num, 2):
#     print(i)

'''
# Question 4: Print numbers from a given start number 
# to a given stop number (exclusive) with a given step
# Test case 1: example input: 2 10 2, example output: 2 4 6 8
# Test case 2: example input: 1 10 3, example output: 1 4 7
'''
## Write and test your code here
# num1 = int(input("Enter your start num: "))
# num2 = int(input("Enter your stop num: "))
# num3 = int(input("Enter your step num: "))
# for i in range (num1, num2, num3):
#     print(i)


'''
# Question 5: Print the squares of numbers from 
# 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 4 9 16
# Test case 2: example input: 3, example output: 0 1 4
'''
## Write and test your code here
# num1 = int(input("Enter your stop num, then we'll sqr the rest: "))
# for i in range (0, num1):
#     print(i**2)


'''
# Question 6: Print the cubes of numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 1 5, example output: 1 8 27 64
# Test case 2: example input: 2 6, example output: 8 27 64 125
'''
## Write and test your code here

# num1 = int(input("Enter your start num, then we'll cube the rest: "))
# num2 = int(input("Enter your stop num, then we'll cube the rest: "))
# for i in range (num1, num2):
#     print(i**3)



'''
# Question 7: Print numbers in reverse from 
# a given start number to 0 (inclusive)
# Test case 1: example input: 5, example output: 5 4 3 2 1 0
# Test case 2: example input: 3, example output: 3 2 1 0
'''
## Write and test your code here
num1 = int(input("Enter the number you wanna start: "))
for i in range(num1, 0, -1):
    print(i)

'''
# Question 8: Print the even numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 2 10, example output: 2 4 6 8
# Test case 2: example input: 1 7, example output: 2 4 6
'''
## Write and test your code here


'''
# Question 9: Print the odd numbers 
# from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 1 3 5 7 9
# Test case 2: example input: 7, example output: 1 3 5
'''
## Write and test your code here


'''
# Question 10: Print the multiplication table 
# of a given number up to 10
# Test case 1: example input: 5, 
example output: 5 10 15 20 25 30 35 40 45 50

# Test case 2: example input: 3, 
example output: 3 6 9 12 15 18 21 24 27 30
'''
## Write and test your code here


'''
# Question 11: Print the first n numbers of the Fibonacci sequence
# Test case 1: example input: 5, example output: 0 1 1 2 3
# Test case 2: example input: 7, example output: 0 1 1 2 3 5 8
'''
## Write and test your code here
