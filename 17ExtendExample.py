import os
from PIL import Image

SRC = IMAGE_DIR
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = LOGO_FILE
DEST = IM_W_LOGO_DESTINATION

logo = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo.size
os.makedirs(DEST, exist_ok=True)
formats = ['.jpg', '.png', '.gif', '.bmp']

for _file in os.listdir(SRC):
	
	# Skip if it's not an image file or if it is logo file
    if _file[-4:].lower() not in formats or _file == LOGO_FILENAME:
        print("Skipping {} because it isn't an image file".format(_file))
        continue
	
	# Skip if file is too small
    im = Image.open("{}{}".format(SRC, _file))
    width, height = im.size
    if width < 2*logo_width or height < 2*logo_height:
        print("{} is too small, skipping it.".format(_file))
        continue

    # Resize image if needed
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print("Resizing {}...".format(_file))
        im = im.resize((width, height))

    # Add logo and save
    print("Adding logo to {}...".format(_file))
    im.paste(logo, (width - logo_width, height - logo_height), logo)
    im.save(os.path.join(DEST, _file))
