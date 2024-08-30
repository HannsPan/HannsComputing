entry = False
highest = -1
subjects = ["English", "Maths", "Science", "Mother Tongue"]

for i in range(4):
  entry = False
  while entry == False:
    marks = int(input("Enter the marks for {} = ".format(subjects[i])))
    if marks < 0 or marks > 100:
      marks = int(input("Enter the marks for {} = ".format(subjects[i])))
    else:
      entry = True




import random

# set this value to false first, this is used in the while loop below to continue looping
entry = False
WORDS = ["apple", "grape", "berry", "guava"]

# chooses a random fruit.
random_index = random.randint(0,len(WORDS)-1)
fruit = WORDS[random_index]

guess = input("Guess a fruit with 5 letters: ")

# validation check to ensure that user type in string with 5 letters...
while len(guess) != 5:
    print("You must guess a 5 letter word.")
    guess = input("Guess a fruit with 5 letters: ")

# after entry, this is the code that will check if your entry matches the word
# this validation is a mess. in class i will teach you a cleaner way to code this
#Yes, THanks
while entry == False:
    
    if len(guess) != 5:
      # ask again cos user did not put in 5 letters
      guess = input("Please input a 5-letter fruit: ")
    else:
      # this means that user enter 5 letters... now need to validate if 
      # if the user guess == to the fruit
      if guess.lower() == fruit: # put in .lower in case user type upper case
          print("Correct!")
          entry = True # set this variable to true to break the loop. see line 56


name_lst = []
class_lst = []

for i in range(3):
  entry = False
  while entry == False:
    names = input("Please enter your name:")
    classes = input("Input your class: ")
    if names == "" or classes == "":
      entry = False
    else:
      name_lst.append(names)
      class_lst.append(classes)
      entry = True
print(class_lst)
print(name_lst)
