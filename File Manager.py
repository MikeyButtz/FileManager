from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    # open a file box window
    # when we want to select a file
    read = easygui.fileopenbox()
    return read


def open_file():
    # open file function
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")


def copy_file():
    # copy file function
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', 'File copied!')


def delete_file():
    # delete file function
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found!")


def rename_file():
    # rename file function
    chosen_file = open_window()
    path1 = os.path.dirname(chosen_file)
    extension = os.path.splitext(chosen_file)[1]
    print("Enter new name for chosen file: ")
    new_name = input()
    path = os.path.join(path1, new_name + extension)
    print(path)
    os.rename(chosen_file, path)
    mb.showinfo('confirmation', "File renamed!")


def move_file():
    # move file function
    source = open_window()
    destination = filedialog.askdirectory()
    if source == destination:
        mb.showinfo('confirmation', "Source and destination are the same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File moved!")


def make_folder():
    # function to make a new folder
    new_folder_path = filedialog.askdirectory()
    print("Enter name of new folder: ")
    new_folder = input()
    path = os.path.join(new_folder_path, new_folder)
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created!")


def remove_folder():
    # function to remove a folder
    del_folder = filedialog.askdirectory()
    os.rmdir(del_folder)
    mb.showinfo('confirmation', "Folder deleted!")


def list_files():
    # function to list all the files in folder
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))
    i = 0
    print("Files in: ", folder_list, "folder are:")
    while i < len(sort_list):
        print(sort_list[i] + '\n')
        i += 1


root = Tk()


Label(root, text="Big Mike's File Manager", font=("Helvetica", 16), fg="red").grid(row = 5, column = 2)
Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)
Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)
Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)
Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)
Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)
Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)
Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)
Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)
root.mainloop()






