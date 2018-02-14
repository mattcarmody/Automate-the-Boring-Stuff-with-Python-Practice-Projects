# Randomly assigns a list of chores to people by email.
# Requires equal number of chores and people.

import random
import smtplib

MY_EMAIL = EMAIL_HERE
DESTS = {EMAIL1: [], EMAIL2: [], EMAIL3: [], EMAIL4: []}
CHORES = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# Assign each person a chore 
for dest in DESTS:
    ran_chore = random.choice(CHORES)
    CHORES.remove(ran_chore)
    DESTS[dest].append(ran_chore)

# Email each person their chore
smtp_obj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(input('login'), input('password'))
for dest in DESTS:
    smtp_obj.sendmail(MY_EMAIL, dest, "Subject: Chore Assignment\n\nThis week's chore is: {}".format(DESTS[dest][0]))   
smtp_obj.quit()
