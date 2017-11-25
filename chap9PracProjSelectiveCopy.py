#! python3
# chap9PracProjSelectiveCopy.py - Copies files of a particular extension to another directory.
#         If the directory does not exist, it is first created.

import os, shutil

absPath = 'C:\\Users\\Papa\\Documents\\mattPython\\automateTheBoringStuff'
ext = input('What type of file extension do you want to copy? (Don\'t include the dot)')
extDirPath = 'C:\\Users\\Papa\\Documents\\mattPython\\' + ext + 'Copy'

if not os.path.exists(extDirPath):
    os.makedirs(extDirPath)
    print('Made the directory... ' + extDirPath)

for folderName, subfolders, filenames in os.walk(absPath):
    for filename in filenames:
        if filename.endswith('.' + ext):
            path = os.path.join(folderName, filename)
            shutil.copy(path, extDirPath)
            print('Copied... ' + filename)
        else:
            continue
print('Done.')
