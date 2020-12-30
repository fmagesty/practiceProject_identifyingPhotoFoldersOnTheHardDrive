#! python3
# Import modules and write comments to describe this program.

import os 
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith('.png') or filename.endswith('jpg'):
            numNonPhotoFiles += 1
            continue # skip to next filename

        # Open image file using Pillow.
        try:
            im = Image.open(filename)
        except FileNotFoundError:
            continue
        width, height = im.size
        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1

    # If more than half of files were photos.
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print('Found photo folder in: ' + os.path.abspath(foldername))
print('Done.')