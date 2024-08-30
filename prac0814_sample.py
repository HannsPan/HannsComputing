'''SCT Practice

A main program calls a user-defined function to perform certain tasks. 
Below is a main program which
allows user to enter the temperatures for a few days and return the 
highest temperature rounded up to nearest integer 
and the lowest temperature rounded down to nearest integer.
'''
import math

def bound(templist):
    newlst = []
    for i in templist:
        newlst.append(int(i))

    maxi = max(newlst)
    mini = min(newlst)
    avri = sum(newlst) / len(newlst)

    return int(maxi), int(mini), round(avri,1)


temperature = input('Enter the temperatures you have recorded. Separate each temperature with comma: ')
lst = temperature.split(',')

(top, bottom, average) = bound(lst)
print('Highest temperature round up to nearest integer: ', top)
print('Lowest temperature round down to nearest integer: ', bottom)
print('Average temperature rounding to 1 decimal place: ', average)

'''
7 Open the file RANGE.py. Save your program as RANGE_&lt;your
name&gt;_&lt;class&gt;_&lt;index_number&gt;.
8 Within the program, create a user-defined function named bound which [9]
 receives a list called lst from the main program above
 find the highest temperature and round up to the nearest integer
 find the lowest temperature and round down to nearest integer
 find the average temperature rounding to 1 decimal place
 return the highest, lowest and average temperatures to the main program

9 When you program is working, use the following test data to show your test result. 
Your output should look like this.
Enter the temperatures you have recorded. Separate each temperature with comma:
28.9,33.0,34.2,27.9,30.2
Highest temperature round up to nearest integer: 35
Lowest temperature round down to nearest integer: 27
Average temperature rounding to 1 decimal place: 30.8   
'''


    # if temperature == max():
    #     return highest
    

# def evenodd(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#     # a = number % 2
#     # return (a)

# number = int(input("Pls input your number: "))
# print("Is number {} even? : {}".format(number, evenodd(number)))

# import math

# def bound(templist):
#     newlist = []
#     for i in templist:
#         newlist.append(int(i))

#     maxtemp = max(newlist)
#     mintemp = min(newlist)
#     avgtemp = sum(newlist)/ len(newlist)

#     return int(maxtemp), int(mintemp), int(avgtemp)