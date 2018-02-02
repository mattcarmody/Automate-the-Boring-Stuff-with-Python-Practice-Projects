#! /usr/bin/python3
# chap17PracProjExtendExample.py

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = '/home/matt/AutomateBook/automate_online-materials/catLogoSmall.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok=True)
formats = ['.jpg', '.png', '.gif', '.bmp']

for filename in os.listdir('.'):
	
	# Skip if it's not an image file or if it is logo file
    if filename[-4:].lower() not in formats or filename == LOGO_FILENAME:
        print("Skipping " + filename + " because it isn't an image file")
        continue
	
	# Skip if file is too small
    im = Image.open(filename)
    width, height = im.size
    if width < 2*logoWidth or height < 2*logoHeight:
        print(filename + " is too small, skipping it.")
        continue

    # Resize image if needed
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo and save
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('withLogo', filename))
