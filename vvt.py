while True:
    lenflag = False
    upper = False
    lower = False
    digit = False        #everything ill reset to false
    special = False

    pw = input("Enter a password: ") #Pass123!@#
    if len(pw) >= 8:
        lenflag = True
        print("Length is ok")

    for c in pw: 
        if c.isupper() and upper == False:
            upper = True
            print("Upper is ok")
        elif c.islower() and lower == False:
            lower = True
            print("Lower is ok")
        elif c.isdigit() and digit == False:
            digit = True
            print("Digit is ok")
        elif c in "!@#$%^&*()" and special == False:
            special = True
            print("Special is ok")

    if lenflag and upper and lower and digit and special:
        print("{} is valid".format(pw))
        break
    else:
        print("{} is not valid".format(pw)) 