import os
import re

# End directory with a / (or \\ on Windows)
DIRECTORY = '{YOUR_DIRECTORY_HERE}'

file_regex = re.compile(input('What are you looking for?\n'))

# Search each file in the directory.
results = []
for _file in os.listdir(DIRECTORY):
    if _file.endswith(".txt"):
        file_holder = open('{}{}'.format(DIRECTORY, _file))
        file_text = file_holder.read()
        if file_regex.findall(file_text):
            results.append(_file)
        file_holder.close()
if results:
    print('The following files have a match:')
    for i in results:
        print(i)
else:
    print("No match.")
