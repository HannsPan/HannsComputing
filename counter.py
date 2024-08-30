#### COUNTER ALGORITHM ##########

message = input("Enter the words : ")

# Count the a in this string 
# count the b in the string

counta = 0
countb = 0
countc = 0

for i in message:
    if i == "a":
        counta = counta + 1
        #counta += 1
    if i == "b":
        countb = countb + 1
    if i == "c":
        countc = countc + 1
print("There is {} total of A's in the message".format(counta))
print("There is {} total of B's in the message".format(countb))
print("There is {} total of C's in the message".format(countc))    

if counta == 0:
        print("The to As in the message is {}" .format(counta))

## MAX/ MIN ##
nums =[2,23,45,3564,65,67,68,-556,4000,4325]
# Find the maximum number and minimum number in this list of numbers
max = 0
min = nums[0] #max(nums)

for i in nums:
    if i > max:
        max = i
        print("The current number is {}".format(i))
        print("The max number is {}".format(i))
        
    if i < min:
        min = i
        
    
print("The max number is {}.".format(max))
print("The min number is {}.".format(min))


# DICTIONARY
menu = {'friedrice':5.5, 'spaghetti':10, 'hamburger':8} 

# access a key value
print(menu['friedrice'])