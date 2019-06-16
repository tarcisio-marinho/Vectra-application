from tkinter import Tk, Label, Entry, Button, PhotoImage, LEFT, BOTTOM
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def shutdown():
    pass

def restart():
    pass



window = Tk()
 
window.title("Vectra app")
 
window.geometry('500x500')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)

shutdown_button = Button(window, command = shutdown)

logo = PhotoImage(file = resource_path('assets/terminal.png'))
small_logo = logo.subsample(10, 10)


shutdown_button.config(image = small_logo , compound = BOTTOM )

''' restart_button = Button(window, text="Restart", command=restart)
logo = PhotoImage(file = 'assets/restart.png')
small_logo = logo.subsample(5, 5)
restart_button.config(image = small_logo , compound = BOTTOM )
 '''


shutdown_button.grid(column=2, row=0)
''' restart_button.grid(column=10, row=0)
 ''' 
window.mainloop()