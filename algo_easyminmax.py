# Write a program to find the largest and smallest numbers in 
# a list using 
# 1. max()
# 2. min()
# 3. without using max()
# 4. without using min()
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

####################################################
# Answer for Question 1 here
maxnum = max(list1)
print(f"The maximum number in the list is {maxnum}")

####################################################
# Answer for Question 2 here
minnum = min(list1)
print(f"The minimum number in the list is {minnum}")

####################################################
# Answer for Question 3 here
maxnum2 = list1[0]

for i in list1:
    if i > maxnum2:
        maxnum2 = i

print(f"The maximun number is {maxnum2}")

####################################################
# Answer for Question 4 here
minnum2 = list1[0]

for i in list1:
    if i < minnum2:
        minnum2 = i

print(f"The minimum number is {minnum2}")


######################################################
# Question 5:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their positions in the list.

# Assume that the first item in the list is position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 5 here

fasttime = swim_times[0]
slowtime = swim_times[0]

fastindex = 0
slowindex = 0

countindex = 1

sum = 0


for swimmer in swim_times:
    if swimmer < fasttime:
        fasttime = swimmer
        fastindex = countindex
    if swimmer > slowtime:
        slowtime = swimmer
        slowindex = countindex

    countindex += 1
    
    
#Calculate the sum of all the nums in the list
    sum = sum + swimmer

print(f"Fastest swimmer is #{fastindex} and the time is {fasttime}s")
print(f"Slowest swimmer is #{slowindex} and the time is {slowtime}s")


# Calculate average
average = sum / len(swim_times)

print(f"The sum of all the numbers in the list is {round(sum,2)}")
print(f"The average of all the numbers in the list is {round(average,2)}")

########################################################
# Question 6:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
donations = {
    'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
    'Class 1A': 450, 'Class 1B': 530, 'Class 2C': 470, 'Class 3D': 310,
    'Class 4E': 415, 'Class 5F': 390
}
# Answer for Question 6 here
highclass = ""
lowclass = ""

lowamount = 99999999999999999999999999999
highamount = 0

for classing , amt in donations.items():
    if amt > highamount:
        highamount = amt
        highclass = classing
    if amt < lowamount:
        lowamount = amt
        lowclass = classing

print(f"Lowestclass is {lowclass} and the amt collected is ${lowamount}")
print(f"highest class is {highclass} and the amt collected is ${highamount}")
# loop through dictionary 




#################################################################
# Question 7: 
# A bookstore keeps track of their sales figures each day 
# for the month of June. The sales for the 30 days are provided 
# in the list below. Find the days with the highest and lowest sales. 
# Assume that the first item in the list corresponds to Day 1.
#################################################################
daily_sales = [120, 98, 135, 105, 150, 112, 80, 130, 95, 110, 
               102, 85, 140, 99, 123, 145, 78, 90, 136, 145, 
               132, 108, 75, 88, 142, 115, 97, 121, 89, 100]
# Answer for Question 7 here

lowestsale = daily_sales[0]
highestsale = daily_sales[0]

highindex = 0
lowindex = 0

day = 1

for i in daily_sales:
    if i > lowestsale:
        lowestsale = i
        lowindex = day
    if i < highestsale:
        highestsale = i
        highindex = day

    day += 1


print(f"The day with the highest sale is day {highindex} with a total of {highestsale} books sold.")
print(f"The day with the lowest sale is day {lowindex} with a total of {lowestsale} books sold.")







#################################################################
# Question 8:
# A mathematics teacher recorded the final exam scores (out of 100) of 
# students in the dictionary below. 
# Write Python code to identify the student 
# with the highest and lowest exam scores, and print their names and scores.
#################################################################
exam_scores = {
    'Ali': 88, 'Benny': 75, 'Chloe': 92, 'Diana': 85,
    'Ethan': 78, 'Farid': 81, 'Grace': 66, 'Haziq': 94,
    'Ivy': 71, 'Jun': 88}
# Answer for Question 8 here

highestscore = 0
lowestscore = 99999999999999999

highname = ""
lowname = ""

for name , score in exam_scores.items():
    if score > highestscore:
        highestscore = score
        highname = name

    if score < lowestscore:
        lowestscore = score
        lowname = name

print(f"The student with the highest score is {highname} with a score of {highestscore}")
print(f"The student with the lowest score is {lowname} with a score of {lowestscore}")
        


##################################################################
# Question 9: 
# Hourly temperature measurements (°C) for a specific day are given below. 
# Write Python code to determine the highest and lowest temperatures, 
# along with the corresponding hour of measurement. 
# (First measurement at index 0 corresponds to midnight, 
#  and each subsequent value is measured hourly.)
##################################################################
hourly_temperatures = [26.4, 25.9, 25.1, 24.6, 24.2, 23.8, 24.5, 25.6, 
                       27.3, 29.0, 30.5, 31.2, 32.0, 33.1, 32.8, 31.6,
                       30.8, 29.4, 28.1, 27.5, 27.0, 26.8, 26.0, 25.7]
# Answer for Question 9 here

lowesttemp = hourly_temperatures[0]
highesttemp = hourly_temperatures[0]

highindex2 = 0
lowindex2 = 0

hourlyindex = 0

for i in hourly_temperatures:
    if i > highesttemp:
        highesttemp = i
        highindex2 = hourlyindex
    if i < lowesttemp:
        lowesttemp = i
        lowindex2 = hourlyindex

print(f"The highest temperature is {highesttemp}c at the {highindex} hour.")
print(f"The lowest temperature is {lowesttemp}c at the {lowindex} hour.")




##################################################################