from tkinter import Tk, Label, Entry, Button, PhotoImage, LEFT, BOTTOM, scrolledtext, INSERT, messagebox
import sys, os, subprocess


def resource_path(relative_path)-> str:
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def parse_terminal_return(output):
    return_string = ''
    for line in output:
        return_string += line.decode("utf-8") 

    return return_string

def execute_command(command)-> list:
    terminal_output = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
    err = terminal_output.stderr.readlines()
    if(err):
        messagebox.showinfo('terminal error', parse_terminal_return(err))
    else:
        messagebox.showinfo('terminal Output', parse_terminal_return(terminal_output.stdout.readlines()))

    
def shutdown() -> int:
    pass

def restart() -> int:
    pass

def terminal():


    txt = Entry(window,width=10)
    txt.grid(column=1, row=0)

    
    
    run = Button(window, text="run", command=lambda: execute_command(txt.get()))
    run.grid(column=2, row=0)



window = Tk()
window.title("Vectra app")
window.geometry('500x500')
 
shutdown_button = Button(window, command = shutdown)
logo = PhotoImage(file = resource_path('assets/shutdown.png')).subsample(10, 10)
shutdown_button.config(image=logo)
shutdown_button.grid(column=10, row=200)

restart_button = Button(window, command=restart)
restart_logo = PhotoImage(file = resource_path('assets/restart.png')).subsample(9, 9)
restart_button.config(image = restart_logo)
restart_button.grid(column=30, row=200)


terminal_button = Button(window, command=terminal)
terminal_logo = PhotoImage(file = resource_path('assets/terminal.png')).subsample(5, 5)
terminal_button.config(image = terminal_logo)
terminal_button.grid(column=50, row=200)




window.mainloop()