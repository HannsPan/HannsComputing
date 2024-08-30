'''

  Design a program that

      1) allows user to enter a string. The string consists of uppercase letters

      2) shift each character of the string 3 places to the right

      3) Output the encrypted string

      **Homework**

Design a program that

    1) encrypts lowercase and uppercase string and shift it 3 places to the right
    2) extend the program to allow user to choose
       Option 1: encrypt a string
       Option 2: decrypt a string
       - If user chooses option 1, allow user to enter a string to encrypt. Then your program will encrypt the string and output the encrypted string
       - If user chooses option 2, allow user to enter an encrypted string. Then your program will decrypt the string and output the original string
    3) Test Case 1:
       Please select
       Option 1: Encrypt a string
       Option 2: Decrypt a string
       Enter your option:  1
       Enter a string: OXyzEN
       The encrypted string is RAbcHQ
    4) Test Case 2:
       Please select
       Option 1: Encrypt a string
       Option 2: Decrypt a string
       Enter your option:  2
       Enter a string: HqCbph
       The original string is EnZyme   
'''

# Upper >> 65 - 90 (26)
# Lower >> 97 - 122 (26)

shift = 3

test = "A"
if test.isupper():
  



var_1 = str(input("Enter a string consisting of uppercase letter: "))
for i in var_1:
  var_2 = ord(i)
  var_3 = var_2 + 3
  var_4 = chr(var_3)


  print(var_4, end="")  #end it as a stringggg


# Upper >> 65 - 90 (26)
# Lower >> 97 - 122 (26)

shift = 3

#ordtest = ord(test)
offset = 0

def encrypt_char(inchar, shift):
    
    if inchar.isupper():
        offset = 65
    else:
        offset = 97

    encrypted = offset + (ord(inchar) - offset + shift) % 26
    #print(encrypted)
    return chr(encrypted)

def decrypt_char(inchar, shift):
    
    if inchar.isupper():
        offset = 65
    else:
        offset = 97

    encrypted = offset + (ord(inchar) - offset - shift) % 26
    #print(encrypted)
    return chr(encrypted)

# check encryption 
test = "OXyzEN"
e_string = ""
for c in test:
    # print(encrypt_char(c, shift))
    e_string = e_string + encrypt_char(c, shift)
print(e_string)

# decryption
d_string = ""
for c in "HqCbph":
    # print(encrypt_char(c, shift))
    d_string = d_string + decrypt_char(c, shift)
print(d_string)
