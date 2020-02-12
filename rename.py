import os	
from tkinter import *	
from tkinter.ttk import Combobox

def clickList():
    combo = Combobox(window, width = sizeForTxtFields)
    combo['values']= os.listdir()
    combo.current(1) #set the selected item
    combo.grid(column=1, row=1)

def go():
    """rename files"""
    files = os.listdir()
    for item in files:
        temp = item
        os.rename(item,temp.replace(txtOld.get(),txtNew.get(),1))
    labelStatus.configure(
        text = 'done',
        fg = 'green'
    )
    clickList()



window = Tk() 
window.title("Welcome to rename files app")
window.geometry('350x200')



btnGo = Button(window, text="Go", bg="#bdecb6", fg="red", command=go)



sizeForTxtFields = 30

labelOld = Label(window, text = "old word")
labelNew = Label(window, text = "new word")
labelStatus = Label(window, text = "")
labelFiles = Label(window, text = "files")

txtOld = Entry(window, width = sizeForTxtFields, bg = '#ffb2ba')
txtNew = Entry(window, width = sizeForTxtFields, bg = '#b2fcef')

labelFiles.grid(column = 0, row = 1)
labelOld.grid(column = 0, row = 4)
labelNew.grid(column = 0, row = 5)
labelStatus.grid(column = 1, row = 7)

txtOld.grid(column = 1, row = 4)
txtNew.grid(column = 1, row = 5)

btnGo.grid(column = 1, row = 6)





def centerWindow():
    w = window.winfo_reqwidth()
    h = window.winfo_reqheight()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('+%d+%d' % (x, y))
clickList()
centerWindow()
window.mainloop()