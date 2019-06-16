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

def terminal():
    pass


window = Tk()
 
window.title("Vectra app")
 
window.geometry('500x500')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)


shutdown_button = Button(window, command = shutdown)
logo = PhotoImage(file = resource_path('assets/shutdown.png')).subsample(10, 10)
shutdown_button.config(image=logo)

restart_button = Button(window, command=restart)
restart_logo = PhotoImage(file = resource_path('assets/restart.png')).subsample(10, 10)
restart_button.config(image = restart_logo)


terminal_button = Button(window, command=terminal)
terminal_logo = PhotoImage(file = resource_path('assets/terminal.png')).subsample(5, 5)
terminal_button.config(image = terminal_logo)



shutdown_button.grid(column=10, row=200)
restart_button.grid(column=20, row=200)
terminal_button.grid(column=30, row=200)

window.mainloop()