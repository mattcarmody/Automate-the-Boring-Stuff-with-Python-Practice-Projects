#! python3
# chap9PracProjDeleteUnneededFiles.py - Scans computers for large files and folders.
#       Is not set up to delete the large files and directories, only find them and print to screen.

import os

# Set a directory to search.
path = 'C:\\Users\\Papa\\Pictures'

# Set a size threshold.
fileThreshold = 9000000 # 9MB
subThreshold = 1000000000 # 1GB

# Walk through directory looking for threshold.
print('Search begins...')
for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) >= fileThreshold:
                print(filename + ' is ' + str(os.path.getsize(os.path.join(foldername, filename))))

# Brief intermission.
print('AND NOW PART TWO.')

# Sum and print size of subdirectories.
subSizeList = []
for foldername, subfolders, filenames in os.walk(path):
    size = sum(os.path.getsize(os.path.join(foldername, filename)) for filename in filenames)
    subSizeList.append(size)
    if size > subThreshold:
        print(str(size).rjust(11) + ' is the size of ' + foldername)

# That's all folks.
print(str(sum(subSizeList)))
print('Done.')
