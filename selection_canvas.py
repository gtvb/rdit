"""
This class provides a simple abstraction over the classic 
Canvas widget, which allows for selecting a rectangular 
area inside the given window. We store two point values,
which are the only two things we need to select a region out 
of an image.
"""

import tkinter as tk 

class SelectionCanvas:
    def __init__(self, root: tk.Tk):
        self.start_pos = None
        self.end_pos = None

        self.width = root.winfo_width()
        self.height = root.winfo_height()

        self.has_rect = False

        self.tk_canvas = tk.Canvas(root, width=self.width, height=self.height, background="red")

    def setup_canvas(self):
        self.tk_canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.tk_canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        self.tk_canvas.pack(fill="both", expand=1)

    def clear_canvas(self, event):
        self.tk_canvas.delete("all")
        self.has_rect = False
        self.start_pos = self.end_pos = None

    def on_mouse_move(self, event):
        if not self.has_rect:
            self.tk_canvas.delete("all")
            if not self.start_pos:
                self.start_pos = (event.x, event.y)

            self.end_pos = (event.x, event.y)
            self.tk_canvas.create_rectangle(self.start_pos[0], self.start_pos[1], event.x, event.y)

    def on_mouse_release(self, event):
        self.end_pos = (event.x, event.y)
        self.has_rect = True
