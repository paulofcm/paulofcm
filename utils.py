import imghdr
from tkinter import messagebox, filedialog

import PIL


def images_to_load(str1, str2):
    messagebox.showinfo(str1, str2)
    images = filedialog.askopenfiles()
    return images


def image_to_load(str1, str2):
    messagebox.showinfo(str1, str2)
    image = filedialog.askopenfile()
    return image


def select_path(str1, str2):
    messagebox.showinfo(str1, str2)
    path_selected = filedialog.askdirectory()
    return path_selected


def verify_jpg(path):
    file_extension = imghdr.what(path)
    if file_extension != 'jpg' and file_extension != 'jpeg':
        return False
    else:
        return True


def verify_image(path_file_name):
    try:
        PIL.Image.open(path_file_name)
        return True
    except PIL.UnidentifiedImageError:
        return False
