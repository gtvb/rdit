"""
The objective of this program is to allow anyone 
to manipulate and read text data from a file format
which does not allow easy copying of data, for 
example, in pdf files. Essentialy, all this program
does is take a screenshot of the current screen, allow
the user to select the text area, and after that, 
use an OCR engine to extract the text. 
"""

import tkinter as tk
from selection_canvas import SelectionCanvas

root = tk.Tk()
root.update_idletasks()
# root.attributes("-fullscreen", True)

def take_screenshot():
    print("Taken!")

menu = tk.Menu()
menu.add_command(command=take_screenshot)
root.config(menu=menu)

s_canvas = SelectionCanvas(root)
s_canvas.setup_canvas()
root.bind("<Control-q>", s_canvas.clear_canvas)

root.mainloop()

import tkinter as tk

def expand(event):
    w = root.winfo_screenwidth()
    root.geometry(f"200x50+{(w-200)//2}+0")

def collapse(event):

    w = root.winfo_screenwidth()
    root.geometry(f"200x20+{(w-200)//2}+0")

root = tk.Tk()

collapse(None)
root.overrideredirect(True)
root.attributes('-topmost', True)

button = tk.Button(root, text="x", command=root.destroy)
button.pack(side="left")


button2 = tk.Button(root, text="open Top level", command=tk.Toplevel)
button2.pack(side="left", expand=True, fill="both")

root.bind("<Enter>", expand)
root.bind("<Leave>", collapse)
root.mainloop()
