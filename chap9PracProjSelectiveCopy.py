#! python3
# chap9PracProjSelectiveCopy.py - Copies files of a particular extension to another directory.
#         If the directory does not exist, it is first created.

import os, shutil

absPath = 'C:\\Users\\Papa\\Documents\\mattPython\\automateTheBoringStuff'
ext = input('What type of file extension do you want to copy? (Don\'t include the dot)')
extDirPath = absPath + '\\' + ext + 'Copy'

for filename in os.listdir(absPath):
    if filename.endswith('.' + ext):
        if not os.path.exists(extDirPath):
            os.makedirs(extDirPath)
            print('Made the directory... ' + extDirPath)
        shutil.copy(filename, extDirPath)
        print('Copied... ' + filename)
    else:
        continue
print('Done.')
