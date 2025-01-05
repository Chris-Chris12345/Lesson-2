from tkinter import *
from tkinter.ttk import *

root = Tk()

bar = Progressbar(root, orient=HORIZONTAL, length= 100, mode="determinate")

# Function responsible for the updation
# of the progress bar value
#The update() and update_idletask() methods are useful for processing any pending or idle tasks. However, the only difference between update() and update_idletasks() is that update() processes all the events present in the
#  application, while update_idletasks() only processes those events which are not running or stable.

def progressbar():
    import time
    bar['value']= 20
    root.update_idletasks()
    time.sleep(1)

    bar['value']= 40
    root.update_idletasks()
    time.sleep(1)

    bar['value']= 60
    root.update_idletasks()
    time.sleep(1)

    bar['value']= 80
    root.update_idletasks()
    time.sleep(1)

    bar['value']= 100


bar.pack(pady=10)

Button(root, text="Start", command=progressbar).pack(pady=10)
root.mainloop()