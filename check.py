# num1 = int(input("Enter your start num, then we'll cube the rest: "))
# num2 = int(input("Enter your stop num, then we'll cube the rest: "))
# for i in range (num1, num2):
#     print(i**3)

# range(start, stop, step) # starting value, stopping value, and the increment
# e.g. range(1, 11, 2) 
# start >> start from 1
# stop >> stop at (11 - 1) up to 11 but not including 11.
# step >> increase by 2 every time
# so will print out, 1, 3, 5, 7, 9

## while loop uses a condition to keep looping
# e.g.
# count = 0
# while count < 10:
#     print(count)
#     count += 1

'''
Task 1 (length check)
There is a list of 5-letter words related to fruits. User has to input his/her guess. 
Your program checks whether the guess is correct. 
Your program also needs to validate 
whether user's input consists of 5 letters. 
If the input does not consist of 5 letters, ask user to input again.

Part of the program is given below. Continue with the program to fulfil the requirements above?
'''
#This is the clue give, but I don't understand this can help explain to me Thanks :)#

# this code is messy i feel like rewriting it haha
# but i try to change for you

#ok
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
        print("You must guess a 5 letter word.")
        guess = input("b Please input a 5-letter fruit: ")
    else:
        # this means that user enter 5 letters... now need to validate if 
        # if the user guess == to the fruit
        if guess.lower() == fruit: # put in .lower in case user type upper case
            print("Correct!")
            entry = True # set this variable to true to break the loop. see line 55
        else:
            # wrong fruit
            print("Wrong. Guess again")
            guess = input("Please input a 5-letter fruit: ")

