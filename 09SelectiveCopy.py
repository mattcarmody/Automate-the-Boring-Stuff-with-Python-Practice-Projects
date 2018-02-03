import os 
import shutil

# Linux users: 
# Beware creating a directory that starts with a "." will be hidden. 
# Your script will run without errors but you won't see the files in Files
# or in the terminal unless you explicitly call for hidden files.

SRC = "{YOUR_DIRECTORY_TO_BE_COPIED_HERE}"
DEST = "{WHERE_TO_PASTE}"

ext = input("What type of file extension do you want to copy?")
if not ext.startswith("."):
    ext = ".{}".format(ext)

if not os.path.exists(DEST):
    os.makedirs(DEST)
    print('Made the directory... {}'.format(DEST))

for folder, subfolders, filenames in os.walk(SRC):
    for filename in filenames:
        if filename.endswith(ext):
            shutil.copy(os.path.join(folder, filename), DEST)
            print("Copied... {}".format(filename))
print('Done.')
