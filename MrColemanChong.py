prefix = {"A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9", "J":"10", "K":"11", "L":"12", "M":"13", "N":"14", "O":"15", "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20", "U":"21", "V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26"}
carplate = input("Enter your car plate number EXCEPT the FIRST PREFIX: ")
CP_list=[prefix[carplate[1]],prefix[carplate[2]],int(carplate[3]),int(carplate[4]),int(carplate[5]),int(carplate[6])] #Contains all the digits
total=0
sum=[]
weightage=[10, 15, 14, 15, 16, 17]


# if carplate.upper() == "A":

if prefix[carplate] == "A":
    print(1)
'''
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

###### ANSWER FOR DEBUGGING

# == check for equality, single = is variable assignment
if action.upper() == "B": ## missing colon and == # change to uppercase
    if books[book_id] == "AVAILABLE": # change to upper case
        books[book_id] = "BORROWED" # change to uppercase, change to book_id
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action.upper() == "R": # missing == # change to uppercase
    if books[book_id] == "BORROWED": # change to upper case
        books[book_id] = "AVAILABLE" # should be []
        print("You have returned the book.") # missing ""
    else:
        print("The book is already available.") # indentation error
else: # wrong indentation
    print("Invalid action.") # missing ""

print(books)
'''