from tkinter import *
from tkinter.filedialog import *


root = Tk()
root.geometry("500x500")
root.title("Memorizer")

btn = Button(root, text = "Open", width = 20, command =  None)
btn.place(x = 190, y = 70)

entry = Entry(root,  width = 25)
entry.place(x = 190, y = 100)

btn2 = Button(root, text = "Add", width = 20, command = None)
btn2.place(x = 190, y = 130)

frame = Frame(root)
frame.pack(side = LEFT)
scroll = Scrollbar(frame, orient = "vertical")
scroll.pack(side = RIGHT, fill = Y)

list = Listbox(frame, width = 50, bg = "yellow", yscrollcommand = scroll)
list.pack(side = LEFT, padx = 10)
list.place 
scroll.config(command = list.yview)


#btn3 = Button(root, text = "Save", width = 20, command = None)
#btn3.place(x = )






root.mainloop()




























