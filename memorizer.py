from tkinter import *
from tkinter.filedialog import *


root = Tk()
root.geometry("500x500")
root.title("Memorizer")

def openFile():
    fin = askopenfile(title = "Open FIle")
# If filename selected
    if fin is not None:
        list.delete(0, END)

        items = fin.readlines()
    
        for item in items:
            list.insert(END, item.strip())

def addItem():
    list.insert(END, entry.get()) 
    entry.delete(0, END)

def deleteItem():
    index = list.curselection()
    if index:
        list.delete(index)

def saveFile():
    fout = asksaveasfile(defaultextension = ".txt")
    if fout is not None:
        for item in list.get(0, END):
            print(item.strip(), file = fout)
        list.delete(0,END)


btn = Button(root, text = "Open", width = 20, command =  openFile)
btn.place(x = 190, y = 70)

entry = Entry(root,  width = 25)
entry.place(x = 190, y = 100)

btn2 = Button(root, text = "Add", width = 20, command = addItem)
btn2.place(x = 190, y = 130)

frame = Frame(root)
frame.pack(side = LEFT)
scroll = Scrollbar(frame, orient = "vertical")
scroll.pack(side = RIGHT, fill = Y)

list = Listbox(frame, width = 50, bg = "yellow", yscrollcommand = scroll)
list.pack(side = LEFT, padx = 10)
scroll.config(command = list.yview)


btn3 = Button(root, text = "Save", width = 20, command = saveFile)
btn3.place(x = 340, y = 200)

btn4 = Button(root, text = "Delete", width = 20, command = deleteItem)
btn4.place(x = 340, y = 250)

btn5 = Button(root, text = "Exit", width = 10, command = quit)
btn5.place(x = 230, y = 350)





root.mainloop()




















