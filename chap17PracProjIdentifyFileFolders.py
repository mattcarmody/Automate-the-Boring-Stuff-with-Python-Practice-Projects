#! /usr/bin/python3
# chap17PracProjIdentifyFileFolders.py

import os
from PIL import Image

photoExt = ['.jpg', '.png']
minDim = 500

for foldername, subfolders, filenames in os.walk('/home/matt'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if filename[-4:].lower() not in photoExt:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im = Image.open(os.path.join(foldername, filename))
        imWidth, imHeight = im.size

        # Check if width & height are larger than 500.
        if imWidth > minDim and imHeight > minDim:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(foldername)
