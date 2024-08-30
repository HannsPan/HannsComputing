'''
Q2
You are given a list of computing paper 1 marks and paper 2 marks

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

Design a program to

1.  update Ken's mathematics mark to 83
2.  show the average of paper 1 marks and average of paper 2 marks
3.  ask user to enter a person and the paper he wants to search. 
If the person is in the list, show the respective mark.
Otherwise shows that the person cannot be found

Open the file computing.py and work on the program.  
Save your file as computing_yourname_class.py.
'''

# VARIABLE TYPE
# 

paper1 = {"Ken": 80, 
          "Mike": 84, 
          "Ash": 55, 
          "Zee": 65}

### TO CHANGE THE VALUE OF A KEY IN THE DICTIONARY
#print(paper1["Ken"]) # TO RETRUEVE A VALUE
paper1["Ken"] = 83 # 
# paper1["Mike"] = 83 # 
# paper1["Ash"] = 83 # 
# paper1["Zee"] = 83 # 
#print(paper1)


scores = [80,84,55,65] # BASED ON THE INDEX
scores[0] = 83 ## CHANGE IN A LIST


paper2 = {"Ken": 88, 
          "Mike": 64, 
          "Ash": 65, 
          "Zee": 85}

paper2["Ken"] = 83 


#############
# 2.  show the average of paper 1 marks and average of paper 2 marks
# loop through all the keys in dictionary
sum = 0
count = 0
for student in paper1:
    print(student) # printing out the key 
    #print(paper1[student]) # print out the value
    score = paper1[student]
    sum = sum + score
    count = count + 1

print(sum/ count)



#3.  ask user to enter a person and the paper he wants to search. 
name = input("Search for who? ")
papernum = input("What Paper? ")

if papernum == "1":
    # pass
    if name in paper1: # checks for existence of this value in dictionary
        score = paper1[name]
        print("{}'s score is {}".format(name, score))
    else:
        print("{} does not exist.".format(name))
    # search paper1 dictionary
elif papernum == "2":
    pass
    # search paper2 dictionary
else:
    print ("Invalid paper")

