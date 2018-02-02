#! python3
# chap8RegexFileSearch.py - Searches all .txt files in a location for matches.

import re, os

# Define Regex.
fileRegex = re.compile(str(input('What are you looking for?\n')))

# Search each file in the directory.
results = []
for file in os.listdir('C:\\Users\\Papa\\Documents\\mattPython\\automateTheBoringStuff'):
    if file.endswith(".txt"):
        fileHolder = open('C:\\Users\\Papa\\Documents\\mattPython\\automateTheBoringStuff\\' + file)
        fileText = fileHolder.read()
        if fileRegex.findall(fileText):
            results.append(file)
        fileHolder.close()
print('The following files have a match:')
for i in results:
    print(i)
