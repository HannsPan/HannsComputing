#Check counter.py


## Identify 10 errors and correct them
## Test with the test case 9780596520687 which is a valid ISBN
## Test with the test case 9781681972712 which is invalid


total = 0 #change 13 to 0

isbn = input("Enter an ISBN-13 number with no spaces ")

check_digit = int(isbn[12]) ##Change isbn[13] to isbn[12]

for i in range(12):

    if i%2 == 0:    ## change 1 to 0
        multiplier_weight = 1 ##change 0 to 1
    else:   
        multiplier_weight = 3

    total = total + isbn[i] * multiplier_weight  
    ## change position
    ## int(isbn[i])

remainder = total % 10 ##change to %11 to %10
if remainder == 0:
    check_digit = 0  ## change to result = 0
else:
    result = remainder - 10 ##should 10 - remainder

if result == remainder: ## change remainder to check_digit
    print ("ISBN Number is valid")
else: #ADD :
    print ("ISBN Number is invalid")

