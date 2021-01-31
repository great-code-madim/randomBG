import os, ctypes, getpass
from random import randint

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            images.append(filename)
    return images


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'python3 %s' % file_path)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

USER_NAME = getpass.getuser()
folder = os.getcwd() + "\\Wallpapers"

images = load_images_from_folder(folder)
choice = folder + "\\" + images[randint(0, len(images)-1)]
print(choice)
SPI_SETDESKWALLPAPER = 20
add_to_startup(os.getcwd() + "\\randomBG.py") 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, choice , 0)
