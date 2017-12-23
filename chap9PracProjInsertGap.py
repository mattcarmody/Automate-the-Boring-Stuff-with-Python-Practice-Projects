#!/usr/bin/python3
# chap9PracProjInsertGap.py

import re
import shutil
import os

insertionPoint = 3

# Define regex to find numbered spam files.
gapRegex = re.compile(r'''(
    (spam)    # given prefix
    (\d+)      # number
    (.txt)    # given file type
    )''', re.VERBOSE)
    
# Create list of the integers in the file names.
numlst = []
filelst = []
for file in os.listdir('./chap9TestFiles'):
	if gapRegex.search(file):
		num = gapRegex.search(file).group(3)
		filelst.append(file)
		numlst.append(num)
numlst = sorted(numlst)
print(numlst)
filelst = sorted(filelst)
print(filelst)

# Rename files after insertion point, starting at the end, leaving a gap.
for i in range(len(numlst)-1, insertionPoint-1, -1):
	originalName = filelst[i]
	newName = "spam" + str(i+1).zfill(3) + ".txt"
	shutil.move('./chap9TestFiles/' + originalName, './chap9TestFiles/' + newName)
	print("Renamed " + filelst[i])
