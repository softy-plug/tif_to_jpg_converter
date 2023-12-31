import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
tiff_folder = askdirectory(title='Select folder with tif images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the tif folder
for file_name in os.listdir(tiff_folder):
    if file_name.endswith('.tif') or file_name.endswith('.TIF'):
        # open tif image and convert to jpg
        tif_image = Image.open(os.path.join(tiff_folder, file_name))
        jpg_image = tif_image.convert('RGB')

        # create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # save jpg image with maximum quality
        jpg_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All tif images in {tiff_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug