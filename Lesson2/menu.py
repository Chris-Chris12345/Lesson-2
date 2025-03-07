from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Menu")

#creating menu bar
menubar = Menu(root)

#adding file, menu and commands
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="New file", command=None)
file.add_command(label="Open...", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=None)
edit.add_command(label="Paste", command=None)
edit.add_separator()
edit.add_command(label="Undo", command=None)

root.config(menu=menubar)
root.mainloop()