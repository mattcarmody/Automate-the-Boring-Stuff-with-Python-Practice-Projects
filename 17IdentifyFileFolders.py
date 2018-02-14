import os
from PIL import Image

SRC = BASE_DIRECTORY_TO_WALK
PHOTO_EXT = ['.jpg', '.png']
MIN_DIM = 500

for foldername, subfolders, filenames in os.walk(SRC):
    num_photos = 0
    num_non_photos = 0
    for _file in filenames:
        # Check if file extension isn't .png or .jpg.
        if _file[-4:].lower() not in PHOTO_EXT:
            num_non_photos += 1
            continue

        # Open image file using Pillow.
        im = Image.open(os.path.join(foldername, _file))
        im_width, im_height = im.size

        # Check if width & height are larger than 500.
        if im_width > MIN_DIM and im_height > MIN_DIM:
            # Image is large enough to be considered a photo.
            num_photos += 1
        else:
            # Image is too small to be a photo.
            num_non_photos += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if num_photos > num_non_photos:
        print(foldername)
