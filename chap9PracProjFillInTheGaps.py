#!/usr/bin/python3
# chap9PracProjFillInTheGaps.py - Find gaps in suffix numbering, rename to fill the gaps (keeping files in original order.)

import re
import shutil
import os

# Define regex to find numbered spam files.
gapRegex = re.compile(r'''(
    (spam)    # given prefix
    (\d+)      # number
    (.txt)    # given file type
    )''', re.VERBOSE)

# Create list of the integers in the file names.
numlst = []
filelst = []
for file in os.listdir('.'):
	if gapRegex.search(file):
		num = gapRegex.search(file).group(3)
		filelst.append(file)
		numlst.append(num)
numlst = sorted(numlst)
print(numlst)
filelst = sorted(filelst)
print(filelst)

# Loop through and rename files.
for i in range(len(numlst)):
	originalName = filelst[i]
	newName = "spam" + str(i).zfill(3) + ".txt"
	if originalName == newName:
		print("Skipped " + originalName)
	else:
		shutil.move(originalName, newName)
		print("Renamed " + filelst[i])

