import tkinter
from tkinter import *

top = Tk()
menubar=Menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Saveas...")
file.add_command(label="Close")

file.add_seperator()


file.add_command(label="Exit",command=top.destroy)


menubar.add_cascade(label="File",menu=file)
edit=Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="SelectAll")

edit.add_seperator()

menubar.add_cascade(label="Edit",menu=edit)

help=Menu(menubar,tearoff=2)
help.add_command(label="About")

menubar.add_cascade(label="Help",menu=help)

top.config(menu=menubar)
top.mainloop()
