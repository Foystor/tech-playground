'''
ask user to enter password
1 digit, 1 lowercase, 1 uppercase, 1 spcial character, length >= 8
'''


import string

'''
print(string.digits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
'''

d = lc = uc = s = False
pw = input("Enter a password: ")

for c in pw:  ## abc123
  if c in string.digits:
    d = True
  if c in string.ascii_lowercase:
    lc = True
  if c in string.ascii_uppercase:
    uc = True
  if c in string.punctuation:  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    s = True

if len(pw) >= 8 and d and lc and uc and s:
  print("Password is VALID!")
else:
  print("Password is unvalid")
  if len(pw) < 8:
    print("Too short")
  if not d:
    print("Password should have at least one digit")
  if not lc:
    print("Password should have at least one lowercase letter")
  if not uc:
    print("Password should have at least one uppercase letter")
  if not s:
    print("Password should have at least one special character")




'''
import string

d = lc = uc = s = False
pw = input("Enter a password: ")

for c in pw : ## abc123
  if c in '0123456789' :
    d = True
  if c in 'abcdefghijklmnopqrstuvwxyz':
    lc = True
  if c in string.ascii_uppercase:
    uc = True
  if c in string.punctuation: # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    s = True

if len(pw) >= 8 and d and lc and uc and s:
  print("Password is VALID!!!")
else:
  print("Password is invalid")
  if len(pw) < 8 :
    print("Too short")
  if not d :
    print("Password should have at least one digit")
  if not lc :
    print("Password should have at least one lowercase letter")
  if not uc :
    print("Password should have at least one uppercase letter")
  if not s :
    print("Password should have at least one special character")
'''


