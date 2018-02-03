import re
import shutil
import os

DIR = "{YOUR_DIRECTORY_HERE}"
INSERTION_POINT = 3

# Define regex to find numbered spam files.
gap_regex = re.compile(r'''(
    (spam)    # given prefix
    (\d+)      # number
    (.txt)    # given file type
    )''', re.VERBOSE)
    
# Create list files matching regex criteria.
files = []
for _file in os.listdir(DIR):
	if gap_regex.search(_file):
		files.append(_file)
files = sorted(files)

# Rename files after insertion point, starting at the end, leaving a gap.
# This is to avoid overwriting.
for i in range(len(files)-1, INSERTION_POINT-1, -1):
	original_name = files[i]
	new_name = "spam{}.txt".format(str(i+1).zfill(3))
	shutil.move("{}{}".format(DIR, original_name), "{}/{}".format(DIR, new_name))
	print("Renamed {}".format(files[i]))
