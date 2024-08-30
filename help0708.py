'''
# **Q5: Find the max, min, average given 5 numbers**

Ask the user to enter 5 numbers. Check whether there are 5 numbers. 
If not, ask the user to input all over again.

Create three functions to find the max, min, average of the 5 numbers. 
Return the respective values.

>  *Test case*

    Enter 1st number: 2
    Enter 2nd number: 5
    Enter 3rd number: 9
    Enter 4th number: 0
    Enter 5th number: 6

    Max number is 9
    Min number is 0
    Average is 3.2
'''
# in this case, the parameter is expected to be a list
def findmax(numbers):
    #return max(numbers)

    # if not allowed to use the max function above. 
    # then you have to do this the manual way
    maxnum = 0
    for i in numbers:
        if i > maxnum:
            maxnum = i
    return maxnum

def findmin(numbers):
    #return min(numbers)

    # if not allowed to use the min function above
    # then you have to do this the manual way
    minnum = max(numbers) + 1
    for i in numbers:
        if i < minnum:
            minnum = i
    return minnum

def findavg(numbers):
    #return sum(numbers) / len(numbers)

    # if not allowed to use the sum above,
    # then have to manually calculate the sum
    sum = 0
    count = 0
    for i in numbers:
        sum = sum + i # or sum += i
        count = count + 1
    return sum / count

listnums = []
while True:
    # assuming here that the user always enters a number. i.e. i am not validating
    num = int(input("Enter a number: "))
    listnums.append(num)

    if len(listnums) == 5: 
        print("5 numbers have been entered. ")
        break
    else:
        print("Please continue until 5 numbers are entered.")

print("The numbers are {}".format(listnums))

print("The maximum number is {}".format(findmax(listnums)))
print("The minimum number is {}".format(findmin(listnums)))
print("The average number is {}".format(findavg(listnums)))
            
