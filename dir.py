import os
import tkinter
from tkinter import filedialog, messagebox

import utils

root = tkinter.Tk()
root.wm_withdraw() # this completely hides the root window


def create_dir():
    path = utils.select_path()
    if path != None:
        messagebox.showinfo("Diretory", "What the new dir name")
        new_path = input("Path name : ").strip()
        if len(new_path)>0:
            path_to_create = (path+"//"+new_path)
            try:
                os.mkdir(path_to_create)
                print("Path created")
            except FileExistsError:
                pass


def del_dir():
    messagebox.showinfo("Diretory", "Select dir to del")
    path = utils.select_path()
    if len(path) > 0:
        try:
            os.rmdir(path)
            print("Path removed")
        except FileExistsError:
            pass










