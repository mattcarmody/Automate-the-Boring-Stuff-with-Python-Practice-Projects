#! /usr/bin/python3
# chap16PracProjChoreAssignment.py
# Randomly assigns a list of chores to people by email.
# Requires equal number of chores and people.

import random
import smtplib

destDict = {'carmodym2+1@gmail.com': [], 'carmodym2+2@gmail.com': [], 'carmodym2+3@gmail.com': [], 'carmodym2+4@gmail.com': []}
choreList = ['dishes', 'bathroom', 'vacuum', 'walk dog', 'dust']

# Assign each person a chore 
for dest in destDict:
    randomChore = random.choice(choreList)
    choreList.remove(randomChore)
    destDict[dest].append(randomChore)

# Email each person their chore
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(input('login'), input('password'))
for dest in destDict:
    smtpObj.sendmail("brownj4745@yahoo.com", dest, "Subject: Chore Assignment\n\nThis week's chore is: " + destDict[dest][0])   
smtpObj.quit()
