# Q3: Convert From Lowercase to Uppercase and Vice Versa
# Design a program to ask user to create a username. 
# Check all the characters in the username. If the character is in uppercase, 
# convert it to lowercase and vice versa. Display the new username after conversion.

# Test case 1:

# Create an username: WhyWantToBeBotak
# Your new username is wHYwANTtObEbOTAK

# .upper()    .lower()   ## change to upper or lower
# .isupper()    .islower()   # check whether upper or lower
# # how to check each character in a string???

# def convertcase(word):
#   if i in word


username = input("Enter Your Username: ")
newusername = ""

for i in username:
  if i.isupper():
    newusername = newusername + i.lower()
  elif i.islower():
    newusername = newusername + i.upper()
  else:
    print("Invalid")

print(newusername)


