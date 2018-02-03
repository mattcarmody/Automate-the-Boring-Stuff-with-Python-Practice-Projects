# Scans computers for large files and folders. (does not delete anything)

import os

PATH = '{YOUR_PATH_HERE}'

FILE_THRESHOLD = 2000000 # 2MB
DIR_THRESHOLD = 10000000 # 10MB

# Walk through directory looking for big files.
print('The search begins...')
for foldername, subfolders, filenames in os.walk(PATH):
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) >= FILE_THRESHOLD:
                print('{} is {}'.format(os.path.abspath(filename), os.path.getsize(os.path.join(foldername, filename))))

print('AND NOW PART TWO.')

# Walk through directory looking for big subdirectories.
for foldername, subfolders, filenames in os.walk(PATH):
    size = sum(os.path.getsize(os.path.join(foldername, filename)) for filename in filenames)
    if size > DIR_THRESHOLD:
        print('{} is {} Bytes'.format(foldername, size))

print('Done.')
