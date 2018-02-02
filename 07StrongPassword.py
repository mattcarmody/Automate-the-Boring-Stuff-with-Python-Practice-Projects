#! python3
# chap7PracProjStrongPassword.py - Tells you if the password passed is strong.

import re

con = True
while con:
    # Pass a password string
    password = str(input('Enter your password.'))

    # Does it have at least one uppercase character?
    passwordRegex1 = re.compile(r'''(
        [A-Z]
        )''', re.VERBOSE)
    # Does it have at least one lowercase character?
    passwordRegex2 = re.compile(r'''(
        [a-z]
        )''', re.VERBOSE)
    # Does it have at least one numeric digit?
    passwordRegex3 = re.compile(r'''(
        \d
        )''', re.VERBOSE)
    # Run regexes to get mo's
    mo1 = passwordRegex1.search(password)
    mo2 = passwordRegex2.search(password)
    mo3 = passwordRegex3.search(password)
    # Check to see if password fit all criteria
    if (mo1 and mo2 and mo3 and len(password)>7):
            print('Solid password.')
            con = False
    if not(len(password) > 7):
            print('This password should be 8 characters long.')
    if not mo1:
        print('This password should have at least one uppercase letter.')
    if not mo2:
        print('This password should have at least one lowercase letter.')
    if not mo3:
        print('This password should have at least one numerical digit.')
