import os
import re
import shutil

DIR = "{YOUR_DIRECTORY_HERE}"

# Define regex to find numbered spam files.
gap_regex = re.compile(r'''(
    (spam)    # given prefix
    (\d+)     # number
    (.txt)    # given file type
    )''', re.VERBOSE)

# Create list of the integers in the file names.
file_names = []
for _file in os.listdir(DIR):
	if gap_regex.search(_file):
		file_names.append(_file)

file_names = sorted(file_names)

# Loop through and rename files.
for i, original_name in enumerate(file_names):
	new_name = "spam{}.txt".format(str(i).zfill(3))
	if original_name == new_name:
		print("Skipped {}".format(original_name))
	else:
		shutil.move("{}/{}".format(DIR, original_name),"{}/{}".format(DIR, new_name))
		print("Renamed {}".format(original_name))

