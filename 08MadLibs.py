#! python3
# chap8PracProjMadLibs.py - MadLibs program that reads in from a file,
#                   updates with user input,
#                   writes out to a new file,
#                   and prints to the user.

import re

# Read in text from file and create a list of all the words.
textFile = open('madLibsFeed.txt')
textContent = textFile.read()
textWords = list(textContent.split())
textFile.close()

# Define regex to recognize placeholders in list.
madLibRegex = re.compile(r'''(
    ADJECTIVE |
    VERB |
    NOUN |
    ADVERB
    )''', re.VERBOSE)
mo = madLibRegex.findall(textContent)

# Call for user input words and use them to replace placeholders.
for i in range(len(textWords)):
    if madLibRegex.match(textWords[i]):
        # Handle scenarios in which match ends with punctuation.
        if textWords[i].endswith('.'):
            sub = (str(input("Enter your own " + textWords[i][:-1].lower() +": ")) + '.')
        elif textWords[i].endswith(','):
            sub = (str(input("Enter your own " + textWords[i][:-1].lower() +": ")) + ',')
        else:
            sub = (str(input("Enter your own " + textWords[i].lower() +": ")))
        textWords.remove(textWords[i])
        textWords.insert(i, sub)
    else:
        continue

# Tie updated list into a string.        
space = ' '
newSentence = space.join(textWords)

# Store updated list in a new file.
newFile = open('madLibsOutput.txt', 'w')
newFile.write(str(newSentence))
newFile.close()

# Print updated list to user.
print(newSentence)
