import os, ctypes
from random import randint

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            images.append(filename)
    return images

folder = os.getcwd() + "\\Wallpapers"

images = load_images_from_folder(folder)
choice = folder + "\\" + images[randint(0, len(images)-1)]
print(choice)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, choice , 0)
