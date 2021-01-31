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


# Get location of file and set it as working directory.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

USER_NAME = getpass.getuser()
folder = os.getcwd() + "\\Wallpapers"
add_to_startup(os.getcwd() + "\\randomBG.py")

images = load_images_from_folder(folder)
choice = folder + "\\" + images[randint(0, len(images)-1)]

# Windows specific function that changes the wallpaper.
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, choice , 0)
